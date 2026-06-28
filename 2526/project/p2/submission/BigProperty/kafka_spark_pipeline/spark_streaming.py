import json
import os
import joblib
from elasticsearch import Elasticsearch, helpers

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

MODEL_PATH = "models/best_model.pkl"
VECTORIZER_PATH = "models/best_tfidf_vectorizer.pkl"
CONFIG_PATH = "models/deployment_config.json"

KAFKA_TOPIC = "grab-reviews"
KAFKA_SERVER = "kafka:29092"

ES_HOST = "http://elasticsearch:9200"
ES_INDEX = "grab-sentiment-results"

OUTPUT_CSV = "data/predictions_output.csv"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

classes = config["classes"]

spark = (
    SparkSession.builder
    .appName("GrabRealTimeSentimentAnalysis")
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

raw_stream = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", KAFKA_SERVER)
    .option("subscribe", KAFKA_TOPIC)
    .option("startingOffsets", "latest")
    .load()
)

parsed_stream = (
    raw_stream
    .selectExpr("CAST(value AS STRING) AS json_value")
    .select(from_json(col("json_value"), schema).alias("data"))
    .select("data.*")
)


def write_predictions(batch_df, batch_id):
    pdf = batch_df.toPandas()

    if pdf.empty:
        return

    texts = pdf["processed_text"].fillna("").astype(str).tolist()

    X = vectorizer.transform(texts)
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)

    pdf["predicted_sentiment"] = [classes[int(p)] for p in predictions]
    pdf["confidence_score"] = [float(max(prob)) for prob in probabilities]
    pdf["batch_id"] = int(batch_id)

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
                "confidence_score": row["confidence_score"],
                "source": row["source"],
                "event_time": row["event_time"],
                "batch_id": int(row["batch_id"])
            }
        })

    helpers.bulk(es, actions)

    write_header = not os.path.exists(OUTPUT_CSV)
    pdf.to_csv(OUTPUT_CSV, mode="a", header=write_header, index=False)

    print(f"Batch {batch_id}: stored {len(pdf)} records to Elasticsearch and CSV.")
    print(pdf[["review_id", "true_sentiment", "predicted_sentiment", "confidence_score"]].head())


query = (
    parsed_stream.writeStream
    .foreachBatch(write_predictions)
    .outputMode("append")
    .option("checkpointLocation", "checkpoints/grab_sentiment")
    .start()
)

print("Spark streaming job started. Waiting for Kafka messages...")
query.awaitTermination()