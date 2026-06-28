import json
import os
import joblib
import pandas as pd
from elasticsearch import Elasticsearch, helpers

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

MODEL_PATH = "models/best_model.pkl"
VECTORIZER_PATH = "models/best_tfidf_vectorizer.pkl"
CONFIG_PATH = "models/deployment_config.json"

KAFKA_TOPIC = "grab-reviews"
KAFKA_SERVER = "localhost:9092"

ES_HOST = "http://localhost:9200"
ES_INDEX = "grab-sentiment-results"

OUTPUT_CSV = "data/predictions_output.csv"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

classes = config["classes"]

spark = (
    SparkSession.builder
    .appName("GrabKafkaSparkBatchSentiment")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("review_id", IntegerType(), True),
    StructField("content", StringType(), True),
    StructField("processed_text", StringType(), True),
    StructField("true_sentiment", StringType(), True),
    StructField("source", StringType(), True),
    StructField("event_time", StringType(), True)
])

print("Reading messages from Kafka topic:", KAFKA_TOPIC)

df = (
    spark.read
    .format("kafka")
    .option("kafka.bootstrap.servers", KAFKA_SERVER)
    .option("subscribe", KAFKA_TOPIC)
    .option("startingOffsets", "earliest")
    .option("endingOffsets", "latest")
    .load()
)

parsed_df = (
    df.selectExpr("CAST(value AS STRING) AS json_value")
    .select(from_json(col("json_value"), schema).alias("data"))
    .select("data.*")
)

pdf = parsed_df.toPandas()

if pdf.empty:
    print("No Kafka messages found. Please run kafka_producer.py first.")
    spark.stop()
    exit()

texts = pdf["processed_text"].fillna("").astype(str).tolist()

X = vectorizer.transform(texts)
predictions = model.predict(X)
probabilities = model.predict_proba(X)

pdf["predicted_sentiment"] = [classes[int(p)] for p in predictions]
pdf["confidence_score"] = [float(max(prob)) for prob in probabilities]

print("Prediction completed.")
print(pdf[["review_id", "true_sentiment", "predicted_sentiment", "confidence_score"]].head())

write_header = not os.path.exists(OUTPUT_CSV)
pdf.to_csv(OUTPUT_CSV, mode="a", header=write_header, index=False)

print(f"Saved prediction output to {OUTPUT_CSV}")

es = Elasticsearch(ES_HOST)

actions = []
for _, row in pdf.iterrows():
    actions.append({
        "_index": ES_INDEX,
        "_source": {
            "review_id": int(row["review_id"]),
            "content": row["content"],
            "processed_text": row["processed_text"],
            "true_sentiment": row["true_sentiment"],
            "predicted_sentiment": row["predicted_sentiment"],
            "confidence_score": float(row["confidence_score"]),
            "source": row["source"],
            "event_time": row["event_time"]
        }
    })

helpers.bulk(es, actions)

print(f"Stored {len(pdf)} records into Elasticsearch index: {ES_INDEX}")

spark.stop()