# run_all.py

import subprocess
import threading
import time

# Script paths
KAFKA_PRODUCER_SCRIPT = "kafka_live_producer.py"
SPARK_CONSUMER_SCRIPT = "spark_kafka_consumer.py"
DASHBOARD_SCRIPT = "streamlit_dashboard.py"

def run_kafka_producer():
    print("▶️ Launching Kafka Live Producer...")
    subprocess.run(["python", KAFKA_PRODUCER_SCRIPT])

def run_spark_consumer():
    print("▶️ Launching Spark Kafka Consumer...")
    subprocess.run(["spark-submit", SPARK_CONSUMER_SCRIPT])

def run_dashboard():
    print("▶️ Launching Streamlit Dashboard...")
    subprocess.run(["streamlit", "run", DASHBOARD_SCRIPT])

if __name__ == "__main__":
    print("🚀 Starting Full Sentiment Analysis Pipeline...\n")

    kafka_thread = threading.Thread(target=run_kafka_producer)
    spark_thread = threading.Thread(target=run_spark_consumer)
    dashboard_thread = threading.Thread(target=run_dashboard)

    kafka_thread.start()
    time.sleep(5)

    spark_thread.start()
    time.sleep(10)

    dashboard_thread.start()

    kafka_thread.join()
    spark_thread.join()
    dashboard_thread.join()