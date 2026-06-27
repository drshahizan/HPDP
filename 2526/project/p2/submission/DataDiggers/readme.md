# 👀 Project 2: Real-Time Sentiment Analysis using Apache Spark and Kafka

✦ Data source: Google Play reviews — Touch 'n Go, Grab, foodpanda

| Name | Matric Number | Role
|------|------|------|
| NUR FIRZANA BINTI BADRUS HISHAM | A23CS0156 | Data Engineer |
| NURAISYAH |  | Model Engineer |
| HAANI |  |  Pipeline Engineer |
| IKA |  | Visualization & Performance Engineer |


## 📂Repository Structure

```
HPDP/2526/project/p2/submission/DataDiggers/
├── README.md
├── data/
│   ├── raw_data/
│   |   └── cleaned_step1.csv
│   |   └── labeled_reviews.csv
│   |   └── lemmatized.csv
│   |   └── raw_reviews.csv
│   |   └── tokenized.csv
│   └── cleaned_data.csv        # hands off to model engineer to start their job
├── data_cleaning/              # DATA ENGINEER FOLDER
│   └── clean_text.ipynb        # 3rd step
│   └── export_dataset.ipynb    # 6th step
│   └── label_data.ipynb        # 2nd step
│   └── lemmatize.ipynb         # 5th step
│   └── scrape_reviews.ipynb    # 1st step
│   └── tokenize_review.ipynb   # 4th step
├── model_training.ipynb
├── kafka_spark_pipeline/
│   ├── spark_streaming.py
│   ├── dashboard/
│   └── elastic_mappings.json
├── kibana_visualizations.json
├── reports/
│   └── final_report.pdf
├── presentation_slides.pdf
└── requirements.txt
```
