# Kafka + Spark Game Review Processing Pipeline

This project sets up a complete data processing pipeline using Kafka and Spark to process Steam game reviews with sentiment analysis.

## Prerequisites

- Docker Desktop for Windows
- Python 3.8+
- Your `steam_game_reviews.csv` file from the sentiment analysis project

## Quick Start

1. **Install Python dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. **Start Kafka and Spark services:**
   \`\`\`bash
   setup.bat
   \`\`\`

3. **Run the complete pipeline:**
   \`\`\`bash
   python run_pipeline.py
   \`\`\`

## Architecture

\`\`\`
Steam Reviews CSV → Kafka Producer → Kafka Topic → Spark Streaming → Processed Results
                                  ↓
                              Kafka Consumer → Real-time Processing
\`\`\`

## Components

### 1. Kafka Setup (`docker-compose.yml`)
- Zookeeper for coordination
- Kafka broker for message streaming
- Spark master and worker nodes

### 2. Data Producer (`kafka_producer.py`)
- Reads your CSV file
- Sends reviews to Kafka topics
- Handles batching and error recovery

### 3. Data Consumer (`kafka_consumer.py`)
- Consumes reviews from Kafka
- Performs real-time sentiment analysis
- Saves processed results

### 4. Spark Streaming (`spark_streaming.py`)
- Processes streaming data from Kafka
- Performs aggregations and analytics
- Outputs results to multiple sinks

### 5. Pipeline Orchestrator (`run_pipeline.py`)
- Coordinates all components
- Manages threading and lifecycle

## Usage

### Individual Components

**Start only Kafka and Spark:**
\`\`\`bash
docker-compose up -d
\`\`\`

**Run producer only:**
\`\`\`bash
python kafka_producer.py
\`\`\`

**Run consumer only:**
\`\`\`bash
python kafka_consumer.py
\`\`\`

**Run Spark streaming only:**
\`\`\`bash
python spark_streaming.py
\`\`\`

### Monitoring

- **Kafka Topics:** `docker exec kafka kafka-topics --list --bootstrap-server localhost:9092`
- **Spark Master UI:** http://localhost:8080
- **Spark Worker UI:** http://localhost:8081

### Topics Created

- `game-reviews`: Raw review data
- `sentiment-results`: Aggregated sentiment analysis
- `processed-reviews`: Fully processed review data

## Output Files

- `processed_reviews.csv`: Consumer output
- `./spark-data/processed-reviews/`: Spark streaming output
- `./spark-data/sentiment-by-game/`: Sentiment analysis by game
- `./spark-data/overall-sentiment/`: Overall sentiment statistics

## Stopping Services

\`\`\`bash
docker-compose down
\`\`\`

## Troubleshooting

1. **Port conflicts:** Make sure ports 2181, 9092, 8080, 8081 are available
2. **Memory issues:** Adjust Spark worker memory in docker-compose.yml
3. **CSV file not found:** Ensure `steam_game_reviews.csv` is in the project directory
4. **Docker issues:** Restart Docker Desktop and try again

## Customization

- Modify batch sizes in `kafka_producer.py`
- Adjust Spark streaming intervals in `spark_streaming.py`
- Add more Kafka topics for different data types
- Scale up Spark workers by modifying docker-compose.yml
\`\`\`

```batch file="stop.bat"
@echo off
echo Stopping Kafka and Spark services...

docker-compose down

echo Cleaning up containers...
docker container prune -f

echo Services stopped successfully!
pause
