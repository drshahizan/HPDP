# Real-Time Sentiment Pipeline (Kafka → Spark → Elasticsearch → Kibana)

End-to-end streaming pipeline for HPDP Project 2. Review messages are streamed
through **Kafka**, classified in real time by the trained **Logistic Regression**
model inside **Spark Structured Streaming**, stored in **Elasticsearch**, and
visualized in **Kibana**.

```
producer.py ──▶ Kafka topic "reviews" ──▶ Spark (TF-IDF + LogReg) ──▶ Elasticsearch ──▶ Kibana
```

## Prerequisites
- Docker + Docker Compose
- Trained model artifacts in `../models/` (run `model_training.ipynb` first):
  `tfidf_vectorizer.joblib`, `logistic_regression.joblib`, `label_map.json`
- Python on host with `kafka-python` + `pandas` (already in the project env) for the producer

## Run it

```bash
cd kafka_spark_pipeline

# 1. Start infrastructure (Kafka, Elasticsearch, Kibana)
docker compose up -d kafka elasticsearch kibana

# 2. Create the Kafka topic (Spark errors if it subscribes before the topic exists)
#    NOTE: run this in PowerShell, NOT Git Bash (Git Bash mangles the /opt/... path).
docker exec hpdp-kafka /opt/kafka/bin/kafka-topics.sh --create --topic reviews --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --if-not-exists

# 3. Start the Spark streaming classifier (builds the Spark image first time)
docker compose up --build spark        # leave running in its own terminal

# 4. Stream the reviews from the host (in another terminal)
uv run python producer.py --rate 20    # 20 reviews/sec
#   --limit 500   send only first 500
#   --rate 0      blast as fast as possible (for throughput tests)
```

Watch the Spark terminal — it prints one line per micro-batch:
`[batch 3] 200 records | 1850.0 rec/s | acc=0.88 | latency=0.4s`

## See the results
- **Kibana**: http://localhost:5601 → Stack Management → Data Views →
  create data view on index `sentiment_reviews` (time field `processed_at`).
- **Raw check**:
  `curl http://localhost:9200/sentiment_reviews/_count`

## Suggested Kibana visualizations (brief §10)
1. Sentiment distribution **pie chart** (`predicted_sentiment`)
2. Sentiment **over time** line chart (`processed_at` × `predicted_sentiment`)
3. Per-app breakdown bar chart (`app_name` × `predicted_sentiment`)
4. Real-time **stream view** (data table sorted by `processed_at` desc, auto-refresh)

Export them to `dashboard/kibana_visualizations.ndjson` for submission
(Stack Management → Saved Objects → Export).

## Batch vs streaming comparison (brief §6.4)
While the live pipeline is running it writes `streaming_metrics.csv` (one row per
micro-batch). Then:

```bash
uv run python benchmark.py
```

prints a batch-vs-streaming table (records, total time, throughput, accuracy,
latency) ready to drop into the report.

## Shut down
```bash
docker compose down          # keep data
docker compose down -v       # also wipe Elasticsearch + caches
```
