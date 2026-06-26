<h1 align="center">
  Real-Time Sentiment Analysis of BUDI95 YouTube Comments
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
    <th>Role</th>
  </tr>
  <tr>
    <td>Goe Jie Ying</td>
    <td> A23CS0224 </td>
    <td> Group Leader, NLP & Model Engineer </td>
  </tr>
  <tr>
    <td> Nawwarah Auni binti Nazrudin </td>
    <td> A23CS0143 </td>
    <td> Data Engineer </td>
  </tr>
  <tr>
    <td> Yasmin Batrisyia Binti Zahiruddin </td>
    <td> A23CS0201 </td>
    <td> Pipeline & Visualization Engineer </td>
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
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Fast%26Furious/reports/Final_Report.pdf"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Slides</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=25px height=23px></a>
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
      <a href="https://drive.google.com/file/d/19TiWEuIOY_1NO8Z1GXZfswDU_zTDC-4v/view?usp=drive_link"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="https://drive.google.com/file/d/1r4nbZrxtFcHoTkCA69CgFVmgUQV5AIQQ/view?usp=drive_link"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Jupyter Notebook for Preprocessing</td>
    <td align="center">
      <a href="notebooks/02_Preprocessing.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Jupyter Notebook for Model Training</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Fast%26Furious/notebooks/model_training.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
    <tr>
    <td>Kafka Spark Pipeline</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/tree/main/2526/project/p2/Fast%26Furious/kafka_spark_pipeline"><img width=24px alt="image" src="https://github.com/user-attachments/assets/94653bd8-d182-4344-add6-e579077b2299" />

</a>
    </td>

  </tr>
</table>

---

## 📌 Introduction
In the digital era, online platforms such as YouTube and social media have become important channels for people to express opinions on social issues, products, services, and government policies. These user-generated comments provide valuable insights into public sentiment and perception. Sentiment analysis, a Natural Language Processing (NLP) technique, is used to classify text into categories such as positive, negative, or neutral and is widely adopted by organizations and governments for data-driven decision making.

With the introduction of Malaysia’s BUDI95 fuel subsidy policy, public discussions on YouTube have increased significantly, resulting in a large volume of continuously generated comments. This makes manual analysis inefficient and highlights the need for automated solutions. Although sentiment analysis models can classify opinions, many existing systems focus only on model development and ignore real-time processing requirements. In addition, performance may vary due to data complexity, multilingual content, and informal language commonly found in social media.

To address these challenges, this project develops a real-time sentiment analysis pipeline using Apache Kafka and Apache Spark. YouTube comments related to the fuel subsidy policy are collected through web scraping, preprocessed using NLP techniques, and classified using both machine learning and transformer-based models. The results are then stored in Elasticsearch and visualized using Kibana, enabling real-time sentiment monitoring and analysis.

---

## 🎯 Objectives

The primary goals of this project are:
- To collect YouTube comments related to Malaysia’s fuel subsidy policies using web scraping techniques.  
- To preprocess and clean textual data using Natural Language Processing techniques, including tokenization and stop-word removal.  
- To develop and evaluate sentiment classification models using machine learning and transformer-based approaches.  
- To compare model performance using evaluation metrics such as Accuracy, Precision, Recall, and F1-Score.  
- To implement a real-time sentiment analysis pipeline using Apache Kafka and Apache Spark Structured Streaming.  
- To store sentiment classification results in Elasticsearch and visualize the outputs using Kibana dashboards.  
- To compare the performance of batch processing and streaming processing approaches.  

---

## ⚙️ System Architecture
The architecture of this project uses three major technologies in the Apache ecosystem, which are Apache Kafka, Apache Spark, and Elasticsearch. These components work along to produce a robust pipeline for streaming data, real-time processing and finally provide a dashboard. This section explains each component's roles and how they work together. 

The system consist of three major parts: 

