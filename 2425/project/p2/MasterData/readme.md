<h1 align="center"> 
  MasterData - Real-Time Sentiment on Youtube's Video Comments related to Traveling in Malaysia
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>BERNICE LIM JING XUAN</td>
    <td>A22EC0038</td>
  </tr>
  <tr>
    <td width=80%>KEK JESSLYN</td>
    <td>A22EC0057</td>
  </tr>
  <tr>
    <td width=80%>TAN JUN YUAN</td>
    <td>A22EC0107</td>
  </tr>
</table>

---

### 1.0 Introduction

#### 1.1 Background

Over the last few years, Malaysia has registered a high rise in tourism due to a diversity of cultures, landscapes and present-day amenities. As the amount of digital content has increased, YouTube has turned into a potent window that travellers use to chart and report their experiences. 

The remarks made by viewers on travel-related videos do not just constitute a matter of personal opinion but can also become an excellent source of data to define public attitudes towards tourism in Malaysia.

This project explores the use of **real-time sentiment analysis** to comprehend how people feel about travelling in Malaysia by reviewing YouTube comments. An entire **big data pipeline** was created using Apache technologies to **ingest**, **process**, and **analyze** this comment data.

We used the **YouTube Data API** to retrieve comments from 10 YouTube videos featuring travel experiences in Malaysia. A total of **2730 raw comments** were collected, cleaned, and manually categorized into **positive**, **neutral**, and **negative** sentiments. Any inconsistencies were re-labelled using the **Hugging Face pre-trained transformer model** and manually verified.

Two models—**Naive Bayes** and **LSTM**—were trained and evaluated for classification performance. Then, a streaming data pipeline was developed using **Dockerized Apache Kafka** to send new YouTube comments into **Apache Spark Structured Streaming** for real-time predictions with all three models: Naive Bayes, LSTM, and Hugging Face. Results were stored in **Elasticsearch** and visualized on a **Kibana dashboard**.

#### 1.2 Objectives

The main objectives of this project are:

- ✅ Build a **real-time sentiment analysis pipeline** focused on YouTube travel comments in Malaysia  
- ⚙️ Use **Apache Kafka** for real-time data ingestion  
- 🔄 Use **Apache Spark** for real-time sentiment classification  
- 🗃️ Store processed results in **Elasticsearch**  
- 📊 Visualize trends using **Kibana dashboards**  
- 🧠 Apply multiple models (Naive Bayes, LSTM, Hugging Face) to classify sentiments as **positive**, **neutral**, or **negative**


#### 1.3 Scope

This project involves the following components:

- Collecting comments from selected YouTube travel videos using the **YouTube API**
- Cleaning and preprocessing using **NLP techniques**
- Training and evaluating three sentiment models: **Naive Bayes**, **LSTM**, and **Hugging Face Transformer**
- Developing a real-time data pipeline using **Kafka**, **Spark**, and **Elasticsearch**
- Displaying live sentiment results with **Kibana**
- Focusing analysis on **public opinion about travel in Malaysia**

---

### 2.0 Data Acquisition & Preprocessing

#### 2.1 Sources

Comments were collected from over 20 YouTube videos related to Malaysian travel experiences. These videos were chosen for their relevance, popularity, and location diversity.

**Sample URLs:**

- https://www.youtube.com/watch?v=fqlaE_NSjS0  
- https://www.youtube.com/watch?v=UKy1WGdlXdg  
- https://www.youtube.com/watch?v=S2NDPhOeSfI  
- https://www.youtube.com/watch?v=kNR61myFC1s  
- https://www.youtube.com/watch?v=KH3wGlxHg_4  
- https://www.youtube.com/watch?v=Qx4KNva9DWk  
- https://www.youtube.com/watch?v=G1UrANBKY_k  
- https://www.youtube.com/watch?v=ze6M63y8Rm4  
- https://www.youtube.com/watch?v=ajxkQYxLNdY  
- https://www.youtube.com/watch?v=g6fb0yzziMM  
- https://www.youtube.com/watch?v=Xv0velteJnc  
- https://www.youtube.com/watch?v=LtPBMvHa8Y8  
- https://www.youtube.com/watch?v=stSMG6tvsrw  
- https://www.youtube.com/watch?v=EVG-IH8cMYs  
- https://www.youtube.com/watch?v=jgK-sFaxr6E  
- https://www.youtube.com/watch?v=jobgAn1GQrI  
- https://www.youtube.com/watch?v=GrECQdICe6A  


#### 2.2 Tools

- **YouTube Data API v3** – for comment extraction  
- **Python** – scripting and preprocessing  
- **Apache Kafka** – real-time streaming  
- **Google Colab** – model training  
- **Jupyter Notebook** – EDA and experimentation  
- **NLTK**, **spaCy**, **Hugging Face Transformers** – for NLP


#### 2.3 Cleaning Steps

- Converted text to **lowercase**
- Removed **emojis**, **special characters**, and **URLs**
- **Tokenized** comments into individual words
- Removed **English stopwords**
- Applied **stemming/lemmatization**
- **Labeled** comments manually and corrected with **Hugging Face transformer model**

---

### 3.0 Sentiment Model Development

#### 3.1 Model Choice

Three models were selected and compared:

- **Naive Bayes Classifier (Scikit-learn)**  
  - A fast and interpretable baseline model

- **LSTM Neural Network (TensorFlow)**  
  - Captures the **sequential nature** of language in comments

- **Hugging Face Transformer**  
  - Pretrained model: `cardiffnlp/twitter-roberta-base-sentiment`  
  - Trained on **social media sentiment** and used directly for inference



#### 3.2 Training Process

- Dataset: **2730 cleaned comments**
- Split into **training** and **testing** sets
- **Naive Bayes**: Trained on **TF-IDF** features
- **LSTM**: Used **GloVe word embeddings** + padded sequences
- **Hugging Face**: Used out-of-the-box for inference



#### 3.3 Evaluation

- **Naive Bayes Accuracy**: ~79%  
- **LSTM Accuracy**: ~85%  
- **Hugging Face**: Used as a **reference model only**

---


