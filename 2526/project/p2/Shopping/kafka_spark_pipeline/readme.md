# Project 2 — Real-Time Sentiment Analysis Pipeline
## Kafka + CNN + Elasticsearch + Kibana

---

## Folder Structure

```
kafka_spark_pipeline/
├── docker-compose.yml          ← starts all services
├── producer.py                 ← streams data to Kafka
├── cnn_stream_consumer.py      ← CNN inference → Elasticsearch (streaming)
├── cnn_batch_consumer.py       ← CNN inference → Elasticsearch (batch)
├── setup_index.py              ← creates Elasticsearch index
├── elastic_mappings.json       ← Elasticsearch schema
├── spark_consumer.py           ← Spark version (reference)
├── spark_streaming_local.py    ← Spark local version (reference)
├── requirements.txt            ← Python dependencies
├── readme.md                   ← this file
├── data/
│   └── cleaned_data.csv         ← cleaned Malaysian reviews dataset
└── models/
    ├── best_cnn_sentiment.keras  ← trained CNN model
    └── cnn_tokenizer.pkl         ← CNN tokenizer
```

---

## Prerequisites

Make sure you have all of these before starting:

- **Docker Desktop** installed and running
- **Python 3.10+** installed
- At least **6 GB RAM** free
- The `models/` folder with both model files (get from Ru Qian)

---

## Step 1 — Install Python Dependencies

Open a terminal in the `kafka_spark_pipeline/` folder and run:

```bash
pip install kafka-python-ng pandas numpy requests tensorflow
```

---

## Step 2 — Start Docker Services

```bash
docker compose up -d zookeeper kafka kafka-init elasticsearch kibana
```

This starts 5 services:

| Service       | URL                    | Purpose                        |
|---------------|------------------------|--------------------------------|
| Zookeeper     | localhost:2181         | Kafka dependency               |
| Kafka         | localhost:9092         | Message broker                 |
| kafka-init    | —                      | Auto-creates `sentiment-stream` topic |
| Elasticsearch | http://localhost:9200  | Stores sentiment results       |
| Kibana        | http://localhost:5601  | Dashboard & visualization UI   |

Wait **60 seconds** for all services to fully start, then verify Elasticsearch is ready:

```bash
curl http://localhost:9200/_cluster/health
```

Expected: `"status":"yellow"` or `"status":"green"`.

> The Kafka topic `sentiment-stream` is created automatically by `kafka-init`. You do not need to create it manually.

---

## Step 3 — Create Elasticsearch Index

Run this **once** before starting the pipeline:

```bash
python setup_index.py
```

Expected output:
```
Elasticsearch is up
Index 'sentiment_results' created successfully.
ES setup complete. You can now start the consumer.
```

---

## Step 4 — Run the Pipeline

You need **3 terminals** open at the same time, all in the `kafka_spark_pipeline/` folder.

### Terminal 1 — Start CNN Streaming Consumer

```bash
python cnn_stream_consumer.py
```

Wait until you see:
```
CNN Streaming started! Waiting for data...
Now run producer.py in another terminal
```

### Terminal 2 — Start Kafka Producer

```bash
python producer.py --data data/cleaned_data.csv --delay 0.3
```

Optional flags:
```bash
--delay 0.5     # slow down (default: 0.3s between messages)
--loop          # keep streaming the dataset on repeat
```

### What you should see

**Terminal 2 (Producer):**
```
[PRODUCER] INFO — Sent 50 messages so far...
[PRODUCER] INFO — Sent 100 messages so far...
```

**Terminal 1 (Consumer):**
```
[CNN-CONSUMER] INFO — [Positive |+1] (true=Positive ) correct=True  | batu cave unforgettable blend...
[CNN-CONSUMER] INFO — [Negative |-1] (true=Negative ) correct=True  | terrible experience food cold...
[CNN-CONSUMER] INFO — Written 10 records to Elasticsearch.
[CNN-CONSUMER] INFO — Total processed: 10 | Throughput: 3.2 records/sec
```

