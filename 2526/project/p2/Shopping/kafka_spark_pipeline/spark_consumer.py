"""
spark_streaming/spark_consumer.py
==================================
PySpark Structured Streaming job that:
  1. Reads review messages from Kafka topic 'sentiment-stream'
  2. Deserialises the JSON payload
  3. Loads the trained Naive Bayes + TF-IDF model
  4. Predicts sentiment (Negative / Neutral / Positive)
  5. Writes results to Elasticsearch index 'sentiment_results'

Run inside the spark-master container:
  spark-submit \
    --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,\
               org.elasticsearch:elasticsearch-spark-30_2.12:8.11.0 \
    /opt/spark_streaming/spark_consumer.py
"""

import json
import joblib
import logging
import numpy as np
from datetime import datetime, timezone

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, udf, from_json, current_timestamp, lit
)
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, TimestampType
)

# ── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SPARK] %(levelname)s — %(message)s",
)
log = logging.getLogger(__name__)

# ── Configuration ─────────────────────────────────────────────────────────────
KAFKA_BROKER   = "kafka:29092"
KAFKA_TOPIC    = "sentiment-stream"
ES_HOST        = "elasticsearch:9200"
ES_INDEX       = "sentiment_results"
MODEL_PATH     = "/opt/models/naive_bayes_sentiment.joblib"
TFIDF_PATH     = "/opt/models/tfidf_vectorizer.joblib"
CHECKPOINT_DIR = "/tmp/spark_checkpoints/sentiment"

LABEL_NAMES = {0: "Negative", 1: "Neutral", 2: "Positive"}

# ── Schema for incoming Kafka JSON messages ───────────────────────────────────
MESSAGE_SCHEMA = StructType([
    StructField("review_id",   IntegerType(), True),
    StructField("review_text", StringType(),  True),
    StructField("true_label",  StringType(),  True),
    StructField("timestamp",   StringType(),  True),
])


def load_models():
    """Load NB classifier and TF-IDF vectorizer from disk."""
    log.info(f"Loading model from  : {MODEL_PATH}")
    log.info(f"Loading TF-IDF from : {TFIDF_PATH}")
    clf   = joblib.load(MODEL_PATH)
    tfidf = joblib.load(TFIDF_PATH)
    log.info("Models loaded successfully.")
    return clf, tfidf


def build_predict_udf(clf, tfidf):
    """
    Build a Spark UDF that takes a review string and returns a
    sentiment label string.

    We capture clf and tfidf in the closure — Spark will serialise
    them to each executor automatically.
    """
    def predict(text: str) -> str:
        if not text or not text.strip():
            return "Unknown"
        try:
            vec   = tfidf.transform([text])
            pred  = clf.predict(vec)[0]          # integer 0, 1, or 2
            return LABEL_NAMES.get(int(pred), "Unknown")
        except Exception as e:
            return f"Error: {str(e)[:50]}"

    return udf(predict, StringType())


def create_spark_session() -> SparkSession:
    """Build a SparkSession with Kafka and ES connectors."""
    spark = (
        SparkSession.builder
        .appName("SentimentStreamingPipeline")
        .master("spark://spark-master:7077")
        # Kafka connector
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,"
            "org.elasticsearch:elasticsearch-spark-30_2.12:8.11.0"
        )
        # Elasticsearch settings
        .config("es.nodes",       "elasticsearch")
        .config("es.port",        "9200")
        .config("es.index.auto.create", "true")
        .config("es.nodes.wan.only",    "true")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    log.info("SparkSession created.")
    return spark


def write_to_elasticsearch(batch_df, batch_id: int):
    """
    Micro-batch writer — called by Spark for each micro-batch.
    Writes the batch to Elasticsearch using the ES-Hadoop connector.
    """
    count = batch_df.count()
    if count == 0:
        return

    log.info(f"Batch {batch_id}: writing {count} records to ES index '{ES_INDEX}'")

    (
        batch_df.write
        .format("org.elasticsearch.spark.sql")
        .option("es.resource",          ES_INDEX)
        .option("es.mapping.id",        "review_id")   # use review_id as ES doc _id
        .option("es.write.operation",   "upsert")
        .mode("append")
        .save()
    )
    log.info(f"Batch {batch_id}: done.")


def main():
    spark = create_spark_session()
    clf, tfidf = load_models()
    predict_udf = build_predict_udf(clf, tfidf)

    # ── Read stream from Kafka ────────────────────────────────────────────────
    raw_stream = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe",               KAFKA_TOPIC)
        .option("startingOffsets",         "latest")
        .option("failOnDataLoss",          "false")
        .load()
    )

    # ── Parse JSON payload ────────────────────────────────────────────────────
    parsed = (
        raw_stream
        .select(
            col("offset").alias("kafka_offset"),
            col("partition").alias("kafka_partition"),
            col("timestamp").alias("kafka_ingest_time"),
            from_json(col("value").cast("string"), MESSAGE_SCHEMA).alias("data")
        )
        .select(
            "kafka_offset",
            "kafka_partition",
            "kafka_ingest_time",
            col("data.review_id").alias("review_id"),
            col("data.review_text").alias("review_text"),
            col("data.true_label").alias("true_label"),
            col("data.timestamp").alias("source_timestamp"),
        )
    )

    # ── Run sentiment prediction ──────────────────────────────────────────────
    predictions = (
        parsed
        .withColumn("predicted_sentiment", predict_udf(col("review_text")))
        .withColumn("processed_at",        current_timestamp())
        .withColumn("pipeline_version",    lit("naive_bayes_v1"))
        # Correctness flag (only available because we have ground truth labels)
        .withColumn(
            "is_correct",
            (col("predicted_sentiment") == col("true_label")).cast("string")
        )
    )

    # ── Print to console for debugging ───────────────────────────────────────
    console_query = (
        predictions
        .select(
            "review_id",
            "review_text",
            "true_label",
            "predicted_sentiment",
            "is_correct",
            "processed_at",
        )
        .writeStream
        .outputMode("append")
        .format("console")
        .option("truncate", "true")
        .option("numRows", 10)
        .trigger(processingTime="5 seconds")
        .start()
    )

    # ── Write to Elasticsearch ───────────────────────────────────────────────
    es_query = (
        predictions
        .writeStream
        .outputMode("append")
        .foreachBatch(write_to_elasticsearch)
        .option("checkpointLocation", CHECKPOINT_DIR)
        .trigger(processingTime="5 seconds")
        .start()
    )

    log.info("Streaming queries started. Waiting for data...")
    log.info(f"  Console query id : {console_query.id}")
    log.info(f"  ES query id      : {es_query.id}")

    # Wait until terminated (Ctrl+C)
    spark.streams.awaitAnyTermination()


if __name__ == "__main__":
    main()
