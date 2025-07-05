# 📡 Real-Time Sentiment Analysis System (YouTube Comments)

This project sets up a real-time sentiment analysis pipeline using **Apache Kafka**, **Apache Spark**, **Elasticsearch**, and **Kibana** — all run within **Docker Compose**. It collects YouTube comments, performs sentiment analysis, and visualizes the results in real-time.

---

## 🛠️ Setup Instructions

### 🔧 Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.8+ (Python 10 recommended)
- `pip` (Python package manager)

---

## 🚀 How to Run the System

### 1️⃣ Start Docker Services

In terminal run the command below to run the docker container make sure that the docker desktop is open and started.

```bash
docker-compose up -d
```

This starts Kafka, Zookeeper, Spark, Elasticsearch, and Kibana in detached mode.

---

### 2️⃣ Run the YouTube Comment Producer

Open a **new terminal** and run:

```bash
python producer.py
```

This script streams YouTube comments into the Kafka topic.

---

### 3️⃣ Enter the Spark Container

Open **another terminal** and enter the Spark container:

```bash
docker-compose exec spark /bin/bash
```

---

### 4️⃣ Install Python Packages in Spark

Inside the container, install the required libraries:

```bash
pip install joblib scikit-learn
```

Then exit the container:

```bash
exit
```

---

### 5️⃣ Run Spark Structured Streaming Job

In the terminal, run the Spark job that consumes from Kafka and writes to Elasticsearch:

```bash
docker-compose exec spark spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.2,org.elasticsearch:elasticsearch-spark-30_2.12:8.13.4 \
  /opt/bitnami/spark/work/spark_stream.py
```

---

### 6️⃣ (Optional) Re-run the Producer

If needed, you can re-run the producer in a new terminal:

```bash
python producer.py
```

---

## 📊 Accessing Kibana Dashboard

Once the data is being streamed into **Elasticsearch**, you can access and visualize it using **Kibana**.

### ✅ Step-by-Step Guide

1. **Open Kibana:**  
   Visit [http://localhost:5601](http://localhost:5601) in your browser.

2. **Create a Data View:**  
   - Navigate to **Stack Management** > **Data Views**  
   - Click **Create data view**
   - Set the name to something like `youtube-comments*` (or match your index pattern)
   - Click **Create data view**

3. **Explore Data in Discover:**  
   - Go to **Discover** in the sidebar
   - Select your created data view
   - View real-time comment data with fields like `comment_text`, `sentiment`, `video_id`, etc.

4. **Open or Create a Dashboard:**  
   - Navigate to **Dashboard** in the sidebar
   - You can:
     - Open an existing dashboard (if you imported one from the `/dashboard` folder)
     - Or click **Create dashboard**, then **Add from library** to include saved visualizations (like pie charts, bar graphs, sentiment over time)

---

📌 *Tip: To import a pre-built dashboard, go to **Stack Management > Saved Objects**, click **Import**, and select the `.ndjson` file inside the `dashboard/` folder.*



---

## 📁 Project Structure

```bash
.
├── docker-compose.yml
├── producer.py
├── spark_stream.py
├── models/
│   └── sentiment_model.pkl
├── README.md
└── ...
```

---

## 📬 Contact

For any issues or questions, feel free to open an issue or contact the team.


