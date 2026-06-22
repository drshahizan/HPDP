"""
kafka_producer.py
=================
Reads the cleaned comments CSV and streams each row into the Kafka topic,
one message at a time, with a small delay to simulate a live feed.

Usage:
    python kafka_producer.py --csv youtube_comments_cleaned_roberta.csv \
                             --topic youtube-comments --delay 0.2

    # Stream only the first 500 rows (handy for the batch-vs-streaming test):
    python kafka_producer.py --limit 500 --delay 0
"""

import argparse
import json
import time

import pandas as pd
from kafka import KafkaProducer

DEFAULT_BOOTSTRAP = "localhost:9092"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="youtube_comments_cleaned_roberta.csv")
    ap.add_argument("--topic", default="youtube-comments")
    ap.add_argument("--bootstrap", default=DEFAULT_BOOTSTRAP)
    ap.add_argument("--text-col", default="cleaned_text")
    ap.add_argument("--label-col", default="sentiment",
                    help="ground-truth column, sent along for accuracy checks")
    ap.add_argument("--delay", type=float, default=0.2,
                    help="seconds between messages (0 = as fast as possible)")
    ap.add_argument("--limit", type=int, default=0,
                    help="stop after N messages (0 = all rows)")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    df = df.dropna(subset=[args.text_col])
    if args.limit:
        df = df.head(args.limit)
    print(f"Loaded {len(df):,} rows from {args.csv}")

    producer = KafkaProducer(
        bootstrap_servers=args.bootstrap,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        linger_ms=10,
    )

    sent = 0
    for idx, row in df.iterrows():
        msg = {
            "id": int(idx),
            "text": str(row[args.text_col]),
            "true_sentiment": (str(row[args.label_col])
                               if args.label_col in df.columns else None),
            "event_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        producer.send(args.topic, value=msg)
        sent += 1
        if sent % 100 == 0:
            print(f"  sent {sent:,} messages...")
        if args.delay:
            time.sleep(args.delay)

    producer.flush()
    producer.close()
    print(f"Done. {sent:,} messages sent to topic '{args.topic}'.")


if __name__ == "__main__":
    main()
