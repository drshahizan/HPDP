"""Spark Structured Streaming job.

Reads review messages from Kafka, classifies each one with the deployed model
(Logistic Regression + TF-IDF — the best model from the offline comparison), and
writes the results to Elasticsearch. Per-micro-batch throughput/latency is logged
for the batch-vs-streaming comparison (brief 6.4).

Submitted by docker-compose:
    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
        /app/pipeline/spark_streaming.py
"""
import csv
import json
import os
import time
from pathlib import Path

import joblib

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

from elasticsearch import Elasticsearch, helpers

# ---- config (from docker-compose env) --------------------------------------
KAFKA_BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "kafka:29092")
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "reviews")
ELASTIC_HOST = os.environ.get("ELASTIC_HOST", "http://elasticsearch:9200")
ES_INDEX = os.environ.get("ES_INDEX", "sentiment_reviews")

MODEL_DIR = Path("/app/models")
PIPELINE_DIR = Path("/app/pipeline")
METRICS_CSV = PIPELINE_DIR / "streaming_metrics.csv"

MAX_KEYWORDS = 40   # tokens stored per review for the word cloud

# ---- load the deployed model once on the driver ----------------------------
print("Loading model artifacts ...", flush=True)
tfidf = joblib.load(MODEL_DIR / "tfidf_vectorizer.joblib")
clf = joblib.load(MODEL_DIR / "logistic_regression.joblib")
label_map = json.loads((MODEL_DIR / "label_map.json").read_text())
ID2LABEL = {int(k): v for k, v in label_map["id2label"].items()}
print("Loaded Logistic Regression (deployed model)", flush=True)

# ---- Elasticsearch index ----------------------------------------------------
es = Elasticsearch(ELASTIC_HOST, request_timeout=30)
mapping = json.loads((PIPELINE_DIR / "elastic_mappings.json").read_text())
if not es.indices.exists(index=ES_INDEX):
    es.indices.create(index=ES_INDEX, body=mapping)
    print(f"Created index '{ES_INDEX}'", flush=True)

# message schema
schema = StructType([
    StructField("review_id", StringType()),
    StructField("app_name", StringType()),
    StructField("cleaned_text", StringType()),
    StructField("rating", DoubleType()),
    StructField("review_date", StringType()),
    StructField("sentiment_label", StringType()),   # ground truth (optional)
    StructField("sent_at", DoubleType()),
])


def _init_metrics():
    if not METRICS_CSV.exists():
        with METRICS_CSV.open("w", newline="") as f:
            csv.writer(f).writerow(
                ["batch_id", "num_records", "process_sec",
                 "throughput_rec_per_sec", "avg_latency_sec", "batch_accuracy"])


def process_batch(batch_df, batch_id):
    t0 = time.time()
    rows = [r.asDict() for r in batch_df.collect()]
    rows = [r for r in rows if r.get("cleaned_text")]
    if not rows:
        return

    texts = [r["cleaned_text"] for r in rows]

    # --- Deployed model: Logistic Regression (TF-IDF) ---
    lr_proba = clf.predict_proba(tfidf.transform(texts))
    lr_ids = lr_proba.argmax(axis=1)

    now = time.time()
    docs, latencies, correct, labelled = [], [], 0, 0
    for i, r in enumerate(rows):
        lr_label = ID2LABEL[int(lr_ids[i])]
        # de-duplicated tokens for the word cloud
        keywords = list(dict.fromkeys(r["cleaned_text"].split()))[:MAX_KEYWORDS]
        docs.append({
            "_index": ES_INDEX,
            "_id": r.get("review_id"),
            "_source": {
                "review_id": r.get("review_id"),
                "app_name": r.get("app_name"),
                "text": r.get("cleaned_text"),
                "keywords": keywords,
                "rating": r.get("rating"),
                "predicted_sentiment": lr_label,
                "confidence": float(lr_proba[i].max()),
                "true_sentiment": r.get("sentiment_label"),
                "review_date": r.get("review_date"),
                "processed_at": now,
            },
        })
        if r.get("sent_at"):
            latencies.append(now - r["sent_at"])
        if r.get("sentiment_label"):
            labelled += 1
            correct += int(lr_label == r["sentiment_label"])

    helpers.bulk(es, docs)

    dt = time.time() - t0
    n = len(docs)
    metrics = [
        batch_id, n, round(dt, 4), round(n / dt, 1) if dt else 0.0,
        round(sum(latencies) / len(latencies), 4) if latencies else "",
        round(correct / labelled, 4) if labelled else "",
    ]
    with METRICS_CSV.open("a", newline="") as f:
        csv.writer(f).writerow(metrics)
    print(f"[batch {batch_id}] {n} records | {metrics[3]} rec/s | "
          f"acc={metrics[5]} | latency={metrics[4]}s", flush=True)


def main():
    _init_metrics()
    spark = (SparkSession.builder
             .appName("HPDP-SentimentStreaming")
             .getOrCreate())
    spark.sparkContext.setLogLevel("WARN")

    raw = (spark.readStream
           .format("kafka")
           .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP)
           .option("subscribe", KAFKA_TOPIC)
           .option("startingOffsets", "latest")
           .option("failOnDataLoss", "false")
           .load())

    parsed = (raw.selectExpr("CAST(value AS STRING) AS json")
              .select(from_json(col("json"), schema).alias("d"))
              .select("d.*"))

    query = (parsed.writeStream
             .foreachBatch(process_batch)
             .outputMode("append")
             .option("checkpointLocation", "/tmp/hpdp_checkpoint")
             .start())

    print(f"Streaming from '{KAFKA_TOPIC}' -> '{ES_INDEX}'. Waiting for data ...",
          flush=True)
    query.awaitTermination()


if __name__ == "__main__":
    main()