- Apache Kafka: Acts as the high throughput, fault-tolerant message broker. It decouples the data source form processing engine, receiving incoming YouTube comments sequentially and hosting them in  a distributed queue topic. 
- Apache Spark: Used Spark Structured Streaming to ingest micro-batches of data from Kafka in real time. It works by performing JSON schema parsing, deserialization, and coordinate inference through a deep learning sentiment model to enrich the raw stream. 
- Elasticsearch: Serves as the distributed search and analytics engine. It receives the enriched JSON documents (contains the original text, metadata, predicted sentiment labels, and confidence scores) via bulk indexing, making the data instantly queryable for downstream dashboards. 



### Workflow Diagram
![Workflow Diagram](https://github.com/yAsmin241/HPDP-Project/blob/ea0da0a38f5bed46af0482b77fbae91141716793/System%20architecture%20p2.drawio.png)


---

## 🚀 Getting Started

### Prerequisites
- **Docker Desktop** — for Kafka, Zookeeper, Elasticsearch, Kibana
- **Python 3.11** — required (PySpark 3.5.1 is not compatible with Python 3.12/3.13)
- **Java 11 or 17** — required by PySpark (`java -version` to check)
- **`saved_models/`** — folder from the model training notebook (LR, NB, XLM-RoBERTa weights)

---

### Installation and Setup
**1. Clone the repository:**
```bash
git clone https://github.com/drshahizan/HPDP
cd HPDP/2425/project/p2/Fast&Furious/kafka_spark_pipeline
```
 
**2. Create a Python 3.11 virtual environment and activate it:**
```powershell
# Windows PowerShell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```
```bash
# Mac/Linux
python3.11 -m venv venv
source venv/bin/activate
```
 
If PowerShell blocks the activation script, run this first:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
 
**3. Install Python dependencies:**
```bash
pip install -r requirements.txt
```
 
**4. Place required files:**
- Copy the `saved_models/` folder into `kafka_spark_pipeline/`
- Copy `youtube_comments_cleaned_roberta.csv` into `kafka_spark_pipeline/`
  
**5. Start the Docker infrastructure:**
```bash
docker compose up -d
```
 
Wait ~30 seconds, then verify all four containers are running:
```bash
docker compose ps
```
 
Confirm services are healthy:
- Elasticsearch: `http://localhost:9200` → should return JSON with `"You Know, for Search"`
- Kibana: `http://localhost:5601` → should show the Kibana home screen
**6. Fix Windows Spark environment** (required on Windows):
```powershell
Remove-Item Env:\SPARK_HOME -ErrorAction SilentlyContinue
$env:PATH = "C:\hadoop\bin;" + $env:PATH
```
 
> **Note for Windows users:** Spark requires `winutils.exe` and `hadoop.dll` in `C:\hadoop\bin`. Download the Hadoop 3.3.5 pair from [cdarlint/winutils](https://github.com/cdarlint/winutils/tree/master/hadoop-3.3.5/bin) if not already present.
 
---
    
### Running the Pipeline
#### Option A — One-click startup (Windows PowerShell, recommended)
 
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\start_demo.ps1
```
 
Wait for:
```
Streaming from topic 'youtube-comments' -> index 'sentiment-results'.
Start the producer in another terminal. Ctrl-C to stop.
```
 
#### Option B — Manual startup
 
```powershell
python setup_index.py --index sentiment-results --recreate
docker exec kafka kafka-topics --create --topic youtube-comments --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
Remove-Item -Recurse -Force _chk_sentiment -ErrorAction SilentlyContinue
$env:MODEL_OVERRIDE="lr"
python spark_streaming.py
```
 
#### Stream the data (second terminal)
 
```powershell
.\venv\Scripts\Activate.ps1
python kafka_producer.py --delay 0
```
 
Expected Spark output:
```
[sentiment_model] loaded 'sklearn' (classical) from saved_models
[batch 1]  200 records |  3.798s |    52.7 rec/s -> ES
[batch 2] 3149 records |  0.175s | 17998.9 rec/s -> ES
```
 
#### Verify data
```
http://localhost:9200/sentiment-results/_count
```
Should return `"count": 3349`.

---

### Accessing the Dashboard
1. Open `http://localhost:5601`
2. Navigate to **☰ menu → Dashboard**
3. Open **Malaysian YouTube Sentiment Dashboard**
4. Set the time range to **Today** if panels appear empty
To import the dashboard from file:
- **☰ → Stack Management → Saved Objects → Import** → select `dashboard/kibana_visualizations.json`
The dashboard includes:
- **Sentiment Distribution** — pie chart (56.11% negative, 30.31% neutral, 13.59% positive)
- **Sentiment Metrics** — absolute counts (1,879 / 1,015 / 455)
- **Confidence Distribution** — histogram of model prediction confidence
- **Sentiment Over Time** — time-series by sentiment class


---

## 📂 File Descriptions
- `README.md`: This file.
- `data/`: Raw and cleaned YouTube comments collected from 16 videos related to Malaysia's BUDI95 fuel subsidy policy.
- `notebooks/`: Google Colab notebooks covering the full pipeline from scraping to sentiment labelling and model training.
- `kafka_spark_pipeline/`: Python scripts for streaming YouTube comments through Apache Kafka and classifying them in real time using Apache Spark.
- `dashboard/`: Kibana dashboard export file for visualising real-time sentiment results.
- `reports/`: Final project report documenting the full system development and findings.

---

## 📊 Results

The analysis of the Reddit comments yielded several key insights:



### Kibana Dashboard


---

## 🛠️ Optimization and Comparison

### Model Comparison

| Model | Accuracy | Precision (Neg / Neu / Pos) | Recall (Neg / Neu / Pos) | F1-Score (Neg / Neu / Pos) |
|---|---|---|---|---|
| Multinomial Naive Bayes | 0.6388 | 0.68 / 0.53 / 0.37 | 0.86 / 0.38 / 0.09 | 0.76 / 0.44 / 0.14 |
| Logistic Regression | 0.6373 | 0.75 / 0.49 / 0.36 | 0.75 / 0.53 / 0.30 | 0.75 / 0.51 / 0.33 |
| XLM-RoBERTa ⭐ | **0.7403** | **0.81 / 0.66 / 0.53** | **0.83 / 0.65 / 0.47** | **0.82 / 0.66 / 0.50** |    

Naive Bayes achieved the lowest performance with a weighted F1 of 0.5987,
struggling heavily on the positive class (F1 = 0.14) due to its tendency
to over-predict the dominant negative class. Logistic Regression improved
slightly to a weighted F1 of 0.6357 through balanced class weighting, with
notable gains on the neutral and positive classes. XLM-RoBERTa outperformed
both classical models with a weighted F1 of 0.7381 and accuracy of 74.03%,
benefiting from its multilingual pretraining on 100 languages including Malay,
which allowed it to handle code-switched Manglish comments more effectively
than TF-IDF-based approaches.


---

## 🏋️ Conclusion
This project built a real-time sentiment analysis pipeline for YouTube comments on Malaysia's BUDI95 fuel subsidy policy. A total of 3,448 comments were collected from 16 YouTube videos, preprocessed using NLP techniques, and labelled using XLM-RoBERTa. Among the three models evaluated, XLM-RoBERTa performed best with a weighted F1-score of 0.7381 and accuracy of 74.03%. Sentiment analysis revealed that 61.5% of public comments were negative, which reflects strong public dissatisfaction toward the policy. The pipeline was integrated with Apache Kafka, Spark Structured Streaming, Elasticsearch, and Kibana for real-time monitoring. It achieves 81.19% classification accuracy in both batch and streaming modes.

---

## 🚀 Future Work

- Expand data collection to other platforms such as X (Twitter), Facebook, and Threads for a more complete picture of public opinion
- Build a more comprehensive Malay slang dictionary and improve language detection specifically for Manglish text
- Add emoji sentiment mapping to retain emotional signals that are currently removed during preprocessing
- Explore stronger multilingual models such as XLM-RoBERTa-Large or mBERT fine-tuned on a larger Malaysian social media corpus to improve performance, especially on the minority positive class
- Deploy XLM-RoBERTa directly in the streaming pipeline on GPU-backed infrastructure for higher accuracy in real-time classification
