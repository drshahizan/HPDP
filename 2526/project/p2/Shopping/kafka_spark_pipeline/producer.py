"""
kafka_producer/producer.py
==========================
Reads cleaned_data.xlsx row by row and sends each review as a JSON
message to the Kafka topic 'sentiment-stream'.

This simulates real-time ingestion of Malaysian Google Maps reviews.

Column names expected in the Excel file:
  - clean_review  : preprocessed review text
  - label         : sentiment label  (-1=Negative, 0=Neutral, 1=Positive)
"""

import json
import time
import argparse
import logging
import pandas as pd
from datetime import datetime, timezone
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

# ── Logging setup ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [PRODUCER] %(levelname)s — %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── Constants ─────────────────────────────────────────────────────────────────
KAFKA_BROKER  = "localhost:9092"   # change to kafka:29092 if running inside Docker
KAFKA_TOPIC   = "sentiment-stream"
DATA_PATH     = "../data/cleaned_data.csv"
TEXT_COL      = "clean_review"
LABEL_COL     = "label"

LABEL_MAP = {
    -1.0: "Negative",
     0.0: "Neutral",
     1.0: "Positive",
    # integer keys as fallback
    -1: "Negative",
     0: "Neutral",
     1: "Positive",
}


def create_producer(broker: str, retries: int = 10) -> KafkaProducer:
    """Create a KafkaProducer, retrying until the broker is ready."""
    for attempt in range(1, retries + 1):
        try:
            producer = KafkaProducer(
                bootstrap_servers=broker,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                acks="all",           # wait for all replicas to confirm
                retries=3,
            )
            log.info(f"Connected to Kafka broker at {broker}")
            return producer
        except NoBrokersAvailable:
            log.warning(f"Broker not ready (attempt {attempt}/{retries}). Retrying in 5s...")
            time.sleep(5)
    raise RuntimeError(f"Could not connect to Kafka at {broker} after {retries} attempts.")


def load_data(path: str) -> pd.DataFrame:
    """Load the cleaned Excel dataset."""
    log.info(f"Loading dataset from: {path}")
    df = pd.read_csv(path)
    log.info(f"Loaded {len(df):,} rows | Columns: {list(df.columns)}")

    # Keep only needed columns and drop nulls
    df = df[[TEXT_COL, LABEL_COL]].dropna()
    df[TEXT_COL] = df[TEXT_COL].astype(str).str.strip()
    df = df[df[TEXT_COL] != ""]
    log.info(f"After cleaning: {len(df):,} valid rows")
    return df


def stream_reviews(
    producer: KafkaProducer,
    df: pd.DataFrame,
    delay: float = 0.3,
    loop: bool = False,
):
    """
    Send each review as a Kafka message.

    Parameters
    ----------
    producer : KafkaProducer
    df       : DataFrame with clean_review and label columns
    delay    : seconds to wait between messages (simulates real-time)
    loop     : if True, keep streaming the dataset in a loop forever
    """
    iteration = 0
    total_sent = 0

    while True:
        iteration += 1
        log.info(f"── Starting stream pass {iteration} ({len(df)} messages) ──")

        for idx, row in df.iterrows():
            label_raw = row[LABEL_COL]
            label_str = LABEL_MAP.get(label_raw, "Unknown")

            message = {
                "review_id"    : int(total_sent),
                "review_text"  : str(row[TEXT_COL]),
                "true_label"   : label_str,
                "timestamp"    : datetime.now(timezone.utc).isoformat(),
            }

            # Send message — on_delivery callback logs errors
            producer.send(
                KAFKA_TOPIC,
                value=message,
                key=str(total_sent).encode("utf-8"),
            )

            total_sent += 1

            if total_sent % 50 == 0:
                log.info(f"  Sent {total_sent:,} messages so far...")

            time.sleep(delay)

        producer.flush()
        log.info(f"Pass {iteration} complete. Total sent: {total_sent:,}")

        if not loop:
            break

    log.info(f"Producer finished. Total messages sent: {total_sent:,}")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kafka Producer for sentiment reviews")
    parser.add_argument("--broker",  default=KAFKA_BROKER,  help="Kafka broker address")
    parser.add_argument("--topic",   default=KAFKA_TOPIC,   help="Kafka topic name")
    parser.add_argument("--data",    default=DATA_PATH,      help="Path to cleaned_data.xlsx")
    parser.add_argument("--delay",   type=float, default=0.3, help="Delay between messages (seconds)")
    parser.add_argument("--loop",    action="store_true",    help="Loop the dataset continuously")
    args = parser.parse_args()

    KAFKA_TOPIC = args.topic

    producer = create_producer(args.broker)
    df       = load_data(args.data)

    try:
        stream_reviews(producer, df, delay=args.delay, loop=args.loop)
    except KeyboardInterrupt:
        log.info("Producer stopped by user.")
    finally:
        producer.close()
        log.info("Producer connection closed.")
