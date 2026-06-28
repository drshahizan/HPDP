# SECP3133 Project 2: Real-Time Sentiment Analysis using Apache Spark and Kafka

Welcome to our repository for the High Performance Data Processing Project 2.

This project focuses on building a real-time sentiment analysis pipeline using Apache Kafka, Apache Spark Structured Streaming, Elasticsearch, Kibana, and machine learning. The system processes Grab Malaysia app review data and predicts user sentiment as Positive, Neutral, or Negative.

---

## 👥 Group Information

| Item              | Details                                                   |
| :---------------- | :-------------------------------------------------------- |
| **Course**        | SECP3133 High Performance Data Processing                 |
| **Lecturer**      | DR. SEAH CHOON SEN                                        |
| **Project Title** | Real-Time Sentiment Analysis using Apache Spark and Kafka |
| **Member 1**      | LAU YAN KAI (A23CS0098)                                   |
| **Member 2**      | NEO LI XIN (A23CS0253)                                    |
| **Member 3**      | ELIJAH SHE YU SHENG (A23CS0073)                           |
| **Member 4**      | CHEW CHIU XIAN (A23CS0061)                                |

---

## 📌 Project Overview

This project develops a real-time sentiment analysis system for Grab Malaysia app reviews. The main objective is to process user review data through a streaming pipeline and automatically classify each review into Positive, Neutral, or Negative sentiment.

The pipeline uses Apache Kafka as the streaming data ingestion layer, Apache Spark Structured Streaming as the real-time processing engine, a TF-IDF vectorizer and Naive Bayes model for sentiment prediction, and Elasticsearch as the storage layer. The processed results are also exported into CSV format for dashboard development using Kibana or Power BI.

---

## 🎯 Project Objectives

* Collect and prepare a Malaysian-relevant review dataset for sentiment analysis.
* Apply text preprocessing to clean and structure review data.
* Train and deploy sentiment classification models using Natural Language Processing techniques.
* Stream review data using Apache Kafka.
* Process incoming review messages using Apache Spark Structured Streaming.
* Integrate a trained TF-IDF and Naive Bayes sentiment model into the streaming pipeline.
* Store prediction results in Elasticsearch for searching, filtering, and dashboard visualization.
* Export processed prediction results into CSV format for further analysis.
* Compare batch and streaming processing approaches for sentiment analysis.
* Produce a dashboard and final report to present the project findings.

---

## 🌐 Dataset Profile

### Data Source

* **Dataset:** Grab Malaysia App Reviews
* **Data Type:** User review text data
* **Storage Format:** CSV
* **Main Input File:** `grab_reviews_preprocessed.csv`
* **Total Preprocessed Records:** 5,491 records
* **Sentiment Classes:** Positive, Neutral, Negative

### Dataset Columns

| Column           | Description                                                 |
| :--------------- | :---------------------------------------------------------- |
| `content`        | Original user review text                                   |
| `processed_text` | Cleaned and preprocessed review text                        |
| `sentiment`      | True sentiment label used for model training and evaluation |

---

## 🧹 Data Preprocessing

The dataset was preprocessed before being used in the real-time pipeline. The preprocessing stage prepares noisy review text into a cleaner format suitable for machine learning.

The preprocessing process includes:

* Converting text into lowercase.
* Removing unnecessary symbols, special characters, and noise.
* Cleaning review text for better model input.
* Preparing the `processed_text` column for TF-IDF feature extraction.
* Saving the cleaned output as `grab_reviews_preprocessed.csv`.

---

## 🤖 Sentiment Model Development

The sentiment prediction model uses a machine learning approach suitable for text classification.

### Model Components

| Component                  | Description                                          |
| :------------------------- | :--------------------------------------------------- |
| **TF-IDF Vectorizer**      | Converts processed text into numerical text features |
| **Naive Bayes Classifier** | Predicts the sentiment category of each review       |
| **Output Labels**          | Positive, Neutral, Negative                          |

### Deployment Files

