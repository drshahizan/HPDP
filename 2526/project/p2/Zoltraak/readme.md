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
      <a href="https://github.com/drshahizan/HPDP/tree/main/2526/project/p2/Zoltraak/reports"><img src="https://github.com/user-attachments/assets/4f5391d9-f205-4dd6-8c08-1f8307bd55bf" width=24px height=23px></a>
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
        <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Zoltraak/data/raw_data/raw_data.csv">
          <img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591/" width="25px" height="23px">
        </a>
      </td>
  </tr>
  <tr>
    <td>Cleaned Data</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/blob/main/2526/project/p2/Zoltraak/data/raw_data/cleaned_data.csv"><img src="https://github.com/user-attachments/assets/3ee1c27e-9bd6-4b2e-b54b-7fd597879591" width=25px height=23px></a>
    </td>
  </tr>
  <tr>
    <td>Preprocess & Train Model</td>
    <td align="center">
      <a href="https://github.com/drshahizan/HPDP/tree/main/2526/project/p2/Zoltraak/notebook"><img src="https://github.com/user-attachments/assets/928d0405-924d-4464-81f1-bb4a1bd963b1" width=24px height=23px></a>
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
This project applies a high-performance data processing approach to capture and understand public sentiment regarding the cost of living, inflation, and lifestyle in Malaysia. By extracting and analyzing spontaneous audience feedback from six selected YouTube videos, the system classifies public opinion into positive, negative, and neutral sentiments. 

## 🏗️ System Architecture
The end-to-end pipeline follows a Lambda-style streaming architecture to handle both batch and real-time workloads:
* **Data Source**: Collects unstructured YouTube comments using the YouTube Data API v3.
* **Ingestion Layer**: Uses Apache Kafka as a central message broker to receive incoming comment messages.
* **Processing Layer**: Utilizes Apache Spark Structured Streaming to process micro-batches, clean text, extract features, and classify sentiment.
* **Storage Layer**: Stores the classified text, sentiment labels, and timestamps in Elasticsearch.
* **Visualization Layer**: Presents interactive findings, such as sentiment distribution and word clouds, via Kibana dashboards

## 🧠 Machine Learning Models
To classify the unstructured text, the project compared two different machine learning models:
* **Support Vector Machine (SVM)**: Selected as the primary deployment model because it achieved a superior overall accuracy of 82.18%.
* **Long Short-Term Memory (LSTM)**: Achieved a lower accuracy of 79.51% and showed signs of overfitting by epoch 5 during training.

## ⚡ Batch vs. Streaming Performance
The system was benchmarked on 4,470 YouTube comments to compare historical (batch) and real-time (streaming) capabilities:
* **Batch Mode**: Processed the dataset 4.6 times faster with a throughput of over 3,000 records per second. 
* **Streaming Mode**: Achieved a throughput of about 675 records per second, which is lower due to the overhead of transforming and classifying one comment at a time.
* **Accuracy**: Processing modes introduced no model degradation, with batch mode scoring 0.923 and streaming mode scoring 0.908.

## 📈 Key Findings
The pipeline successfully processed a total of 22,360 records to reveal the following sentiment distribution:
* **Positive Sentiment (48.68%)**: The majority of comments expressed favorable views about Malaysia as a travel destination and place of residence.
* **Neutral Sentiment (42.37%)**: Formed a large body of informational or observational commentary that did not lean emotionally in either direction.
* **Negative Sentiment (8.94%)**: Critical or unfavorable opinions were relatively rare in the dataset.
