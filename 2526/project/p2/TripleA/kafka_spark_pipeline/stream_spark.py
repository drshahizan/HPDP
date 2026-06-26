from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

from model_loader import predict
from elasticsearch import Elasticsearch
from deep_translator import GoogleTranslator

import time
import pandas as pd

# ELASTICSEARCH
es = Elasticsearch("http://localhost:9200")

def push_to_es(doc):
    es.index(index="youtube_sentiment", document=doc)

def translate_to_english(text):
    if not text or not isinstance(text, str):
        return ""
    try:
        translated = GoogleTranslator(source="auto", target="en").translate(text)
        return translated if translated else text  # Fall back if translation returns None
    except Exception as e:
        print(f"Translation failed: {e}")
        return text


# SPARK
spark = SparkSession.builder \
    .appName("KafkaStreaming") \
    .master("local[*]") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    ) \
    .getOrCreate()

schema = StructType() \
    .add("comment", StringType()) \
    .add("author", StringType()) \
    .add("timestamp", StringType()) \
    .add("video_id", StringType()) \
    .add("comment_id", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "youtube_comments") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

def process_batch(batch_df, batch_id):
    rows = batch_df.collect()

    if not rows:
        print(f"[Batch {batch_id}] No records, skipping.")
        return

    batch_start = time.time()

    for r in rows:
        comment = r["comment"] if r["comment"] else ""
        translated = translate_to_english(comment)

        if not translated.strip():
            print(f"Skipping empty comment from {r['author']}")
            continue

        label, confidence = predict(translated)

        doc = {
            "video_id": r["video_id"],
            "comment_id": r["comment_id"],
            "comment": r["comment"],
            "comment_translated": translated,
            "author": r["author"],
            "timestamp": r["timestamp"],
            "sentiment_label": label,
            "sentiment_confidence": float(confidence),
            "mode": "streaming"
        }

        print(doc)
        push_to_es(doc)

    batch_end = time.time()
    batch_duration = batch_end - batch_start
    throughput = len(rows) / batch_duration if batch_duration > 0 else 0

    print(f"[Batch {batch_id}] Records: {len(rows)} | Duration: {batch_duration:.2f}s | Throughput: {throughput:.2f} rec/s")

    # Push metrics to ES
    es.index(index="pipeline_metrics", document={
        "mode": "streaming",
        "batch_id": batch_id,
        "total_records": len(rows),
        "duration_seconds": batch_duration,
        "throughput_per_second": throughput,
        "timestamp": pd.Timestamp.now().isoformat()
    })

query = json_df.writeStream \
    .foreachBatch(process_batch) \
    .start()

query.awaitTermination()