Each record written to Elasticsearch contains:

| Field                | Type    | Description                              |
|----------------------|---------|------------------------------------------|
| `review_id`          | integer | Unique review ID                         |
| `review_text`        | text    | Original review text                     |
| `true_label`         | keyword | Ground truth: Negative / Neutral / Positive |
| `predicted_sentiment`| keyword | CNN prediction: Negative / Neutral / Positive |
| `predicted_label`    | integer | CNN prediction as integer: **-1 / 0 / 1** |
| `is_correct`         | keyword | `"True"` or `"False"`                   |
| `throughput_rps`     | float   | Records processed per second             |
| `batch_size`         | integer | Batch size when this record was written  |
| `pipeline_version`   | keyword | `"cnn_v1"`                              |
| `processed_at`       | date    | Timestamp when CNN processed this record |
| `source_timestamp`   | date    | Timestamp when producer sent the message |

---

## Step 5 — Verify Data in Elasticsearch

Check total documents stored:

```bash
curl http://localhost:9200/sentiment_results/_count
```

Browse actual records (returns first 10):

```
http://localhost:9200/sentiment_results/_search?pretty
```

Check sentiment distribution:

```bash
curl -X POST "http://localhost:9200/sentiment_results/_search?pretty" -H "Content-Type: application/json" -d "{\"size\":0,\"aggs\":{\"sentiments\":{\"terms\":{\"field\":\"predicted_sentiment\"}}}}"
```

---

## Step 6 — Build Kibana Dashboard

Open **http://localhost:5601** in your browser.

### 6.1 — Create a Data View

1. Go to **Menu (☰) → Management → Stack Management**
2. Under Kibana, click **Data Views**
3. Click **Create data view**
4. Name: `sentiment_results`
5. Index pattern: `sentiment_results`
6. Timestamp field: `processed_at`
7. Click **Save data view to Kibana**

## Step 7 — Stop Everything

Press `Ctrl+C` in both terminals, then stop Docker:

```bash
docker compose down
```

To also delete all Elasticsearch stored data:

```bash
docker compose down -v
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Docker containers don't appear | Make sure Docker Desktop is running, then retry `docker compose up -d` |
| `NoBrokersAvailable` error | Wait 30 more seconds — Kafka takes time to start |
| `index_not_found_exception` in ES | Run `python setup_index.py` first |
| Model file not found | Ensure `models/best_cnn_sentiment.keras` and `models/cnn_tokenizer.pkl` exist |
| Kibana shows no data | Check consumer is running and has written records: `curl http://localhost:9200/sentiment_results/_count` |
| Port already in use | Run `docker compose down` then `docker compose up -d` again |
| ES returns connection refused | Wait longer — ES takes ~45s to boot |

---

## Pipeline Architecture

```
cleaned_data.csv
      ↓
 producer.py              (Kafka Producer — streams reviews row by row)
      ↓
 Kafka Topic              (sentiment-stream, 3 partitions)
      ↓
cnn_stream_consumer.py    (CNN inference, batches of 10)
      ↓
 Elasticsearch            (index: sentiment_results)
      ↓
   Kibana                 (Dashboard at http://localhost:5601)
```

---

## Label Scale Reference

The dataset uses **-1 / 0 / 1** labels. The CNN model outputs class indices **0 / 1 / 2**, which are remapped to match:

| Dataset label | Meaning  | CNN class | `predicted_label` in ES |
|---------------|----------|-----------|--------------------------|
| -1            | Negative | 0         | -1                       |
|  0            | Neutral  | 1         |  0                       |
|  1            | Positive | 2         |  1                       |

---

## Technologies Used

| Technology       | Role                                  |
|------------------|---------------------------------------|
| Apache Kafka     | Real-time message streaming           |
| CNN (TensorFlow) | Sentiment classification model        |
| Elasticsearch    | Storage and fast querying             |
| Kibana           | Dashboard and visualization           |
| Docker           | Container orchestration for services  |
