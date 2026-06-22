"""
spark_streaming.py
==================
The heart of the pipeline (your main deliverable).

Flow:
    Kafka topic  ->  Spark Structured Streaming  ->  predict sentiment
                 ->  write enriched records to Elasticsearch

Design note — why foreachBatch instead of a row-by-row UDF:
    In local[*] mode, foreachBatch runs on the DRIVER. That means the
    model is loaded ONCE in this process and reused for every micro-batch,
    with no per-row reloading and no tricky serialisation of a PyTorch
    model out to executors. It is the most robust setup for a laptop and
    keeps throughput sane. Each micro-batch is small, so collecting it to
    the driver is fine.

Run it (the --packages flag pulls the Spark<->Kafka connector on first run):
    python spark_streaming.py

If you prefer spark-submit:
    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
        spark_streaming.py
"""

import os
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, LongType

from sentiment_model import predict_batch

# ---- config ------------------------------------------------------------
KAFKA_BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "youtube-comments")
ES_HOST = os.environ.get("ES_HOST", "http://localhost:9200")
ES_INDEX = os.environ.get("ES_INDEX", "sentiment-results")
SPARK_KAFKA_PKG = "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"

es = Elasticsearch(ES_HOST)

# JSON schema of each Kafka message (matches kafka_producer.py).
schema = StructType([
    StructField("id", LongType()),
    StructField("text", StringType()),
    StructField("true_sentiment", StringType()),
    StructField("event_time", StringType()),
])


def process_batch(batch_df, batch_id):
    rows = batch_df.collect()
    if not rows:
        return

    texts = [r["text"] for r in rows]

    t0 = time.time()
    labels, confs = predict_batch(texts)
    elapsed = time.time() - t0

    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    actions = []
    for r, label, conf in zip(rows, labels, confs):
        actions.append({
            "_index": ES_INDEX,
            "_source": {
                "id": r["id"],
                "text": r["text"],
                "sentiment": label,
                "true_sentiment": r["true_sentiment"],
                "confidence": round(conf, 4),
                "@timestamp": now,
            },
        })
    bulk(es, actions)

    n = len(rows)
    rps = n / elapsed if elapsed > 0 else float("inf")
    print(f"[batch {batch_id}] {n:>4} records | "
          f"{elapsed:6.3f}s | {rps:8.1f} rec/s -> ES")


def main():
    spark = (SparkSession.builder
             .appName("RealTimeSentiment")
             .config("spark.jars.packages", SPARK_KAFKA_PKG)
             .config("spark.sql.shuffle.partitions", "2")
             .getOrCreate())
    spark.sparkContext.setLogLevel("WARN")

    raw = (spark.readStream
           .format("kafka")
           .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP)
           .option("subscribe", KAFKA_TOPIC)
           .option("startingOffsets", "latest")
           .load())

    parsed = (raw.selectExpr("CAST(value AS STRING) AS json")
                 .select(from_json(col("json"), schema).alias("d"))
                 .select("d.*"))

    query = (parsed.writeStream
             .foreachBatch(process_batch)
             .option("checkpointLocation", "./_chk_sentiment")
             .start())

    print(f"Streaming from topic '{KAFKA_TOPIC}' -> index '{ES_INDEX}'.")
    print("Start the producer in another terminal. Ctrl-C to stop.")
    query.awaitTermination()


if __name__ == "__main__":
    main()
