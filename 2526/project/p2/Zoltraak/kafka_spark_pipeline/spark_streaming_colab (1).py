# -*- coding: utf-8 -*-
"""
# Spark Streaming: Real-Time YouTube Sentiment Classification (Google Colab)

**Run all cells top-to-bottom.** Java, Kafka, and all dependencies are installed automatically.

**Architecture:**
CSV → Kafka Producer → Kafka Topic → Spark Structured Streaming → SVM Classifier → Elasticsearch → Kibana Dashboard
"""

# ════════════════════════════════════════════════════════════════════════════
# Cell 0: Install Java, Kafka, and System Dependencies
# Installs Java 11 (required by both Kafka and Spark), downloads and
# extracts Kafka 3.6.1, and defines all shared configuration variables
# (paths, Kafka settings, output directories) used throughout the notebook.
# ════════════════════════════════════════════════════════════════════════════
import os, sys, subprocess, tarfile, urllib.request

print('Installing Java 11...')
subprocess.run(['apt-get', 'install', '-y', '-q', 'openjdk-11-jdk'], check=True)
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'
java_ver = subprocess.run(['java', '-version'], capture_output=True, text=True)
print('Java:', java_ver.stderr.split('\n')[0])

print('\nInstalling Docker...')
subprocess.run(['apt-get', 'install', '-y', '-q', 'docker.io'], check=True)
subprocess.run(['service', 'docker', 'start'], capture_output=True)
print('Docker ready.')

KAFKA_VERSION = '3.6.1'
SCALA_VERSION = '2.13'
KAFKA_TGZ     = f'kafka_{SCALA_VERSION}-{KAFKA_VERSION}.tgz'
KAFKA_URL     = f'https://archive.apache.org/dist/kafka/{KAFKA_VERSION}/{KAFKA_TGZ}'
KAFKA_HOME    = f'/opt/kafka_{SCALA_VERSION}-{KAFKA_VERSION}'

if os.path.exists(os.path.join(KAFKA_HOME, 'bin', 'kafka-server-start.sh')):
    print('\nKafka already installed at', KAFKA_HOME)
else:
    print(f'\nDownloading Kafka {KAFKA_VERSION}...')
    urllib.request.urlretrieve(KAFKA_URL, f'/tmp/{KAFKA_TGZ}')
    print('Extracting...')
    with tarfile.open(f'/tmp/{KAFKA_TGZ}', 'r:gz') as tar:
        tar.extractall('/opt/')
    os.remove(f'/tmp/{KAFKA_TGZ}')
    print('Kafka installed at', KAFKA_HOME)

KAFKA_BIN         = os.path.join(KAFKA_HOME, 'bin')
BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC             = 'youtube-sentiment'
DELAY_SECONDS     = 0.03
OUTPUT_DIR        = '/content/streaming_output'
MODEL_DIR         = '/content/models'
JAR_DIR           = '/content/jars'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MODEL_DIR,  exist_ok=True)
os.makedirs(JAR_DIR,    exist_ok=True)

os.environ['PYSPARK_PYTHON']        = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['SPARK_LOCAL_IP']        = '127.0.0.1'

print('\n--- Config Summary ---')
print('Kafka home :', KAFKA_HOME)
print('Kafka bin  :', KAFKA_BIN)
print('Output dir :', OUTPUT_DIR)
print('Model dir  :', MODEL_DIR)
print('Python     :', sys.executable)
print('Java home  :', os.environ['JAVA_HOME'])


# ════════════════════════════════════════════════════════════════════════════
# Cell 1: Install Python Dependencies
# Installs all required Python packages: PySpark 3.5.2 for stream
# processing, kafka-python for Kafka integration, scikit-learn for the
# SVM classifier, elasticsearch client for Elastic Cloud indexing,
# and matplotlib/pandas for data handling and visualization.
# ════════════════════════════════════════════════════════════════════════════
import subprocess, sys

result = subprocess.run(
    [sys.executable, '-m', 'pip', 'install',
     'pyspark==3.5.2',
     'kafka-python',
     'pandas',
     'matplotlib',
     'scikit-learn',
     'joblib',
     'elasticsearch==8.19.0',
     '-q'],
    capture_output=True, text=True
)
if result.returncode != 0:
    print('ERROR:', result.stderr)
else:
    print('All packages installed.')

