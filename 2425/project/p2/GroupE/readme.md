<h1 align="center"> 
  Group E - Youtube Comments Sentiment Analysis
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>DANIAL HARRIZ BIN MOHD ASINEH @MOHD ASNEH</td>
    <td>A22EC0152</td>
  </tr>
  <tr>
    <td width=80%>CHAI YU TONG</td>
    <td>A22EC0145</td>
  </tr>
  <tr>
    <td width=80%>KOH SU XUAN</td>
    <td>A22EC0060</td>
  </tr>
  <tr>
    <td width=80%>TIEW CHUAN RONG</td>
    <td>A22EC0112</td>
  </tr>
</table>

### Links for related documents:
<table>
  <tr>
    <th>Documents</th>
    <th>Links</th>
  </tr>
  <tr>
    <td>Report</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2425/project/p2/GroupE/reports/final_report.pdf"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Presentation Slides</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2425/project/p2/GroupE/reports/presentation_slides.pptx"><img src="https://github.com/user-attachments/assets/c09e2ce5-80ce-4236-9508-c65d1f079cda" width=25px height=23px？</a>
    </td>
  </tr>
  <tr>
    <td>Presentation Video</td>
    <td align="center">
      <a href="https://youtu.be/yIZRAfI5rMA"><img src="https://github.com/user-attachments/assets/2dec74b1-9d2d-4cec-ae38-a57f7ac1711c" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Raw Data</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2425/project/p2/GroupE/data/youtube_comments.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2425/project/p2/GroupE/data/cleaned_youtube_comments.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px？</a>
    </td>
  </tr>
  <tr>
    <td>Preprocess</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2425/project/p2/GroupE/notebooks/preprocessing.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Train Model</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2425/project/p2/GroupE/notebooks/model_training.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
</table>

---
## Table of Contents

