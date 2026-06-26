<h1 align="center">
  🛍️ Shopping - Real-Time Sentiment Analysis on Google Maps Reviews of Tourist Attractions in Malaysia
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>TAN YI YA</td>
    <td>A23CS0187</td>
  </tr>
  <tr>
    <td width=80%>NURUL ADRIANA BINTI KAMAL JEFRI</td>
    <td>A23CS0258</td>
  </tr>
  <tr>
    <td width=80%>TEH RU QIAN</td>
    <td>A23CS0191</td>
  </tr>
</table>

---

## 📑 Project Overview

This project implements a complete, end-to-end data pipeline for real-time sentiment analysis. Our group focuses on scraping and analyzing **Google Map Reviews** of relevant commercial locations in Malaysia to gauge public sentiment (Positive, Negative, or Neutral) in real time. 

By leveraging modern big data technologies, this project bridges the gap between raw, unstructured text data and actionable, real-time business insights.

---

### Links for related documents:
<table>
  <tr>
    <th>Documents</th>
    <th>Links</th>
  </tr>
  <tr>
    <td>Report</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Shopping/reports/SECP3133_Project2_Shopping_Report.pdf"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Slides</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/c09e2ce5-80ce-4236-9508-c65d1f079cda" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Video</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/2dec74b1-9d2d-4cec-ae38-a57f7ac1711c" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Raw Data</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Shopping/data/raw_data.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Shopping/data/cleaned_data.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Web Scraping</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Shopping/data/gmap_scraper.py"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Data Preprocessing</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Shopping/notebooks/data_preprocessing.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Train Model using Convolutional Neural Network (CNN)</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Shopping/notebooks/cnn_sentiment_classification.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Train Model using BERT</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Shopping/notebooks/bert_sentiment_classification.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
</table>

---

## Table of Contents