import pyspark
result2 = subprocess.run(['java', '-version'], capture_output=True, text=True)
print('Python  :', sys.version.split()[0])
print('PySpark :', pyspark.__version__)
print('Java    :', result2.stderr.splitlines()[0] if result2.stderr else 'not found')


# ════════════════════════════════════════════════════════════════════════════
# Cell 2: Upload CSV
# Loads the YouTube comments dataset into the Colab runtime.
# Option A: upload via file picker. Option B: mount from Google Drive.
# The CSV must contain columns: comment_clean, sentiment, video_id, user.
# ════════════════════════════════════════════════════════════════════════════
from google.colab import files
uploaded = files.upload()
CSV_PATH = list(uploaded.keys())[0]
print('CSV path:', CSV_PATH)

# Option B: Load from Google Drive (comment out Option A above)
# from google.colab import drive
# drive.mount('/content/drive')
# CSV_PATH = '/content/drive/MyDrive/hpdp/project2/youtube_comments_with_sentiment.csv'
# print('CSV path:', CSV_PATH)


# ════════════════════════════════════════════════════════════════════════════
# Cell 3: Start ZooKeeper and Kafka Broker
# Launches ZooKeeper (port 2181) then the Kafka broker (port 9092) as
# background processes inside the Colab runtime. Polls each port until
# the service is confirmed ready before proceeding.
# ════════════════════════════════════════════════════════════════════════════
import subprocess, time, os, socket

ZK_SCRIPT    = os.path.join(KAFKA_BIN, 'zookeeper-server-start.sh')
KAFKA_SCRIPT = os.path.join(KAFKA_BIN, 'kafka-server-start.sh')
ZK_CFG       = os.path.join(KAFKA_HOME, 'config', 'zookeeper.properties')
KAFKA_CFG    = os.path.join(KAFKA_HOME, 'config', 'server.properties')

def is_port_open(port, host='localhost', timeout=2):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except:
        return False

if is_port_open(2181):
    print('ZooKeeper already running on port 2181.')
