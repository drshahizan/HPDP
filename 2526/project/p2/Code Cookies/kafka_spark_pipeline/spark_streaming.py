import os
import sys
import pyspark

# Must be before all other imports
os.environ['SPARK_HOME'] = os.path.dirname(pyspark.__file__)
os.environ.pop('PYSPARK_SUBMIT_ARGS', None)
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

import joblib
import pandas as pd
from datetime import datetime, timezone
from elasticsearch import Elasticsearch, helpers
from langdetect import detect, LangDetectException
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType


# =========================
# CONFIGURATION
# =========================

KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "foodpanda_reviews"
ELASTICSEARCH_URL = "http://localhost:9200"
ES_INDEX = "foodpanda_streaming_reviews"
CHECKPOINT_LOCATION = "checkpoint_foodpanda_streaming"


# =========================
# LOAD MODEL FILES
# =========================

nb_model = joblib.load("naive_bayes_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")


# =========================
# LANGUAGE FILTER
# =========================

def is_malaysian_review(text):
    if not text or len(text.strip()) < 5:
        return False
    try:
        lang = detect(text)
        return lang in ['en', 'ms']
    except LangDetectException:
        return False


# =========================
# ELASTICSEARCH CONNECTION
# =========================

def get_es_client():
    return Elasticsearch(
        ELASTICSEARCH_URL,
        verify_certs=False,
        ssl_show_warn=False
    )


# =========================
# CREATE ELASTICSEARCH INDEX
# =========================

def create_elasticsearch_index():
    es = get_es_client()

    if not es.ping():
        raise ConnectionError("Cannot connect to Elasticsearch. Make sure it is running on port 9200.")

    if not es.indices.exists(index=ES_INDEX):
        es.indices.create(
            index=ES_INDEX,
            mappings={
                "properties": {
                    "review_id":    {"type": "keyword"},
                    "review_text":  {"type": "text"},
                    "username":     {"type": "keyword"},
                    "rating":       {"type": "float"},
                    "review_date":  {"type": "date", "ignore_malformed": True},
                    "thumbs_up":    {"type": "integer"},
                    "reply":        {"type": "text"},
                    "replied_at":   {"type": "date", "ignore_malformed": True},
                    "sentiment":    {"type": "keyword"},
                    "confidence":   {"type": "float"},
                    "processed_at": {"type": "date"},
                    "batch_id":     {"type": "long"}
                }
            }
        )
        print(f"Created Elasticsearch index: {ES_INDEX}")
    else:
        print(f"Elasticsearch index already exists: {ES_INDEX}")


# Test connection and create index
es_test = get_es_client()
print("Ping:", es_test.ping())
print("Info:", es_test.info())
create_elasticsearch_index()


# =========================
# SPARK SESSION
# =========================

spark = SparkSession.builder \
    .appName("FoodpandaSentimentStreamingToElasticsearch") \
    .master("local[*]") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3"
    ) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")


# =========================
# KAFKA MESSAGE SCHEMA
# =========================

schema = StructType() \
    .add("review_id",   StringType()) \
    .add("review_text", StringType()) \
    .add("rating",      StringType()) \
    .add("review_date", StringType()) \
    .add("username",    StringType()) \
    .add("thumbs_up",   StringType()) \
    .add("reply",       StringType()) \
    .add("replied_at",  StringType())


# =========================
# READ STREAM FROM KAFKA
# =========================

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_SERVER) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "earliest") \
    .load()

json_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")


# =========================
# PREDICTION + SAVE TO ELASTICSEARCH
# =========================

def predict_and_save(batch_df, batch_id):
    pdf = batch_df.toPandas()

    if pdf.empty:
        return

    pdf["review_text"] = pdf["review_text"].fillna("").astype(str)

    # Filter to English and Malay only
    pdf = pdf[pdf["review_text"].apply(is_malaysian_review)].reset_index(drop=True)

    if pdf.empty:
        print(f"Batch {batch_id}: No EN/MS reviews found, skipping.")
        return

    texts = pdf["review_text"].tolist()

    # Sentiment prediction
    X = vectorizer.transform(texts)
    preds = nb_model.predict(X)
    probs = nb_model.predict_proba(X)
    sentiments = label_encoder.inverse_transform(preds)
    confidence_scores = probs.max(axis=1)

    pdf["sentiment"]    = sentiments
    pdf["confidence"]   = confidence_scores
    pdf["processed_at"] = datetime.now(timezone.utc).isoformat()
    pdf["batch_id"]     = int(batch_id)

    # Clean numeric fields
    pdf["rating"]    = pd.to_numeric(pdf["rating"], errors="coerce")
    pdf["thumbs_up"] = pd.to_numeric(pdf["thumbs_up"], errors="coerce")

    # Clean date fields
    for date_col in ["review_date", "replied_at"]:
        if date_col in pdf.columns:
            pdf[date_col] = pd.to_datetime(pdf[date_col], errors="coerce")
            pdf[date_col] = pdf[date_col].apply(
                lambda x: x.isoformat() if pd.notnull(x) else None
            )

    # Replace NaN with None — DataFrame level
    pdf = pdf.where(pd.notnull(pdf), None)

    output_cols = [
        "review_id", "review_text", "username", "rating",
        "review_date", "thumbs_up", "reply", "replied_at",
        "sentiment", "confidence", "processed_at", "batch_id"
    ]
    output_cols = [c for c in output_cols if c in pdf.columns]
    records = pdf[output_cols].to_dict("records")

    # Replace NaN with None — record level (extra safety)
    cleaned_records = []
    for record in records:
        cleaned = {
            k: (None if (isinstance(v, float) and pd.isna(v)) else v)
            for k, v in record.items()
        }
        cleaned_records.append(cleaned)
    records = cleaned_records

    actions = [
        {
            "_index": ES_INDEX,
            "_id": record.get("review_id"),
            "_source": record
        }
        for record in records
    ]

    try:
        es = get_es_client()
        success, failed = helpers.bulk(es, actions, raise_on_error=False)
        print("=" * 60)
        print(f"Batch ID: {batch_id} | Indexed: {success} | Failed: {len(failed)}")
        print("=" * 60)
        if failed:
            print("Sample failure:", failed[0])
    except Exception as e:
        print(f"Bulk indexing error: {e}")
        return

    for record in records[:5]:
        print("Review:    ", record.get("review_text", "")[:80])
        print("Sentiment: ", record.get("sentiment"))
        print("Confidence:", round(record.get("confidence") or 0, 4))
        print("-" * 60)


# =========================
# START STREAMING
# =========================

query = json_df.writeStream \
    .foreachBatch(predict_and_save) \
    .option("checkpointLocation", CHECKPOINT_LOCATION) \
    .start()

print("Spark streaming started.")
print("Waiting for Kafka messages...")

query.awaitTermination()