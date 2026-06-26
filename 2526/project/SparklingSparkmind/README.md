# Project 2: Real-Time Sentiment Analysis using Apache Spark and Kafka

**Course:** SECP3133 High Performance Data Processing
**Semester:** 2025/2026, Semester 2
**Deadline:** -

## Group Members

| Name | Matric No. | Role |
|---|---|---|
| DAYANG | A23CS | Data & NLP Engineer (Acquisition + Preprocessing) |
| FARRA | A23CS | Model Engineer (Sentiment Classification) |
| SAFIYA | A23CS | Pipeline Engineer (Kafka + Spark + Storage) |
| AIN NURNABILA BINTI MOHD AZHAR | A23CS0207 | Visualization & Reporting Engineer |

## Project Summary

Real-time sentiment analysis pipeline on Malaysian-relevant text data, using:
- **Kafka** for streaming ingestion
- **Spark Structured Streaming** for parallel processing and model inference
- **Elasticsearch / Apache Druid** for storage
- **Kibana / Apache Superset** for visualization

## Data Source

- **Source:** 
- **Collection tool:** 
- **Approx. volume collected:** 

## Models Compared

| Model | Category | Library |
|---|---|---|
| [e.g. Naive Bayes] | Machine Learning | scikit-learn |
| [e.g. LSTM] | Deep Learning | TensorFlow / PyTorch |

Evaluated using accuracy, precision, recall, F1 score, and confusion matrix (70/20/10 train/test/validation split).

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start Kafka broker and create topic
# [add exact commands once Member 3 finalizes setup]

# 3. Run preprocessing notebook
jupyter notebook notebooks/preprocessing.ipynb

# 4. Train models
jupyter notebook model_training.ipynb

# 5. Start the Spark streaming job
spark-submit kafka_spark_pipeline/spark_streaming.py

# 6. View dashboard
# Open kafka_spark_pipeline/dashboard/dashboard_prototype.html in a browser
# (or Kibana/Superset URL once storage layer is connected)
```

## Repository Structure

```
HPDP/2526/project/Sparkling Sparkmind/
├── README.md
├── data/
│   ├── raw_data/
│   └── cleaned_data.csv
├── notebooks/
│   └── preprocessing.ipynb
├── model_training.ipynb
├── kafka_spark_pipeline/
│   ├── spark_streaming.py
│   ├── dashboard/
│   └── elastic_mappings.json
├── kibana_visualizations.json
├── reports/
│   └── final_report.pdf
├── presentation_slides.pptx
└── requirements.txt
```

## Deliverables Status

Mapped to the 5 required submission items (Section 7 of the brief):

| # | Deliverable | Status | Location |
|---|---|---|---|
| 1 | Final Report (PDF) | [ ] In progress | `reports/final_report.pdf` |
| 2 | Source Code | [ ] In progress | `kafka_spark_pipeline/`, `notebooks/`, `model_training.ipynb` |
| 3 | Dashboard + Dataset | [ ] In progress | `kafka_spark_pipeline/dashboard/`, `data/cleaned_data.csv` |
| 4 | Model Comparison | [ ] In progress | `model_training.ipynb`, `reports/final_report.pdf` (Section 3) |
| 5 | Presentation Slides | [ ] Not started | `presentation_slides.pptx` |

## Progress Checklist

- [ ] Data source confirmed with lecturer (Week 1)
- [ ] Data collection complete
- [ ] Preprocessing pipeline complete
- [ ] At least 2 sentiment models trained and evaluated
- [ ] Kafka broker + topic configured
- [ ] Spark Structured Streaming job integrated with trained model
- [ ] Storage layer (Elasticsearch/Druid) connected
- [ ] Batch vs. streaming comparison complete
- [ ] Dashboards built (pie chart, sentiment-over-time, word clouds)
- [ ] Final report compiled
- [ ] Presentation slides finalized

## Academic Integrity

All work in this repository is original and produced by the listed group members. Public datasets and open-source libraries used for reference or training are credited in the final report's References section, per the course's academic integrity policy.