### 1.0 [Introduction](#10-introduction)  
- 1.1 [Background of the Project](#11-background-of-the-project)  
- 1.2 [Objectives](#12-objectives)  
- 1.3 [Project Scope](#13-project-scope)  

### 2.0 [Data Acquisition & Preprocessing](#20-data-acquisition--preprocessing)  
- 2.1 [Data Source](#21-data-source)  
- 2.2 [Data Acquisition Tools and Process](#22-data-acquisition-tools-and-process)  
- 2.3 [Data Preprocessing and Cleaning Steps](#23-data-preprocessing-and-cleaning-steps)  

### 3.0 [Sentiment Model Development](#30-sentiment-model-development)  
- 3.1 [Model Choice](#31-model-choice)  
- 3.2 [Training Process](#32-training-process)  

### 4.0 [Apache System Architecture](#40-apache-system-architecture)  
- 4.1 [Component Roles and Configuration](#41-component-roles-and-configuration)  
- 4.2 [Workflow Diagram and Data Flow](#42-workflow-diagram-and-data-flow)  

### 5.0 [Analysis & Results](#50-analysis--results)  
- 5.1 [Key Findings](#51-key-findings)  
- 5.2 [Visualization](#52-visualization)  

### 6.0 [Optimization & Comparison](#60-optimization--comparison)  
- 6.1 [Model Optimization](#61-model-optimization)  
- 6.2 [Model Comparison](#62-model-comparison)  

### 7.0 [Conclusion & Future Work](#70-conclusion--future-work)  

---
## 1.0 Introduction

### 1.1 Background of the Project

In our current digital era, social media platforms have truly transformed into key avenues where people express themselves and share their feelings, particularly during significant cultural and religious events. Hari Raya, as one of Malaysia's most celebrated festivals, consistently generates substantial online engagement through various social media platforms. Among these, YouTube notably emerges as a prominent platform for sharing festive content, music, and diverse cultural expressions.

The increase of user-generated content during Hari Raya celebrations shows an opportunity to understand public sentiment and cultural engagement patterns. However, manually analyzing thousands of comments across multiple videos is time consuming and not practical. This project addresses this challenge by implementing an automated real-time sentiment analysis pipeline that leverages cutting-edge big data technology to process and analyze YouTube comments related to Hari Raya.

The system integrates multiple Apache technologies to create a scalable, distributed architecture capable of handling large volumes of streaming data. By combining batch processing, data streaming, machine learning and real-time analysis, this project demonstrates how modern data engineering practices can be applied to extract meaningful insights from social media content that provides valuable perspective on public sentiment during cultural celebrations.

### 1.2 Objectives

- **Real-time Data Processing**  
  Develop a streaming pipeline that can continuously collect and process YouTube comments related to Hari Raya videos using Apache Kafka for data ingestion and Apache Spark for distributed processing.

- **Sentiment Analysis Implementation**  
  Implement and deploy machine learning models to automatically classify comment sentiments as positive, negative, or neutral for enabling real-time understanding of public sentiment. In this project, we have used the Logistic Regression model.

- **Data Visualization and Monitoring**  
  Create interactive dashboards using Kibana to visualize sentiment trends, comment patterns and real-time analysis to provide actionable insights.

- **Model Performance Evaluation**  
  Evaluate and compare the performance of different machine learning models using multiple evaluation metrics including Accuracy, Precision, Recall and F1 Score analysis to identify the most effective approach for sentiment classification of Malay language content.

### 1.3 Project Scope

**Data Sources**  
The system focuses on YouTube comments from selected Hari Raya-related videos, including traditional songs, modern interpretations, and cultural content. The dataset includes comments in multiple languages (primarily Malay, with some English and regional languages) from videos with varying popularity levels.

**Containerization and Orchestration**  
The project implements a fully containerized architecture using:

- **Docker Containers**: Individual containers for each service component ensuring isolation and portability  
- **Docker Compose**: Multi-container orchestration for simplified deployment and service management  
- **Service Isolation**: Each component (Zookeeper, Kafka, Spark, Elasticsearch, Kibana) runs in its own container  
- **Volume Management**: Persistent data storage and model sharing between containers  
- **Network Configuration**: Inter-container communication and external port exposure

**Machine Learning Models**  
The scope includes training and deploying two primary sentiment classification models:

- Naive Bayes classifier for baseline sentiment analysis  
- Logistic Regression model for comparative performance evaluation  
- TF-IDF vectorization for text feature extraction

**System Architecture**  
The project implements a microservices architecture with:

- Zookeeper for distributed coordination  
- Kafka for message streaming  
- Spark for stream processing  
- Elasticsearch for data storage and search  
- Kibana for visualization and monitoring

**Model Evaluation and Comparison**

- **Accuracy**: Overall classification accuracy for both models  
- **Precision**: Scores for positive, negative, and neutral sentiment classes  
- **Recall**: Scores to measure the ability to identify all instances of each sentiment class  
- **F1 Score**: Harmonic mean of precision and recall for balanced performance evaluation

## 2.0 Data Acquisition & Preprocessing

### 2.1 Data Source

The primary data source for this project was comments from YouTube videos. YouTube was chosen as a rich source of public opinion for several reasons:

- **High Engagement**  
  YouTube is one of the most popular social media platforms in Malaysia, where users actively share their thoughts and feelings in the comments section.

- **Cultural Relevance**  
  For a topic like *Hari Raya*, YouTube has tons of vlogs, advertisements and music videos that generate significant public discussion. This makes it an ideal platform to capture genuine sentiment.

- **Data Accessibility**  
  With the right tools, YouTube comments can be systematically collected and provide a large volume of text data for analysis.

The search query `"Hari Raya"` was selected to ensure the collected data was directly related to a significant cultural event in Malaysia to align with the project's requirement, which is to analyze sentiment on a locally relevant topic.

---

### 2.2 Data Acquisition Tools and Process

The data acquisition process was automated using Python scripts and key libraries:

- **googleapiclient**  
  The `build()` function from this library was used to interact with the official YouTube Data API v3. This allowed us to programmatically search for videos relevant to our query.

- **youtube-comment-downloader**  
  A specialized Python library designed to efficiently scrape comments from specified YouTube video URLs without violating YouTube's terms of service for public data access.

- **Pandas**  
  Used for structuring the collected data into a `DataFrame` and saving it for offline processing.

#### The acquisition workflow was executed in four main steps:

1. **Video Search**  
   An API call was made to the YouTube Data API to search for the top 10 most relevant videos using the search query `"Hari Raya"`.

2. **Video ID Extraction**  
   From the search results, the unique `videoId` for each of the 10 videos was extracted.

3. **Comment Scraping and Storage**  
   The `youtube-comment-downloader` library was then used to iterate through the list of `videoId`s. For each video, the script fetched the associated public comments. A loop collected the comments until a predefined limit of 1,000 comments was reached. Each comment was stored along with its source `videoId` to maintain traceability.

4. **Raw Data Export**  
   The final collection of raw comments was structured into a Pandas `DataFrame` and saved as a CSV file named `youtube_comments.csv`.

---

### 2.3 Data Preprocessing and Cleaning Steps

Raw text from social media is inherently noisy, containing URLs, special characters, inconsistent capitalization and other elements that can decrease the performance of a sentiment analysis model. Therefore, a preprocessing and cleaning pipeline was implemented using the **Pandas** and **`re`** (Regular Expressions) libraries in Python.

A function `clean_text()` was defined to apply the steps sequentially to each comment:

- **Lowercasing**  
  All text was converted to lowercase to ensure uniformity. For example, `"Happy"`, `"happy"` and `"HAPPY"` are treated as the same word.

- **URL Removal**  
  A regular expression was used to identify and remove all hyperlinks from the comments.
  ```python
  re.sub(r"http\S+|www\S+", '', text)

- **Symbol and Emoji Removal**  
  Used regular expression:

  ```python
  re.sub(r"^a-zA-z0-9\s.,!?", "", text)

- **Whitespace Normalization**
  Multiple consecutive spaces were collapsed into one, and leading/trailing whitespace was removed using
  ```python
  .strip().

- **Empty Comment Removal**
  Comments that became empty after cleaning (e.g., just emojis or links) were removed to avoid errors during modeling.

The cleaned text was stored in a new column named clean_comment and this processed data was saved to a new file, cleaned_youtube_comments.csv, ready for the sentiment labeling and model development phase.
## 3.0 Sentiment Model Development

### 3.1 Model Choice

To fulfill the project requirement of exploring at least two different approaches, we selected two classic machine learning models for training and classification, with the assistance of a deep learning-based model for automated data labeling.

#### Pre-trained Transformer Model (for Data Labeling)

To generate high-quality sentiment labels for our unlabeled YouTube comments, we used a pre-trained model from the Hugging Face `transformers` library. The `pipeline("sentiment-analysis")` function was used, which by default loads a DistilBERT model fine-tuned on the SST-2 (Stanford Sentiment Treebank) dataset.

#### Supervised Machine Learning Models (for Training)

The labels generated by the transformer model were used to train two supervised machine learning classifiers commonly used for text classification:

- **Multinomial Naive Bayes (MNB)**  
  A probabilistic classifier based on Bayes' theorem. It is a popular baseline due to its efficiency, simplicity, and decent performance—especially with word frequency or TF-IDF features.

- **Logistic Regression**  
  A linear model effective for both binary and multi-class classification. It does not assume feature independence (unlike Naive Bayes) and typically yields high accuracy, making it a strong non-probabilistic baseline.

---

### 3.2 Training Process

The training process was designed to ensure reliable, reproducible results using clean features and consistent logic.

#### Automated Data Labeling

The cleaned comments were fed into the pre-trained transformer model using a custom function `classify_sentiment`. The process followed this logic:

- The model classifies each comment and returns a label (`POSITIVE` or `NEGATIVE`) and a confidence score.
- A confidence threshold of `0.90` was applied. Predictions below this confidence were classified as `NEUTRAL` to improve precision.
- Final labels (`POSITIVE`, `NEGATIVE`, `NEUTRAL`) were saved into a new file: `labeled_youtube_comments.csv`.

#### Feature Engineering with TF-IDF

Before model training, text data was vectorized using the `TfidfVectorizer` from `scikit-learn`.

- **TF-IDF (Term Frequency-Inverse Document Frequency)** weighs how important a word is in a document relative to a corpus.
- The vectorizer was configured with `max_features=5000` to capture only the most significant terms, reduce noise, and control dimensionality.

#### Data Splitting

The labeled dataset was split using `train_test_split`:

- **80%** of the data was used for training, **20%** for testing.
- The `stratify=df['label']` argument ensured an equal distribution of `POSITIVE`, `NEGATIVE`, and `NEUTRAL` comments across both sets.

#### Model Fitting

Both models—MNB and Logistic Regression—were trained using:

```python
model.fit(X_train_tfidf, y_train)
```

### 3.3 Evaluation Strategy

To evaluate performance, we applied both standard metrics and custom prediction logic.

#### Prediction with Thresholding

A custom function `apply_threshold()` was defined to interpret model predictions:

- If the highest predicted probability is **below 0.70**, classify the comment as `NEUTRAL`.
- Otherwise, assign the label with the highest probability.

This method improves reliability by reducing false positives and treating uncertain predictions as neutral.

#### Quantitative Metrics

Evaluation was conducted using `classification_report` from `scikit-learn`, which provides the following metrics:

- **Precision** – The ratio of correctly predicted positive observations to the total predicted positives.  
- **Recall** – The ratio of correctly predicted positive observations to all actual positive observations.  
- **F1-Score** – The harmonic mean of Precision and Recall. It balances the impact of false positives and false negatives.

#### Visual Evaluation

A **confusion matrix** was generated for both models. This visual representation illustrates:

- The number of true vs. predicted labels.
- How frequently the model confuses certain classes (e.g., misclassifying `NEUTRAL` as `POSITIVE`).

These visualizations help identify specific weaknesses and misclassifications in model performance.

## 4.0 Apache System Architecture

### 4.1 Component Roles and Configuration

The entire system is containerized and defined in a `docker-compose.yml` file. It includes the following services:

---

#### **Apache Zookeeper**  
`Image: confluentinc/cp-zookeeper:7.6.1`  
Acts as a centralized coordination service for distributed components, primarily used to manage the state of the Apache Kafka cluster. Zookeeper is a critical prerequisite for Kafka.

---

#### **Apache Kafka**  
`Image: confluentinc/cp-kafka:7.6.1`  
Kafka is the core distributed messaging system (data backbone) of the pipeline. It decouples the data source (producer) from the data processing components (consumers).

**Project Implementation:**  
A Python script `producer.py` continuously fetches comments from YouTube using the `youtube-comment-downloader` library and publishes them as JSON messages to a Kafka topic named `youtube-comments`, creating a live comment stream.

---

#### **Apache Spark**  
`Image: bitnami/spark:3.4.2`  
Acts as the main processing engine of the pipeline. Spark consumes data from Kafka, applies transformations, and runs the sentiment analysis model in real-time.

**Project Implementation:**  
The `spark_stream.py` script uses Spark Structured Streaming to process the stream from Kafka. It performs the following steps:

- **Data Cleaning**  
  Applies the same text preprocessing pipeline used earlier.

- **Model Inference**  
  Loads the pre-trained Logistic Regression model (`lr_sentiment_model.pkl`) and TF-IDF vectorizer (`tfidf_vectorizer.pkl`) to predict sentiment. These models are broadcasted to Spark workers for efficiency.

- **Data Sinking**  
  The enriched data—including original comment, cleaned text, predicted sentiment, and metadata—is written directly to Elasticsearch.

---

#### **Elasticsearch**  
`Image: docker.elastic.co/elasticsearch:8.13.4`  
A distributed search and analytics engine used as the primary datastore for processed data. Its indexing enables fast querying and aggregation.

**Project Implementation:**  
Spark writes structured results to an index called `youtube-comments6-index` in Elasticsearch.

---

#### **Kibana**  
`Image: docker.elastic.co/kibana:8.13.4`  
Kibana serves as the visualization layer. It allows users to explore and visualize the data stored in Elasticsearch.

**Project Implementation:**  
Kibana connects to Elasticsearch and allows users to build real-time dashboards. These dashboards visualize sentiment trends, comment distributions, and enable interactive exploration of the results.

### 4.2 Workflow Diagram and Data Flow

**Figure 4.2.1: Workflow Diagram**  
![Kafka + Spark + Elasticsearch Workflow Diagram-Page-1 drawio (1)](https://github.com/user-attachments/assets/1df34d7b-00a0-420d-b2e6-c8cc59f069e9)

#### Step-by-Step Data Flow:

1. **Data Ingestion**  
   - `producer.py` scrapes comments from selected YouTube videos.  
   - Each comment is packaged as a JSON object along with metadata (e.g., `video_id`, `title`).

2. **Data Streaming**  
   - The JSON message is published to the `youtube-comments` topic in Kafka.  
   - Kafka stores and buffers these messages for real-time consumption.

3. **Real-Time Consumption & Processing**  
   - `spark_stream.py` acts as the Kafka consumer using Spark Structured Streaming.  
   - Reads data in micro-batches from Kafka as a continuous stream.

4. **Transformation and Analysis**  
   For each comment in the stream:
   - The raw text is cleaned.
   - Cleaned text is vectorized using the pre-loaded TF-IDF vectorizer.
   - Sentiment is predicted using the pre-trained Logistic Regression model.
   - A structured record is generated with original comment, sentiment, and metadata.

5. **Data Persistence**  
   The enriched data from Spark is streamed to Elasticsearch. Elasticsearch indexes this data, making it immediately available for searching and analysis.

6. **Visualization and Insight**  
   - Kibana reads from Elasticsearch and visualizes the data.
   - Dashboards reflect real-time public sentiment trends for "Hari Raya" content on YouTube.

## 5.0 Analysis & Results

### 5.1 Key Findings

After deploying the real-time sentiment analysis system using Docker containers for Apache Kafka, Apache Spark, Elasticsearch, and Kibana, the pipeline successfully collected, processed, and visualized **6,829** comments from **7 Hari Raya-related YouTube videos**. These videos featured popular Malaysian artists like **Siti Nurhaliza**, **Iman Troye**, **Aisha Retno**, and others—selected based on high viewership and strong cultural relevance during the Hari Raya celebration.

---

#### Real-Time Data Collection

The `producer.py` script was responsible for scraping real-time comments and video metadata:

- **Video Metadata:**  
  - Title  
  - Publish date  
  - View count  
  - Like count  
  *(Collected using `yt_dlp`)*

- **Comments:**  
  - Collected using `youtube-comment-downloader`  
  - Streamed continuously as the script ran in real-time

All collected data was formatted as JSON and published to a Kafka topic named `youtube-comments`.

---

#### Real-Time Processing with Apache Spark

The `spark_stream.py` script launched a **Structured Streaming** job in Apache Spark:

- **Data Cleaning:**  
  - Removed links, special characters, excessive whitespace, etc.

- **Sentiment Prediction:**  
  - Used a pre-trained **Logistic Regression** model with **TF-IDF** features  
  - Predicted each comment as `POSITIVE`, `NEUTRAL`, or `NEGATIVE`

- **Data Storage:**  
  - Each processed record was written to an **Elasticsearch** index named `youtube-comments6-index`

---

#### Data Visualization with Kibana

Kibana was launched on `localhost:5061` to visualize the indexed sentiment data interactively. The dashboard included:

- ✅ **Total Number of Comments** collected  
- ✅ **Number of Unique Videos** analyzed  
- ✅ **Pie Chart** displaying the sentiment distribution (positive, neutral, negative)  
- ✅ **Word Cloud** showing the most frequently used words in comments  
- ✅ **Table View** displaying:
  - Video title  
  - Publish date  
  - View count  
  - Like count  
  - Number of comments  
- ✅ **Sentiment Comparison Graph** across all analyzed videos

---

#### Insights

This visual dashboard enabled us to:

- Observe which videos generated the most **positive** or **negative** feedback
- Understand common language patterns and keywords used during Hari Raya discussions
- Monitor public sentiment trends in **real-time**, directly from social media engagement

Overall, the system demonstrated the feasibility and value of using modern big data technologies for live sentiment analysis of culturally significant online content.

### 5.2 Visualization 
[PIC]

## 6.0 Optimization & Comparison

### 6.1 Model Optimization

To improve the accuracy and usability of the sentiment analysis system, several optimization strategies were implemented:

- **Text Preprocessing**  
  YouTube comments were cleaned by removing punctuation, emojis, URLs, and stop words. This reduced noise and improved the quality of model training.

- **Sentiment Labeling with Neutral Class**  
  A **confidence threshold of 0.90** was applied to the Hugging Face transformer predictions. Comments with confidence scores below 90% were labeled as `NEUTRAL`. This allowed for better handling of ambiguous comments that lacked strong sentiment.

- **Efficient Feature Extraction**  
  Both machine learning models used **TF-IDF vectorization** to convert text into numerical features. TF-IDF helps highlight important terms and reduce dimensionality.

- **Model Serialization**  
  The trained models and the TF-IDF vectorizer were serialized using `joblib`, enabling fast loading and reuse—especially beneficial for real-time classification scenarios.

---

### 6.2 Model Comparison

Two traditional machine learning models were trained and evaluated on the transformer-labeled dataset:

| Model              | Accuracy | Precision | Recall | F1-Score | Notes                                |
|-------------------|----------|-----------|--------|----------|--------------------------------------|
| **Logistic Regression** | 0.66     | 0.70      | 0.63   | 0.63     | Balanced performance across classes  |
| **Naive Bayes**         | 0.62     | 0.69      | 0.58   | 0.58     | Better recall for `NEGATIVE` class   |

#### Insights:

- **Logistic Regression** showed the best overall performance, offering more balanced predictions across all sentiment categories.
- **Naive Bayes** had slightly better recall for the `NEGATIVE` class, but struggled with accurately identifying `NEUTRAL` sentiments.
- **NEUTRAL** comments were the hardest to classify for both models, indicating the difficulty of handling ambiguity in short-form social media text.

---

## 7.0 Conclusion & Future Work

This project successfully built a **real-time sentiment analysis system** capable of classifying YouTube comments into `POSITIVE`, `NEUTRAL`, or `NEGATIVE` sentiment categories.

The system leveraged:

- **Apache Kafka** for real-time message streaming  
- **Apache Spark (PySpark)** for distributed stream processing  
- **TF-IDF vectorization** for text feature extraction  
- **Naive Bayes** and **Logistic Regression** as classification models  
- **Transformers (Hugging Face)** for intelligent data labeling

---

### Key Achievements:

- Built a scalable and containerized real-time pipeline
- Collected and labeled thousands of Hari Raya-related comments
- Created live dashboards in Kibana using Elasticsearch
- Achieved ~66% accuracy with Logistic Regression, with balanced precision and recall

---

### Future Enhancements:

- **Improve NEUTRAL Classification**  
  Consider training models on manually labeled datasets that explicitly include a `NEUTRAL` class.

- **Integrate Deep Learning Models**  
  Explore fine-tuned transformer models (e.g., BERT, XLM-RoBERTa) for better context-aware sentiment detection.

- **Expand Dataset**  
  Collect more data across different cultural topics and languages to improve robustness and generalizability.

- **Real-World Applications**  
  Potential use cases include:
  - Social media monitoring  
  - Content moderation  
  - Brand sentiment tracking  
  - Public opinion trend analysis