| File                        | Purpose                                                 |
| :-------------------------- | :------------------------------------------------------ |
| `best_tfidf_vectorizer.pkl` | Saved TF-IDF vectorizer used for feature extraction     |
| `best_model.pkl`            | Saved Naive Bayes model used for prediction             |
| `deployment_config.json`    | Configuration file containing model deployment settings |
| `selected_model.csv`        | Summary of the selected model and performance           |

---

## 🏗️ System Architecture

The system follows a real-time streaming architecture.

```text
Grab Malaysia Reviews CSV
        ↓
Kafka Producer
        ↓
Kafka Topic: grab-reviews
        ↓
Spark Structured Streaming
        ↓
TF-IDF Vectorizer + Naive Bayes Model
        ↓
Elasticsearch Index + CSV Output
        ↓
Kibana / Power BI Dashboard
```

### Main Components

| Component                             | Role                                                        |
| :------------------------------------ | :---------------------------------------------------------- |
| **Apache Zookeeper**                  | Coordinates Kafka service                                   |
| **Apache Kafka**                      | Streams review messages through the `grab-reviews` topic    |
| **Apache Spark Structured Streaming** | Consumes Kafka messages and processes them in micro-batches |
| **TF-IDF + Naive Bayes Model**        | Predicts sentiment of incoming review messages              |
| **Elasticsearch**                     | Stores prediction results in a searchable index             |
| **Kibana / Power BI**                 | Visualizes sentiment analysis results                       |
| **Docker Compose**                    | Runs all major services in containers                       |

---

## ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Apache Kafka
* Apache Spark Structured Streaming
* Elasticsearch
* Kibana
* Docker Compose
* Power BI

---

## 📁 Repository Folder Structure

```text
Project-SentimentAnalysis/
│
├── data/
│   ├── grab_reviews_preprocessed.csv       # Preprocessed Grab Malaysia review dataset
│   └── predictions_output.csv              # Sentiment prediction output
│
├── models/
│   ├── best_model.pkl                      # Trained Naive Bayes model
│   ├── best_tfidf_vectorizer.pkl           # Saved TF-IDF vectorizer
│   ├── deployment_config.json              # Model deployment configuration
│   └── selected_model.csv                  # Selected model summary
│
├── kafka_spark_pipeline/
│   ├── kafka_producer.py                   # Sends review messages to Kafka
│   ├── spark_streaming.py                  # Spark Structured Streaming pipeline
│   ├── spark_batch_kafka.py                # Batch processing version for validation
│   └── test_model.py                       # Tests model loading and prediction
│
├── dashboard/
│   ├── dashboard.pbix                      # Power BI dashboard file
│   ├── dashboard_screenshot.png            # Dashboard preview screenshot
│   └── dashboard_export.pdf                # Exported dashboard report, if available
│
├── report/
│   ├── final_report.pdf                    # Final project report
│   └── presentation_slides.pptx            # Final presentation slides, if available
│
├── screenshots/
│   ├── 01_docker_containers.png            # Docker containers running
│   ├── 02_kafka_topic.png                  # Kafka topic list
│   ├── 03_kafka_producer.png               # Kafka producer output
│   ├── 04_spark_streaming_output.png       # Spark streaming micro-batch output
│   ├── 05_model_integration.png            # Model prediction test
│   ├── 06_elasticsearch_count.png          # Elasticsearch record count
│   └── 07_elasticsearch_search.png         # Elasticsearch sample records
│
├── docker-compose.yml                      # Docker services configuration
├── Dockerfile.spark                        # Custom Spark container configuration
├── requirements.txt                        # Python dependencies
├── README.md                               # Project documentation
└── .gitignore                              # Git ignored files
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```cmd
git clone <repository-url>
cd Project-SentimentAnalysis
```

---

### 2. Create and Activate Virtual Environment

```cmd
py -3.12 -m venv venv
venv\Scripts\activate
```

---

### 3. Install Python Dependencies

```cmd
pip install -r requirements.txt
```

If Kafka import error occurs, run:

```cmd
pip uninstall kafka-python -y
pip install kafka-python-ng
```

---

### 4. Start Docker Services

```cmd
docker compose up -d --build
```

Check whether all containers are running:

```cmd
docker ps
```

Expected containers:

```text
zookeeper
kafka
spark
elasticsearch
kibana
```

---

### 5. Create Kafka Topic

```cmd
docker exec kafka kafka-topics --create --topic grab-reviews --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

