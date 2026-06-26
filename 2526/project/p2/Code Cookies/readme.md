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
      <a href="data/foodpanda_malaysia_reviews_raw.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="data/compressed_data.csv.gz"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocess & Train Model (Naive Bayes)</td>
    <td align="center">
      <a href="https://colab.research.google.com/drive/18O7z_diG7hXtPDPdvRMw9BPMm7f9i8t1?usp=sharing#scrollTo=Model_1_Naive_Bayes"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocess & Train Model (LSTM)</td>
    <td align="center">
      <a href="https://colab.research.google.com/drive/18O7z_diG7hXtPDPdvRMw9BPMm7f9i8t1?usp=sharing#scrollTo=Model_2_LSTM"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
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

Food delivery services have become an essential part of daily life in Malaysia, providing consumers with convenient access to meals through mobile applications. Among these services, Foodpanda is one of the country's leading online food delivery platforms, connecting customers with thousands of restaurants and delivery riders across multiple cities. As the platform continues to expand, millions of users share their experiences through reviews on the Google Play Store, providing valuable insights into customer satisfaction regarding overall user experience, including service quality, customer support and application stability.

These publicly available reviews represent an important source of customer feedback that organizations can utilize to understand user sentiment and identify areas requiring improvement. Automated sentiment analysis supported by real-time data processing technologies has become increasingly important for organisations seeking to monitor customer satisfaction and respond promptly to service issues. Therefore, this project develops a real-time sentiment analysis system that analyses Foodpanda Malaysia Google Play reviews using Apache Kafka and Apache Spark Structured Streaming. Approximately 100,000 reviews were collected from the Malaysian Google Play Store using the **google-play-scraper** Python library. The collected reviews were preprocessed using Natural Language Processing (NLP) techniques, including text cleaning, tokenization, stopword removal, stemming, and lemmatization.

To classify customer opinions, two machine learning models, namely Naive Bayes and LSTM, were trained and evaluated using standard performance metrics. The best-performing model was then integrated into a streaming architecture, where Apache Kafka continuously streams incoming reviews to Apache Spark for real-time sentiment prediction. The classified results are subsequently stored for visualization and analysis, enabling stakeholders to monitor customer sentiment effectively.

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

This project developed a sentiment analysis model to classify Foodpanda customer reviews into three categories: positive, neutral, and negative.

Two different machine learning approaches were implemented and compared:
- Naive Bayes Classifier
- Long Short-Term Memory (LSTM) Neural Network

The objective is to identify customer opinions from review text and evaluate the performance of different sentiment classification approaches.



#### 3.1 Model Choice

Two models were selected for sentiment classification:

##### 1. Naive Bayes Classifier (Scikit-learn)

Naive Bayes was selected as a baseline machine learning model because it is simple, fast, and suitable for text classification tasks. The review text was converted into numerical features using TF-IDF Vectorization before being classified using the Multinomial Naive Bayes algorithm.



##### 2. Long Short-Term Memory (LSTM) Neural Network (TensorFlow/Keras)

LSTM was selected as a deep learning model because it can learn the sequence and relationship between words in customer reviews. The text data was converted into sequences using Tokenizer and padded into a fixed length before being trained using an Embedding layer, LSTM layer, Dropout layer, and Dense output layer.

Both models were trained and evaluated to compare their performance in sentiment classification.



#### 3.2 Training Process

Before training, the dataset was prepared by selecting the review text (`lemmatized_text`) as the input feature and sentiment label as the output.

The following preprocessing steps were performed:

- Removed missing review text data.
- Converted sentiment labels into numerical values using Label Encoder.

<div align="center">

<table>
  <tr>
    <th>Sentiment</th>
    <th>Label</th>
  </tr>
  <tr>
    <td>Negative</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Neutral</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Positive</td>
    <td>2</td>
  </tr>
</table>

</div>


- Split the dataset into training and testing sets using an 80:20 ratio.
- Stratified splitting was applied to maintain the sentiment distribution.



##### Naive Bayes Training

**Preprocessing**
- Text data was transformed into numerical features using TF-IDF Vectorizer.

**Training**
- The extracted TF-IDF features were used to train the Multinomial Naive Bayes classifier.

**Configuration**
<div align="center">

<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Feature Extraction</td><td>TF-IDF</td></tr>
<tr><td>Maximum Features</td><td>5000</td></tr>
<tr><td>Algorithm</td><td>Multinomial Naive Bayes</td></tr>
</table>

</div>

##### LSTM Training

**Preprocessing**
- Text data was converted into sequences using Tokenizer.
- Padding was applied to make all input sequences have the same length.

**Training**
- The processed sequences were trained using an LSTM neural network to learn patterns from customer reviews.

**Configuration**

<div align="center">

<table>
<tr><th>Parameter</th><th>Value</th></tr>
<tr><td>Vocabulary Size</td><td>10000</td></tr>
<tr><td>Sequence Length</td><td>100</td></tr>
<tr><td>Embedding Dimension</td><td>128</td></tr>
<tr><td>LSTM Units</td><td>64</td></tr>
<tr><td>Batch Size</td><td>64</td></tr>
<tr><td>Optimizer</td><td>Adam</td></tr>
<tr><td>Epochs</td><td>10</td></tr>
</table>

</div>

Early stopping was applied during training to reduce overfitting.



#### 3.3 Evaluation

The performance of both models was evaluated using:

- Accuracy
- Weighted F1-score
- Classification Report
- Confusion Matrix

The results were compared to determine which model provides better sentiment classification performance.

<div align="center">

<table>
  <tr>
    <th>Model</th>
    <th>Accuracy</th>
    <th>Weighted F1-score</th>
  </tr>
  <tr>
    <td>Naive Bayes</td>
    <td>84.62%</td>
    <td>82.41%</td>
  </tr>
  <tr>
    <td>LSTM</td>
    <td>87.00%</td>
    <td>85.30%</td>
  </tr>
</table>

</div>

The confusion matrix was also analysed to observe the number of correctly and incorrectly classified sentiment predictions for each class.

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
