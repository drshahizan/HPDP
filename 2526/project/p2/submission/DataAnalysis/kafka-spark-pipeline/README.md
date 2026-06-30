# Kafka-Spark Streaming Pipeline — Malaysian Telecom Sentiment Analysis

This module (built by **Member 2**) implements the real-time streaming pipeline for sentiment analysis of Malaysian telecommunication app reviews. It uses:

- **Apache Kafka** to stream review data
- **Apache Spark Structured Streaming** to consume and process messages
- **Member 1's pre-trained model** (TF-IDF + Logistic Regression) to predict sentiment
- **Elasticsearch** to store classified results for Kibana visualization

---

## Architecture

```
cleaned_data.csv                    
       │                            
       ▼                            
┌──────────────┐   JSON msgs   ┌─────────────────┐   foreachBatch   ┌───────────────────┐
│ Kafka        │ ────────────► │ Spark Structured │ ──────────────► │  Elasticsearch    │
│ Producer     │               │ Streaming        │                 │  telecom-sentiment│
│              │               │                  │                 │                   │
│ (row by row) │               │ TF-IDF + LR      │                 │  ──► Kibana       │
└──────────────┘               │ Model Prediction │                 └───────────────────┘
                               └─────────────────┘                 
```

---

## Option A: Docker Compose (Recommended)

The easiest way to run the full pipeline. Docker Compose spins up **everything** (Zookeeper, Kafka, Elasticsearch, Kibana) in containers.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

### Quick Start

```powershell
cd "c:\hpdp project\kafka-spark-pipeline"

# 1. Start all infrastructure services
docker-compose up -d zookeeper kafka elasticsearch kibana

# 2. Wait ~30 seconds for services to become healthy, then check
docker-compose ps

# 3. Start the Spark Streaming consumer
docker-compose run spark-streaming

# 4. In a NEW terminal — start the Kafka Producer
docker-compose run kafka-producer
```

### Access Points

| Service | URL |
|---|---|
| Elasticsearch | http://localhost:9200 |
| Kibana | http://localhost:5601 |
| Kafka (external) | localhost:9092 |

### Teardown

```powershell
docker-compose down -v   # Stops containers and removes volumes
```

---

## Option B: Manual Installation

If you prefer to run each service locally without Docker, follow the steps below.

### Prerequisites

| Software | Version | Download |
|---|---|---|
| Python | 3.8+ | https://www.python.org/downloads/ |
| Java JDK | 8 or 11 | https://adoptium.net/ |
| Apache Kafka | 3.x | https://kafka.apache.org/downloads |
| Apache Spark | 3.5.x | https://spark.apache.org/downloads.html |
| Elasticsearch | 8.x | https://www.elastic.co/downloads/elasticsearch |
| Kibana | 8.x | https://www.elastic.co/downloads/kibana |

### Python Packages

```bash
pip install kafka-python pandas joblib scikit-learn pyspark
```

---

## Step 1: Install & Start Elasticsearch

Since Elasticsearch is not yet installed, follow these steps:

### 1.1 Download Elasticsearch

1. Go to https://www.elastic.co/downloads/elasticsearch
2. Download the **Windows zip** package (e.g., `elasticsearch-8.14.0-windows-x86_64.zip`)
3. Extract to a convenient location, e.g., `C:\elasticsearch`

### 1.2 Configure Elasticsearch (Disable Security for Local Dev)

Edit `C:\elasticsearch\config\elasticsearch.yml` and add/modify these lines:

```yaml
# Disable security for local development (DO NOT use in production)
xpack.security.enabled: false
xpack.security.http.ssl.enabled: false

# Network settings
network.host: localhost
http.port: 9200
```

### 1.3 Start Elasticsearch

```powershell
cd C:\elasticsearch
.\bin\elasticsearch.bat
```

Verify it's running:

```powershell
curl http://localhost:9200
```

You should see a JSON response with `"tagline" : "You Know, for Search"`.

### 1.4 (Optional) Install Kibana

1. Download from https://www.elastic.co/downloads/kibana
2. Extract to `C:\kibana`
3. Start: `.\bin\kibana.bat`
4. Open http://localhost:5601 in your browser

---

## Step 2: Start Kafka

### 2.1 Start Zookeeper

```powershell
cd C:\kafka
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```

### 2.2 Start Kafka Broker

Open a **new terminal**:

```powershell
cd C:\kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

### 2.3 Create the Kafka Topic

Open a **new terminal**:

```powershell
cd C:\kafka
.\bin\windows\kafka-topics.bat --create --topic telecom-reviews --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

Verify the topic was created:

