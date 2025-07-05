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
### 4.0 Apache System Architecture

**Figure 1: System Architecture Diagram**

The system is divided into two main pipelines: **Batch Processing** and **Real-Time Processing**, both working together to analyze YouTube comments related to “Travelling in Malaysia”.

**Batch Processing:**

- **Scraping & Labeling:** YouTube comments are scraped and labeled using Hugging Face models, followed by manual verification to ensure accuracy.  
- **Model Training:** Cleaned and labeled data is used to train sentiment classification models which are LSTM and Naive Bayes.  
- **Model Deployment:** The trained model is exported, imported into a Python prediction script, and integrated into Apache Spark for further use.

**Real-Time Processing:**

- **Streaming:** New comments are streamed in real time via Apache Kafka.  
- **Sentiment Analysis:** Apache Spark consumes these streams, applies the trained sentiment model, and processes the data.  
- **Storage & Visualization:** Processed comments with sentiment results are stored in Elasticsearch and visualized using Kibana dashboards for real-time trend monitoring.

---

### 5.0 Analysis & Results

#### 5.1 Key Findings

The sentiment analysis was performed on a total of 2,391 comments, with an average model confidence score of 0.812 from the Hugging Face model, indicating generally reliable sentiment predictions. Three models, Naive Bayes, Hugging Face, and LSTM were used to classify comments into positive, neutral, and negative categories.  
From the Naïve Bayes model, the sentiment distribution showed a dominant 75.53% positive, 20.95% neutral, and only 3.51% negative comments. The Hugging Face model was comparatively balanced, with 51.36% positive, 40.8% neutral, and 7.83% negative. Meanwhile, the LSTM model predicted a higher number of neutral comments at 53.99%, followed by 43.37% positive, and 2.64% negative.  
The word cloud analysis revealed that 'Malaysia', 'video', 'KL', 'love', and 'thank' were among the most frequently mentioned keywords, suggesting topics of interest and recurring themes in the comments. Additionally, the sentiment distribution by keywords indicates that words such as 'Malaysia', 'video', 'love', and 'thank' are predominantly associated with positive sentiments.


#### 5.2 Visualizations

We used Kibana to do visualizations. We did some analysis on the total number of comments that had been scrapped, average of hugging face score and some perspectives of LSTM and Naive Bayes model. Besides, we use a word cloud to show which word is frequently used. We did pie charts on different models such as Naive Bayes, Hugging Face and LSTM Model to know their distribution on each type of sentiment (negative, neutral, positive). Not only that, a histogram is constructed to know what are the Top 15 appearance keywords.

**Figure 2: Dashboard Part 1**  
**Figure 3: Dashboard Part 2**  
**Figure 4: Dashboard Part 3**


#### 5.3 Insights

The overall perception in the data set is found as mostly positive and has been emphasized by Naive Bayes model that found more than three-quarters in the comments as positive. Overall, it implies that the general attitude towards the comments is rather positive and appraisive, as well as encouraging and affirming. Hugging Face and the LSTM models however present a less optimistic picture where a larger percentage of neutral remarks, denoting a different sense of sentiment based on the sensitivity and requirements of a specified model.  
The abundance of words like the names of the country of residence (Malaysia), the city (KL), and the notion of love in the word cloud and the positive connotations attached to them indicate a great level of national pride and curiosity of the citizens regarding local tourist information, and the loving interaction with the audience. Moreover, positive tones are also used due to the words such as ‘thank, beautiful, and so on, which makes it obvious that much of the audience contact is pleasant and is considered to be appreciative.  
One of the major insights is variation of model behavior. As opposed to Naive Bayes, which is optimistic, LSTM is more objective towards the comments. This implies that the choice of models can also affect the sentiment analysis significantly and has to be addressed when forming the conclusions or making the business decisions based on the sentiment information.


