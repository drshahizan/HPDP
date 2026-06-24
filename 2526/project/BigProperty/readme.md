# SECP3133 Project 1: Optimizing High-Performance Data Processing for Large-Scale Web Crawlers

Welcome to our group's repository for the High Performance Data Processing project.

## Group Information

* **Members:**

  * LAU YAN KAI - A23CS0098
  * CHEW CHIU XIAN - A23CS0061
  * ELIJAH SHE YU SHENG - A23CS0073
  * NEO LI XIN - A23CS0253

## 📌 Project Overview

This project focuses on designing, developing, and optimizing a large-scale web crawler for collecting property listing data from iProperty Malaysia. The project applies high-performance computing techniques to improve crawling efficiency and data processing performance.

The crawler collects more than 100,000 property records, processes the raw data into a structured format, and evaluates the effectiveness of optimization techniques through performance benchmarking.

## 🎯 Project Objectives

* Develop a web crawler capable of collecting at least 100,000 property records from iProperty Malaysia.
* Extract and store property information in a structured format.
* Perform data cleaning, transformation, and validation.
* Implement high-performance computing techniques such as multithreading and multiprocessing.
* Evaluate and compare baseline and optimized implementations using quantitative performance metrics.

## 🌐 Target Website

* Website: iProperty Malaysia
* Category: Property Listings for Sale
* Data Source Type: Public property listing data
* Total Raw Records Collected: 102,502

## 📊 Dataset Description

### Raw Dataset

| Column      | Description                              |
| ----------- | ---------------------------------------- |
| page        | Page number where listing was collected  |
| raw_text    | Original extracted property listing text |
| listing_url | URL of the property listing              |
| scraped_at  | Timestamp when data was collected        |

### Processed Dataset

| Column         | Description                        |
| -------------- | ---------------------------------- |
| listing_url    | Unique property listing identifier |
| property_type  | Property category                  |
| price_rm       | Property price (MYR)               |
| price_psf      | Price per square foot              |
| built_up_sqft  | Built-up area                      |
| land_area_sqft | Land area                          |
| furnishing     | Furnishing status                  |
| scraped_at     | Standardized timestamp             |

## 📈 Data Collection Summary

| Description                 |                        Value |
| --------------------------- | ---------------------------: |
| Total Raw Records Collected |                      102,502 |
| Unique Listing URLs         |                       95,004 |
| Duplicate Records           |                        7,498 |
| Dataset Format              |                          CSV |
| Raw Dataset File            | iproperty_raw_100k_final.csv |

## 🧹 Data Cleaning Summary

The data cleaning process included:

* Duplicate record removal using `listing_url` as the primary identifier.
* Missing value handling using median imputation for numerical attributes.
* Standardization of categorical values.
* Data type validation and schema enforcement.
* Timestamp normalization and formatting.

## ⚙️ Tools and Technologies

| Tool / Framework   | Purpose                         |
| ------------------ | ------------------------------- |
| Python             | Main programming language       |
| Selenium           | Browser automation and crawling |
| ChromeDriver       | Browser driver                  |
| webdriver-manager  | Driver management               |
| BeautifulSoup      | HTML parsing                    |
| Requests           | Optimized crawling experiments  |
| ThreadPoolExecutor | Multithreading optimization     |
| Pandas             | Data cleaning and processing    |
| CSV                | Data storage                    |
| VS Code            | Development environment         |
| Windows CMD        | Execution and monitoring        |

## 🚀 Optimization Techniques

### 1. Multithreading

The optimized crawler uses Python's `ThreadPoolExecutor` to perform concurrent requests and improve crawling throughput.

### 2. Multiprocessing

Parallel execution techniques were explored to reduce overall execution time and improve scalability.

### 3. Concurrent Data Processing

Data cleaning and transformation tasks were designed to support high-performance processing workflows.

### 4. Resource Monitoring

Execution time, CPU utilization, memory consumption, and throughput were measured to evaluate optimization effectiveness.

## 📊 Data Processing Pipeline

### Data Collection

* Selenium-based page navigation
* BeautifulSoup HTML parsing
* CSV dataset generation
* Crawling log generation

### Data Cleaning

* Duplicate removal
* Missing value handling
* Validation checks
* Schema enforcement

### Data Transformation

* Regular expression extraction
* Property type classification
* Price extraction
* Area extraction
* Furnishing status classification
* Timestamp standardization

## ⚡ Performance Evaluation Metrics

The project evaluates optimization effectiveness using:

* Execution Time
* Peak Memory Usage
* CPU Utilization
* Throughput
* Records Processed

## 📁 Project Structure

```text
iProperty-WebCrawler/
│
├── data/
│   ├── raw/
│   │   └── iproperty_raw_100k_final.csv
│   │
│   ├── processed/
│   │   └── iproperty_cleaned.csv
│   │
│   └── logs/
│       └── crawling_log_100k_final.csv
│
├── scripts/
│   ├── crawler.py
│   ├── cleaner.py
│   ├── transformer.py
│   ├── optimizer.py
│   └── performance_evaluation.py
│
├── report/
│   └── SECP3133_Project_Report.pdf
│
├── images/
│   ├── crawling_output.png
│   ├── dataset_preview.png
│   └── performance_charts.png
│
├── README.md
└── requirements.txt
```

## 👥 Team Responsibilities

| Member              | Role                            |
| ------------------- | ------------------------------- |
| Neo Li Xin          | Project Lead & System Architect |
| Elijah She Yu Sheng | Data Collection Engineer        |
| Lau Yan Kai         | Data Processing Engineer        |
| Chew Chiu Xian      | HPC & Performance Specialist    |

## 🔒 Ethical Considerations

* Only publicly available property listing data was collected.
* No login-protected or private user information was accessed.
* Random delays were used to reduce server load.
* No CAPTCHA bypassing or security circumvention techniques were employed.
* Crawling logs were maintained for transparency and responsible crawling.

## 📌 Conclusion

This project successfully developed a large-scale property web crawler capable of collecting over 100,000 records from iProperty Malaysia. Through data cleaning, transformation, and optimization techniques, the project demonstrates how high-performance computing concepts can improve large-scale data collection and processing workflows.

The final dataset provides a structured foundation for future analytics, business intelligence, and machine learning applications involving Malaysian property market data.

