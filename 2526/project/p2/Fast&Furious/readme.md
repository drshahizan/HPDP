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
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Fast%26Furious/notebooks/02_preprocessing.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Jupyter Notebook for Model Training</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Fast%26Furious/notebooks/model_training.ipynb"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
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



### Workflow Diagram



---

## 🚀 Getting Started

### Prerequisites



### Installation and Setup

    

### Running the Pipeline


    

### Accessing the Dashboard



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

| Model       | Accuracy    | Precision (Pos/Neg/Neu) | Recall (Pos/Neg/Neu)   | F1-Score (Pos/Neg/Neu) |



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
