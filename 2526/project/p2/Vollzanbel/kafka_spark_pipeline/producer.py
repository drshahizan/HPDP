"""Kafka producer — replays cleaned_data.csv into the `reviews` topic to
simulate a real-time stream of app reviews.

Run on the host (after `docker compose up -d kafka`):
    uv run python kafka_spark_pipeline/producer.py --rate 20
    uv run python kafka_spark_pipeline/producer.py --limit 500 --rate 50

--rate  messages per second (0 = as fast as possible)
--limit max messages to send (0 = whole file)
"""
import argparse
import json
import time
from pathlib import Path

import pandas as pd
from kafka import KafkaProducer

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cleaned_data.csv"

FIELDS = ["review_id", "app_name", "cleaned_text", "rating",
          "review_date", "sentiment_label"]  # sentiment_label = ground truth, for accuracy checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bootstrap", default="localhost:9092")
    ap.add_argument("--topic", default="reviews")
    ap.add_argument("--rate", type=float, default=20.0, help="messages/sec (0=max)")
    ap.add_argument("--limit", type=int, default=0, help="max messages (0=all)")
    args = ap.parse_args()

    df = pd.read_csv(DATA, usecols=lambda c: c in FIELDS)
    df = df[df["cleaned_text"].notna()]
    if args.limit:
        df = df.head(args.limit)

    producer = KafkaProducer(
        bootstrap_servers=args.bootstrap,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        linger_ms=50,
    )

    delay = 1.0 / args.rate if args.rate > 0 else 0.0
    sent = 0
    t0 = time.time()
    print(f"Streaming {len(df)} reviews -> {args.bootstrap} topic '{args.topic}' "
          f"(rate={args.rate}/s)")
    try:
        for rec in df.to_dict(orient="records"):
            rec["sent_at"] = time.time()       # for end-to-end latency measurement
            producer.send(args.topic, rec)
            sent += 1
            if sent % 500 == 0:
                print(f"  sent {sent} ...")
            if delay:
                time.sleep(delay)
    finally:
        producer.flush()
        producer.close()
    dt = time.time() - t0
    print(f"Done. Sent {sent} messages in {dt:.1f}s ({sent/dt:.1f} msg/s).")


if __name__ == "__main__":
    main()