else:
    zk = subprocess.Popen(
        [ZK_SCRIPT, ZK_CFG],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    print('Waiting for ZooKeeper...')
    for i in range(20):
        time.sleep(1)
        if is_port_open(2181):
            print(f'ZooKeeper ready after {i+1}s (PID: {zk.pid})')
            break
    else:
        print('WARNING: ZooKeeper may not have started.')

if is_port_open(9092):
    print('Kafka broker already running on port 9092.')
else:
    kafka_proc = subprocess.Popen(
        [KAFKA_SCRIPT, KAFKA_CFG],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    print('Waiting for Kafka broker...')
    for i in range(30):
        time.sleep(1)
        if is_port_open(9092):
            print(f'Kafka broker ready after {i+1}s (PID: {kafka_proc.pid})')
            break
    else:
        print('WARNING: Kafka broker may not have started.')


# ════════════════════════════════════════════════════════════════════════════
# Cell 4: Create Kafka Topic
# Creates the 'youtube-sentiment' topic with 3 partitions and replication
# factor 1 on the local Kafka broker. Uses --if-not-exists so it is safe
# to rerun. Verifies creation by listing all active topics.
# ════════════════════════════════════════════════════════════════════════════
import subprocess, os, socket

TOPICS_SCRIPT = os.path.join(KAFKA_BIN, 'kafka-topics.sh')

def is_port_open(port, host='localhost', timeout=2):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except:
        return False

if not is_port_open(9092):
    print('ERROR: Kafka is not running. Run Cell 3 first.')
else:
    result = subprocess.run(
        [TOPICS_SCRIPT, '--create', '--topic', TOPIC,
         '--bootstrap-server', BOOTSTRAP_SERVERS,
         '--partitions', '3', '--replication-factor', '1', '--if-not-exists'],
        capture_output=True, text=True
    )
    print(result.stdout or result.stderr)
    verify = subprocess.run(
        [TOPICS_SCRIPT, '--list', '--bootstrap-server', BOOTSTRAP_SERVERS],
        capture_output=True, text=True
    )
    print('Topics:', verify.stdout.strip())


# ════════════════════════════════════════════════════════════════════════════
# Cell 5: Download Kafka Connector JARs for Spark
# Downloads the 4 JAR files required for Spark Structured Streaming to
# read from Kafka: spark-sql-kafka connector, kafka-clients, token
# provider, and commons-pool2. Versions are pinned to match PySpark 3.5.2.
# ════════════════════════════════════════════════════════════════════════════
import urllib.request, os

base = 'https://repo1.maven.org/maven2'
jars = [
    (f'{base}/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.2/spark-sql-kafka-0-10_2.12-3.5.2.jar',
     os.path.join(JAR_DIR, 'spark-kafka.jar')),
    (f'{base}/org/apache/kafka/kafka-clients/3.4.1/kafka-clients-3.4.1.jar',
     os.path.join(JAR_DIR, 'kafka-clients.jar')),
    (f'{base}/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.2/spark-token-provider-kafka-0-10_2.12-3.5.2.jar',
     os.path.join(JAR_DIR, 'spark-token-kafka.jar')),
    (f'{base}/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar',
     os.path.join(JAR_DIR, 'commons-pool2.jar')),
]
for url, path in jars:
    if not os.path.exists(path):
        print(f'Downloading {os.path.basename(path)}...')
        urllib.request.urlretrieve(url, path)
    print('OK:', os.path.basename(path))

JAR_LIST = ','.join(p for _, p in jars)
print('\nAll JARs ready.')


# ════════════════════════════════════════════════════════════════════════════
# Cell 5b: Connect to Elastic Cloud
# Establishes a connection to the hosted Elasticsearch cluster on Elastic
# Cloud using an API key. Replaces the Docker-based local setup to avoid
# RAM limitations in the Colab free tier. Verifies connectivity by pinging
# the cluster and printing the cluster name.
# ════════════════════════════════════════════════════════════════════════════
from elasticsearch import Elasticsearch

ES_HOST    = 'https://38f80a6c2c73498486c951188e1cf6f9.us-central1.gcp.cloud.es.io:443'
ES_API_KEY = 'eHR0V0FKOEJRa0ZiWVNibllUSEU6M0xxZjVZa2RIbTEwcXhqSnBLQmdHdw=='

es = Elasticsearch(
    ES_HOST,
    api_key=ES_API_KEY,
    verify_certs=True
)
print('Connected:', es.ping())
print('Cluster:', es.info()['cluster_name'])


# ════════════════════════════════════════════════════════════════════════════
# Cell 5c: Create Elasticsearch Index
# Creates the 'youtube_sentiment_index' index with explicit field mappings:
# keyword types for sentiment labels, video_id, and user fields; text type
# for comment content; and date type for the event_time timestamp.
# Skips creation if the index already exists.
# ════════════════════════════════════════════════════════════════════════════
INDEX_NAME = 'youtube_sentiment_index'

if not es.indices.exists(index=INDEX_NAME):
    es.indices.create(index=INDEX_NAME, mappings={
        'properties': {
            'video_id'           : {'type': 'keyword'},
            'user'               : {'type': 'keyword'},
            'comment'            : {'type': 'text'},
            'predicted_sentiment': {'type': 'keyword'},
            'true_sentiment'     : {'type': 'keyword'},
            'event_time'         : {'type': 'date'},
        }
    })
    print(f'Index "{INDEX_NAME}" created.')
else:
    print(f'Index "{INDEX_NAME}" already exists.')


# ════════════════════════════════════════════════════════════════════════════
# Cell 6: Train and Save SVM Model
# Trains a linear SVM classifier with TF-IDF vectorization (5000 features)
# on 80% of the dataset. Evaluates on the remaining 20% and prints a
# classification report. Saves both the trained SVM and TF-IDF vectorizer
# as .pkl files for use inside the Spark UDF during streaming.
# ════════════════════════════════════════════════════════════════════════════
import pandas as pd, joblib, os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f'CSV not found: {CSV_PATH}\nRe-run Cell 2 to upload your CSV.')

df = pd.read_csv(CSV_PATH)
df = df[['comment_clean', 'sentiment']].dropna()
label_map = {'Negative': 0, 'Neutral': 1, 'Positive': 2}
df['label'] = df['sentiment'].map(label_map)
print('Samples:', len(df))
print(df['sentiment'].value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    df['comment_clean'].values, df['label'].values,
    test_size=0.2, random_state=42, stratify=df['label']
)
tfidf = TfidfVectorizer(max_features=5000)
svm   = SVC(kernel='linear', probability=True)
svm.fit(tfidf.fit_transform(X_train), y_train)

y_pred = svm.predict(tfidf.transform(X_test))
print(classification_report(y_test, y_pred, target_names=['Negative', 'Neutral', 'Positive']))

SVM_PATH   = os.path.join(MODEL_DIR, 'svm_model.pkl')
TFIDF_PATH = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')
joblib.dump(svm,   SVM_PATH)
joblib.dump(tfidf, TFIDF_PATH)
print('Model saved to', MODEL_DIR)


# ════════════════════════════════════════════════════════════════════════════
# Cell 7: Start Kafka Producer in Background
# Reads all rows from the CSV and publishes each one as a JSON message to
# the Kafka topic at ~33 messages/second using a daemon thread. Runs in
# the background so Spark streaming can consume messages simultaneously.
# Each message includes video_id, user, comment, comment_clean,
# published_at, and true_sentiment fields.
# ════════════════════════════════════════════════════════════════════════════
import json, threading, time, os
import pandas as pd
from kafka import KafkaProducer

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f'CSV not found: {CSV_PATH}\nRe-run Cell 2 to upload your CSV.')

