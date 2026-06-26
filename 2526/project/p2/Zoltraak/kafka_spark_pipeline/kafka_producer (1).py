# -*- coding: utf-8 -*-
"""
# Kafka Producer: Stream YouTube Comments to Kafka (Google Colab)

This notebook reads `youtube_comments_with_sentiment.csv` and streams each 
comment as a JSON message to the `youtube-sentiment` Kafka topic.

**Run cells in order.** Java and Kafka are installed automatically inside this Colab runtime.
"""

# ════════════════════════════════════════════════════════════════════════════
# Cell 0: Install Java & Kafka
# Installs Java (required by Kafka) and downloads Kafka 3.6.1 into the
# Colab runtime. Also defines all shared configuration variables used
# throughout the notebook.
# ════════════════════════════════════════════════════════════════════════════
import os, subprocess, tarfile, urllib.request, sys

print('Installing Java...')
subprocess.run(['apt-get', 'install', '-y', '-q', 'default-jdk'], check=True)
java_ver = subprocess.run(['java', '-version'], capture_output=True, text=True)
print('Java ready:', java_ver.stderr.split('\n')[0])

KAFKA_VERSION = '3.6.1'
SCALA_VERSION = '2.13'
KAFKA_TGZ     = f'kafka_{SCALA_VERSION}-{KAFKA_VERSION}.tgz'
KAFKA_URL     = f'https://archive.apache.org/dist/kafka/{KAFKA_VERSION}/{KAFKA_TGZ}'
KAFKA_HOME    = f'/opt/kafka_{SCALA_VERSION}-{KAFKA_VERSION}'

if os.path.exists(os.path.join(KAFKA_HOME, 'bin', 'kafka-server-start.sh')):
    print('Kafka already installed at', KAFKA_HOME)
else:
    print(f'Downloading Kafka {KAFKA_VERSION}...')
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

print('Kafka home :', KAFKA_HOME)
print('Kafka bin  :', KAFKA_BIN)
print('Python     :', sys.executable)


# ════════════════════════════════════════════════════════════════════════════
# Cell 1: Install Python Dependencies
# Installs kafka-python (Kafka client library) and pandas (CSV handling)
# using pip inside the Colab runtime.
# ════════════════════════════════════════════════════════════════════════════
import subprocess, sys

result = subprocess.run(
    [sys.executable, '-m', 'pip', 'install', 'kafka-python', 'pandas', '-q'],
    capture_output=True, text=True
)
print(result.stdout or 'Packages already up to date.')
if result.returncode != 0:
    print('ERROR:', result.stderr)
else:
    print('Done.')


# ════════════════════════════════════════════════════════════════════════════
# Cell 2: Upload CSV
# Uploads the YouTube comments dataset into the Colab runtime.
# Option A: file picker upload. Option B: mount from Google Drive.
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
# Launches ZooKeeper (port 2181) and the Kafka broker (port 9092) as
# background processes. Waits and confirms each service is ready before
# proceeding. Skip if already running.
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
    print('Waiting for ZooKeeper to start...')
    for i in range(20):
        time.sleep(1)
        if is_port_open(2181):
            print(f'ZooKeeper ready after {i+1}s (PID: {zk.pid})')
            break
    else:
        print('WARNING: ZooKeeper may not have started. Check manually.')

if is_port_open(9092):
    print('Kafka broker already running on port 9092.')
else:
    kafka_proc = subprocess.Popen(
        [KAFKA_SCRIPT, KAFKA_CFG],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    print('Waiting for Kafka broker to start...')
    for i in range(30):
        time.sleep(1)
        if is_port_open(9092):
            print(f'Kafka broker ready after {i+1}s (PID: {kafka_proc.pid})')
            break
    else:
        print('WARNING: Kafka broker may not have started. Check manually.')


# ════════════════════════════════════════════════════════════════════════════
# Cell 4: Create Kafka Topic
# Creates the Kafka topic 'youtube-sentiment' with 3 partitions and
# replication factor 1. Skips creation if the topic already exists.
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
    print('ERROR: Kafka is not running on port 9092. Run Cell 3 first.')
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
# Cell 5: Run Producer
# Reads the CSV and publishes each row as a JSON message to the Kafka topic
# at ~33 messages/second using a background thread. Each message contains
# video_id, user, comment, comment_clean, published_at, and true_sentiment.
# ════════════════════════════════════════════════════════════════════════════
import json, time, threading, os
import pandas as pd
from kafka import KafkaProducer

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f'CSV not found: {CSV_PATH}\nRe-run Cell 2 to upload your CSV.')

def run_producer():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries=3
    )
    df    = pd.read_csv(CSV_PATH)
    total = len(df)
    print(f'Loaded {total} comments. Streaming to topic [{TOPIC}]...')

    sent = 0
    for _, row in df.iterrows():
        message = {
            'video_id'      : str(row.get('video_id', '')),
            'user'          : str(row.get('user', '')),
            'comment'       : str(row.get('comment', '')),
            'comment_clean' : str(row.get('comment_clean', '')),
            'published_at'  : str(row.get('published_at', '')),
            'true_sentiment': str(row.get('sentiment', ''))
        }
        producer.send(TOPIC, value=message)
        sent += 1
        if sent % 500 == 0:
            print(f'  [{sent}/{total}] messages produced...')
        time.sleep(DELAY_SECONDS)

    producer.flush()
    producer.close()
    print(f'Producer done. Total sent: {sent}')

producer_thread = threading.Thread(target=run_producer, daemon=True)
producer_thread.start()
print('Producer thread started.')
print('You can now run the Spark Streaming notebook in parallel.')


# ════════════════════════════════════════════════════════════════════════════
# Cell 6: Wait for Producer to Finish
# Blocks execution until the producer thread completes sending all messages.
# Confirms when all records have been successfully published to Kafka.
# ════════════════════════════════════════════════════════════════════════════
producer_thread.join()
print('All messages sent to Kafka.')