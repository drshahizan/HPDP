# 🛍️ Project 2: Real-Time Sentiment Analysis using Apache Spark and Kafka

**Course:** High Performance Data Processing (HPDP)
**Group Name:** Shopping

## 👥 Team Members

| Name | Student ID | Role / Responsibilities |
| :--- | :--- | :--- |
| TEH RU QIAN | A23CS0191 | Group Leader / [Role] |
| TAN YI YA | A23CS0187 | Data & NLP Engineer / [Role] |
| NURUL ADRIANA BINTI KAMAL JEFRI  | A23CS0258 | Pipeline & Visualization Engineer / [Role] |

---

## 📑 Project Overview

This project implements a complete, end-to-end data pipeline for real-time sentiment analysis. Our group focuses on scraping and analyzing **Google Map Reviews** of relevant commercial locations in Malaysia to gauge public sentiment (Positive, Negative, or Neutral) in real time. 

By leveraging modern big data technologies, this project bridges the gap between raw, unstructured text data and actionable, real-time business insights.

---

## 🏗️ Architecture & Pipeline

Our pipeline consists of five primary stages:

1. **Data Collection (Scraping):** Using **Selenium**, we scrape publicly available customer reviews from Google Maps. 
2. **Streaming Ingestion:** The scraped reviews are pushed into **Apache Kafka**, acting as our real-time streaming layer.
3. **Stream Processing & NLP:** **Apache Spark** consumes the Kafka streams. We apply Natural Language Processing (NLP) techniques (cleaning, tokenization, stop-word removal, and lemmatization) to preprocess the text.
4. **Sentiment Classification:** The cleaned text is passed through our trained Machine Learning models (e.g., Naive Bayes and LSTM) to classify the sentiment.
5. **Storage & Visualization:** The classified results are stored in **[Elasticsearch / Apache Druid]** and visualized via real-time interactive dashboards using **[Kibana / Apache Superset]**.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Data Scraping** | Selenium | Automates browser interaction to extract dynamic Google Map reviews. |
| **Message Broker** | Apache Kafka | Streams text data from our scraper into the processing layer. |
| **Data Processing** | Apache Spark | Processes data streams in parallel and applies sentiment models. |
| **NLP & ML** | [NLTK / spaCy / Hugging Face] | Text preprocessing, feature extraction, and model training. |
| **Data Storage** | [Elasticsearch / Apache Druid] | Stores classified results for rapid querying. |
| **Visualization** | [Kibana / Apache Superset] | Interactive dashboarding for sentiment trends. |

---

## ⚙️ Setup and Installation

### Prerequisites
Ensure the following are installed and configured on your local machine or cluster:
* Python 3.8+
* Apache Spark (v3.x)
* Apache Kafka and Zookeeper
* [Elasticsearch / Apache Druid]
* Selenium Webdriver (e.g., ChromeDriver)

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)[your-repo-link]/Shopping.git
cd Shopping
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Infrastructure
```bash
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka
bin/kafka-server-start.sh config/server.properties
```

### 4. Run the Scraper and Producer
```bash
python scripts/scraper_producer.py
```

### 5. Run the Spark Streaming Application
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 scripts/spark_streaming.py
```