def run_producer():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    df_stream = pd.read_csv(CSV_PATH)
    sent = 0
    for _, row in df_stream.iterrows():
        producer.send(TOPIC, value={
            'video_id'      : str(row.get('video_id', '')),
            'user'          : str(row.get('user', '')),
            'comment'       : str(row.get('comment', '')),
            'comment_clean' : str(row.get('comment_clean', '')),
            'published_at'  : str(row.get('published_at', '')),
            'true_sentiment': str(row.get('sentiment', ''))
        })
        sent += 1
        if sent % 500 == 0:
            print(f'  Producer: {sent} messages sent...')
        time.sleep(DELAY_SECONDS)
    producer.flush()
    producer.close()
    print(f'Producer done. Total: {sent}')

producer_thread = threading.Thread(target=run_producer, daemon=True)
producer_thread.start()
print('Producer running in background...')


# ════════════════════════════════════════════════════════════════════════════
# Cell 8: Create Spark Session
# Initialises a local SparkSession with the Kafka connector JARs loaded.
# Configured with 2 local cores, disabled Spark UI, and fixed driver host
# to avoid networking issues inside Colab. Sets SPARK_HOME to the correct
# PySpark installation path to ensure the right JARs are used.
# ════════════════════════════════════════════════════════════════════════════
import os, sys, pyspark
from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = os.path.dirname(pyspark.__file__)

jars_needed = ['spark-kafka.jar', 'kafka-clients.jar', 'spark-token-kafka.jar', 'commons-pool2.jar']
JAR_LIST = ','.join(os.path.join(JAR_DIR, j) for j in jars_needed)

print('Python version:', sys.version)
print('JAVA_HOME:     ', os.environ.get('JAVA_HOME', 'NOT SET'))
print('SPARK_HOME:    ', os.environ['SPARK_HOME'])

spark = SparkSession.builder \
    .master('local[2]') \
    .appName('YouTubeSentimentStreaming') \
    .config('spark.jars', JAR_LIST) \
    .config('spark.ui.enabled', 'false') \
    .config('spark.driver.host', '127.0.0.1') \
    .config('spark.driver.bindAddress', '127.0.0.1') \
    .config('spark.executor.heartbeatInterval', '20s') \
    .config('spark.network.timeout', '300s') \
    .config('spark.python.worker.timeout', '300s') \
    .getOrCreate()

print('\nSuccess! Spark version:', spark.version)


# ════════════════════════════════════════════════════════════════════════════
# Cell 9: Define Schema and Sentiment UDF
# Defines the JSON schema that matches the Kafka message structure.
# Creates a PySpark UDF that loads the trained SVM + TF-IDF models
# (cached per worker) and predicts sentiment for each comment as
# Positive, Neutral, or Negative. The UDF is applied to every
# incoming message in the stream.
# ════════════════════════════════════════════════════════════════════════════
import joblib, os
from pyspark.sql.functions import from_json, col, udf, current_timestamp, window
from pyspark.sql.types import StructType, StructField, StringType

schema = StructType([
    StructField('video_id',       StringType()),
    StructField('user',           StringType()),
    StructField('comment',        StringType()),
    StructField('comment_clean',  StringType()),
    StructField('published_at',   StringType()),
    StructField('true_sentiment', StringType()),
])

_model_cache = {}
_lmap = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}

@udf(returnType=StringType())
def predict_sentiment(text):
    if 'svm' not in _model_cache:
        _model_cache['svm']   = joblib.load(os.path.join('/content/models', 'svm_model.pkl'))
        _model_cache['tfidf'] = joblib.load(os.path.join('/content/models', 'tfidf_vectorizer.pkl'))
    try:
        vec  = _model_cache['tfidf'].transform([str(text)])
        pred = _model_cache['svm'].predict(vec)[0]
        return _lmap[int(pred)]
    except:
        return 'Neutral'

