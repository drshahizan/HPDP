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
    <a href="notebooks/Preprocess_%26_Train_Model_LSTM.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width="24" height="23"></a>
  </td>
</tr>
  <tr>
    <td>Preprocess & Train Model (Model 2)</td>
    <td align="center">
      <a href="notebooks/Preprocess_%26_Train_Model_Naive_Bayes.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Full and Complete Code in our Repository</td>
    <td align="center">
      <a href="https://colab.research.google.com/drive/11qpJJ-H06XOxtF457mggG1SqM9hm5-x0?usp=sharing"><img src="https://github.com/user-attachments/assets/2e0abbaa-3b7f-450f-92f6-41fd0e6e4dad" width=24px height=23px></a>
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
 
- Naive Bayes Classifier : 
very fast, lightweight, and resource efficient probabilistic model ideal for low-latency live streaming 
- LSTM Neural Network : 
A deep learning model that captures word order and long term context, which is good for understanding complex or mixed user feedback for example praising the price but complaining about the app.

#### 3.2 Training Process

- The cleaned dataset (25000 comments) was split into 70% training, 20% testing and 10 % evaluate sets
- Naive Bayes : The text was converted into numerical features using TF-IDF Vectorizer and trained using Scikit-Learn.
- LSTM : Text was converted into padded integer sequences, passed through an Embedding layer, a spatial dropout layer, an LSTM layer, and a dense output layer with softmax activation. 

#### 3.3 Evaluation

Naive Bayes : 

- validation set  
<img width="717" height="340" alt="NBV" src="https://github.com/user-attachments/assets/0e9042fe-00bc-4d78-9ca2-1302b13a6cd3" />

<img width="750" height="600" alt="nb_confusion_validation" src="https://github.com/user-attachments/assets/a4d0ce2b-ff93-4a1b-b227-fb637f1f12b5" />

- testing set 
<img width="693" height="346" alt="NVT" src="https://github.com/user-attachments/assets/406bd104-142b-4090-b374-bf744c433d72" />

<img width="750" height="600" alt="nb_confusion_test" src="https://github.com/user-attachments/assets/58f01dcd-293f-4f6f-9443-af08a8ecbedd" />


LSTM : 

- validation set
<img width="633" height="341" alt="LV" src="https://github.com/user-attachments/assets/f8f8e16d-3127-4e32-97dc-46fa2e43bcef" />

<img width="750" height="600" alt="lstm_confusion_validation" src="https://github.com/user-attachments/assets/21abeb1a-334b-4ce4-8b77-35199bf40acc" />


- testing set 
<img width="667" height="343" alt="LT" src="https://github.com/user-attachments/assets/75f274b7-a4fb-46dd-a629-67917afd9e02" />

<img width="750" height="600" alt="lstm_confusion_test" src="https://github.com/user-attachments/assets/39443cb0-18af-4146-b802-c28b73a13ae0" />


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

The sentiment analysis pipeline successfully processed 40,000 AirAsia Google Play Store reviews scraped from the Malaysian region. The raw dataset comprised reviews spanning multiple languages across 43 unique language codes. Following language detection, 27,206 English reviews were retained and subjected to the full NLP preprocessing pipeline. After noise removal, emoji filtering, and non-Latin script exclusion, the final cleaned dataset consisted of 27,197 reviews, with 12,803 multilingual and low-quality entries removed.

The final cleaned dataset exhibited a class-imbalanced sentiment distribution, with 17,260 negative reviews (63.5%), 8,439 positive reviews (31.0%), and 1,498 neutral reviews (5.5%). This distribution reflects a genuine skew in user behaviour on app stores, where dissatisfied users tend to leave reviews more frequently than satisfied ones. To address this imbalance during training, RandomOverSampler was applied exclusively to the training set, balancing all three classes to 12,081 samples each, while the validation and test sets were left untouched to ensure unbiased evaluation.

The dataset was split into 19,037 training samples (70%), 5,440 test samples (20%), and 2,720 validation samples (10%). Two models were trained and evaluated on this split.
Among the two trained models, Naive Bayes outperformed LSTM across all key metrics on the test set. Naive Bayes achieved a test accuracy of 83.42%, precision of 87.59%, recall of 83.42%, and an F1 score of 85.23%. The LSTM model achieved a test accuracy of 74.54%, precision of 88.01%, recall of 74.54%, and an F1 score of 79.90%. Both models showed consistent performance between their validation and test evaluations, indicating stable generalisation without significant overfitting.

A notable weakness across both models was the poor classification performance on the neutral class. Naive Bayes achieved a neutral class F1 score of 0.25 on the test set, while LSTM achieved 0.19. This is attributable to the severe underrepresentation of neutral reviews and the linguistic ambiguity of 3-star reviews, which frequently contain mixed positive and negative language that is difficult to distinguish from either extreme class.

Based on these results, Naive Bayes was selected as the deployed model for the Kafka and Spark streaming pipeline due to its higher overall accuracy, lower inference latency, and better suitability for real-time classification at scale.


#### 5.2 Visualizations

There is total of 5 insights that have been visualized : 

- Chart Sentiment Distribution
  <img width="888" height="455" alt="image" src="https://github.com/user-attachments/assets/f7b2c3dd-e951-4412-9498-7ee6b4edd9a3" />

- Chart WordClouds
   <img width="2685" height="691" alt="chart_wordclouds" src="https://github.com/user-attachments/assets/45b32941-72f1-4985-bc5c-68c2e9ad344b" />

- Chart Model Comparison 
  <img width="922" height="503" alt="image" src="https://github.com/user-attachments/assets/a5983049-798c-4dae-97c1-9fa7278cefcf" />

