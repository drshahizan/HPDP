"""
================================================================================
 Elasticsearch index template setup
 SECP3133 Project 2 · Member 3 (Pipeline & Visualization)
================================================================================

Creates an index template so any future `youtube_sentiment-*` index inherits
the right mapping. Run this once after `docker compose up`, before the Spark
job starts writing documents — otherwise ES will auto-infer types incorrectly
(e.g. mapping `sentiment_label` as a text field instead of keyword, which
breaks Kibana aggregations and pie charts).

────────────────────────────────────────────────────────────────────────────────
 Usage
────────────────────────────────────────────────────────────────────────────────
  python kafka_spark_pipeline/es_setup.py                 # create template + initial index
  python kafka_spark_pipeline/es_setup.py --delete        # nuke and recreate from scratch

  Override the host with ES_HOST=http://host:port (default localhost:9200).
================================================================================
"""

from __future__ import annotations

import argparse
import os
import sys

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

ES_HOST       = os.environ.get("ES_HOST", "http://localhost:9200")
TEMPLATE_NAME = "youtube_sentiment_template"
INDEX_NAME    = "youtube_sentiment"
INDEX_PATTERN = "youtube_sentiment*"

# ── Mapping ─────────────────────────────────────────────────────────────────
# `keyword`  → exact match, aggregations, pie charts, term filters
# `text`     → full-text search, word clouds via significant_text aggs
# `date`     → time-series visualisations
# `float`    → numeric range filters in Kibana
MAPPING = {
    "properties": {
        "comment_id":      {"type": "keyword"},
        "video_id":        {"type": "keyword"},
        "video_title":     {"type": "keyword",
                            "fields": {"text": {"type": "text"}}},
        "comment_text":    {"type": "text"},
        "clean_text":      {"type": "text"},
        "tokens":          {"type": "text"},
        "like_count":      {"type": "integer"},
        "reply_count":     {"type": "integer"},
        "published_at":    {"type": "date"},
        "ingested_at":     {"type": "date"},   # set by producer
        "processed_at":    {"type": "date"},   # set by Spark
        # ── Model outputs ──
        "sentiment_label": {"type": "keyword"},
        "sentiment_score": {"type": "float"},
        "model_used":      {"type": "keyword"},  # "ensemble" / "distilbert" / "logreg"
        # Per-class probabilities for finer dashboard slicing
        "prob_negative":   {"type": "float"},
        "prob_neutral":    {"type": "float"},
        "prob_positive":   {"type": "float"},
    }
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Set up Elasticsearch for the pipeline")
    p.add_argument("--host",   default=ES_HOST,
                   help=f"elasticsearch base URL (default: {ES_HOST})")
    p.add_argument("--delete", action="store_true",
                   help="delete the existing index + template before recreating")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    es = Elasticsearch(args.host, request_timeout=30)
    if not es.ping():
        print(f"[es_setup] ERROR: cannot reach Elasticsearch at {args.host}")
        return 2
    info = es.info()
    print(f"[es_setup] connected: {info['name']} ({info['version']['number']})")

    if args.delete:
        try:
            es.indices.delete(index=INDEX_PATTERN)
            print(f"[es_setup] deleted indices matching {INDEX_PATTERN}")
        except NotFoundError:
            print(f"[es_setup] no existing indices to delete")
        try:
            es.indices.delete_index_template(name=TEMPLATE_NAME)
            print(f"[es_setup] deleted template {TEMPLATE_NAME}")
        except NotFoundError:
            print(f"[es_setup] no existing template to delete")

    # Put the index template — applies to any index matching INDEX_PATTERN
    es.indices.put_index_template(
        name=TEMPLATE_NAME,
        index_patterns=[INDEX_PATTERN],
        priority=100,
        template={
            "settings": {
                "number_of_shards":   1,
                "number_of_replicas": 0,
                "refresh_interval":   "1s",
            },
            "mappings": MAPPING,
        },
    )
    print(f"[es_setup] template '{TEMPLATE_NAME}' upserted "
          f"(pattern: {INDEX_PATTERN})")

    # Create the concrete index so Kibana can immediately discover the data view
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME)
        print(f"[es_setup] created index '{INDEX_NAME}'")
    else:
        print(f"[es_setup] index '{INDEX_NAME}' already exists")

    # Print a verification line
    mapping = es.indices.get_mapping(index=INDEX_NAME)
    n_props = len(mapping[INDEX_NAME]["mappings"].get("properties", {}))
    print(f"[es_setup] mapping has {n_props} fields. ready for ingest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
