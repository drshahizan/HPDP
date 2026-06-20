"""
elasticsearch/setup_index.py
=============================
Creates the Elasticsearch index 'sentiment_results' with proper
field mappings before the Spark consumer starts writing.

Run once before starting the Spark job:
  python elasticsearch/setup_index.py
"""

import json
import time
import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [ES-SETUP] %(levelname)s — %(message)s",
)
log = logging.getLogger(__name__)

ES_HOST  = "http://localhost:9200"   # change to http://elasticsearch:9200 inside Docker
ES_INDEX = "sentiment_results"


INDEX_MAPPING = {
    "settings": {
        "number_of_shards":   1,
        "number_of_replicas": 0,
        "refresh_interval":   "1s",
    },
    "mappings": {
        "properties": {
            "review_id": {
                "type": "integer"
            },
            "review_text": {
                "type":     "text",
                "analyzer": "english",
                "fields": {
                    "keyword": {"type": "keyword", "ignore_above": 512}
                }
            },
            "true_label": {
                "type": "keyword"
            },
            "predicted_sentiment": {
                "type": "keyword"
            },
            "predicted_label": {
                "type": "integer"
            },
            "is_correct": {
                "type": "keyword"
            },
            "pipeline_version": {
                "type": "keyword"
            },
            "source_timestamp": {
                "type":   "date",
                "format": "strict_date_optional_time||epoch_millis"
            },
            "processed_at": {
                "type":   "date",
                "format": "strict_date_optional_time||epoch_millis"
            },
            "throughput_rps": {
                "type": "float"
            },
            "batch_size": {
                "type": "integer"
            },
            "kafka_offset": {
                "type": "long"
            },
            "kafka_partition": {
                "type": "integer"
            },
            "kafka_ingest_time": {
                "type":   "date",
                "format": "strict_date_optional_time||epoch_millis"
            },
        }
    }
}


def wait_for_elasticsearch(host: str, max_retries: int = 20):
    """Poll until Elasticsearch is reachable."""
    for attempt in range(1, max_retries + 1):
        try:
            r = requests.get(f"{host}/_cluster/health", timeout=5)
            if r.status_code == 200:
                log.info(f"Elasticsearch is up (attempt {attempt}).")
                return
        except requests.exceptions.ConnectionError:
            pass
        log.warning(f"Elasticsearch not ready yet (attempt {attempt}/{max_retries}). Retrying in 5s...")
        time.sleep(5)
    raise RuntimeError(f"Cannot reach Elasticsearch at {host}")


def create_index(host: str, index: str, mapping: dict):
    """Create the index, skip if it already exists."""
    url = f"{host}/{index}"

    # Check if index exists
    r = requests.head(url, timeout=5)
    if r.status_code == 200:
        log.info(f"Index '{index}' already exists — skipping creation.")
        return

    # Create the index
    r = requests.put(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(mapping),
        timeout=10,
    )
    if r.status_code in (200, 201):
        log.info(f"Index '{index}' created successfully.")
        log.info(json.dumps(r.json(), indent=2))
    else:
        log.error(f"Failed to create index: {r.status_code} — {r.text}")
        raise RuntimeError("Index creation failed.")


def verify_index(host: str, index: str):
    """Print a summary of the created index."""
    r = requests.get(f"{host}/{index}/_stats", timeout=5)
    if r.status_code == 200:
        stats = r.json()
        docs  = stats["indices"][index]["total"]["docs"]["count"]
        log.info(f"Index '{index}' verified. Current doc count: {docs}")
    else:
        log.warning(f"Could not retrieve index stats: {r.status_code}")


if __name__ == "__main__":
    wait_for_elasticsearch(ES_HOST)
    create_index(ES_HOST, ES_INDEX, INDEX_MAPPING)
    verify_index(ES_HOST, ES_INDEX)
    log.info("ES setup complete. You can now start the Spark consumer.")
