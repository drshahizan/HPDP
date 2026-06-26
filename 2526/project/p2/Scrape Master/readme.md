# Real-Time Sentiment Pipeline for Malaysian Tech-Review YouTube Comments

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-4.1-E25A1C?logo=apachespark&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-7.6-231F20?logo=apachekafka&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.13-005571?logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-8.13-005571?logo=kibana&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Transformers](https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-DistilBERT-FFD21E)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-F7931E?logo=scikit-learn&logoColor=white)
![Course](https://img.shields.io/badge/SECP3133-HPDP-7B1FA2)
![License](https://img.shields.io/badge/license-Academic-43A047)

</div>

A Kafka → Spark → Elasticsearch → Kibana pipeline that listens to Malay/English code-switched comments from the **FUZZ CHANNEL** YouTube channel, classifies each one through a **soft-voting ensemble** of a TF-IDF Logistic Regression and a fine-tuned multilingual DistilBERT, and surfaces the result on a live 10-panel Kibana dashboard within seconds of ingestion.

> Built as the deliverable for **Project 2 — High Performance Data Processing (SECP3133)**, Semester 2, 2025/2026.

---

## 📚 Project Documentation

<div align="center">

| Artefact | Link |
|---|---|
| 📄 Final Report (PDF) | [`reports/final_report.pdf`](https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Scrape%20Master/reports/final_report.pdf) |
| 📄 Turnitin Submission | [`reports/Turnitin_FinalProject.pdf`](reports/Turnitin_FinalProject.pdf) |
| 🎞️ Presentation Slides | [`reports/presentation_slides.pptx`](https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Scrape%20Master/Project%202%20Real%20Time%20Sentiment%20Analysis%20using%20Apache%20Spark%20and%20Kafka.pptx) |
| 🎬 Demo Video | *(to be added)* |
| 🗃️ Raw YouTube Comments | [`data/raw_data/youtube_comments_raw.csv`](https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Scrape%20Master/data/raw_data/youtube_comments_raw.csv) |
| 🧹 Cleaned + Pseudo-labelled Data | [`data/cleaned_data.csv`](https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Scrape%20Master/data/cleaned_data.csv) |
| 🛠️ Preprocessing Notebook | [`notebooks/preprocessing.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Scrape%20Master/notebooks/preprocessing.ipynb) |
| 🧠 Model Training Notebook | [`model_training.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Scrape%20Master/model_training.ipynb) |
| ⚡ Kafka × Spark Pipeline | [`kafka_spark_pipeline/`](https://github.com/drshahizan/HPDP/tree/main/2526/project/p2/Scrape%20Master/kafka_spark_pipeline) |
| 📊 Kibana Dashboard Provisioner | [`kafka_spark_pipeline/kibana_setup.py`](https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Scrape%20Master/kibana_setup.py) |
| 📈 Report Figures | [`reports/figures/`](https://github.com/drshahizan/HPDP/tree/main/2526/project/p2/Scrape%20Master/kafka_spark_pipeline/figures) |

</div>

---

## 👥 Team

| # | Name | Matric No | Primary Role |
|---|---|---|---|
| 1 | *Muhammad Afiq Danish bin Mohd Hazni* | *A23CS0118* | Group Leader & Data Engineer |
| 2 | *Muhammad Adam bin Razali* | *A23CS0116* | NLP & Model Engineer |
| 3 | *PRAVINRAJ A/L SIVABATHI* | *A23CS0171* | Pipeline & Visualization Engineer |

---

## 🎯 Data Source

| | |
|---|---|
| **Channel** | FUZZ CHANNEL — Malaysian tech-review YouTube channel |
| **Content** | Smartphones, tablets, gadgets, software reviews — mixed Malay + English |
| **Volume** | **12,000** comments scraped · **11,836** usable after cleaning |
| **Collection** | YouTube Data API v3 (ToS-clean, no scraping) |
| **Label source** | Pseudo-labels from `cardiffnlp/twitter-xlm-roberta-base-sentiment` |

Label distribution after cleaning: **42.5 % neutral**, **30.9 % negative**, **26.6 % positive**.

---

## 🧠 Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/81300529-43cc-4a3e-aa80-67da9080e849" />


---

## 🧰 Technology used

| Layer | Tools |
|---|---|
| Data Collection | YouTube Data API v3 · `googleapiclient` |
| NLP Preprocessing | NLTK · PySastrawi (Malay stemmer) · Hugging Face Transformers |
| Modelling | scikit-learn (Logistic Regression + TF-IDF) · Hugging Face Transformers (DistilBERT multilingual cased) |
| Ingestion | Apache Kafka 7.6 + Zookeeper · `kafka-python` |
| Stream Processing | Apache Spark 4.1 Structured Streaming · PySpark |
| Storage | Elasticsearch 8.13 |
| Visualisation | Kibana 8.13 |
| Infrastructure | Docker Compose |
| Language | Python 3.13 |

---

## 📊 Model Results

Metrics computed on the held-out test split of **2,368 comments** (70 / 20 / 10 stratified split, seed = 42).

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Inference Speed |
|---|---|---|---|---|---|
| Logistic Regression (TF-IDF) | 0.6136 | 0.6109 | 0.6119 | 0.6112 | ~39,282 rec/s |
| DistilBERT (fine-tuned) | 0.6833 | 0.6791 | 0.6763 | 0.6768 | ~151 rec/s |
| **Ensemble (0.5 / 0.5)** | **0.6921** | **0.6878** | **0.6856** | **0.6866** | ~150 rec/s |

<div align="center">
<img width="2142" height="1477" alt="image" src="https://github.com/user-attachments/assets/dfb11135-7c19-4e63-bc4b-c3f0ca60028b" />

  <br>
  <em>Side-by-side comparison of all four metrics across the three models. Auto-generated by <code>reports/generate_figures.py</code>.</em>
</div>

### Confusion Matrices

<div align="center">

<table>
<tr>
<td align="center" width="33%">
<img width="1051" height="879" alt="image" src="https://github.com/user-attachments/assets/e01a10b1-4c24-43ef-8c35-d7514173dce3" />
<em>Logistic Regression</em>
</td>
<td align="center" width="33%">
<img width="1015" height="879" alt="image" src="https://github.com/user-attachments/assets/770d0c48-c3bb-4126-b306-f8c96c2270e5" />
<em>DistilBERT</em>
</td>
<td align="center" width="33%">
<img width="1046" height="879" alt="image" src="https://github.com/user-attachments/assets/6bdaf1c1-1d7a-4591-86fe-94aee15a98f5" />
<em>Ensemble (0.5 / 0.5) — deployed</em>
</td>
</tr>
</table>

</div>

End-to-end streaming throughput, measured over the full Kafka → Spark → Elasticsearch path: **~28 records / second** on a single GTX 1050 Ti, which is roughly **18 %** of DistilBERT's batch inference speed. The remainder is the price of Kafka serialisation, Spark micro-batch scheduling, and Elasticsearch bulk indexing — i.e. the durability and fault tolerance the streaming architecture provides.

---

## 📸 Dashboard Preview

<div align="center">
 <img width="1894" height="800" alt="Screenshot 2026-06-25 180524" src="https://github.com/user-attachments/assets/5f73107e-eff7-4c9a-9c63-38c3fe55e46d" />
  <em>Full dashboard — 6 KPI cards on top, 4 interactive visualisations below.</em>
</div>
