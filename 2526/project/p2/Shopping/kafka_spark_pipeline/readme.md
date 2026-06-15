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
│   └── cleaned_data.csv        ← cleaned Malaysian reviews dataset
└── models/
    ├── best_cnn_sentiment.keras ← trained CNN model
    └── cnn_tokenizer.pkl        ← CNN tokenizer
```

---

## Prerequisites

Before starting, make sure you have:

- **Docker Desktop** installed and running → https://www.docker.com/products/docker-desktop
- **Python 3.10+** installed → https://www.python.org/downloads
- **Anaconda** (recommended) → https://www.anaconda.com/download
- At least **6GB RAM** available
- The `models/` folder with both model files (get from group member)

---

## Step 1 — Install Python Dependencies

Open terminal/PowerShell in the `kafka_spark_pipeline/` folder:

```bash
pip install kafka-python-ng pandas numpy scikit-learn requests tensorflow
```

Or using conda:

```bash
conda install -c conda-forge pandas numpy scikit-learn requests
pip install kafka-python-ng tensorflow
```

---

## Step 2 — Start Docker Services

```bash
docker-compose up -d
```

This starts 5 services:

| Service       | URL                   | Purpose                  |
|---------------|-----------------------|--------------------------|
| Zookeeper     | localhost:2181        | Kafka dependency         |
| Kafka         | localhost:9092        | Message broker           |
| Elasticsearch | http://localhost:9200 | Stores sentiment results |
| Kibana        | http://localhost:5601 | Dashboard UI             |
| Spark Master  | http://localhost:8082 | Spark Web UI             |

Wait **60 seconds** for all services to fully start.

Verify Elasticsearch is ready:

```bash
curl http://localhost:9200/_cluster/health
```

Should show `"status":"yellow"` or `"status":"green"`.

---

## Step 3 — Create Kafka Topic

```bash
docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --create --topic sentiment-stream --partitions 3 --replication-factor 1
```

Verify topic was created:

```bash
docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --list
```

Should show `sentiment-stream`.

---

## Step 4 — Create Elasticsearch Index

```bash
python setup_index.py
```

Expected output:
```
Elasticsearch is up
Index 'sentiment_results' created successfully.
ES setup complete.
```

---

## Step 5 — Run the Pipeline

You need **two terminals** open at the same time.

### Terminal 1 — Start CNN Consumer

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
python producer.py --data data/cleaned_data.csv --delay 0.5
```

You will see messages being sent:
```
[PRODUCER] INFO — Sent 50 messages so far...
[PRODUCER] INFO — Sent 100 messages so far...
```

And in Terminal 1 you will see CNN predictions:
```
[CNN-CONSUMER] INFO — [Positive ] (true=Positive ) correct=True  | batu cave unforgettable blend...
[CNN-CONSUMER] INFO — [Negative ] (true=Negative ) correct=True  | terrible experience food cold...
[CNN-CONSUMER] INFO — Written 10 records to Elasticsearch.
```

---

## Step 6 — Build Kibana Dashboard

1. Open **http://localhost:5601** in your browser
2. Go to **Menu → Stack Management → Index Patterns**
3. Click **Create index pattern**
4. Enter `sentiment_results` → Next
5. Select `processed_at` as the time field → Create

Then go to **Menu → Dashboard → Create Dashboard** and add these visualizations:

### Visualization 1 — Sentiment Distribution (Pie Chart)
- Create visualization → Pie
- Field: `predicted_sentiment`
- This shows % of Positive / Neutral / Negative

### Visualization 2 — Sentiment Over Time (Line Chart)
- Create visualization → Line
- X-axis: `processed_at` (date histogram)
- Y-axis: Count
- Split series by: `predicted_sentiment`

### Visualization 3 — Accuracy Metric
- Create visualization → Metric
- Filter: `is_correct: "True"`
- Shows total correct predictions

### Visualization 4 — Recent Reviews Table
- Create visualization → Data Table
- Columns: `review_text`, `predicted_sentiment`, `true_label`, `is_correct`, `processed_at`

---

## Step 7 — Verify Data in Elasticsearch

Check total documents indexed:

```bash
curl http://localhost:9200/sentiment_results/_count
```

Check sentiment distribution:

```bash
curl -X POST "http://localhost:9200/sentiment_results/_search?pretty" -H "Content-Type: application/json" -d "{\"size\":0,\"aggs\":{\"sentiment_counts\":{\"terms\":{\"field\":\"predicted_sentiment\"}}}}"
```

---

## Stop Everything

```bash
# Press Ctrl+C in both terminals first, then:
docker-compose down
```

To also delete Elasticsearch data:

```bash
docker-compose down -v
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `docker-compose up` fails | Make sure Docker Desktop is running |
| Kafka not ready | Wait 30 more seconds and retry |
| `NoBrokersAvailable` error | Check `docker ps` — kafka container must be running |
| ES connection refused | Run `curl http://localhost:9200` to check |
| Model file not found | Make sure `models/` folder has both `.keras` and `.pkl` files |
| Port already in use | Run `docker-compose down` then `docker-compose up -d` again |

---

## Pipeline Architecture

```
cleaned_data.csv
      ↓
 producer.py          (Kafka Producer)
      ↓
 Kafka Topic          (sentiment-stream)
      ↓
cnn_stream_consumer.py (CNN Model Inference)
      ↓
 Elasticsearch        (sentiment_results index)
      ↓
   Kibana             (Dashboard & Visualization)
```

---

## Technologies Used

| Technology | Role |
|---|---|
| Apache Kafka | Real-time message streaming |
| CNN (TensorFlow/Keras) | Sentiment classification model |
| Elasticsearch | Storage and fast querying |
| Kibana | Dashboard and visualization |
| Apache Spark | Batch processing and pipeline reference |
| Docker | Container orchestration |