print('Schema and UDF ready.')


# ════════════════════════════════════════════════════════════════════════════
# Cell 10: Read Stream from Kafka and Apply Model
# Connects Spark to the Kafka topic as a streaming source reading from
# the earliest available offset. Parses each JSON message using the
# defined schema, applies the SVM sentiment UDF to the comment_clean
# field, and attaches a current timestamp as event_time.
# ════════════════════════════════════════════════════════════════════════════
import socket

def is_port_open(port, host='localhost', timeout=2):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except:
        return False

if not is_port_open(9092):
    print('ERROR: Kafka is not running. Run Cell 3 first.')
else:
    raw_stream = spark.readStream \
        .format('kafka') \
        .option('kafka.bootstrap.servers', BOOTSTRAP_SERVERS) \
        .option('subscribe', TOPIC) \
        .option('startingOffsets', 'earliest') \
        .load()

    parsed = raw_stream \
        .select(from_json(col('value').cast('string'), schema).alias('data')) \
        .select('data.*') \
        .withColumn('predicted_sentiment', predict_sentiment(col('comment_clean'))) \
        .withColumn('event_time', current_timestamp())

    print('Streaming pipeline defined.')

for q in spark.streams.active:
    q.stop()
print('All streams stopped:', len(spark.streams.active), 'remaining')


# ════════════════════════════════════════════════════════════════════════════
# Cell 11: Write Stream → Memory + Console + Elasticsearch
# Runs 3 parallel streaming sinks:
# 1. Memory sink — stores results in a queryable Spark table for plotting.
# 2. Console sink — prints windowed sentiment counts every 30 seconds.
# 3. Elasticsearch sink — uses foreachBatch with the Python ES client to
#    bulk-index each micro-batch into Elastic Cloud. The native ES Spark
#    connector is avoided due to a known incompatibility with Spark 3.5.
# All streams run for 150 seconds before terminating.
# ════════════════════════════════════════════════════════════════════════════
import os
from elasticsearch import Elasticsearch, helpers
from pyspark.sql.functions import col, window

CLASSIFIED_DIR = os.path.join(OUTPUT_DIR, 'classified')
CHECKPOINT_DIR = os.path.join(OUTPUT_DIR, 'checkpoint')
os.makedirs(CLASSIFIED_DIR, exist_ok=True)
os.makedirs(CHECKPOINT_DIR, exist_ok=True)

import shutil
es_ckpt = os.path.join(CHECKPOINT_DIR, 'es')
if os.path.exists(es_ckpt):
    shutil.rmtree(es_ckpt)
    print('Cleared old ES checkpoint.')

INDEX_NAME = 'youtube_sentiment_index'
ES_HOST    = 'https://38f80a6c2c73498486c951188e1cf6f9.us-central1.gcp.cloud.es.io:443'
ES_API_KEY = 'eHR0V0FKOEJRa0ZiWVNibllUSEU6M0xxZjVZa2RIbTEwcXhqSnBLQmdHdw=='

def write_to_es(batch_df, batch_id):
    if batch_df.isEmpty():
        return
    try:
        es_client = Elasticsearch(ES_HOST, api_key=ES_API_KEY, verify_certs=True)
        rows = batch_df.select(
            'video_id', 'user', 'comment',
            'predicted_sentiment', 'true_sentiment', 'event_time'
        ).toPandas()
        actions = [
            {
                '_index': INDEX_NAME,
                '_source': {
                    'video_id'           : str(row['video_id']),
                    'user'               : str(row['user']),
                    'comment'            : str(row['comment']),
                    'predicted_sentiment': str(row['predicted_sentiment']),
                    'true_sentiment'     : str(row['true_sentiment']),
                    'event_time'         : row['event_time'].isoformat()
                                          if hasattr(row['event_time'], 'isoformat')
                                          else str(row['event_time']),
                }
            }
            for _, row in rows.iterrows()
        ]
        success, failed = helpers.bulk(es_client, actions, raise_on_error=False)
        print(f'Batch {batch_id}: {success} indexed, {len(failed)} failed.')
        if failed:
            print('Sample error:', failed[0])
    except Exception as e:
        print(f'Batch {batch_id} ERROR (skipped): {e}')