### 1.0 Introduction
- [1.1 Background](#11-background)
- [1.2 Objectives](#12-objectives)
- [1.3 Scope](#13-scope)

### 2.0 Data Acquisition & Preprocessing
- [2.1 Sources](#21-sources)
- [2.2 Tools](#22-tools)
- [2.3 Cleaning Steps](#23-cleaning-steps)

### 3.0 Sentiment Model Development
- [3.1 BERT Model](#31-bert-model)
- [3.2 CNN Model](#32-cnn-model)
- [3.3 Model Comparison](#33-model-comparison)

### 4.0 Apache System Architecture
- [4.0 Apache System Architecture](#40-apache-system-architecture)

### 5.0 Analysis & Results
- [5.1 Key Findings](#51-key-findings)
- [5.2 Visualizations](#52-visualizations)
- [5.3 Insights](#53-insights)

### 6.0 Optimisation & Comparison
- [6.0 Optimisation & Comparison](#60-optimisation--comparison)

### 7.0 Conclusion & Future Work
- [7.0 Conclusion & Future Work](#70-conclusion--future-work)

---

### 1.0 Introduction

#### 1.1 Background

The rapid development of information technology has significantly increased the amount of user-generated content online, such as reviews, comments, and social media posts. These data provide valuable information about public opinion, experience, and preferences toward a certain product, service, or destination. In the tourism industry, online reviews play a crucial role in influencing travellers' decisions and shaping the reputation of tourist attractions. Malaysia, being one of the major tourism destinations in Southeast Asia, receives thousands of reviews from both local and international visitors through platforms such as **Google Maps**.

This project aims to develop a **real-time sentiment analysis system** for Google Maps reviews of popular tourist attractions in Malaysia. The system collects reviews through **web scraping**, preprocesses the textual data using **Natural Language Processing (NLP)** techniques, and classifies the reviews into **positive**, **neutral**, and **negative** sentiments using machine learning models.

To support real-time processing, **Apache Kafka** is employed as the streaming platform, while a **Convolutional Neural Network (CNN)** model performs sentiment classification. The analysis results are stored in **Elasticsearch** and visualised through **Kibana dashboards** to provide meaningful insights into visitor sentiments and system performance.

#### 1.2 Objectives

The main objectives of this project are:

- 🌐 Collect English-language **Google Maps reviews** from popular tourist attractions in Malaysia using automated web scraping
- 🤖 Preprocess and label the collected review data using a **pre-trained transformer-based sentiment analysis model**
- 🧠 Train and evaluate both **deep learning** (CNN, BERT) and traditional machine learning models for three-class sentiment classification
- ⚙️ Design and implement a **real-time sentiment analysis pipeline** capable of automatically ingesting, classifying, and storing Google Maps reviews
- 📊 Develop a **Kibana dashboard** for visualising sentiment analysis results

#### 1.3 Scope

This project involves the following components:

- Collecting reviews from **13 popular Malaysian tourist attractions** via Selenium-based web scraping
- Cleaning and preprocessing using **NLP techniques** (tokenization, stopword removal, lemmatization)
- Training and evaluating two sentiment models: **BERT** and **CNN**
- Developing a real-time data pipeline using **Apache Kafka**, **CNN inference**, and **Elasticsearch**
- Displaying live sentiment results with **Kibana dashboards**
- Focusing analysis on **public opinion about tourist attractions in Malaysia**

---

### 2.0 Data Acquisition & Preprocessing

#### 2.1 Sources

Reviews were collected from **13 popular tourist attractions** across Malaysia using a custom Selenium-based web scraper. Locations include:

- Batu Caves
- Petronas Twin Towers
- Pulau Sipadan
- Mossy Forest
- Niah National Park
- Genting SkyWorld
- Taman Negara
- Kek Lok Si Temple
- *(and more)*

A total of **3,271 reviews** were successfully collected. After preprocessing, **3,242 reviews** were retained for model training and pipeline deployment.

#### 2.2 Tools

- **Selenium** – automated web scraping of dynamic Google Maps review pages
- **Python** – scripting and preprocessing
- **NLTK** – tokenization, stopword removal, and lemmatization
- **Hugging Face Transformers** (`cardiffnlp/twitter-roberta-base-sentiment-latest`) – automatic sentiment labeling
- **Apache Kafka** – real-time streaming
- **Google Colab** – model training
- **ftfy** – fixing malformed Unicode characters from web scraping

#### 2.3 Cleaning Steps

- Fixed **encoding artefacts** using the `ftfy` library
- Converted text to **lowercase**
- Removed **emojis**, **URLs**, **special characters**, and **numerical digits**
- **Tokenized** comments into individual words using `word_tokenize()`
- Removed **English stopwords** from the NLTK corpus
- Applied **lemmatization** using `WordNetLemmatizer`
- **Labeled** reviews automatically using the Hugging Face RoBERTa model:
  - Positive (1): **2,533 reviews (78%)**
  - Neutral (0): **448 reviews (14%)**
  - Negative (-1): **261 reviews (8%)**

---

### 3.0 Sentiment Model Development

#### 3.1 BERT Model

**Model Choice:**
BERT (Bidirectional Encoder Representations from Transformers) was selected for its bidirectional attention mechanism, which considers context from both directions simultaneously. The `bert-base-uncased` variant (12 layers, 110 million parameters) was used, suitable for informal text such as Google Maps reviews.

**Training Process:**
<img width="1169" height="407" alt="image" src="https://github.com/user-attachments/assets/d78d1c4a-a40f-42ad-8b7b-a72342a5e4d4" />

- Dataset split: **80:20 (train/test)** with stratified sampling
- Tokenized using `BertTokenizer` with max sequence length of **128 tokens**
- Trained for **4 epochs** using AdamW optimiser (learning rate: 2×10⁻⁵, weight decay: 0.01)
- Linear learning rate scheduler with **10% warm-up** steps
- Gradient clipping at max norm **1.0** to prevent exploding gradients
- Best checkpoint saved based on lowest validation loss

**Evaluation:**

<img width="434" height="375" alt="image" src="https://github.com/user-attachments/assets/eeaf3e04-36e5-4003-8119-e5481413b324" />


<img width="1021" height="409" alt="image" src="https://github.com/user-attachments/assets/334474be-5305-4320-a873-90f88501e976" />


#### 3.2 CNN Model

**Model Choice:**
CNN was chosen as the **primary model for the real-time pipeline** due to its lightweight architecture (only ~1 million parameters) and fast inference speed — critical for continuous streaming. The architecture consists of:
- Conv1D layer (128 filters, kernel size 5)
- GlobalMaxPooling1D
- Dense layer (64 units, ReLU)
- Dropout (rate 0.5)
- Softmax output layer (3 classes)

**Training Process:**
<img width="1184" height="413" alt="Screenshot 2026-06-26 181430" src="https://github.com/user-attachments/assets/fdef1d20-c69a-4139-9123-28e35df7411f" />

- Dataset split: **80:20 (train/test)** → 2,593 training / 649 test reviews
- Keras Tokenizer with vocabulary size of **7,328 unique tokens**
- Padded/truncated to **128 tokens**
- Adam optimiser (learning rate: 1×10⁻³), batch size 16, up to 10 epochs
- **EarlyStopping** and **ModelCheckpoint** callbacks applied
- Best weights saved at **Epoch 2** (val loss: 0.4435); training stopped at Epoch 5

**Evaluation:**

<img width="438" height="381" alt="Screenshot 2026-06-26 182336" src="https://github.com/user-attachments/assets/276e1d66-25e4-4990-8b80-e56643d99151" />

<img width="1208" height="458" alt="Screenshot 2026-06-26 182243" src="https://github.com/user-attachments/assets/58327b9c-daab-4b32-9a71-ed32d43c9454" />


#### 3.3 Model Comparison

| Criteria | BERT | CNN |
|----------|------|-----|
| Accuracy | 87.52% | 81.51% |
| Macro Precision | 0.7286 | 0.6566 |
| Macro Recall | 0.7532 | 0.5289 |
| Macro F1-Score | 0.7374 | 0.5261 |
| Parameters | ~110 million | 1,028,483 |
| Inference Speed | Slow | Fast |
| Memory Usage | High | Low |
| Deployed in Pipeline | ❌ | ✅ |

---

### 4.0 Apache System Architecture

The system operates on a **dual architecture** combining real-time streaming and batch processing.

**Producer Layer:**
- `producer.py` loads reviews sequentially from `cleaned_data.csv` and publishes them to a Kafka topic in JSON format
- Each message includes `review_id`, `review_text`, `sentiment`, and `timestamp`
- A **0.3-second delay** between messages simulates real-world streaming
- Auto-reconnect with up to 10 retries (5-second intervals)

**Broker Layer:**
- **Apache Kafka** acts as the messaging backbone
- **Zookeeper** coordinates brokers and metadata
- Kafka topics are automatically created at startup via `kafka-init`

**Inference Layer:**
- **Streaming Consumer** (`cnn_stream_consumer.py`): subscribes to Kafka, batches every 10 messages, tokenizes to 128 tokens, and runs CNN inference
- **Batch Consumer** (`cnn_batch_consumer.py`): reads all records from `cleaned_data.csv` in a single execution, standardizes to 100 tokens, and captures performance metrics (throughput, CPU usage, memory) via `psutil`
- CNN output labels (0, 1, 2) are mapped to sentiments (-1, 0, +1)

**Storage & Visualisation Layer:**
- Streaming results → `sentiment_results` index in Elasticsearch
- Batch results → `sentiment_batch` and `performance_metrics` indices
- **Kibana** dashboards provide real-time monitoring of sentiment trends and system performance

All services are containerized using **Docker Compose**.

---

### 5.0 Analysis & Results

#### 5.1 Key Findings

The real-time sentiment analysis pipeline was successfully operated in both batch and streaming modes, with results indexed in Elasticsearch and visualized on Kibana.

- **Sentiment Distribution** (pipeline output): Negative 47.54%, Positive 30.53%, Neutral 22.11% — note this is skewed due to duplicate records from multiple streaming pipeline runs during development
- **Model Accuracy**: Average pipeline accuracy of **0.886**, combining both batch and streaming consumer outputs
- **Batch Throughput**: ~**126 records/second** (full dataset in a single vectorised pass)
- **Streaming Throughput**: ~**115 records/second** (micro-batches of 10, with Kafka deserialization overhead)
- **CPU Usage**: Batch mode peaked at ~95%; streaming mode showed lower, distributed usage over time
- **Most Common Terms**: "beautiful place", "amazing place", "good place", "beautiful view", "beautiful island", "diving paradise"

#### 5.2 Visualizations

The Kibana dashboard consists of **8 panels** covering the following:

<img width="1342" height="279" alt="Dashboard layer 1" src="https://github.com/user-attachments/assets/39b767e8-5b5a-4eac-8f6d-02d9084e32d0" />
<img width="1345" height="336" alt="Dashboard layer 2" src="https://github.com/user-attachments/assets/f5962ffa-6d50-4fbf-9aa6-4355a15c6412" />
<img width="1340" height="249" alt="Dashboard layer 3" src="https://github.com/user-attachments/assets/a7ae4c06-b178-4119-b523-c64186afc834" />

1. **Overall Sentiment Distribution** – donut chart of Negative/Neutral/Positive proportions
2. **Model Accuracy (%)** – single-value metric card showing average accuracy (0.886)
3. **Most Talked About** – tag cloud of the top 10 most frequently appearing review terms
4. **Prediction Accuracy Analysis** – grouped bar chart mapping predicted vs. true sentiment labels
5. **Sentiment Density by Length** – stacked bar chart of predicted sentiment by review text length
6. **Sentiment Trend Over Time** – line graph of record count per sentiment class per minute
7. **Batch vs Stream Throughput** – bar chart comparing maximum throughput of both pipeline modes
8. **System Resource Usage** – time-series chart of average CPU usage for batch vs. streaming modes

#### 5.3 Insights

- **Tourist sentiment is predominantly positive.** 78% of the labeled dataset was classified as positive, backed by frequent positive terms such as "beautiful place", "amazing experience", and "diving paradise", reflecting high visitor satisfaction with Malaysian tourist attractions.

- **Class imbalance is the primary limitation of the CNN model.** The macro F1-score of 0.5261 is significantly lower than the accuracy of 0.8151, showing that accuracy alone is an unreliable metric for imbalanced datasets. The Negative class recall of only 0.10 means the model misses 90% of true negative reviews.

- **Batch processing suits fixed-volume retrospective analysis.** With ~126 records/second, batch mode is efficient for periodic reporting, though all records carry the same timestamp, limiting time-trend analysis.

- **Streaming processing enables real-time monitoring with manageable overhead.** At ~115 records/second with time-distributed records, streaming allows Kibana to render meaningful sentiment trends over time — ideal for live monitoring use cases.

- **Duplicate records affect Kibana dashboard reliability.** Since the stream consumer does not purge previous records between runs, sentiment distribution counts are inflated. Index rotation or deduplication should be implemented in future iterations.

---

### 6.0 Optimisation & Comparison

| Technical Aspect | Baseline Architecture | Optimised Architecture | Expected Result |
|---|---|---|---|
| **Sentiment Model** | FP32 TensorFlow/Keras CNN | DistilBERT via ONNX Runtime | Lower memory, faster inference, better classification |
| **Kafka Configuration** | Single topic partition, one consumer | Multiple partitions + consumer group | Higher throughput, improved scalability |
| **Elasticsearch Indexing** | Synchronous per-record indexing | Asynchronous Bulk API micro-batching | Reduced network overhead, faster dashboard updates |

**Proposed Optimisations:**

- 🔁 **Knowledge Distillation + Model Quantisation:** Fine-tune **DistilBERT** from the trained BERT model. DistilBERT retains 97% of BERT's performance with 40% smaller size and 60% faster inference — making transformer-level accuracy feasible for real-time deployment.

- 📨 **Kafka Partitioning + Consumer Group Scaling:** Split the Kafka topic into multiple partitions and process using a consumer group. This enables parallel message processing, fault tolerance, and automatic workload redistribution.

- 🗄️ **Elasticsearch Bulk Indexing + Async Processing:** Replace synchronous per-document indexing with the Bulk API to reduce network overhead and improve indexing throughput for real-time dashboard accuracy.

---

### 7.0 Conclusion & Future Work

This project successfully implemented a real-time sentiment analysis pipeline for Google Maps reviews of Malaysian tourist attractions, integrating **Apache Kafka**, **CNN-based sentiment classification**, **Elasticsearch**, and **Kibana** in a unified Dockerized architecture.

A total of **3,242** English-language reviews were collected from 13 locations via Selenium scraping and labeled using the `cardiffnlp/twitter-roberta-base-sentiment-latest` RoBERTa model. Two models were trained and evaluated — **BERT** (87.52% accuracy, macro F1: 0.7374) and **CNN** (81.51% accuracy, macro F1: 0.5261). Despite BERT's superior classification performance, the **CNN was deployed in the pipeline** due to its lightweight footprint (~1M parameters) and fast inference, which are essential for real-time streaming.

The pipeline achieved a streaming throughput of ~115 records/second and batch throughput of ~126 records/second. Kibana dashboards confirmed that tourist sentiment toward Malaysian attractions is overwhelmingly positive, consistent with the 78% positive proportion in the labeled dataset.

**Future Work:**
- Replace CNN with **DistilBERT** for better minority class detection with manageable latency
- Apply **SMOTE oversampling** or class-weighted loss to address class imbalance
- Implement **Elasticsearch index deduplication** or rotation to ensure dashboard accuracy
- Explore **Kafka partitioning and consumer group scaling** for production-level throughput
- Expand data collection to **TripAdvisor**, **Booking.com**, and include **Malay-language reviews**
