# ============================================================================
# config.py — Central Configuration for the Kafka-Spark-Elasticsearch Pipeline
# ============================================================================
# This file holds all tuneable parameters for the streaming pipeline.
# Member 2 can adjust these settings without touching the main scripts.
#
# Supports two modes:
#   - Local run  : Uses default values (localhost addresses, relative paths)
#   - Docker run : Reads from environment variables set in docker-compose.yml
# ============================================================================

import os

# ---------------------------------------------------------------------------
# Project Paths
# ---------------------------------------------------------------------------
# In Docker the files are at /app/data/ and /app/models/.
# Locally they are relative to this file's parent directory.
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)  # points to "hpdp project" (local)

# Docker puts everything under /app, so check if that path exists
_DOCKER_APP_DIR = "/app"
_IS_DOCKER = os.path.isfile(os.path.join(_DOCKER_APP_DIR, "config.py"))

if _IS_DOCKER:
    DATA_PATH = os.path.join(_DOCKER_APP_DIR, "data", "cleaned_data.csv")
    MODEL_PATH = os.path.join(_DOCKER_APP_DIR, "models", "sentiment_model.pkl")
    VECTORIZER_PATH = os.path.join(_DOCKER_APP_DIR, "models", "vectorizer.pkl")
    LOG_DIR = os.path.join(_DOCKER_APP_DIR, "logs")
else:
    DATA_PATH = os.path.join(PROJECT_DIR, "data", "cleaned_data.csv")
    MODEL_PATH = os.path.join(PROJECT_DIR, "models", "sentiment_model.pkl")
    VECTORIZER_PATH = os.path.join(PROJECT_DIR, "models", "vectorizer.pkl")
    LOG_DIR = os.path.join(BASE_DIR, "logs")

# ---------------------------------------------------------------------------
# Kafka Configuration
# ---------------------------------------------------------------------------
# Docker: env var KAFKA_BOOTSTRAP_SERVERS=kafka:29092  (internal listener)
# Local:  defaults to localhost:9092
# ---------------------------------------------------------------------------
KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = "telecom-reviews"

# Delay (seconds) between each message sent by the producer.
# 0.05s ≈ 20 reviews/sec — adjust for faster/slower simulation.
PRODUCER_DELAY = float(os.environ.get("PRODUCER_DELAY", "0.05"))

# ---------------------------------------------------------------------------
# Spark Configuration
# ---------------------------------------------------------------------------
SPARK_APP_NAME = "TelecomSentimentStreaming"

# ---------------------------------------------------------------------------
# Elasticsearch Configuration
# ---------------------------------------------------------------------------
# Docker: env vars ES_HOST=elasticsearch, ES_PORT=9200
# Local:  defaults to localhost:9200
# ---------------------------------------------------------------------------
ES_HOST = os.environ.get("ES_HOST", "localhost")
ES_PORT = os.environ.get("ES_PORT", "9200")
ES_INDEX = "telecom-sentiment"

# Full Elasticsearch nodes string for the ES-Hadoop connector
ES_NODES = f"{ES_HOST}:{ES_PORT}"
