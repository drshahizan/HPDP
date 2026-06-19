"""
setup_index.py
==============
Creates the Elasticsearch index using elastic_mappings.json.
Run this ONCE before starting the Spark job.

    python setup_index.py --index sentiment-results
    python setup_index.py --index sentiment-results --recreate   # wipe + rebuild
"""

import argparse
import json

from elasticsearch import Elasticsearch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--es", default="http://localhost:9200")
    ap.add_argument("--index", default="sentiment-results")
    ap.add_argument("--mapping", default="elastic_mappings.json")
    ap.add_argument("--recreate", action="store_true",
                    help="delete the index first if it exists")
    args = ap.parse_args()

    es = Elasticsearch(args.es)
    if not es.ping():
        raise SystemExit(f"Cannot reach Elasticsearch at {args.es}. "
                         "Is the container up? (docker compose ps)")

    with open(args.mapping) as f:
        body = json.load(f)

    if es.indices.exists(index=args.index):
        if args.recreate:
            es.indices.delete(index=args.index)
            print(f"Deleted existing index '{args.index}'.")
        else:
            print(f"Index '{args.index}' already exists. "
                  "Use --recreate to wipe it.")
            return

    es.indices.create(index=args.index, body=body)
    print(f"Created index '{args.index}'.")


if __name__ == "__main__":
    main()
