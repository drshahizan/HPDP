<h1 align="center"> 
  Ziyaad - Real-Time Sentiment Analysis on Touch 'n Go eWallet Reviews in Google Play App
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>AHMAD ZIYAAD BIN MOHD ABBAS</td>
    <td>A23CS0206</td>
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
      <a href="reports/proj2_report_ziyaad.pdf"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Slides</td>
    <td align="center">
      <a href="reports/proj2_slides_ziyaad.pptx"><img src="https://github.com/user-attachments/assets/c09e2ce5-80ce-4236-9508-c65d1f079cda" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Video</td>
    <td align="center">
      <a href="<!-- FILL: YOUTUBE LINK -->"><img src="https://github.com/user-attachments/assets/2dec74b1-9d2d-4cec-ae38-a57f7ac1711c" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Raw Data</td>
    <td align="center">
      <a href="data/raw_data/combined_raw.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="data/cleaned_data.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocessing (NLP cleaning &amp; labeling)</td>
    <td align="center">
      <a href="notebooks/preprocessing.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Model Training (Naive Bayes &amp; LSTM)</td>
    <td align="center">
      <a href="notebooks/model_training.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Kafka + Spark Streaming Pipeline</td>
    <td align="center">
      <a href="kafka_spark_pipeline/kafka_spark_streaming_colab.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Elasticsearch Dashboard</td>
    <td align="center">
      <a href="dashboard/elasticsearch_dashboard_colab.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
</table>

---

## 1. Project Overview

This project builds a complete **real-time sentiment analysis pipeline** for Malaysian-relevant
text data, following the Project 2 brief for **High Performance Data Processing (SECP3133)**.

Google Play reviews for **Touch 'n Go eWallet** (`my.com.tngdigital.ewallet`) are scraped,
cleaned with NLP, labeled, and classified by two trained models. The classified output is
streamed through **Apache Kafka + Apache Spark Structured Streaming**, stored in
**Elasticsearch**, and visualized through interactive dashboards. Batch and streaming
performance are compared directly.

## 2. Data Source

| Item | Detail |
|---|---|
| Source | Google Play Store reviews (Touch 'n Go eWallet, `my.com.tngdigital.ewallet`) |
| Tool | `google-play-scraper` (no API key required) |
| Volume collected | 10,000 raw reviews |
| After cleaning & dedup | 9,979 reviews |
| Labeling | Star rating → sentiment: 1–2★ = negative, 3★ = neutral, 4–5★ = positive |

**Why Touch 'n Go eWallet:** 28M+ Malaysian users (no shortage of reviews) and an emotionally
charged, transactional app that produces strong sentiment signal.

## 3. Tech Stack

| Layer | Tool |
|---|---|
| Data collection | `google-play-scraper` (Python) |
| Preprocessing | NLTK — cleaning, tokenization, stopword removal, lemmatization |
| Models | Naive Bayes (scikit-learn) vs LSTM (TensorFlow/Keras) |
| Streaming | Apache Kafka + Apache Spark Structured Streaming |
| Storage | Elasticsearch |
| Dashboard | Plotly / Elasticsearch (interactive HTML dashboards) |

## 4. Results

### 4.1 Class Distribution (cleaned dataset, 9,979 reviews)

| Sentiment | Count | Percentage |
|---|---|---|
| Negative | 6,944 | 69.6% |
| Positive | 2,002 | 20.1% |
| Neutral | 1,033 | 10.4% |

The neutral class is heavily underrepresented — a known property of star-rating-based labeling
(reviewers rate at the extremes). This is addressed with class weighting rather than discarding data.

### 4.2 Model Comparison

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Train Time (s) | Predict Time (s) | Throughput (rev/s) |
|---|---|---|---|---|---|---|---|
| Naive Bayes | 0.6844 | 0.5791 | 0.6166 | 0.5797 | 0.018 | 0.001 | 997,834 |
| LSTM | 0.7425 | 0.4497 | 0.5346 | 0.4839 | 104.461 | 0.7095 | 1,407 |

**Interpretation:** LSTM achieves higher overall **accuracy (74.3%)** by performing well on the
dominant negative class, but Naive Bayes has the better **macro-F1 (0.58 vs 0.48)** — i.e. it is
more balanced across the minority neutral/positive classes. Naive Bayes is also ~700× faster at
inference, which is why it is the model deployed in the real-time streaming pipeline.

### 4.3 Batch vs Streaming Performance

| Mode | Reviews | Total Time (s) | Throughput (rev/s) |
|---|---|---|---|
| Batch | 9,979 | 0.201 | 49,686 |
| Streaming (Kafka + Spark) | 3,000 | 4.98 | 636 |

Batch processing is far higher throughput on a fixed dataset, while the Kafka + Spark streaming
path trades raw speed for real-time, record-by-record processing of incoming reviews.

## 5. System Architecture

```
Google Play  ──► scraper ──► raw CSV ──► preprocessing (NLTK) ──► cleaned + labeled CSV
                                                                        │
                                              ┌─────────────────────────┴───────────┐
                                              ▼                                       ▼
                                  model training (NB / LSTM)               Kafka producer
                                              │                                       │
                                              ▼                                       ▼
                                      saved model ───────────────► Spark Structured Streaming
                                                                    (classify in real time)
                                                                           │
                                                                           ▼
                                                                    Elasticsearch ──► Dashboards
```

## 6. How to Run

1. **Scrape data:** run `scraper/scrape_reviews.py` to collect Google Play reviews into `data/raw_data/`.
2. **Preprocess:** run `notebooks/preprocessing.ipynb` to clean, label, and export `data/cleaned_data.csv`.
3. **Train models:** run `notebooks/model_training.ipynb` to train and compare Naive Bayes and LSTM
   (saves models into `kafka_spark_pipeline/`).
4. **Stream:** run `kafka_spark_pipeline/kafka_spark_streaming_colab.ipynb` to start Kafka + Spark and
   classify reviews in real time, exporting `classified_reviews_for_elasticsearch.csv`.
5. **Dashboard:** run `dashboard/elasticsearch_dashboard_colab.ipynb` to load results into Elasticsearch
   and build the interactive dashboards.
