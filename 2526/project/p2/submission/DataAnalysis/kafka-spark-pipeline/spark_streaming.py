# ============================================================================
# spark_streaming.py — Spark Structured Streaming Consumer + Sentiment Prediction
# ============================================================================
# This script:
#   1. Connects to Kafka and subscribes to the telecom-reviews topic.
#   2. Loads Member 1's pre-trained TF-IDF vectorizer and Logistic Regression
#      model (saved as .pkl files via joblib).
#   3. For each micro-batch of incoming reviews, applies the vectorizer and
#      model to predict sentiment.
#   4. Writes the prediction output (with a match flag) to Elasticsearch
#      using the elasticsearch-py Python client (no JARs needed).
#   5. Logs per-batch and cumulative streaming performance metrics.
#
# Usage:
#   python spark_streaming.py
#
# ============================================================================

import time
import os
import json
from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

import joblib
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, udf, lit, current_timestamp
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
)

from config import (
    SPARK_APP_NAME,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    ES_NODES,
    ES_INDEX,
    MODEL_PATH,
    VECTORIZER_PATH,
    LOG_DIR,
)


# ============================================================================
# 1. Load Member 1's Pre-Trained Model & Vectorizer (on the driver)
# ============================================================================
print("[INFO] Loading sentiment model and vectorizer...")
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
print(f"[OK] Model loaded from: {MODEL_PATH}")
print(f"[OK] Vectorizer loaded from: {VECTORIZER_PATH}")


# ============================================================================
# 2. Define the Kafka Message Schema
# ============================================================================
review_schema = StructType([
    StructField("userName", StringType(), True),
    StructField("cleaned_content", StringType(), True),
    StructField("score", IntegerType(), True),
    StructField("provider", StringType(), True),
    StructField("review_date", StringType(), True),
    StructField("original_sentiment", StringType(), True),
])


# ============================================================================
# 3. Performance Tracking (cumulative across all batches)
# ============================================================================
class StreamingMetrics:
    """Simple container for cumulative streaming metrics."""
    def __init__(self):
        self.total_records = 0
        self.total_batches = 0
        self.total_processing_time = 0.0
        self.start_time = time.time()

metrics = StreamingMetrics()


# ============================================================================
# 4. Batch Processing Function
# ============================================================================
def process_batch(batch_df, batch_id):
    """
    Called for each micro-batch. Applies the ML model and writes results
    to Elasticsearch.
    """
    batch_start = time.time()
    record_count = batch_df.count()

    if record_count == 0:
        print(f"  [Batch {batch_id}] Empty batch — skipping.")
        return

    print(f"\n  [Batch {batch_id}] Processing {record_count:,} records...")

    # ---- Convert to Pandas for sklearn prediction ----
    pdf = batch_df.toPandas()

    # Handle any null cleaned_content values
    pdf["cleaned_content"] = pdf["cleaned_content"].fillna("")

    # ---- Apply TF-IDF Vectorizer ----
    text_data = pdf["cleaned_content"].tolist()
    X_tfidf = vectorizer.transform(text_data)

    # ---- Predict Sentiment ----
    predictions = model.predict(X_tfidf)
    pdf["predicted_sentiment"] = predictions

    # ---- Add match flag (predicted vs original) ----
    pdf["match"] = pdf["predicted_sentiment"] == pdf["original_sentiment"]

    # ---- Add processing timestamp ----
    pdf["processed_at"] = datetime.now().isoformat()

    # ---- Write to Elasticsearch using elasticsearch-py bulk API ----
    es_client = Elasticsearch(f"http://{ES_NODES}")
    actions = [
        {
            "_index": ES_INDEX,
            "_source": row.to_dict(),
        }
        for _, row in pdf.iterrows()
    ]
    bulk(es_client, actions)
    es_client.close()

    # ---- Update Metrics ----
    batch_time = time.time() - batch_start
    metrics.total_records += record_count
    metrics.total_batches += 1
    metrics.total_processing_time += batch_time

    rate = record_count / batch_time if batch_time > 0 else 0
    cumulative_rate = (
        metrics.total_records / metrics.total_processing_time
        if metrics.total_processing_time > 0
        else 0
    )

    print(
        f"  [Batch {batch_id}] ✓ Done — "
        f"{record_count:,} records in {batch_time:.2f}s "
        f"({rate:.0f} rec/s) | "
        f"Cumulative: {metrics.total_records:,} records, "
        f"{cumulative_rate:.0f} rec/s"
    )

    # ---- Show a sample of predictions ----
    sample_size = min(3, len(pdf))
    if sample_size > 0:
        sample = pdf[["userName", "provider", "original_sentiment", "predicted_sentiment", "match"]].head(sample_size)
        print(f"  [Batch {batch_id}] Sample predictions:")
        print(sample.to_string(index=False))


