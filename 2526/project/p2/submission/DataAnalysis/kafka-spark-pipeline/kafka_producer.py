# ============================================================================
# kafka_producer.py — Kafka Producer for Malaysian Telecom Reviews
# ============================================================================
# This script reads cleaned_data.csv and streams each review as a JSON
# message into a Kafka topic, simulating real-time review arrival.
#
# Usage:
#   python kafka_producer.py
#
# The producer sends one message per row with a configurable delay between
# messages. Progress is logged every 500 records, and a final summary is
# printed upon completion.
# ============================================================================

import csv
import json
import time
import sys
import os
from datetime import datetime

from kafka import KafkaProducer
from config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    PRODUCER_DELAY,
    DATA_PATH,
    LOG_DIR,
)


def create_producer():
    """Create and return a KafkaProducer instance with JSON serialization."""
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            acks="all",               # Wait for all replicas to acknowledge
            retries=3,                # Retry on transient failures
            max_block_ms=10000,       # Timeout if Kafka is unreachable
        )
        print(f"[OK] Connected to Kafka at {KAFKA_BOOTSTRAP_SERVERS}")
        return producer
    except Exception as e:
        print(f"[ERROR] Could not connect to Kafka: {e}")
        sys.exit(1)


def stream_reviews(producer, data_path, topic, delay):
    """
    Read the CSV file and send each row as a JSON message to Kafka.

    Message schema:
    {
        "userName":           str,
        "cleaned_content":    str,
        "score":              int,
        "provider":           str,
        "review_date":        str,
        "original_sentiment": str
    }
    """
    sent_count = 0
    skipped_count = 0
    start_time = time.time()
    log_interval = 500  # Print progress every N records

    print(f"\n{'='*60}")
    print(f"  Kafka Producer — Streaming Telecom Reviews")
    print(f"  Topic : {topic}")
    print(f"  Source: {data_path}")
    print(f"  Delay : {delay}s between messages")
    print(f"{'='*60}\n")

    try:
        with open(data_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Skip rows with missing cleaned_content
                cleaned = row.get("cleaned_content", "").strip()
                if not cleaned:
                    skipped_count += 1
                    continue

                # Build the message payload
                message = {
                    "userName": row.get("userName", "Unknown"),
                    "cleaned_content": cleaned,
                    "score": int(row.get("score", 0)),
                    "provider": row.get("provider", "unknown"),
                    "review_date": row.get("at", ""),
                    "original_sentiment": row.get("sentiment", "Unknown"),
                }

                # Send to Kafka
                producer.send(topic, value=message)
                sent_count += 1

                # Progress logging
                if sent_count % log_interval == 0:
                    elapsed = time.time() - start_time
                    rate = sent_count / elapsed if elapsed > 0 else 0
                    print(
                        f"  [PROGRESS] Sent {sent_count:>7,} messages | "
                        f"Elapsed: {elapsed:>7.1f}s | "
                        f"Rate: {rate:>7.1f} msg/s"
                    )

                # Throttle to simulate real-time arrival
                if delay > 0:
                    time.sleep(delay)

        # Flush remaining messages
        producer.flush()

    except FileNotFoundError:
        print(f"[ERROR] Data file not found: {data_path}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[INTERRUPTED] Producer stopped by user.")
        producer.flush()

    # ---- Final Summary ----
    elapsed = time.time() - start_time
    rate = sent_count / elapsed if elapsed > 0 else 0

    summary = (
        f"\n{'='*60}\n"
        f"  PRODUCER SUMMARY\n"
        f"{'='*60}\n"
        f"  Total records sent : {sent_count:,}\n"
        f"  Skipped (empty)    : {skipped_count:,}\n"
        f"  Total time         : {elapsed:.2f} seconds\n"
        f"  Throughput         : {rate:.1f} records/sec\n"
        f"  Finished at        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{'='*60}\n"
    )
    print(summary)

    # Save summary to log file
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, "producer_log.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n--- Run: {datetime.now().isoformat()} ---\n")
        f.write(summary)
    print(f"  Log saved to: {log_file}")

    return sent_count


def main():
    producer = create_producer()
    total = stream_reviews(producer, DATA_PATH, KAFKA_TOPIC, PRODUCER_DELAY)
    producer.close()
    print(f"\n[DONE] Producer finished. {total:,} messages sent to '{KAFKA_TOPIC}'.")


if __name__ == "__main__":
    main()
