<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# 📄 Project 2: Real-Time Sentiment Analysis using Apache Spark and Kafka

> **Student Reference Guide** — High Performance Data Processing (SECP3133)
> Read this document fully before starting the project. It explains every requirement, deadline, and deliverable you need to know.

---

## 📑 Table of Contents

1. [Course Information](#1-course-information)
2. [Introduction](#2-introduction)
3. [Project Overview](#3-project-overview)
4. [Learning Outcomes](#4-learning-outcomes)
5. [Project Requirements](#5-project-requirements)
6. [Technical Tasks](#6-technical-tasks)
7. [Deliverables](#7-deliverables)
8. [Submission Guidelines](#8-submission-guidelines)
9. [Evaluation Criteria](#9-evaluation-criteria)
10. [Recommended Tools and Techniques](#10-recommended-tools-and-techniques)
11. [Example Workflow](#11-example-workflow)
12. [Common Mistakes to Avoid](#12-common-mistakes-to-avoid)
13. [Tips for Success](#13-tips-for-success)
14. [Important Notes](#14-important-notes)
15. [Supporting Resources](#-supporting-resources)

---

## 1. Course Information

This section summarizes the official course details. It places Project 2 within the wider context of the course.

| Item | Details |
|------|---------|
| **Faculty** | Faculty of Computing |
| **Program** | Bachelor of Computer Science (Data Engineering) |
| **Course Code** | SECP3133 |
| **Course Name** | High Performance Data Processing |
| **Academic Session** | 2025/2026, Semester 2 |
| **Credit Hours** | 3 |
| **Course Coordinator** | A.P. Dr. Mohd Shahizan Othman |

**Teaching Team**

| Lecturer | Office | Email |
|----------|--------|-------|
| A.P. Dr. Mohd Shahizan Othman | N28A | shahizan@utm.my |
| Dr. Seah Choon Sen | N28A | seahcs@utm.my |

**Course Synopsis**

High Performance Data Processing employs high performance computing to process data, which is then translated into information and knowledge. The growth of high performance computing and data analytics has enabled the real time interrogation of extremely large datasets. This course covers the fundamentals of high performance computing, data processing, and high performance data processing architecture. Students are also exposed to industry and research case studies, and they gain hands-on experience with Amazon Web Services as a data processing platform.

**Course Learning Outcomes (CLO)**

| CLO | Description |
|-----|-------------|
| CLO1 | Comprehend the concepts of cloud computing, high performance computing, and data processing. |
| CLO2 | Design a high performance computing architecture that considers infrastructure type, data, algorithm, design process, and results. |
| CLO3 | Develop a high performance data processing program and evaluate it against an equivalent sequential program. |
| CLO4 | Demonstrate a high performance project on selected problem domains through written and oral presentation. |

> 📌 **Project 2 primarily supports CLO2, CLO3, and CLO4.** You will design a streaming architecture, develop and evaluate a high performance solution, and present your results in written and oral form.

**Course Assessment Components**

| No. | Component | Focus | Weightage |
|-----|-----------|-------|:---------:|
| 1 | Assignment | Academic paper and crawler | 20% |
| 2 | Lab Exercise | AWS and Apache tools | 20% |
| 3 | Project | Project 1 and Project 2 | 30% |
| 4 | Final Examination | Written examination | 30% |
| | **Total** | | **100%** |

> The Project component carries 30% of the total course assessment and is divided equally between Project 1 and Project 2. **This brief covers Project 2, which contributes 15% to your final course grade.**

---

## 2. Introduction

Welcome to Project 2 of the High Performance Data Processing course. This project gives you a practical opportunity to design and build a real-time sentiment analysis pipeline using modern big data technologies. The activities are designed to connect classroom theory with industry-relevant data engineering practice.

In this project, each group will collect text data from Malaysian-relevant sources, classify the sentiment of that text, and process it through a scalable pipeline built with Apache Kafka and Apache Spark. The final insights will be stored and presented through interactive dashboards.

This document is your official reference for Project 2. Read every section carefully before starting, and return to it throughout the four-week implementation period.

### 📋 Quick Facts

| Item | Details |
|------|---------|
| 📊 **Weightage** | 15% of total course assessment |
| 🕓 **Project Duration** | 4 Weeks |
| 📅 **Submission Deadline** | **Friday, 26 June 2026, 11:59 PM (MST)** |
| 📤 **Submission Channels** | e-Learning Portal and GitHub Repository |
| 👥 **Group Size** | **Maximum 3 students per group** |

> 📌 Each group must include students from **different genders, races, or backgrounds** to encourage diverse perspectives and inclusive teamwork.

---

## 3. Project Overview

Organizations increasingly rely on real-time analytics to understand public opinion about products, events, and social issues. This project simulates that environment by requiring each group to build a complete sentiment analysis system that operates on streaming data.

Each group will select a Malaysian-relevant text source, such as social media posts, online reviews, or news articles. The collected text will be cleaned using natural language processing (NLP) techniques, classified as **positive, negative, or neutral** by a trained model, and processed through a streaming pipeline. The resulting sentiment trends will then be stored and visualized so that insights can be communicated clearly to stakeholders.

### ⚙️ Technologies Involved

| Technology | Role in the Pipeline |
|------------|----------------------|
| **Apache Kafka** | Streams text data from live or batched sources into the processing layer. |
| **Apache Spark** | Processes large volumes of data in parallel and applies the sentiment model. |
| **Elasticsearch or Apache Druid** | Stores classified results and supports fast querying for visualization. |
| **NLP Libraries** (NLTK, spaCy, Hugging Face) | Perform text preprocessing and support model development. |

---

## 4. Learning Outcomes

Upon successful completion of this project, you will be able to:

1. Design and configure a real-time streaming pipeline using Apache Kafka and Apache Spark.
2. Apply standard natural language processing techniques to clean and prepare text data.
3. Train, evaluate, and compare at least two sentiment classification models.
4. Integrate a trained model into a streaming system that classifies text as positive, negative, or neutral.
5. Store and visualize sentiment results using dashboard tools such as Kibana or Apache Superset.
6. Collaborate effectively in a small team and communicate insights through a professional report and presentation.

---

## 5. Project Requirements

### 5.1 Group Composition

This is a group-based project. Students must form their own groups subject to the following requirements:

- **Each group must consist of a maximum of three (3) students.** Groups with more than three members will not be accepted.
- Each group must include members from different genders, races, or backgrounds to encourage diverse perspectives and inclusive collaboration.
- Roles and responsibilities must be distributed clearly among members. Suggested roles include Group Leader, Data and NLP Engineer, and Pipeline and Visualization Engineer.
- Group formation and the chosen data source must be confirmed with the lecturer no later than the end of Week 1.

### 5.2 Technical Requirements

The technical scope of the project is fixed. Each group must satisfy all of the following criteria:

- Collect or stream text data from a Malaysian-relevant source, such as Twitter, Shopee, Google Play reviews, or local news.
- Preprocess the text using NLP methods, including cleaning, tokenization, stop word removal, and stemming or lemmatization.
- Build and train at least two sentiment classification models, for example Naive Bayes and LSTM, and compare their performance.
- Implement real-time processing by streaming data through Apache Kafka and processing it with Apache Spark.
- Store the classified output in Elasticsearch or Apache Druid and produce interactive visual dashboards.
- Compare model and pipeline performance between batch mode and streaming mode.

### 5.3 Suggested Data Sources

Each group must select **one** primary data source. The data must be text-based, publicly available, and suitable for classification into positive, negative, or neutral sentiment.

| Category | Example Sources | Suggested Tools |
|----------|-----------------|-----------------|
| Social Media | Twitter posts filtered by Malaysian keywords or hashtags | Tweepy, Twitter API v2 |
| Customer Reviews | Shopee, Lazada, Google Maps, Google Play app reviews | BeautifulSoup, Selenium, Scrapy, Google Play Scraper |
| News Articles | The Star, Bernama, Free Malaysia Today RSS feeds | newspaper3k, RSS readers |
| Public Datasets | Sentiment140, IMDb, Amazon Reviews (for model training) | Kaggle, IEEE DataPort |

> ✅ Public labeled datasets may be used to train and validate models, but the final pipeline must process Malaysian-relevant data. Confirm your chosen source with the lecturer before collection begins.

---

## 6. Technical Tasks

The project runs over a four-week schedule. Each week has clear objectives and milestones. Follow this schedule closely to ensure steady progress.

### 6.1 Weekly Schedule

| Week | Phase | Key Activities |
|------|-------|----------------|
| **Week 1** | Planning and Data Acquisition | Form the group, select a data source, obtain lecturer approval, and begin collecting text data. |
| **Week 2** | Preprocessing and Modeling | Clean and preprocess the text data, then build, train, and evaluate at least two sentiment models. |
| **Week 3** | Pipeline Integration | Set up Apache Kafka and Apache Spark, integrate the chosen model, and connect the storage layer. |
| **Week 4** | Visualization and Submission | Build dashboards, compare batch and streaming results, finalize the report, and submit all deliverables. |

### 6.2 Suggested Role Assignments

Although roles may be adapted to suit each group, the following structure is recommended for a team of three:

| Role | Primary Responsibilities |
|------|--------------------------|
| Group Leader and Data Engineer | Coordinates the team, manages data acquisition and preprocessing, and tracks progress against the timeline. |
| NLP and Model Engineer | Develops, trains, and evaluates the sentiment models, and prepares the model comparison. |
| Pipeline and Visualization Engineer | Builds the Kafka and Spark pipeline, configures storage, and develops the dashboards. |

> Every member is expected to contribute to coding, testing, and documentation regardless of their primary role.

### 6.3 Model Development Requirements

Each group must develop and compare at least **two** sentiment classification approaches. Acceptable model categories are:

| Model Category | Examples and Tools |
|----------------|--------------------|
| Machine Learning | Naive Bayes, Support Vector Machine, Logistic Regression (scikit-learn). |
| Deep Learning | LSTM, BiLSTM, GRU, or CNN (TensorFlow or PyTorch). |
| Transformer Models | BERT or DistilBERT (Hugging Face Transformers). |

Models must be evaluated using **accuracy, precision, recall, F1 score, and a confusion matrix**. Split the dataset into training, testing, and validation subsets, for example using a 70 / 20 / 10 percent ratio.

### 6.4 Performance Comparison Requirements

To demonstrate how the system behaves under different conditions, each group must compare the following between **batch mode** and **streaming mode**:

- Total processing time required to classify a fixed volume of text.
- Throughput, measured as the number of records processed per second.
- Classification accuracy and consistency across both modes.
- Resource usage, including CPU and memory, where measurable.

> Present your results using clearly labeled tables and charts, and include a short written interpretation of the findings.

---

## 7. Deliverables

Each group must submit the following five deliverables. All items are assessed as part of the final grade.

| No. | Deliverable | Description |
|-----|-------------|-------------|
| 1 | **Final Report (PDF)** | A complete technical report covering data acquisition, model development, system architecture, results, and findings. Must be uploaded to Turnitin in PDF format. |
| 2 | **Source Code** | Python or Scala scripts, model files, and configuration files, organized clearly. Submit as a GitHub repository link or a ZIP archive. |
| 3 | **Dashboard and Dataset** | A working visualization dashboard together with the exported cleaned dataset. |
| 4 | **Model Comparison** | An evaluation of the different models, including batch versus streaming performance results. |
| 5 | **Presentation Slides** | Slide deck for a clear and concise 10-minute group presentation. |

### 7.1 Recommended GitHub Folder Structure

To keep submissions consistent and easy to grade, follow this recommended folder structure for your repository:

```
Project-SentimentAnalysis/
├── README.md
├── data/
│   ├── raw_data/
│   └── cleaned_data.csv
├── notebooks/
│   ├── preprocessing.ipynb
│   └── model_training.ipynb
├── kafka_spark_pipeline/
│   ├── kafka_producer.py
│   └── spark_streaming.py
├── dashboard/
│   ├── elastic_mappings.json
│   └── kibana_visualizations.ndjson
├── reports/
│   ├── final_report.pdf
│   └── presentation_slides.pptx
└── requirements.txt
```

---

## 8. Submission Guidelines

All submissions must follow the rules below. Late or incomplete submissions may result in a deduction of marks at the lecturer's discretion.

### 8.1 Submission Channels

| Channel | Purpose |
|---------|---------|
| e-Learning Portal | Upload the final report (PDF), presentation slides (PPTX), and a link to your GitHub repository. |
| Turnitin | Upload the final report (PDF) for plagiarism verification. |
| GitHub Repository | Host all source code, notebooks, datasets, dashboard files, and configurations using the recommended folder structure. |

### 8.2 Submission Deadline

All deliverables must be submitted by **Friday, 26 June 2026, before 11:59 PM (Malaysian Standard Time)**.

Each submission must clearly state the group name, the names of all members, and a contact email address.

### 8.3 Suggested Final Report Structure

Your final report should follow a professional structure. The recommended sections are:

1. Title Page, including project title, group name, member names, and matric numbers.
2. Table of Contents.
3. Introduction, covering background, objectives, and project scope.
4. Data Acquisition and Preprocessing, describing sources, tools, and cleaning steps.
5. Sentiment Model Development, including model choice, training process, and evaluation.
6. Apache System Architecture, with a workflow diagram for Kafka, Spark, and the storage layer.
7. Analysis and Results, presenting key findings, visualizations, and insights.
8. Optimization and Comparison, covering model and architecture improvements.
9. Conclusion and Future Work.
10. References.
11. Appendix, containing code snippets, configurations, and logs.

### 8.4 Group Submission Table

Register your group and update your submission link in the table below. The **Sample** row shows the expected format.

| Team | Data Source | Tools | Open in GitHub |
|------|-------------|-------|----------------|
| Sample | [StudyMalaysia.com](https://www.studymalaysia.com) | BeautifulSoup | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/tree/main/2425/project/p2) |
| Group A | _To be confirmed_ | _To be confirmed_ | _Add your link_ |
| Group B | _To be confirmed_ | _To be confirmed_ | _Add your link_ |
| Group C | _To be confirmed_ | _To be confirmed_ | _Add your link_ |

---

## 9. Evaluation Criteria

The project is assessed using the rubric below. The total weightage is 100 percent of the project mark, which contributes 15 percent to the overall course grade.

| Assessment Area | Description | Weight |
|-----------------|-------------|:------:|
| Data Acquisition and Preprocessing | Quality of the data source, NLP cleaning steps, and dataset preparation. | 15% |
| Sentiment Model Development | Correct training, evaluation, and comparison of at least two models. | 25% |
| Apache Pipeline Integration | Working Kafka and Spark pipeline with correct model integration. | 20% |
| Real-Time Processing and Comparison | Effective streaming implementation and batch versus streaming comparison. | 10% |
| Visualization and Dashboard | Clarity, accuracy, and usefulness of the sentiment dashboards. | 10% |
| Final Report | Clarity, completeness, and overall professionalism of the document. | 10% |
| Group Presentation | Teamwork, clarity of explanation, time management, and Q and A handling. | 10% |
| **Total** | | **100%** |

---

## 10. Recommended Tools and Techniques

The tools and libraries below are widely used and well documented. You are not limited to this list, but it provides a strong starting point.

| Category | Recommended Tools |
|----------|-------------------|
| Data Collection | Tweepy, BeautifulSoup, Selenium, Scrapy, Google Play Scraper, newspaper3k |
| Text Preprocessing | NLTK, spaCy, Hugging Face Transformers, regular expressions |
| Machine Learning Models | scikit-learn for Naive Bayes, SVM, and Logistic Regression |
| Deep Learning Models | TensorFlow or PyTorch for LSTM, BiLSTM, GRU, and CNN |
| Streaming and Processing | Apache Kafka, Apache Spark Structured Streaming (PySpark) |
| Storage | Elasticsearch, Apache Druid |
| Visualization | Kibana, Apache Superset, Power BI, Tableau, Matplotlib, Seaborn, Plotly |
| Deployment Support | Docker, Google Colab, Databricks, AWS EMR |

**Suggested visualizations to include in the dashboard and report:**

- Sentiment distribution pie chart showing the proportion of positive, negative, and neutral entries.
- Sentiment over time presented as a line graph.
- Word clouds for frequent positive and negative terms.
- A real-time sentiment stream view, where the streaming setup allows it.

---

## 11. Example Workflow

The workflow below illustrates a typical end-to-end project execution. Adapt these steps to suit your chosen data source and tools.

1. **Select a data source.** Identify a Malaysian-relevant text source and confirm it with the lecturer.
2. **Collect the data.** Use an appropriate tool to gather a representative volume of text data.
3. **Preprocess the text.** Convert text to lowercase, remove noise such as URLs and mentions, and apply tokenization and lemmatization.
4. **Build the models.** Train at least two sentiment classifiers and evaluate them with standard metrics.
5. **Select the best model.** Choose the model with the strongest and most consistent performance for deployment.
6. **Set up Kafka.** Install Kafka, start the broker, and create a topic to receive streaming text.
7. **Set up Spark.** Configure a Spark streaming job that consumes data from the Kafka topic.
8. **Integrate the model.** Apply the trained model within the Spark job to classify incoming text in real time.
9. **Store the results.** Write the classified output to Elasticsearch or Apache Druid.
10. **Visualize and analyze.** Build dashboards, compare batch and streaming results, and interpret the findings.
11. **Document and present.** Compile the report, polish the slides, and rehearse as a team.

---

## 12. Common Mistakes to Avoid

Many groups face the same challenges. Being aware of them in advance can save valuable time.

- Choosing a data source that is too small or not suitable for sentiment classification.
- Skipping proper text preprocessing, which often reduces model accuracy significantly.
- Training only one model, when the brief clearly requires at least two for comparison.
- Treating the project as a model-only task and neglecting the Kafka and Spark integration.
- Leaving the streaming pipeline setup until the final week, when it usually needs the most debugging time.
- Reporting accuracy numbers without explaining what they mean or why one model performs better.
- Submitting code without comments, a clear folder structure, or an updated requirements file.

---

## 13. Tips for Success

- Start data collection early, since gathering and labeling text data often takes longer than expected.
- Test the Kafka and Spark setup with a small sample before processing the full dataset.
- Use Docker or a cloud environment to reduce installation and configuration problems.
- Keep the trained model files and configurations under version control.
- Hold short weekly meetings to track progress and resolve blockers quickly.
- Ask the lecturer for guidance whenever the scope or technical approach is unclear.
- Always keep a backup copy of the dataset, models, and code outside the main repository.

---

## 14. Important Notes

- **Plagiarism**, including copying code or text without proper attribution, will be treated as a serious academic offense. Students who submit copied work may receive a mark of zero and face disciplinary action by the Faculty.
- Each group member must contribute fairly. Imbalanced contributions may affect individual marks.
- All data must be collected legally and ethically, and the terms of service of each source must be respected.
- Submitting outside the official channels listed in this guide will result in the submission being treated as missing.
- Direct any questions regarding scope or grading to the lecturer or teaching assistant during the course period.

---

## 🔗 Supporting Resources

Use the companion files below for detailed guidance on each part of the project:

- 🗃️ [Sample Dataset Sources (Twitter, Reviews, News)](p2_data.md)
- 🛠️ [Apache Spark and Kafka Setup Guide](p2_setup.md)
- 📊 [Visualization Tools and Examples](p2_visual.md)
- 🧠 [Sentiment Model Training Tips](p2_model.md)
- 📄 [Final Report Template](p2_report.md)
- 📁 [GitHub Folder Submission Template](p2_github.md)

---

## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions, or errors in the content.

You can also contact the course coordinator through [LinkedIn](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
