# SECP3133 Project 1: Optimizing High-Performance Data Processing for Large-Scale Web Crawlers

Welcome to our group's repository for the High Performance Data Processing project.

## Group Information
* **Members:**
  * CHOH JING YI - A23CS0296
  * TAN ZHI MING - A23CS0189
  * LEE YIN SHEN - A23CS0236
  * BRENDAN CHIA YAN FEI - A23CS0211

## 📌 Project Overview

This project focuses on designing, developing, and optimizing a high-performance web crawler for large-scale data extraction from Mudah.my, a Malaysian online marketplace. The selected domain for this project is property listings for sale.

The main objective is to collect at least 100,000 structured records, clean and process the dataset, apply high-performance computing techniques, and evaluate the performance improvement between a baseline crawler and an optimized crawler.

## 🎯 Project Objectives

- Build a web crawler to extract property listing data from Mudah.my.
- Collect more than 100,000 structured property records.
- Store the extracted data in CSV format.
- Clean and process the raw dataset.
- Apply high-performance optimization techniques.
- Compare baseline and optimized crawler performance.
- Generate charts for performance evaluation and dataset analysis.

## 🌐 Target Website

- Website: Mudah.my
- Category: Properties for Sale
- Data Source Type: Public property listing data
- Final Dataset Size: 101,403 cleaned records

## 📊 Dataset Description

The cleaned dataset contains 13 columns:

| Column        | Description                               |
| ------------- | ----------------------------------------- |
| Property_ID   | Unique identifier of the property listing |
| Title         | Property listing title                    |
| Price_RM      | Property price in Malaysian Ringgit       |
| Region        | Malaysian region/state                    |
| Subarea       | Specific area or district                 |
| Property_Type | Type of property                          |
| Title_Type    | Property title type                       |
| Size_sqft     | Property size in square feet              |
| Bedrooms      | Number of bedrooms                        |
| Bathrooms     | Number of bathrooms                       |
| Agent_Firm    | Agent firm or private seller              |
| Listing_URL   | URL of the listing                        |
| Scraped_At    | Timestamp when the data was scraped       |

## 🧹 Data Cleaning Summary

| Cleaning Step                      |  Result |
| ---------------------------------- | ------: |
| Initial raw rows                   | 120,257 |
| Duplicate Property_ID rows removed |  13,409 |
| Invalid price/size rows removed    |       1 |
| Unreasonable value rows removed    |   5,444 |
| Final cleaned rows                 | 101,403 |
| Final columns                      |      13 |

The final cleaned dataset contains 101,403 unique property records, which satisfies the project requirement of at least 100,000 structured records.

## ⚙️ Tools and Technologies

| Tool / Library | Purpose                        |
| -------------- | ------------------------------ |
| Python         | Main programming language      |
| requests       | Baseline sequential crawler    |
| aiohttp        | Asynchronous optimized crawler |
| asyncio        | Concurrent crawling            |
| pandas         | Data cleaning and analysis     |
| matplotlib     | Chart generation               |
| psutil         | CPU and memory tracking        |
| VS Code        | Development environment        |
| GitHub         | Source code submission         |

## 🚀 Optimization Techniques

This project applied several optimization techniques:

### 1. Asynchronous Crawling

The optimized crawler uses `aiohttp` and `asyncio` to send multiple HTTP requests concurrently. This improves crawling speed compared to the baseline sequential crawler.

### 2. Concurrency Control

A semaphore was used to limit the number of concurrent requests. This prevents excessive requests from being sent at the same time and helps reduce the risk of overloading the website.

### 3. Search Space Partitioning

The large-scale crawler partitions the crawling process by region and property type. This allows the crawler to collect more records beyond basic page-based crawling.

### 4. Batch Data Writing

The crawler writes extracted records into CSV files in batches, reducing unnecessary file operations.

## 📈 Performance Evaluation

A fair performance comparison was conducted using the same workload:

- Pages crawled: 50
- Records collected: 2,000

| Method              | Pages Crawled | Records Collected | Total Time Seconds | Throughput Records/Second | Memory Usage MB | CPU Usage % |
| ------------------- | ------------: | ----------------: | -----------------: | ------------------------: | --------------: | ----------: |
| Baseline Sequential |            50 |             2,000 |              91.24 |                     21.92 |           38.36 |         1.5 |
| Optimized Async     |            50 |             2,000 |               7.50 |                    266.60 |           39.67 |         5.3 |

## ⚡ Performance Improvement

The optimized async crawler achieved:

- Speedup: 12.17× faster
- Throughput improvement: 12.16× higher

This shows that asynchronous crawling significantly improves the efficiency of the web crawler.

## 📊 Generated Charts

### Performance Charts

- Total processing time comparison
- Throughput comparison
- Memory usage comparison
- CPU usage comparison

### Dataset Analysis Charts

- Top 10 regions by number of property listings
- Top 10 property types
- Property price distribution
- Property size distribution

## 📁 Project Structure

```text
Web-Crawler-Project/
│
├── data/
│   ├── raw/
│   │   ├── baseline_mudah_properties.csv
│   │   ├── optimized_mudah_properties.csv
│   │   ├── mudah_properties_large_raw.csv
│   │   └── mudah_properties_partitioned_raw.csv
│   │
│   ├── processed/
│   │   ├── mudah_properties_cleaned.csv
│   │   ├── cleaning_summary.txt
│   │   └── dataset_analysis_summary.txt
│   │
│   └── performance/
│       └── performance_results.csv
│
├── images/
│   ├── total_time_comparison.png
│   ├── throughput_comparison.png
│   ├── memory_usage_comparison.png
│   ├── cpu_usage_comparison.png
│   ├── top_regions_by_listings.png
│   ├── top_property_types.png
│   ├── price_distribution.png
│   └── size_distribution.png
│
├── scripts/
│   ├── 01_test_connection.py
│   ├── 02_baseline_crawler.py
│   ├── 03_optimized_async_crawler.py
│   ├── 04_generate_performance_charts.py
│   ├── 05_large_scale_async_crawler.py
│   ├── 06_large_scale_partitioned_crawler.py
│   ├── 07_clean_large_dataset.py
│   └── 08_generate_dataset_charts.py
│
├── report/
├── README.md
└── requirements.txt
```
