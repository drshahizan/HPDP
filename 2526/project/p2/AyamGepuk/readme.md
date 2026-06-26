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



#### 2.2 Tools



#### 2.3 Cleaning Steps



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
