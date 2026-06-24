# 🥔 BigPotato | JobStreet High Performance Data Processing Pipeline

This repository contains the project work for **SECP3133 High Performance Data Processing**.
Our project focuses on building a large-scale web crawling and data processing pipeline using job listing data collected from **JobStreet Malaysia**.

Instead of only collecting data, this project also evaluates how different processing engines perform when handling structured job listing records.

---

## 📌 Project Title

**Optimizing High-Performance Data Processing for Large-Scale Web Crawlers**

---

## 👥 Team Members

| Name                   | Matric No |
| ---------------------- | --------- |
| Cheryl Cheong Kah Voon | A23CS0060 |
| Chau Ying Jia          | A23CS0213 |
| Lau Yee Wen            | A23CS0099 |
| Poh Lok Yee            | A23CS0262 |

---

## 📝 Project Summary

The main purpose of this project is to collect job listing data from JobStreet Malaysia and process it using several high-performance data processing approaches.

The project pipeline includes:

1. Crawling job listing data from JobStreet Malaysia
2. Saving the raw scraped data in JSON format
3. Cleaning and transforming the dataset
4. Processing the cleaned dataset using Pandas, Polars, and DuckDB
5. Comparing the performance of each processing method

---

## 🌐 Target Website

**Website:** JobStreet Malaysia
**URL:** https://my.jobstreet.com/
**Data Type:** Public job listing data

The crawler extracts job-related information from different job classifications on JobStreet Malaysia.

---

## 📂 Data Collected

The dataset contains the following main attributes:

| Attribute        | Description                             |
| ---------------- | --------------------------------------- |
| `job_title`      | Title of the job position               |
| `company`        | Name of the hiring company              |
| `location`       | Job location                            |
| `classification` | Job category or industry classification |
| `salary`         | Salary information shown in the listing |
| `salary_min`     | Extracted minimum salary value          |
| `salary_max`     | Extracted maximum salary value          |

---

## 📊 Dataset Overview

| Description                 |   Value |
| --------------------------- | ------: |
| Raw records collected       | 105,094 |
| Job classifications crawled |      30 |
| Final cleaned records       |  25,209 |
| Raw data format             |    JSON |
| Cleaned data format         |     CSV |

---

## 🔄 Data Processing Workflow

```text
JobStreet Malaysia
        ↓
Web Crawling
        ↓
Raw Data Storage
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Optimized Data Processing
        ↓
Performance Evaluation
```

---

## 🧹 Data Cleaning Steps

The raw dataset was cleaned and transformed before performance testing. The main cleaning steps include:

* Removing duplicate job records
* Handling missing values
* Standardizing text fields
* Cleaning job classification values
* Extracting salary ranges into numeric columns
* Standardizing location names
* Validating and rearranging data types

---

## 🛠️ Tools and Frameworks

| Tool / Framework | Usage                                  |
| ---------------- | -------------------------------------- |
| Python           | Main programming language              |
| Playwright       | Web crawling and browser automation    |
| BeautifulSoup    | HTML parsing                           |
| AsyncIO          | Asynchronous crawling                  |
| JSON             | Raw data storage                       |
| Pandas           | Data cleaning and optimized processing |
| Polars           | Lazy execution and parallel processing |
| DuckDB           | SQL-based analytical processing        |
| Matplotlib       | Performance visualization              |
| Google Colab     | Development and testing environment    |

---

## ⚡ Optimization Methods

Three optimized processing approaches were implemented and compared with the baseline Pandas approach.

### 🐼 Pandas Optimized Pipeline

Pandas optimization was applied by reducing unnecessary memory usage and improving processing efficiency.

Main techniques:

* Loading only required columns
* Specifying data types during reading
* Converting repeated text columns into category type
* Using vectorized string operations
* Applying efficient filtering and grouping

### 🚀 Polars Lazy Execution Pipeline

Polars was used to improve processing speed through lazy execution and parallel processing.

Main techniques:

* Lazy CSV scanning
* Query optimization before execution
* Parallel aggregation
* Expression-based transformation
* Final execution only when required

### 🦆 DuckDB SQL Processing

DuckDB was used as an analytical SQL engine to process CSV data efficiently.

Main techniques:

* Direct CSV querying
* SQL-based filtering
* Grouping and aggregation
* Analytical queries without fully loading the dataset into memory

---

## 📈 Performance Evaluation

The performance of each method was measured using:

* Execution time
* Memory usage
* CPU usage
* Throughput

### Average Benchmark Results

| Method                | Execution Time (s) | Memory Usage (MB) | CPU Usage (%) | Throughput |
| --------------------- | -----------------: | ----------------: | ------------: | ---------: |
| Baseline Pandas       |               0.31 |              3.92 |         27.99 | 128,736.72 |
| Optimized Pandas      |               0.15 |             0.001 |         44.10 | 178,116.33 |
| Polars Lazy Execution |               0.07 |              0.79 |         16.88 | 400,751.48 |
| DuckDB SQL            |               0.23 |              0.02 |         39.07 | 110,278.38 |

---

## 🔍 Main Findings

Based on the benchmark results:

* **Polars Lazy Execution** achieved the fastest execution time.
* **Polars** also recorded the highest throughput.
* **Optimized Pandas** achieved the lowest memory usage.
* **DuckDB** was useful for SQL-based analytical processing.
* The baseline Pandas method was still practical, but less efficient compared to optimized approaches.

Overall, **Polars** showed the best performance for this project’s processing workload.

---

## 📁 Repository Structure

```text
BigPotato/
│
├── data/
│   ├── raw_data.json
│   └── cleaned_data.csv
│
├── p1/
│   ├── crawler.ipynb
│   ├── clean_data.ipynb
│   └── optimize_pipeline.ipynb
│
├── p2/
│   ├── performance_before.csv
│   ├── performance_after.csv
│   └── evaluation_charts.ipynb
│
├── report/
│   └── HPDP_Project_Report.pdf
│
├── README.md
└── requirements.txt
```

---

## 👩‍💻 Team Responsibilities

| Member                 | Main Responsibility                                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Poh Lok Yee            | Developed the JobStreet web crawler, handled pagination, asynchronous crawling, and raw JSON data storage               |
| Chau Ying Jia          | Developed the data cleaning pipeline, removed duplicates, handled missing values, and generated the cleaned CSV dataset |
| Lau Yee Wen            | Designed the system architecture and implemented optimization pipelines using Pandas, Polars, and DuckDB                |
| Cheryl Cheong Kah Voon | Conducted performance evaluation, measured benchmark metrics, and generated performance charts                          |

---

## 🎓 Course Information

**Course:** SECP3133 High Performance Data Processing
**Lecturer:** Dr. Seah Choon Sean
**Faculty:** Faculty of Computing, Universiti Teknologi Malaysia
**Semester:** Semester 2 2025/2026

---


