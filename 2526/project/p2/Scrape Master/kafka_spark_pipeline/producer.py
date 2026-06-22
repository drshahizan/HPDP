"""
================================================================================
 Kafka Producer  —  FUZZ CHANNEL Sentiment Pipeline
 SECP3133 Project 2 · Member 3 (Pipeline & Visualization)
================================================================================

Streams rows from cleaned_data.csv into a Kafka topic, one JSON message per
comment, throttled at a configurable rate. Used to feed the Spark Structured
Streaming consumer (spark_streaming.py) for real-time sentiment classification.

The message body intentionally includes BOTH text variants Member 1 produced:
    clean_text     — light cleaning, for the transformer model
    tokens         — normalized + stemmed, for the TF-IDF Logistic Regression
…so the Spark side can dispatch on whichever model is selected by
models/best_model_info.json without extra preprocessing.

────────────────────────────────────────────────────────────────────────────────
 Usage
────────────────────────────────────────────────────────────────────────────────
  python pipeline/producer.py                 # default: 50 msg/s, all rows
  python pipeline/producer.py --rate 200      # faster
  python pipeline/producer.py --limit 500     # smoke-test mode
  python pipeline/producer.py --loop          # loop forever (good for demos)
  python pipeline/producer.py --topic foo     # custom topic

  Override the broker with KAFKA_BOOTSTRAP=host:port (default localhost:9092).
================================================================================
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import signal
import sys
import time
import warnings
from datetime import datetime, timezone
from pathlib import Path

# kafka-python 3.x emits a DeprecationWarning for the lambda serializers we
# pass in — they work fine, the warning is just noise on every run.
warnings.filterwarnings("ignore", category=DeprecationWarning, module=r"kafka(\..*)?")
logging.getLogger("kafka").setLevel(logging.ERROR)

import pandas as pd
from kafka import KafkaProducer
# kafka-python renamed/restructured connection errors between 2.x and 3.x.
# Catch the broadest connection-time error class that exists on either.
try:
    from kafka.errors import NoBrokersAvailable as _ConnectError
except ImportError:
    from kafka.errors import KafkaConnectionError as _ConnectError

# ── Configuration ───────────────────────────────────────────────────────────
DEFAULT_TOPIC     = "youtube-comments-raw"
DEFAULT_BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
DEFAULT_CSV       = Path(__file__).resolve().parent.parent / "cleaned_data.csv"

# Columns sent downstream. Everything else in the CSV is dropped to keep the
# message small (Kafka throughput is bytes-per-second).
PAYLOAD_COLS = [
    "comment_id",
    "video_id",
    "video_title",
    "comment_text",      # original text — useful for the dashboard tooltip
    "clean_text",        # transformer input
    "tokens",            # logistic regression input
    "like_count",
    "reply_count",
    "published_at",      # ISO timestamp the comment was posted
]


def build_producer(bootstrap: str) -> KafkaProducer:
    """Connect to Kafka with sensible production-ish defaults for dev use."""
    return KafkaProducer(
        bootstrap_servers=bootstrap,
        value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8"),
        key_serializer=lambda k: k.encode("utf-8") if k else None,
        # acks=1 = leader-ack, good balance between throughput and durability
        acks=1,
        linger_ms=10,        # micro-batch up to 10 ms for better throughput
        compression_type="gzip",
    )


def load_dataframe(path: Path) -> pd.DataFrame:
    print(f"[producer] loading {path} ...")
    df = pd.read_csv(path, encoding="utf-8-sig")
    df = df.dropna(subset=["comment_id", "comment_text"]).copy()
    df = df.reset_index(drop=True)
    # Make sure every payload column exists so the message schema is stable
    for col in PAYLOAD_COLS:
        if col not in df.columns:
            df[col] = None
    print(f"[producer] loaded {len(df):,} rows")
    return df[PAYLOAD_COLS]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Stream cleaned_data.csv to Kafka")
    p.add_argument("--csv",       default=str(DEFAULT_CSV),
                   help=f"path to cleaned_data.csv (default: {DEFAULT_CSV})")
    p.add_argument("--bootstrap", default=DEFAULT_BOOTSTRAP,
                   help=f"kafka bootstrap servers (default: {DEFAULT_BOOTSTRAP})")
    p.add_argument("--topic",     default=DEFAULT_TOPIC,
                   help=f"kafka topic to write to (default: {DEFAULT_TOPIC})")
    p.add_argument("--rate", type=float, default=50.0,
                   help="messages per second (default: 50). Use 0 for unthrottled.")
    p.add_argument("--limit", type=int, default=None,
                   help="only send N rows (default: all)")
    p.add_argument("--offset", type=int, default=0,
                   help="skip the first N rows before sending (default: 0). "
                        "Useful for benchmarks that must avoid replaying already-indexed comment_ids.")
    p.add_argument("--loop",  action="store_true",
                   help="when EOF reached, restart from the top (good for demos)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    df = load_dataframe(Path(args.csv))
    if args.offset:
        df = df.iloc[args.offset:].reset_index(drop=True)
        print(f"[producer] skipped first {args.offset:,} rows (offset)")
    if args.limit:
        df = df.head(args.limit)
        print(f"[producer] limited to {args.limit:,} rows")

    try:
        producer = build_producer(args.bootstrap)
    except _ConnectError:
        print(f"[producer] ERROR: no Kafka broker at {args.bootstrap}.")
        print("           did you 'docker compose up -d'?")
        return 2

    # Graceful Ctrl-C
    stopping = {"flag": False}
    def _on_sigint(*_):
        print("\n[producer] Ctrl-C — flushing and exiting ...")
        stopping["flag"] = True
    signal.signal(signal.SIGINT, _on_sigint)

    sleep_per_msg = (1.0 / args.rate) if args.rate > 0 else 0.0
    total_sent    = 0
    started_at    = time.time()
    print(f"[producer] streaming to topic '{args.topic}' at "
          f"{args.rate if args.rate > 0 else 'unthrottled'} msg/s "
          f"(loop={args.loop}) ...")

    while not stopping["flag"]:
        for record in df.itertuples(index=False):
            if stopping["flag"]:
                break
            msg = {col: getattr(record, col) for col in PAYLOAD_COLS}
            # Add an "ingested_at" stamp so we can measure end-to-end latency
            msg["ingested_at"] = datetime.now(timezone.utc).isoformat()
            producer.send(args.topic, key=msg["comment_id"], value=msg)
            total_sent += 1
            if total_sent % 500 == 0:
                rate = total_sent / max(time.time() - started_at, 1e-6)
                print(f"[producer]   sent {total_sent:>6,}   "
                      f"({rate:>6.1f} msg/s avg)")
            if sleep_per_msg:
                time.sleep(sleep_per_msg)
        if not args.loop:
            break
        print("[producer] EOF — looping back to start")

    producer.flush(timeout=30)
    producer.close(timeout=10)
    elapsed = time.time() - started_at
    print(f"[producer] done. sent {total_sent:,} messages in {elapsed:.1f}s "
          f"({total_sent/max(elapsed,1e-6):.1f} msg/s avg)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
