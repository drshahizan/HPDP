<h1 align="center">
  Real-Time Sentiment Analysis of Reddit Movie Comments
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
    <th>Role</th>
  </tr>
  <tr>
    <td width=80%>Goe Jie Ying</td>
    <td> A23CS0224 </td>
    <td> Group Leader, NLP & Model Engineer </td>
  </tr>
  <tr>
    <td width=80%> Nawwarah Auni binti Nazrudin </td>
    <td> A23CS0143 </td>
    <td> Data Engineer </td>
  </tr>
  <tr>
    <td width=80%> Yasmin Batrisyia Binti Zahiruddin </td>
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
      <a href=""><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
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
      <a href="https://youtu.be/EY0r6jGFGqY?si=8LtOilehTcim6CJN"><img src="https://github.com/user-attachments/assets/2dec74b1-9d2d-4cec-ae38-a57f7ac1711c" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Raw Data</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Jupyter Notebook for Preprocessing</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Jupyter Notebook for Model Training</td>
    <td align="center">
      <a href=""><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
</table>

---

## 📌 Introduction

This project showcases a real-time sentiment analysis pipeline designed to process and visualize opinions from Reddit, focusing on discussions within movie-related subreddits. By leveraging a powerful stack of big data technologies, including **Apache Kafka**, **Apache Spark**, and the **Elastic Stack** (Elasticsearch and Kibana), the system can ingest, analyze, and display sentiment from a continuous stream of Reddit comments. The core of the analysis is a sentiment classification model that categorizes comments as positive, negative, or neutral.

---

## 🎯 Objectives

The primary goals of this project are:

* **Data Collection and Preprocessing**: To gather a substantial dataset of Reddit comments and clean the text to prepare it for analysis.
* **Model Development and Comparison**: To train and evaluate two distinct sentiment analysis models: a classical **Multinomial Naïve Bayes** model and a more advanced **Bidirectional Long Short-Term Memory (Bi-LSTM)** network.
* **Real-Time Data Pipeline**: To build and deploy a Dockerized Apache-based architecture capable of performing near-real-time sentiment analysis on streaming data.
* **Interactive Visualization**: To create a dashboard that presents actionable insights and visual representations of the sentiment data.

---

## ⚙️ System Architecture

The project is built around a three-tier architecture that facilitates a seamless flow of data from ingestion to visualization.

1.  **Apache Kafka**: Acts as the central nervous system of the pipeline. A Python-based producer script uses the Reddit API to fetch comments in real-time and streams them into a Kafka topic. This provides a scalable and fault-tolerant buffer for the incoming data.

2.  **Apache Spark**: Serves as the processing engine. Spark's Structured Streaming API consumes the data from the Kafka topic, performs necessary cleaning and transformations, and applies the trained sentiment analysis model to each comment.

3.  **Elasticsearch and Kibana**: Form the storage and visualization layer. The processed and sentiment-analyzed data from Spark is indexed in Elasticsearch, a powerful search and analytics engine. Kibana is then used to create interactive dashboards and visualizations, allowing for an in-depth exploration of the data.

The entire architecture is containerized using **Docker**, ensuring portability and ease of deployment.

### Workflow Diagram



---

## 🚀 Getting Started

### Prerequisites

* Docker and Docker Compose
* Python 3.8+


### Installation and Setup

1.  **Clone the repository:**
    

2.  **Create a `.env` file** in the root directory and add your Reddit API credentials:
   

3.  **Build and start the Docker containers:**
    

### Running the Pipeline

1.  **Start the Kafka producer** to begin streaming Reddit comments:
    

2.  **Submit the Spark streaming job** to start processing the data:
    

### Accessing the Dashboard



---

## 📂 File Descriptions



---

## 📊 Results

The analysis of the Reddit comments yielded several key insights:



### Kibana Dashboard


---

## 🛠️ Optimization and Comparison



### Model Comparison

| Model       | Accuracy    | Precision (Pos/Neg/Neu) | Recall (Pos/Neg/Neu)   | F1-Score (Pos/Neg/Neu) |



---

## 🏋️ Conclusion



---

## 🚀 Future Work


