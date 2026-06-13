"""
spark_streaming_local.py
=========================
Local PySpark Structured Streaming job using CNN model.
Optimized for low memory (4GB RAM).
"""

import os
import sys
import json
import pickle
import logging
import tempfile
import numpy as np

os.environ["HADOOP_HOME"] = os.environ.get("HADOOP_HOME", "C:\\hadoop")
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
# Limit TensorFlow memory usage
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, from_json, current_timestamp, lit
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SPARK-CNN] %(levelname)s — %(message)s",
)
log = logging.getLogger(__name__)

KAFKA_BROKER   = "localhost:9092"
KAFKA_TOPIC    = "sentiment-stream"
ES_HOST        = "localhost"
ES_PORT        = "9200"
ES_INDEX       = "sentiment_results"
MODEL_PATH     = "models/best_cnn_sentiment.keras"
TOKENIZER_PATH = "models/cnn_tokenizer.pkl"
MAX_LEN        = 128

CHECKPOINT_DIR = os.path.join(tempfile.gettempdir(), "spark_cnn_checkpoint2")
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
log.info(f"Checkpoint dir: {CHECKPOINT_DIR}")

LABEL_NAMES = {0: "Negative", 1: "Neutral", 2: "Positive"}

MESSAGE_SCHEMA = StructType([
    StructField("review_id",   IntegerType(), True),
    StructField("review_text", StringType(),  True),
    StructField("true_label",  StringType(),  True),
    StructField("timestamp",   StringType(),  True),
])

# Load model and tokenizer once at global scope
log.info(f"Loading CNN model     : {MODEL_PATH}")
log.info(f"Loading CNN tokenizer : {TOKENIZER_PATH}")

import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')  # Force CPU only to save memory

CNN_MODEL = tf.keras.models.load_model(MODEL_PATH)
with open(TOKENIZER_PATH, "rb") as f:
    CNN_TOKENIZER = pickle.load(f)
log.info("CNN model and tokenizer loaded.")


def predict(text: str) -> str:
    if not text or not text.strip():
        return "Unknown"
    try:
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        seq    = CNN_TOKENIZER.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post", truncating="post")
        probs  = CNN_MODEL.predict(padded, verbose=0)
        pred   = int(np.argmax(probs, axis=1)[0])
        return LABEL_NAMES.get(pred, "Unknown")
    except Exception:
        return "Error"

predict_udf = udf(predict, StringType())


def write_to_elasticsearch(batch_df, batch_id: int):
    import requests

    rows = batch_df.collect()
    if not rows:
        return

    log.info(f"Batch {batch_id}: writing {len(rows)} records to Elasticsearch...")
    bulk_body = ""

    for row in rows:
        meta = json.dumps({"index": {"_index": ES_INDEX, "_id": str(row["review_id"])}})
        doc  = json.dumps({
            "review_id"           : row["review_id"],
            "review_text"         : row["review_text"],
            "true_label"          : row["true_label"],
            "predicted_sentiment" : row["predicted_sentiment"],
            "is_correct"          : row["is_correct"],
            "pipeline_version"    : row["pipeline_version"],
            "source_timestamp"    : row["source_timestamp"],
            "processed_at"        : str(row["processed_at"]),
        })
        bulk_body += meta + "\n" + doc + "\n"

    try:
        r = requests.post(
            f"http://{ES_HOST}:{ES_PORT}/_bulk",
            headers={"Content-Type": "application/x-ndjson"},
            data=bulk_body,
            timeout=30,
        )
        if r.status_code in (200, 201):
            if r.json().get("errors", False):
                log.warning(f"Batch {batch_id}: some ES writes had errors.")
            else:
                log.info(f"Batch {batch_id}: {len(rows)} records written successfully.")
        else:
            log.error(f"Batch {batch_id}: ES returned {r.status_code}")
    except Exception as e:
        log.error(f"Batch {batch_id}: ES write failed — {e}")


def main():
    log.info("Creating local SparkSession...")
    spark = (
        SparkSession.builder
        .appName("SentimentStreamingCNN")
        .master("local[2]")
        .config("spark.driver.memory", "512m")        # reduced memory
        .config("spark.executor.memory", "512m")
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true")
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.0"
        )
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    log.info("SparkSession ready.")

    raw_stream = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe",               KAFKA_TOPIC)
        .option("startingOffsets",         "latest")
        .option("failOnDataLoss",          "false")
        .option("maxOffsetsPerTrigger",    "20")       # process 20 records per batch
        .load()
    )

    parsed = (
        raw_stream
        .select(
            from_json(col("value").cast("string"), MESSAGE_SCHEMA).alias("data"),
            col("timestamp").alias("kafka_ingest_time"),
        )
        .select(
            col("data.review_id").alias("review_id"),
            col("data.review_text").alias("review_text"),
            col("data.true_label").alias("true_label"),
            col("data.timestamp").alias("source_timestamp"),
            "kafka_ingest_time",
        )
    )

    predictions = (
        parsed
        .withColumn("predicted_sentiment", predict_udf(col("review_text")))
        .withColumn("processed_at",        current_timestamp())
        .withColumn("pipeline_version",    lit("cnn_v1"))
        .withColumn(
            "is_correct",
            (col("predicted_sentiment") == col("true_label")).cast("string")
        )
    )

    # Console output
    console_query = (
        predictions
        .select("review_id", "review_text", "true_label", "predicted_sentiment", "is_correct")
        .writeStream
        .outputMode("append")
        .format("console")
        .option("truncate", "true")
        .option("numRows", 5)
        .option("checkpointLocation", os.path.join(CHECKPOINT_DIR, "console"))
        .trigger(processingTime="15 seconds")
        .start()
    )

    # Elasticsearch output
    es_query = (
        predictions
        .writeStream
        .outputMode("append")
        .foreachBatch(write_to_elasticsearch)
        .option("checkpointLocation", os.path.join(CHECKPOINT_DIR, "es"))
        .trigger(processingTime="15 seconds")
        .start()
    )

    log.info("========================================")
    log.info("  CNN Streaming started! Waiting for data...")
    log.info("  Now run producer.py in another terminal")
    log.info("========================================")

    spark.streams.awaitAnyTermination()


if __name__ == "__main__":
    main()