query_memory = parsed \
    .select('video_id', 'user', 'comment', 'predicted_sentiment', 'true_sentiment', 'event_time') \
    .writeStream \
    .outputMode('append') \
    .format('memory') \
    .queryName('results') \
    .trigger(processingTime='10 seconds') \
    .start()

query_console = parsed \
    .groupBy(window(col('event_time'), '30 seconds'), col('predicted_sentiment')) \
    .count() \
    .writeStream \
    .outputMode('complete') \
    .format('console') \
    .option('truncate', False) \
    .trigger(processingTime='30 seconds') \
    .start()

query_es = parsed \
    .select('video_id', 'user', 'comment', 'predicted_sentiment', 'true_sentiment', 'event_time') \
    .writeStream \
    .outputMode('append') \
    .option('checkpointLocation', os.path.join(CHECKPOINT_DIR, 'es')) \
    .foreachBatch(write_to_es) \
    .trigger(processingTime='10 seconds') \
    .start()

print('Streaming running (Console + Memory + Elasticsearch)...')
print('Waiting 150 seconds...')

query_memory.awaitTermination(150)
query_console.awaitTermination(150)
query_es.awaitTermination(150)

print('Streaming complete!')


# ════════════════════════════════════════════════════════════════════════════
# Cell 12: Analyse and Plot Results
# Reads classified results from the in-memory Spark table and converts
# to a Pandas DataFrame. Saves results as CSV, then generates two charts:
# a bar chart showing comment count per sentiment class, and a pie chart
# showing the percentage distribution. Also computes streaming accuracy
# by comparing predicted vs true sentiment labels.
# ════════════════════════════════════════════════════════════════════════════
import pandas as pd
import matplotlib.pyplot as plt
import os

results = spark.sql('SELECT * FROM results').toPandas()

if results.empty:
    print('No results yet. Re-run after streaming completes.')
else:
    print(f'Total classified rows: {len(results)}')
    print(results.head())

    out_csv = os.path.join(OUTPUT_DIR, 'streaming_results.csv')
    results.to_csv(out_csv, index=False)
    print('CSV saved to', out_csv)

    dist   = results['predicted_sentiment'].value_counts()
    colors = {'Positive': '#2ecc71', 'Neutral': '#3498db', 'Negative': '#e74c3c'}
    bcols  = [colors.get(s, 'grey') for s in dist.index]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].bar(dist.index, dist.values, color=bcols, edgecolor='white')
    axes[0].set_title('Streaming Output: Sentiment Distribution', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Comment Count')
    for i, v in enumerate(dist.values):
        axes[0].text(i, v + 10, str(v), ha='center', fontweight='bold')

    axes[1].pie(dist.values, labels=dist.index, colors=bcols,
                autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})
    axes[1].set_title('Sentiment Share (%)', fontsize=14, fontweight='bold')

    plt.suptitle('YouTube Comments — Real-Time Streaming Results', fontsize=14)
    plt.tight_layout()

    out_img = os.path.join(OUTPUT_DIR, 'streaming_results.png')
    plt.savefig(out_img, dpi=150)
    plt.show()
    print('Chart saved to', out_img)

    matched = results.dropna(subset=['predicted_sentiment', 'true_sentiment'])
    if len(matched):
        acc = (matched['predicted_sentiment'] == matched['true_sentiment']).mean()
        print(f'Streaming accuracy vs true labels: {acc:.4f}')


# ════════════════════════════════════════════════════════════════════════════
# Cell 13: Verify Data in Elasticsearch
# Connects to the Elastic Cloud cluster and checks the total document
# count in the youtube_sentiment_index. Retrieves and prints 3 sample
# documents to confirm the data structure was indexed correctly.
# ════════════════════════════════════════════════════════════════════════════
from elasticsearch import Elasticsearch

ES_HOST    = 'https://38f80a6c2c73498486c951188e1cf6f9.us-central1.gcp.cloud.es.io:443'
ES_API_KEY = 'eHR0V0FKOEJRa0ZiWVNibllUSEU6M0xxZjVZa2RIbTEwcXhqSnBLQmdHdw=='

es = Elasticsearch(ES_HOST, api_key=ES_API_KEY, verify_certs=True)

count = es.count(index='youtube_sentiment_index')
print(f'Total docs in ES: {count["count"]}')

resp = es.search(index='youtube_sentiment_index', body={'query': {'match_all': {}}, 'size': 3})
for hit in resp['hits']['hits']:
    print(hit['_source'])