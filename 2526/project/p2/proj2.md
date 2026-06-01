<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# 📄 Project 2: Real-Time Sentiment Analysis using Apache Spark and Kafka

## 1. Introduction

Welcome to Project 2 of the High Performance Data Processing course. This project gives you a practical opportunity to design and build a real-time sentiment analysis pipeline using modern big data technologies. The activities are designed to connect classroom theory with industry-relevant data engineering practice.

In this project, each group will collect text data from Malaysian-relevant sources, classify the sentiment of that text, and process it through a scalable pipeline built with Apache Kafka and Apache Spark. The final insights will be stored and presented through interactive dashboards.

<p align="center">
  <img src="P2%20HPDP%20info.png" height="500">
</p>

### 📋 Quick Facts

| Item | Details |
|------|---------|
| Document| [Assignment brief](https://liveutm-my.sharepoint.com/:b:/g/personal/shahizan_live_utm_my/IQD01fs00domRKiDSzmH8OozAWCc0ImRWB3DBO2f411hI8I?e=sLZiM6)|
| 📊 **Weightage** | 15% of total course assessment |
| 🕓 **Project Duration** | 4 Weeks |
| 📅 **Submission Deadline** | **Friday, 26 June 2026, 11:59 PM (MST)** |
| 📤 **Submission Channels** | e-Learning Portal and GitHub Repository |
| 👥 **Group Size** | **Maximum 3 students per group** |

> 📌 Each group must include students from **different genders, races, or backgrounds** to encourage diverse perspectives and inclusive teamwork.

## 2. Project Overview

Organizations increasingly rely on real-time analytics to understand public opinion about products, events, and social issues. This project simulates that environment by requiring each group to build a complete sentiment analysis system that operates on streaming data.

Each group will select a Malaysian-relevant text source, such as social media posts, online reviews, or news articles. The collected text will be cleaned using natural language processing (NLP) techniques, classified as **positive, negative, or neutral** by a trained model, and processed through a streaming pipeline. The resulting sentiment trends will then be stored and visualized so that insights can be communicated clearly to stakeholders.

### ⚙️ Technologies Involved

| Technology | Role in the Pipeline |
|------------|----------------------|
| **Apache Kafka** | Streams text data from live or batched sources into the processing layer. |
| **Apache Spark** | Processes large volumes of data in parallel and applies the sentiment model. |
| **Elasticsearch or Apache Druid** | Stores classified results and supports fast querying for visualization. |
| **NLP Libraries** (NLTK, spaCy, Hugging Face) | Perform text preprocessing and support model development. |


## 3. Learning Outcomes

Upon successful completion of this project, you will be able to:

1. Design and configure a real-time streaming pipeline using Apache Kafka and Apache Spark.
2. Apply standard natural language processing techniques to clean and prepare text data.
3. Train, evaluate, and compare at least two sentiment classification models.
4. Integrate a trained model into a streaming system that classifies text as positive, negative, or neutral.
5. Store and visualize sentiment results using dashboard tools such as Kibana or Apache Superset.
6. Collaborate effectively in a small team and communicate insights through a professional report and presentation.

## 4. Project Requirements

### 4.1 Group Composition

This is a group-based project. Students must form their own groups subject to the following requirements:

- **Each group must consist of a maximum of three (3) students.** Groups with more than three members will not be accepted.
- Each group must include members from different genders, races, or backgrounds to encourage diverse perspectives and inclusive collaboration.
- Roles and responsibilities must be distributed clearly among members. Suggested roles include Group Leader, Data and NLP Engineer, and Pipeline and Visualization Engineer.
- Group formation and the chosen data source must be confirmed with the lecturer no later than the end of Week 1.

### 4.2 Technical Requirements

The technical scope of the project is fixed. Each group must satisfy all of the following criteria:

- Collect or stream text data from a Malaysian-relevant source, such as Twitter, Shopee, Google Play reviews, or local news.
- Preprocess the text using NLP methods, including cleaning, tokenization, stop word removal, and stemming or lemmatization.
- Build and train at least two sentiment classification models, for example Naive Bayes and LSTM, and compare their performance.
- Implement real-time processing by streaming data through Apache Kafka and processing it with Apache Spark.
- Store the classified output in Elasticsearch or Apache Druid and produce interactive visual dashboards.
- Compare model and pipeline performance between batch mode and streaming mode.

### 4.3 Suggested Data Sources

Each group must select **one** primary data source. The data must be text-based, publicly available, and suitable for classification into positive, negative, or neutral sentiment.

| Category | Example Sources | Suggested Tools |
|----------|-----------------|-----------------|
| Social Media | Twitter posts filtered by Malaysian keywords or hashtags | Tweepy, Twitter API v2 |
| Customer Reviews | Shopee, Lazada, Google Maps, Google Play app reviews | BeautifulSoup, Selenium, Scrapy, Google Play Scraper |
| News Articles | The Star, Bernama, Free Malaysia Today RSS feeds | newspaper3k, RSS readers |
| Public Datasets | Sentiment140, IMDb, Amazon Reviews (for model training) | Kaggle, IEEE DataPort |

> ✅ Public labeled datasets may be used to train and validate models, but the final pipeline must process Malaysian-relevant data. Confirm your chosen source with the lecturer before collection begins.


### 4.4 Group Submission Table

Register your group and update your submission link in the table below. The **Sample** row shows the expected format.

| Team | Data Source | Tools | Open in GitHub |
|------|-------------|-------|----------------|
| Sample | [Youtube](https://www.youtube.com/results?search_query=travelling+in+malaysia) | Beautiful soup| [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](MasterData) |
| Shopping | Google Map Review  | selenium | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](Shopping) |
| Zoltraak | Youtube | Beautiful soup | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)] |
| Group C |  |  | _Add your link_ |
| WebMiner | Twitter | Beautiful soup | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](WebMiner) |
| Triple A | YouTube | Beautiful soup | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)]() |
| Scrape Master | Foodpanda | Beautiful soup |  [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)]() |
| Fast&Furious | YouTube (Geography Malaysia)  | Beautiful soup | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](Fast&Furious) |



## 🔗 Supporting Resources

Use the companion files below for detailed guidance on each part of the project:

- 🗃️ [Sample Dataset Sources (Twitter, Reviews, News)](p2_data.md)
- 🛠️ [Apache Spark and Kafka Setup Guide](p2_setup.md)
- 📊 [Visualization Tools and Examples](p2_visual.md)
- 🧠 [Sentiment Model Training Tips](p2_model.md)
- 📄 [Final Report Template](p2_report.md)
- 📁 [GitHub Folder Submission Template](p2_github.md)



## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions, or errors in the content.

You can also contact the course coordinator through [LinkedIn](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