```powershell
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

---

## Step 3: Run the Pipeline

### 3.1 Start the Spark Streaming Consumer (Terminal 1)

Start the consumer **first** so it's ready to receive messages:

```powershell
cd "c:\hpdp project\kafka-spark-pipeline"

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,org.elasticsearch:elasticsearch-spark-30_2.12:8.14.0 spark_streaming.py
```

You should see:
```
[OK] SparkSession created.
[OK] Subscribed to Kafka topic.
[OK] Streaming query started. Waiting for messages...
```

### 3.2 Start the Kafka Producer (Terminal 2)

Open a **new terminal** and start streaming reviews:

```powershell
cd "c:\hpdp project\kafka-spark-pipeline"
python kafka_producer.py
```

You will see progress logs like:
```
[PROGRESS] Sent   500 messages | Elapsed:    25.3s | Rate:   19.8 msg/s
[PROGRESS] Sent 1,000 messages | Elapsed:    50.5s | Rate:   19.8 msg/s
```

Meanwhile, the Spark terminal will show batch processing:
```
[Batch 1] Processing 47 records...
[Batch 1] ✓ Done — 47 records in 1.23s (38 rec/s)
```

### 3.3 Stop the Pipeline

Press `Ctrl+C` in both terminals when done. Both scripts will print a final performance summary and save logs to the `logs/` directory.

> **Tip**: For a quick test, you can increase the producer delay in `config.py` or stop the producer early with Ctrl+C after a few hundred messages.

---

## Step 4: Verify Results in Elasticsearch

### Check document count:

```powershell
curl http://localhost:9200/telecom-sentiment/_count
```

### View a sample document:

```powershell
curl "http://localhost:9200/telecom-sentiment/_search?size=1&pretty"
```

### Check prediction accuracy (match rate):

```powershell
curl -X POST "http://localhost:9200/telecom-sentiment/_search?pretty" -H "Content-Type: application/json" -d "{\"size\": 0, \"aggs\": {\"match_rate\": {\"terms\": {\"field\": \"match\"}}}}"
```

---

## Step 5: Kibana Dashboard (Member 3)

Once the Elasticsearch index is populated, Member 3 can create Kibana dashboards by:

1. Opening http://localhost:5601
2. Going to **Stack Management → Data Views** and creating a data view for `telecom-sentiment`
3. Building visualizations for:
   - Sentiment distribution (pie chart)
   - Provider-wise sentiment (bar chart)
   - Prediction accuracy (match rate)
   - Reviews over time (timeline)

---

## File Structure

```
kafka-spark-pipeline/
├── config.py              # Central configuration (Kafka, Spark, ES settings)
├── kafka_producer.py      # Kafka producer — streams CSV rows to Kafka
├── spark_streaming.py     # Spark consumer — predicts sentiment, writes to ES
├── docker-compose.yml     # Docker Compose for full infrastructure
├── Dockerfile             # Container image for the pipeline app
├── requirements.txt       # Pinned Python dependencies
├── logs/                  # Auto-generated logs and metrics
│   ├── .gitkeep
│   ├── producer_log.txt   # (generated at runtime)
│   ├── streaming_log.txt  # (generated at runtime)
│   └── checkpoints/       # (Spark checkpoint directory)
└── README.md              # This file
```

---

## Configuration Reference

All settings are in [`config.py`](config.py):

| Parameter | Default | Description |
|---|---|---|
| `KAFKA_BOOTSTRAP_SERVERS` | `localhost:9092` | Kafka broker address |
| `KAFKA_TOPIC` | `telecom-reviews` | Kafka topic name |
| `PRODUCER_DELAY` | `0.05` | Seconds between messages (0.05 = ~20 msg/s) |
| `SPARK_APP_NAME` | `TelecomSentimentStreaming` | Spark application name |
| `ES_HOST` | `localhost` | Elasticsearch host |
| `ES_PORT` | `9200` | Elasticsearch port |
| `ES_INDEX` | `telecom-sentiment` | Target Elasticsearch index |

---

## Troubleshooting

| Issue | Solution |
|---|---|
| `kafka.errors.NoBrokersAvailable` | Ensure Kafka is running: check Zookeeper and broker terminals |
| `ConnectionRefusedError` on ES | Ensure Elasticsearch is running and security is disabled |
| Spark can't find packages | Use `--packages` flag with spark-submit (not `pip install`) |
| `java.lang.ClassNotFoundException` | Ensure Java 8 or 11 is installed and `JAVA_HOME` is set |
| Empty batches in Spark | Start the producer after Spark is listening |
| Model/vectorizer not found | Ensure `models/sentiment_model.pkl` and `models/vectorizer.pkl` exist |

---

## Performance Metrics

Both scripts automatically collect and log metrics:

**Producer metrics** (saved to `logs/producer_log.txt`):
- Total records sent
- Total elapsed time
- Throughput (records/second)

**Streaming metrics** (saved to `logs/streaming_log.txt`):
- Per-batch: record count, processing time, throughput
- Cumulative: total records, total batches, overall throughput
- Pipeline uptime

---

## Elasticsearch Document Schema

Each document in the `telecom-sentiment` index contains:

```json
{
  "userName": "Cheo Yan Ho",
  "cleaned_content": "terrible app when i want to pay...",
  "score": 1,
  "provider": "maxis",
  "review_date": "2023-07-02",
  "original_sentiment": "Negative",
  "predicted_sentiment": "Negative",
  "match": true,
  "processed_at": "2025-06-30T15:30:00"
}
```
