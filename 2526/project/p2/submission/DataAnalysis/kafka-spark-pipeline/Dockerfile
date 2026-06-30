# ============================================================================
# Dockerfile — Pipeline Application Container
# ============================================================================
# Build context must be the project root (hpdp project/) so that data/ and
# models/ directories are accessible.
#
# Uses python:3.10-slim + OpenJDK 17 (required by PySpark/Spark).
# This avoids relying on the apache/spark-py image which has inconsistent
# tag availability on Docker Hub.
#
# Used by both kafka-producer and spark-streaming services in docker-compose.
# ============================================================================

FROM python:3.10-slim-bookworm

# ---- Install Java (required by PySpark) ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-17-jre-headless \
        curl \
        procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PYTHONUNBUFFERED=1
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# ---- Install Python dependencies ----
COPY kafka-spark-pipeline/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# ---- Copy pipeline code ----
COPY kafka-spark-pipeline/config.py /app/config.py
COPY kafka-spark-pipeline/kafka_producer.py /app/kafka_producer.py
COPY kafka-spark-pipeline/spark_streaming.py /app/spark_streaming.py

# ---- Copy data and models from the project ----
COPY data/cleaned_data.csv /app/data/cleaned_data.csv
COPY models/sentiment_model.pkl /app/models/sentiment_model.pkl
COPY models/vectorizer.pkl /app/models/vectorizer.pkl

# ---- Create logs directory ----
RUN mkdir -p /app/logs

WORKDIR /app

# Default command (overridden by docker-compose)
CMD ["python", "kafka_producer.py"]
