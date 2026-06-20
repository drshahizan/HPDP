"""
cnn_stream_consumer.py
=======================
Pure Python streaming consumer (no Spark JVM overhead).
Reads from Kafka → CNN inference → writes to Elasticsearch.

This achieves the same pipeline result without heavy JVM memory usage.

Run with:
  python cnn_stream_consumer.py
"""

import os
import json
import pickle
import logging
import time
import numpy as np
import requests
from datetime import datetime, timezone

# Limit TensorFlow memory
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from kafka import KafkaConsumer
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [CNN-CONSUMER] %(levelname)s — %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── Config ────────────────────────────────────────────────────────────────────
KAFKA_BROKER   = "localhost:9092"
KAFKA_TOPIC    = "sentiment-stream"
KAFKA_GROUP    = "cnn-sentiment-group"
ES_HOST        = "http://localhost:9200"
ES_INDEX       = "sentiment_results"
MODEL_PATH     = "models/best_cnn_sentiment.keras"
TOKENIZER_PATH = "models/cnn_tokenizer.pkl"
MAX_LEN        = 128
BATCH_SIZE     = 10   # process 10 messages then write to ES

LABEL_NAMES  = {0: "Negative", 1: "Neutral", 2: "Positive"}
# CNN outputs class 0/1/2; remap to -1/0/1 to match the dataset's label scale
LABEL_TO_INT = {0: -1, 1: 0, 2: 1}


def load_models():
    log.info(f"Loading CNN model     : {MODEL_PATH}")
    tf.config.set_visible_devices([], 'GPU')
    model = tf.keras.models.load_model(MODEL_PATH)

    log.info(f"Loading CNN tokenizer : {TOKENIZER_PATH}")
    with open(TOKENIZER_PATH, "rb") as f:
        tokenizer = pickle.load(f)

    log.info("Models loaded successfully.")
    return model, tokenizer


def predict_batch(texts, model, tokenizer):
    """Run CNN inference; returns (label_strings, label_ints) where ints are -1/0/1."""
    seqs   = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(seqs, maxlen=MAX_LEN, padding="post", truncating="post")
    probs  = model.predict(padded, verbose=0)
    preds  = np.argmax(probs, axis=1)
    labels     = [LABEL_NAMES.get(int(p), "Unknown") for p in preds]
    int_labels = [LABEL_TO_INT.get(int(p), 0)        for p in preds]
    return labels, int_labels


def write_to_elasticsearch(records):
    """Bulk write records to Elasticsearch."""
    bulk_body = ""
    for rec in records:
        meta = json.dumps({"index": {"_index": ES_INDEX, "_id": str(rec["review_id"])}})
        doc  = json.dumps(rec)
        bulk_body += meta + "\n" + doc + "\n"

    try:
        r = requests.post(
            f"{ES_HOST}/_bulk",
            headers={"Content-Type": "application/x-ndjson"},
            data=bulk_body,
            timeout=10,
        )
        if r.status_code in (200, 201):
            if r.json().get("errors", False):
                log.warning("Some ES writes had errors.")
            else:
                log.info(f"Written {len(records)} records to Elasticsearch.")
        else:
            log.error(f"ES returned {r.status_code}: {r.text[:100]}")
    except Exception as e:
        log.error(f"ES write failed: {e}")


def main():
    model, tokenizer = load_models()

    log.info(f"Connecting to Kafka at {KAFKA_BROKER}, topic: {KAFKA_TOPIC}")
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id=KAFKA_GROUP,
        auto_offset_reset="latest",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        consumer_timeout_ms=60000,   # wait up to 60s for messages
    )
    log.info("Kafka consumer connected.")
    log.info("========================================")
    log.info("  CNN Streaming started! Waiting for data...")
    log.info("  Now run producer.py in another terminal")
    log.info("========================================")

    batch_texts   = []
    batch_records = []
    total_processed = 0
    start_time = time.time()

    try:
        for message in consumer:
            data = message.value

            review_id   = data.get("review_id", total_processed)
            review_text = data.get("review_text", "")
            true_label  = data.get("true_label", "Unknown")
            source_ts   = data.get("timestamp", "")

            batch_texts.append(review_text)
            batch_records.append({
                "review_id"       : review_id,
                "review_text"     : review_text,
                "true_label"      : true_label,
                "source_timestamp": source_ts,
            })

            # Process when batch is full
            if len(batch_texts) >= BATCH_SIZE:
                predictions, int_preds = predict_batch(batch_texts, model, tokenizer)

                total_processed += len(batch_texts)
                elapsed    = time.time() - start_time
                throughput = total_processed / elapsed if elapsed > 0 else 0

                es_records = []
                for rec, pred, pred_int in zip(batch_records, predictions, int_preds):
                    rec["predicted_sentiment"] = pred
                    rec["predicted_label"]     = pred_int          # -1 / 0 / 1
                    rec["is_correct"]          = str(pred == rec["true_label"])
                    rec["pipeline_version"]    = "cnn_v1"
                    rec["processed_at"]        = datetime.now(timezone.utc).isoformat()
                    rec["throughput_rps"]      = round(throughput, 2)
                    rec["batch_size"]          = len(batch_texts)
                    es_records.append(rec)

                    log.info(
                        f"  [{pred:8s}|{pred_int:+d}] (true={rec['true_label']:8s}) "
                        f"correct={rec['is_correct']:5s} | "
                        f"{rec['review_text'][:50]}"
                    )

                write_to_elasticsearch(es_records)
                log.info(f"Total processed: {total_processed} | Throughput: {throughput:.1f} records/sec")

                batch_texts   = []
                batch_records = []

    except KeyboardInterrupt:
        log.info("Consumer stopped by user.")

    finally:
        # Process remaining records
        if batch_texts:
            predictions, int_preds = predict_batch(batch_texts, model, tokenizer)
            total_processed += len(batch_texts)
            elapsed    = time.time() - start_time
            throughput = total_processed / elapsed if elapsed > 0 else 0
            es_records = []
            for rec, pred, pred_int in zip(batch_records, predictions, int_preds):
                rec["predicted_sentiment"] = pred
                rec["predicted_label"]     = pred_int
                rec["is_correct"]          = str(pred == rec["true_label"])
                rec["pipeline_version"]    = "cnn_v1"
                rec["processed_at"]        = datetime.now(timezone.utc).isoformat()
                rec["throughput_rps"]      = round(throughput, 2)
                rec["batch_size"]          = len(batch_texts)
                es_records.append(rec)
            write_to_elasticsearch(es_records)

        elapsed = time.time() - start_time
        rps = total_processed / elapsed if elapsed > 0 else 0
        log.info(f"Done. Total: {total_processed} records in {elapsed:.1f}s "
                 f"({rps:.1f} records/sec)")
        consumer.close()


if __name__ == "__main__":
    main()
