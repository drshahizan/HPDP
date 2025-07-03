# 🛠️ Kafka + Spark Real-Time Pipeline (Windows)

Follow these steps to run your Kafka + Spark-based real-time data pipeline on Windows:

---

## ✅ 1. Environment Requirements

Make sure you have:

* ✅ **Python 3.8 – 3.11** (Recommended: Python 3.10)
* ✅ **Java 11 (JDK)** installed and `JAVA_HOME` set
* ✅ Download the zip file, extract it and open it in code editor application

---

## 📦 2. Install Python Dependencies

### Install core dependencies:

```bash
pip install -r requirements.txt
```

### Install Spark-specific dependencies:

```bash
pip install -r spark_requirements.txt
```

---

## ⚙️ 3. Setup Hadoop (for Windows support)

Run the environment setup script:

```bash
python setup_env.py
```

> 💡 This script sets up Hadoop binaries needed for Spark on Windows.

### ➕ Add Hadoop to PATH: (Optional, if cannot run spark then add it)

Manually add the following to your **system environment variables**:

```
C:\hadoop\bin
```

---

## 🐘 4. Start Kafka

### Step 1: Download Kafka

* Download Kafka from the official website: [https://kafka.apache.org/downloads](https://kafka.apache.org/downloads)
* Extract it to:

  ```
  C:\Kafka
  ```

### Step 2: Start Zookeeper

In **Terminal 1**:

```bash
cd C:\Kafka
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```

### Step 3: Start Kafka Server

In **Terminal 2**:

```bash
cd C:\Kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

---

## 🚀 5. Run the Real-Time Producer (Kafka Publisher)

In **Terminal 3** (inside the folder provided (not inside the C:\kafka):

```bash
python index.py
```

---

## 🔄 6. Start Spark Streaming Application

In **Terminal 4**:

```bash
python spark_stream.py
```

> This process consumes Kafka stream, processes it using Spark, and stores results to Supabase.

---

## ✅ You're all set!

Make sure all terminals are running and the data should now flow through:

* Reddit → Kafka → Spark → Supabase

---

