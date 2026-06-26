<h1 align="center"> 
  AyamGepuk - 	Air Asia App
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD NAIM BIN ABDULLAH</td>
    <td>A23CS0138</td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD MUKHRITZ AL IMAN BIN MOHD RAFFI</td>
    <td>A23CS0250</td>
  </tr>
  <tr>
    <td width=80%>SYARIFAH DANIA BINTI SYED ABU BAKAR</td>
    <td>A23CS0183</td>
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
      <a href="reports"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
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
        <a href="data">
          <img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591/" width="25px" height="23px">
        </a>
      </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
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

Recently, the aviation and travel sector has turned to or using digital platforms to optimize their operation and also customer relations. As the leading low-cost carrier in the region, AirAsia depends heavily on its mobile app for bookings, check-ins, updates, and support. Because of this, mobile app reviews are more than just a personal feedback; they provide valuable information that reflects real-time public sentiment, customer satisfaction and operational issues.

This project deploys an end-to-end, live sentiment analysis pipeline that ingests, processes, and evaluates user feedback for the AirAsia mobile app. By observing the trends in feedback, stakeholders can dynamically identify system bugs, user interface bottlenecks, and operational failures as they occur. To handle the high volume and velocity of incoming review streams, the system utilizes a high-performance big data architecture powered by Apache technologies for data ingestion, cleaning, sentiment scoring, and persistent storage.

#### 1.2 Objectives

The main objectives of this project are:
- To build a production-ready, real-time sentiment analysis data pipeline focused on user feedback for the AirAsia mobile application.
- To implement an Apache Kafka messaging cluster to stream raw Google Play Store reviews reliably and concurrently.
- To leverage Apache Spark Structured Streaming for low-latency streaming ingestion and real-time distributed execution of machine learning models.
- To use Elasticsearch for storing processed results. 
- To visualize sentiment trends using Kibana dashboards.
- To classify comments into positive, neutral, or negative sentiments using multiple machine learning models. 



#### 1.3 Scope

This project covers the following key components:
- Ingesting a dataset of approximately 40,000 historic and active mobile reviews of the AirAsia application directly from the Google Play Store.
- Structuring text normalization techniques using Natural Language Processing (NLP) tools to clean unstructured review scripts.
- Implementing and serializing a statistical machine learning classifier (Naive Bayes) and a Deep Learning Sequence model (LSTM) to run concurrent comparative   sentiment inference.
- Displaying real-time sentiment results through a Kibana dashboard. 


---

### 2.0 Data Acquisition & Preprocessing

#### 2.1 Sources

The textual dataset used for the baseline training and downstream streaming emulation originates directly from public user logs on the Google Play Store. The application under analysis is the official AirAsia mobile app. To generate sufficient data variety and capture micro-trends, seasonal booking surges, and historical release stability, approximately 40,000 rows of user reviews were requested. The raw inputs capture vital attributes such as the user review text, the reviewer's star rating, app version, and timestamp metadata. 

Sources for scrapping
https://play.google.com/store/apps/details?id=com.airasia.mobile&hl=en


#### 2.2 Tools

- Google Play Scraper: Collects user reviews directly from the Google Play Store.
- Python Frameworks Cleans the data and saves trained models.
- Apache Kafka: Streams the collected reviews in real time.
- Apache Spark Structured Streaming: Processes the live data stream instantly and reliably.
- NLP Libraries : Cleans and prepares the review text by breaking down words and finding their root forms.


#### 2.3 Cleaning Steps

Raw user reviews on app stores are highly unformatted and contain noise. To clean the data before model ingestion, the text was processed through an automated NLP pipeline containing these steps:
1. Case Normalization: Converted all review text strings to lowercase to enforce feature uniformity.
2. Noise and Character Filtering: Filtered out emojis, non-ASCII characters, app symbols, hyper-text markup links, and punctuation marks using regular expressions.
3. Tokenization: Split text blocks into individual semantic tokens or words via NLTK word splitters.
4. Stopword Elimination: Filtered out standard English stopwords like ”the”, “is” that contain zero unique contextual sentiment weights.
5. Lemmatization: Applied spaCy’s morphological processor (en_core_web_sm) to reduce inflectional word variants to their canonical root forms


---

### 3.0 Sentiment Model Development

#### 3.1 Model Choice

Two models were selected to classify AirAsia reviews as positive, neutral, or negative : 
 
Naive Bayes Classifier : 
very fast, lightweight, and resource efficient probabilistic model ideal for low-latency live streaming 

LSTM Neural Network : 
A deep learning model that captures word order and long term context, which is good for understanding complex or mixed user feedback for example praising the price but complaining about the app.

#### 3.2 Training Process

- The cleaned dataset (25000 comments) was split into 70% training, 20% testing and 10 % evaluate sets
- Naive Bayes : The text was converted into numerical features using TF-IDF Vectorizer and trained using Scikit-Learn.
- LSTM : Text was converted into padded integer sequences, passed through an Embedding layer, a spatial dropout layer, an LSTM layer, and a dense output layer with softmax activation. 

#### 3.3 Evaluation



---

### 4.0 Apache System Architecture

The System has been divided into 2 pipelines which is Batch Processing (Historical Collection & Optimization) and Real Time Processing ( Live Streaming Ingestion & Inference Engines). 

Batch Processing 

- Ingestion and Labeling : 
Scrapes user reviews of the AirAsia Apps from the app store page and saves it as CSV files.

- Feature Extraction and Training :
Cleans the review text using NLP techniques and trains both model which is Naive Bayes and LSTM models.
 
- Asset Packaging : 
Saves the final trained models and components into storage so it can be used later by the streaming engine.

Streaming Processing 

- Collecting Live Data : 
Apache Kafka collect new user reviews in real time exactly as they are posted

- Reading the Stream : 
Apache Spark connect to Kafka so it can read the incoming reviews instantly

- Analyzing Sentiment :
Spark sends the text to the trained AI models and it will classify if the review is positive, neutral or negative.

- Stream Sinks :
The prediction are saved in two place which in SQLite and CSV file 	

- Visualization :
Using Matplotlip and Seaborn to create an interactive dashboard that show what users are saying about the app over time 


---

### 5.0 Analysis & Results

#### 5.1 Key Findings



#### 5.2 Visualizations



#### 5.3 Insights



---

### 6.0 Optimisation & Comparison



---

### 7.0 Conclusion & Future Work

The data pipeline uses the Google Play Scrapper to extract customer reviews from the Google Play store. The data is then cleaned and structured for serialization utilizing foundational Python frameworks, including Pandas, NumPy, and Pickle. Apache Kafka is then being used to handle the real-time data flow while Apache Spark is structured streaming that makes the process to be faster and more reliable. Finally, NLP libraries like NLTK and spaCy will handle the underlying text preparation by breaking down review sentences into individual tokens and reducing words to their base grammatical forms. 

As a future enhancement, This pipeline can be scaled widely by integrating others platform to get more data such as Apple App Store APIs to ingest iOS user feedback alongside the existing Android stream. Furthermore, implementing Aspect-Based Sentiment Analysis (ABSA) within the Spark streaming layer will allow the pipeline to automatically separate software bugs from broader airline operational complaints, yielding much more specific, actionable insights. 

---

### 8.0 References



---

### 9.0 Appendix
