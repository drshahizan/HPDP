<h1 align="center"> 
  Code Cookies - Real-Time Sentiment Pipeline on Google Play Reviews of Popular Malaysian Apps
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
    <th>Role</th>
  </tr>
  <tr>
    <td width=80%>Najma Shakirah binti Shahrulzaman</td>
    <td>A23CS0140</td>
    <td>Group Leader & Pipeline Engineer</td>
  </tr>
  <tr>
    <td width=80%>Nurul Asyikin Binti Khairul Anuar</td>
    <td>A23CS0162</td>
    <td>NLP Model & Visualization Engineer</td>
  </tr>
  <tr>
    <td width=80%>Harini A/P Sangaran</td>
    <td>A23CS0081</td>
    <td>Data & NLP Engineer</td>
  </tr>
</table>

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
      <a href="reports/final_report.pdf"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Slides</td>
    <td align="center">
      <a href="reports/presentation_slides.pptx"><img src="https://github.com/user-attachments/assets/c09e2ce5-80ce-4236-9508-c65d1f079cda" width=25px height=23px></a>
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
      <a href="data/tng_raw_data.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="data/cleaned_data.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocess & Train Model (Model 1)</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocess & Train Model (Model 2)</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Full and Complete Code in our Repository</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/2e0abbaa-3b7f-450f-92f6-41fd0e6e4dad" width=24px height=23px></a>
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
- [3.1 Model Choice](#31-model-choice)
- [3.2 Training Process](#32-training-process)
- [3.3 Evaluation](#33-evaluation)

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

### 8.0 References
- [8.0 References](#80-references)

### 9.0 Appendix
- [9.0 Appendix](#90-appendix)

---

### 1.0 Introduction

#### 1.1 Background

Touch 'n Go eWallet (TNG) is one of Malaysia's most widely used digital payment platforms, serving millions of users across toll payments, e-commerce, bill payments, and peer-to-peer transfers. As the app continues to grow in adoption, user reviews on the Google Play Store have become a valuable and openly accessible source of public opinion, capturing real experiences with the app's performance, features, and reliability.

This project builds a **real-time sentiment analysis pipeline** to understand how Malaysian users feel about the TNG eWallet app by processing reviews scraped directly from the **Google Play Store**. A complete **big data pipeline** was developed using Apache technologies to **ingest**, **process**, and **analyse** this review data at scale.

Reviews were collected using the **Google Play Scraper** library, targeting English-language reviews from Malaysian users. The collected reviews were cleaned, preprocessed using standard NLP techniques, and labelled into **positive**, **neutral**, and **negative** sentiment categories. Two classification models were trained and compared for performance. A streaming pipeline was then built using **Dockerized Apache Kafka** to feed incoming reviews into **Apache Spark Structured Streaming** for real-time sentiment inference, with results stored in **Elasticsearch** and visualised on a **Kibana dashboard**.

#### 1.2 Objectives

The main objectives of this project are:

- ✅ Build a **real-time sentiment analysis pipeline** focused on Google Play reviews of the TNG eWallet app
- ⚙️ Use **Apache Kafka** for real-time data ingestion and streaming
- 🔄 Use **Apache Spark Structured Streaming** for real-time sentiment classification
- 🗃️ Store processed results in **Elasticsearch**
- 📊 Visualize sentiment trends using **Kibana dashboards**
- 🧠 Train and compare at least **two sentiment classification models** to classify reviews as **positive**, **neutral**, or **negative**
- 📈 Compare **batch processing** vs **streaming mode** in terms of throughput, accuracy, and resource usage

#### 1.3 Scope

This project involves the following components:

- Collecting English-language reviews of the TNG eWallet app from the **Google Play Store** (Malaysian region) using the `google-play-scraper` Python library
- Cleaning and preprocessing review text using **NLP techniques** including tokenization, stopword removal, and lemmatization
- Training and evaluating at least two sentiment models and selecting the best performer for deployment
- Developing a real-time data pipeline using **Apache Kafka** (producer) and **Apache Spark Structured Streaming** (consumer)
- Storing classified output in **Elasticsearch** and presenting live insights through **Kibana dashboards**
- Comparing pipeline and model performance under **batch** and **streaming** conditions

---

### 2.0 Data Acquisition & Preprocessing

#### 2.1 Sources

Reviews were collected from the official **TNG eWallet listing on the Google Play Store** using the `google-play-scraper` Python library. The scraper was configured to target English-language reviews from Malaysian users (`lang='en'`, `country='my'`), sorted by newest first.

**App Details:**

| Field | Value |
|---|---|
| App Name | TNG eWallet |
| App ID | `my.com.tngdigital.ewallet` |
| Platform | Google Play Store |
| Region | Malaysia (`country='my'`) |
| Language | English (`lang='en'`) |
| Target Volume | Up to 50,000 reviews (historical bulk load) |
| Kafka Topic | `tng_reviews` |

**Data Collection Strategy:**

The Kafka producer (`kafka_producer.py`) operates in two phases:

- **Phase 1 – Bulk Historical Load:** Fetches up to 50,000 of the most recent reviews in batches of 1,000, deduplicating by `reviewId` and saving to `tng_raw_data.csv` while simultaneously publishing each review to the Kafka topic.
- **Phase 2 – Real-Time Monitoring:** After the bulk load completes, the producer polls for the latest 50 reviews every 15 seconds, forwarding any new unseen reviews to Kafka in real time.

Each review record contains the following fields:

| Field | Description |
|---|---|
| `app_id` | App package identifier |
| `review_id` | Unique review ID (used for deduplication) |
| `username` | Reviewer's display name |
| `score` | Star rating (1–5) |
| `content` | Review text |
| `timestamp` | Date and time of the review |
| `thumbsUpCount` | Number of helpful votes |

#### 2.2 Tools

- **`google-play-scraper`** – Python library for extracting app reviews from the Google Play Store
- **Apache Kafka** – Real-time data streaming and message queuing
- **Python** – Scripting, data collection, and preprocessing
- **Pandas** – Data handling and CSV management
- **Google Colab / Jupyter Notebook** – Model training and experimentation
- **NLTK** – Tokenization, stopword removal, and stemming
- **spaCy** – Lemmatization and linguistic preprocessing
- **Hugging Face Transformers** – Pre-trained transformer model for labelling and inference
- **scikit-learn** – Machine learning model training and evaluation
- **Docker** – Containerised deployment of Kafka and related services

#### 2.3 Cleaning Steps

The raw review text collected from the Google Play Store was preprocessed through the following steps:

- **Lowercasing** – All review text converted to lowercase for consistency
- **Noise Removal** – Removed URLs, HTML tags, special characters, punctuation, and numeric digits
- **Emoji Handling** – Emojis stripped from review text (or optionally converted to descriptive tokens)
- **Tokenization** – Review content split into individual word tokens
- **Stopword Removal** – Common English stopwords (e.g. *the*, *is*, *and*) removed using NLTK's stopword list
- **Lemmatization** – Words reduced to their base dictionary form using spaCy (e.g. *running* → *run*, *payments* → *payment*)
- **Short Review Filtering** – Reviews with fewer than 3 meaningful tokens after cleaning were excluded
- **Sentiment Labelling** – Star ratings were used as a proxy for initial labelling (1–2 stars → negative, 3 stars → neutral, 4–5 stars → positive), with Hugging Face transformer model predictions used to verify and correct borderline cases

---

### 3.0 Sentiment Model Development

#### 3.1 Model Choice

#### 3.2 Training Process

#### 3.3 Evaluation

---

### 4.0 Apache System Architecture

---

### 5.0 Analysis & Results

#### 5.1 Key Findings

#### 5.2 Visualizations

#### 5.3 Insights

---

### 6.0 Optimisation & Comparison

---

### 7.0 Conclusion & Future Work

---

### 8.0 References

---

### 9.0 Appendix