- Chart Batch vs Streaming
  <img width="891" height="365" alt="image" src="https://github.com/user-attachments/assets/242a92cc-545e-4dde-88a3-f137f79054c2" />

- Chart Sentiment over time 
<img width="922" height="386" alt="image" src="https://github.com/user-attachments/assets/2c8d83c5-adf9-46ca-a0f1-d0b638413d19" />

#### 5.3 Insights

Several meaningful insights were derived from the pipeline output:
- App stability is the primary driver of negative sentiment. The high frequency of crash-related and performance-related terms in negative reviews indicates that technical issues, particularly app crashes during flight check-in and boarding pass retrieval, represent the most significant pain points for AirAsia users.
- Positive sentiment is concentrated around core booking functionality. Users who leave positive reviews consistently highlight the convenience of the booking and flight management features, suggesting that while the primary use case is well-received, peripheral features such as payment processing and customer support require improvement.
- Neutral sentiment remains rare and linguistically ambiguous. The low volume and mixed content of 3-star reviews poses an ongoing challenge for ternary sentiment classifiers. Future work incorporating aspect-based sentiment analysis could decompose mixed feedback into more specific issue categories.
- The overall sentiment trend shows no significant improvement in user satisfaction during the observation period. Negative reviews consistently exceeded 60% of the cleaned dataset, suggesting that recurring technical and operational issues have not been resolved at a pace that meaningfully improves aggregate user sentiment.



---

### 6.0 Optimisation & Comparison

A controlled performance comparison was executed between batch and streaming processing architectures to assess pipeline efficiency under different operating paradigms. A trained Naive Bayes classifier was evaluated on a test dataset to measure processing time, throughput, and classification consistency. Additionally, the Naive Bayes model's predictive performance was benchmarked against a Long Short-Term Memory (LSTM) network to validate model selection. 

#### 6.1 Processing Time KIV
Batch mode processed 25000 reviews in 0.0303 seconds by vectorizing all records simultaneously through a single TF-IDF matrix transformation. The same volume took 1.4729 seconds when it was processed as it arrived from the Kafka topic, using the streaming mode. This is about 48.6 times, which seems reasonable due to the overhead of each individual TF-IDF call and the Spark micro-batch scheduling for streaming mode.

#### 6.2 Throughput
In alignment with the processing time metrics, throughput capacities diverged heavily between the two modes:
Batch Mode: Achieved a high-efficiency rate of over 16,500 records per second (rec/s), demonstrating its optimal design for large-scale, historical data ingestion and bulk transformation.
Streaming Mode: Produced a significantly lower throughput of approximately 340 rec/s.
While streaming throughput is visibly compressed in comparison to bulk processing, an ingestion rate of 340 rec/s remains more than sufficient for live production environments, where user reviews arrive sequentially as continuous, sparse individual events rather than massive parallel blocks.

#### 6.3 Accuracy and Consistency
The evaluation yielded an identical classification accuracy of 89.60% (0.896) across both processing architectures. This confirms that the serialized Naive Bayes model maintains absolute classification parity and deterministic consistency, regardless of whether the underlying data ingestion layer is a static batch file or an active Spark Streaming/Kafka pipeline. The integration of real-time messaging layers introduced zero degradation to the feature engineering or inference boundaries. 

#### 6.4 Resource Usage
In both batch and streaming modes, the 25000-record sample run resulted in a memory delta of 0.00 MB, signifying there was no measurable additional memory overhead at this scale for either mode. For larger production deployments, it would be expected that the peak memory footprint of batch mode would be higher due to full matrix materialization, while streaming mode would have a lower stable memory footprint per micro-batch.



---

### 7.0 Conclusion & Future Work

The data pipeline uses the Google Play Scrapper to extract customer reviews from the Google Play store. The data is then cleaned and structured for serialization utilizing foundational Python frameworks, including Pandas, NumPy, and Pickle. Apache Kafka is then being used to handle the real-time data flow while Apache Spark is structured streaming that makes the process to be faster and more reliable. Finally, NLP libraries like NLTK and spaCy will handle the underlying text preparation by breaking down review sentences into individual tokens and reducing words to their base grammatical forms. 

As a future enhancement, This pipeline can be scaled widely by integrating others platform to get more data such as Apple App Store APIs to ingest iOS user feedback alongside the existing Android stream. Furthermore, implementing Aspect-Based Sentiment Analysis (ABSA) within the Spark streaming layer will allow the pipeline to automatically separate software bugs from broader airline operational complaints, yielding much more specific, actionable insights. 

---

### 8.0 References

- Apache Software Foundation. (n.d.). Apache Kafka Architecture Documentation. Retrieved from https://kafka.apache.org/

- Apache Software Foundation. (n.d.). Spark Structured Streaming Programming Guide. Retrieved from https://spark.apache.org/

- Bird, S., Klein, E., & Loper, E. (2009). Natural Language Processing with Python. O'Reilly Media.

- Chollet, F. (2015). Keras: Deep Learning for Humans. Retrieved from https://keras.io/

- Honnibal, M., & Montani, I. (2017). spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing.

- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.


---

### 9.0 Appendix

- Air Asia Apps in the Google Play Store
  <img width="821" height="559" alt="image" src="https://github.com/user-attachments/assets/92ae8389-9a59-4856-8ad2-5f32290e06da" />

- Rating and Revire in the AirAsia apps
 <br> <img width="529" height="677" alt="image" src="https://github.com/user-attachments/assets/9a7641b1-fa15-4720-8d73-1d65e6f543ad" />
