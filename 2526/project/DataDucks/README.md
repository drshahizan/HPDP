````markdown
# Project 1: Optimizing High-Performance Data Processing for Large-Scale Web Crawlers

## Team Information

**Team Name:** DataDucks

**Target Website:** https://soyacincau.com/

**Course:** High-Performance Data Processing

---

# Group Members

| Member | Role |
|---------|------|
| Gui Kah Sin | Ingestion Lead |
| Woo Cheng Shuan | Data Pipeline Lead |
| Sabrina Heng Wei Qi | HPC Specialist |
| Ling Yu Qian | Performance Analytics Lead |

---

# Project Overview

This project aims to develop a high-performance web crawler capable of extracting large-scale structured data from **SoyaCincau**, one of Malaysia's leading technology news websites. The collected data is cleaned, transformed, and optimized using High-Performance Computing (HPC) techniques to improve processing efficiency.

The project demonstrates the complete data engineering workflow, from web crawling and data cleaning to parallel processing and performance evaluation.

---

# Project Objectives

- Develop an AJAX-based web crawler for extracting structured article data.
- Store collected data in JSON and CSV formats.
- Perform data cleaning and preprocessing.
- Apply High-Performance Computing (HPC) optimization techniques.
- Compare sequential and optimized processing performance.
- Evaluate execution time, CPU usage, memory usage, and throughput.

---

# Dataset Information

**Source Website**

- SoyaCincau

**Final Clean Dataset**

- 30,834 structured article records

**Data Fields**

- Article Title
- Article URL
- Category
- Publication Date
- Article Summary (Excerpt)

---

# Project Workflow

```text
SoyaCincau Website
        │
        ▼
AJAX-based Web Crawler
        │
        ▼
raw_data.json
        │
        ▼
Data Cleaning
        │
        ▼
cleaned_data.csv
        │
        ▼
HPC Optimization
(Sequential, Multithreading,
 Multiprocessing, Dask)
        │
        ▼
Performance Evaluation
        │
        ▼
Performance Metrics
```

---

# Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Development Environment | Google Colab |
| Web Crawling | Requests, BeautifulSoup |
| Data Processing | Pandas, NumPy |
| Multithreading | ThreadPoolExecutor |
| Multiprocessing | Python multiprocessing |
| Distributed Processing | Dask |
| Data Storage | JSON, CSV |

---

# Project Phases

## Phase 1 – Data Collection

- AJAX-based web crawling
- Progressive data storage
- JSON dataset generation

## Phase 2 – Data Cleaning

- Remove invalid records
- Handle missing values
- Remove duplicate records
- Standardize text fields
- Standardize date format
- Validate URLs
- Export cleaned dataset

## Phase 3 – High-Performance Optimization

Implemented four processing approaches:

- Sequential Processing (Baseline)
- Multithreading
- Multiprocessing
- Dask Distributed Processing

Performance metrics collected:

- Execution Time
- CPU Usage
- Memory Usage
- Throughput (records/second)

---

# Repository Structure

```text
Project1/
│
├── data/
│   ├── raw_data.json
│   ├── cleaned_data.csv
│   ├── optimized_data.csv
│   └── performance_metrics.csv
│
├── notebooks/
│   ├── main_crawler.ipynb
│   ├── clean_data.ipynb
│   ├── optimize_pipeline.ipynb
│   └── evaluation_charts.ipynb
│
├── report/
│   └── Final_Report.pdf
│
├── slides/
│   └── Presentation_Slides.pdf
│
└── README.md
```

---

# Team Responsibilities

## Member 1 – Gui Kah Sin (Ingestion Lead)

- Develop the AJAX-based web crawler.
- Handle page routing and request exceptions.
- Implement progressive data storage.
- Ensure ethical web crawling practices.
- Prepare the project background and data collection documentation.

## Member 2 – Woo Cheng Shuan (Data Pipeline Lead)

- Develop the data cleaning pipeline.
- Handle missing values and duplicate records.
- Standardize dataset structure.
- Validate cleaned data.
- Export the final cleaned dataset.

## Member 3 – Sabrina Heng Wei Qi (HPC Specialist)

- Implement sequential processing benchmark.
- Implement multithreading optimization.
- Implement multiprocessing optimization.
- Implement Dask distributed processing.
- Collect execution time, CPU usage, memory usage, and throughput metrics.
- Design the HPC system architecture.
- Document optimization techniques.

## Member 4 – Ling Yu Qian (Performance Analytics Lead)

- Analyze performance metrics.
- Generate comparison charts.
- Compare baseline and optimized performance.
- Interpret experimental results.
- Prepare conclusions and future work.

---

# Performance Evaluation

The following performance metrics were collected during the optimization process:

- Execution Time
- CPU Usage
- Memory Usage
- Throughput (records/second)

Performance metrics are stored in:

```text
performance_metrics.csv
```

Performance visualization is generated using:

```text
evaluation_charts.ipynb
```

---

# References

- https://soyacincau.com/
- Python Documentation
- Pandas Documentation
- BeautifulSoup Documentation
- Dask Documentation

---

# License

This repository was developed for academic purposes as part of the **High-Performance Data Processing** course.
````