Check topic list:

```cmd
docker exec kafka kafka-topics --list --bootstrap-server localhost:9092
```

Expected output:

```text
grab-reviews
```

---

### 6. Run Spark Structured Streaming

Open the first terminal:

```cmd
docker exec -it spark bash
```

Inside the Spark container, run:

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 kafka_spark_pipeline/spark_streaming.py
```

Expected output:

```text
Spark streaming job started. Waiting for Kafka messages...
```

Keep this terminal running.

---

### 7. Run Kafka Producer

Open a second terminal:

```cmd
cd Project-SentimentAnalysis
venv\Scripts\activate
python kafka_spark_pipeline\kafka_producer.py
```

The producer will send review records into the Kafka topic `grab-reviews`.

---

### 8. Check Elasticsearch Output

Check the number of stored prediction records:

```cmd
curl http://localhost:9200/grab-sentiment-results/_count?pretty
```

Check sample prediction documents:

```cmd
curl "http://localhost:9200/grab-sentiment-results/_search?pretty&size=3"
```

---

## 📊 Output

The pipeline produces two main outputs:

| Output                   | Description                                              |
| :----------------------- | :------------------------------------------------------- |
| `grab-sentiment-results` | Elasticsearch index containing prediction results        |
| `predictions_output.csv` | CSV file containing prediction results for dashboard use |

### Output Fields

| Field                 | Description                    |
| :-------------------- | :----------------------------- |
| `review_id`           | Review record identifier       |
| `content`             | Original review text           |
| `processed_text`      | Cleaned review text            |
| `true_sentiment`      | Original sentiment label       |
| `predicted_sentiment` | Model prediction result        |
| `confidence_score`    | Confidence score of prediction |
| `source`              | Data source name               |
| `event_time`          | Time when message was produced |
| `batch_id`            | Spark micro-batch identifier   |

---

## ⚠️ Note on Demo Output

The full preprocessed dataset contains 5,491 records. However, for demonstration and testing, the Kafka producer may be limited to 50 review messages.

This is controlled in `kafka_producer.py`:

```python
LIMIT_MESSAGES = 50
```

To stream all records, change the setting to:

```python
LIMIT_MESSAGES = None
```

The streaming pipeline remains the same for both demo and full-dataset execution.

---

## 📈 Visualization

The prediction results can be visualized using:

* Kibana through Elasticsearch.
* Power BI through `predictions_output.csv`.

Suggested dashboard visuals include:

* Sentiment distribution chart.
* Count of Positive, Neutral, and Negative reviews.
* Confidence score analysis.
* Review-level prediction table.
* Sentiment trend over time.

---

## ✅ Project Status

| Component                       | Status    |
| :------------------------------ | :-------- |
| Data acquisition                | Completed |
| Data preprocessing              | Completed |
| Sentiment model development     | Completed |
| Model comparison                | Completed |
| Kafka producer                  | Completed |
| Kafka topic setup               | Completed |
| Spark batch processing          | Completed |
| Spark Structured Streaming      | Completed |
| Model integration               | Completed |
| Elasticsearch storage           | Completed |
| CSV output                      | Completed |
| Dashboard visualization         | Completed |
| Final report writing            | Completed |
| Screenshots and evidence        | Completed |
| GitHub repository documentation | Completed |

---

## 🔒 Ethical and Operational Considerations

* The project uses review data for academic analysis only.
* The dataset is used for sentiment analysis and not for personal identification.
* The pipeline processes text-based review data without exposing private user information.
* Docker Compose is used to improve reproducibility and reduce environment setup issues.
* The producer can be limited during testing to avoid unnecessary load during demonstration.

---

## 📌 Summary

This project successfully implements a real-time sentiment analysis pipeline using Apache Kafka and Apache Spark Structured Streaming. Grab Malaysia app review data is streamed through Kafka, processed using Spark, classified using a TF-IDF and Naive Bayes sentiment model, and stored in Elasticsearch and CSV format. The system demonstrates how real-time data processing and machine learning can be integrated into a scalable sentiment analysis workflow.

