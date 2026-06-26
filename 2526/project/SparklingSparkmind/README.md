# Project 2: Real-Time Sentiment Analysis using Apache Spark and Kafka

**Course:** SECP3133 High Performance Data Processing
**Semester:** 2025/2026, Semester 2
**Deadline:** Friday, 26 June 2026, 11:59 PM (MYT)

## Group Members

| Name | Matric No. | Role |
|---|---|---|
| [Member 1 name] | [matric] | Data & NLP Engineer (Acquisition + Preprocessing) |
| [Member 2 name] | [matric] | Model Engineer (Sentiment Classification) |
| [Member 3 name] | [matric] | Pipeline Engineer (Kafka + Spark + Storage) |
| Bella (Ain Nurnabila Binti Mohd Azhar) | A23CS0207 | Visualization & Reporting Engineer |

## Project Summary

Real-time sentiment analysis pipeline on Malaysian-relevant text data, using:
- **Kafka** for streaming ingestion
- **Spark Structured Streaming** for parallel processing and model inference
- **Elasticsearch / Apache Druid** for storage
- **Kibana / Apache Superset** for visualization

## Repository Structure

```
P2/[your_group]/
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

## Status

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

## Contact

For questions about this submission, contact: [group contact email]
