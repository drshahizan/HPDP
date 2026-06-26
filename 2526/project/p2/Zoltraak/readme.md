<h1 align="center"> 
  Zoltraak - 	Youtube (Cost of Living in Malaysia)
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>DHESHIEGHAN A/L SARAVANA MOORTHY</td>
    <td>A23CS0072</td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD AFIQ DANIAL BIN ROZAIDIE</td>
    <td>A23CS0117</td>
  </tr>
  <tr>
    <td width=80%>AHMAD ADIB ZIKRI BIN A.MAZLAM</td>
    <td>A23CS0205</td>
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
        <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Zoltraak/youtube_comments_OTFQhyEHymE.csv">
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

# 📊 YouTube Comment Sentiment Analysis: Malaysia Cost of Living

## 📖 Project Overview
This project applies a high-performance data processing approach to capture and understand public sentiment regarding the cost of living, inflation, and lifestyle in Malaysia[cite: 1]. By extracting and analyzing spontaneous audience feedback from six selected YouTube videos, the system classifies public opinion into positive, negative, and neutral sentiments[cite: 1]. 

## 🏗️ System Architecture
The end-to-end pipeline follows a Lambda-style streaming architecture to handle both batch and real-time workloads[cite: 1]:
* **Data Source**: Collects unstructured YouTube comments using the YouTube Data API v3[cite: 1].
* **Ingestion Layer**: Uses Apache Kafka as a central message broker to receive incoming comment messages[cite: 1].
* **Processing Layer**: Utilizes Apache Spark Structured Streaming to process micro-batches, clean text, extract features, and classify sentiment[cite: 1].
* **Storage Layer**: Stores the classified text, sentiment labels, and timestamps in Elasticsearch[cite: 1].
* **Visualization Layer**: Presents interactive findings, such as sentiment distribution and word clouds, via Kibana dashboards[cite: 1].

## 🧠 Machine Learning Models
To classify the unstructured text, the project compared two different machine learning models[cite: 1]:
* **Support Vector Machine (SVM)**: Selected as the primary deployment model because it achieved a superior overall accuracy of 82.18%[cite: 1].
* **Long Short-Term Memory (LSTM)**: Achieved a lower accuracy of 79.51% and showed signs of overfitting by epoch 5 during training[cite: 1].

## ⚡ Batch vs. Streaming Performance
The system was benchmarked on 4,470 YouTube comments to compare historical (batch) and real-time (streaming) capabilities[cite: 1]:
* **Batch Mode**: Processed the dataset 4.6 times faster with a throughput of over 3,000 records per second[cite: 1]. 
* **Streaming Mode**: Achieved a throughput of about 675 records per second, which is lower due to the overhead of transforming and classifying one comment at a time[cite: 1].
* **Accuracy**: Processing modes introduced no model degradation, with batch mode scoring 0.923 and streaming mode scoring 0.908[cite: 1].

## 📈 Key Findings
The pipeline successfully processed a total of 22,360 records to reveal the following sentiment distribution[cite: 1]:
* **Positive Sentiment (48.68%)**: The majority of comments expressed favorable views about Malaysia as a travel destination and place of residence[cite: 1].
* **Neutral Sentiment (42.37%)**: Formed a large body of informational or observational commentary that did not lean emotionally in either direction[cite: 1].
* **Negative Sentiment (8.94%)**: Critical or unfavorable opinions were relatively rare in the dataset[cite: 1].