# ============================================================================
# 5. Main Streaming Pipeline
# ============================================================================
def main():
    print(f"\n{'='*70}")
    print(f"  Spark Structured Streaming — Telecom Sentiment Pipeline")
    print(f"{'='*70}")
    print(f"  Kafka Source  : {KAFKA_BOOTSTRAP_SERVERS} / {KAFKA_TOPIC}")
    print(f"  Elasticsearch : {ES_NODES} / {ES_INDEX}")
    print(f"  Model         : {MODEL_PATH}")
    print(f"  Vectorizer    : {VECTORIZER_PATH}")
    print(f"{'='*70}\n")

    # ---- Create Spark Session ----
    spark = SparkSession.builder \
        .appName(SPARK_APP_NAME) \
        .config("spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1") \
        .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")
    print("[OK] SparkSession created.")

    # ---- Read from Kafka ----
    kafka_stream = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
        .option("subscribe", KAFKA_TOPIC) \
        .option("startingOffsets", "latest") \
        .option("failOnDataLoss", "false") \
        .load()

    print("[OK] Subscribed to Kafka topic.")

    # ---- Parse JSON value from Kafka message ----
    parsed_stream = kafka_stream \
        .selectExpr("CAST(value AS STRING) as json_str") \
        .select(from_json(col("json_str"), review_schema).alias("data")) \
        .select("data.*")

    # ---- Start the streaming query with foreachBatch ----
    query = parsed_stream.writeStream \
        .foreachBatch(process_batch) \
        .outputMode("update") \
        .option("checkpointLocation", os.path.join(LOG_DIR, "checkpoints")) \
        .start()

    print("[OK] Streaming query started. Waiting for messages...\n")
    print("     Press Ctrl+C to stop the pipeline.\n")

    try:
        query.awaitTermination()
    except KeyboardInterrupt:
        print("\n[INTERRUPTED] Stopping streaming pipeline...")
        query.stop()
    finally:
        # ---- Final Performance Summary ----
        elapsed = time.time() - metrics.start_time
        overall_rate = (
            metrics.total_records / metrics.total_processing_time
            if metrics.total_processing_time > 0
            else 0
        )

        summary = (
            f"\n{'='*70}\n"
            f"  STREAMING PIPELINE SUMMARY\n"
            f"{'='*70}\n"
            f"  Total records processed  : {metrics.total_records:,}\n"
            f"  Total batches            : {metrics.total_batches}\n"
            f"  Total processing time    : {metrics.total_processing_time:.2f}s\n"
            f"  Overall throughput       : {overall_rate:.1f} records/sec\n"
            f"  Pipeline uptime          : {elapsed:.2f}s\n"
            f"  Elasticsearch index      : {ES_INDEX}\n"
            f"  Finished at              : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"{'='*70}\n"
        )
        print(summary)

        # Save summary to log file
        os.makedirs(LOG_DIR, exist_ok=True)
        log_file = os.path.join(LOG_DIR, "streaming_log.txt")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n--- Run: {datetime.now().isoformat()} ---\n")
            f.write(summary)
        print(f"  Log saved to: {log_file}")

        spark.stop()
        print("[DONE] Spark session closed.")


if __name__ == "__main__":
    main()
