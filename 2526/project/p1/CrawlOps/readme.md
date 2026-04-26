# Project 1: Optimizing High-Performance Data Processing for Large-Scale Web Scrapers

**Course:** SECP3133 - High Performance Data Processing

**University:** Universiti Teknologi Malaysia (UTM)

**Faculty:** Faculty of Computing

**Group Name:** CrawlOps

**Section:** 01

**Lecturer:** ASSOC. PROF. DR. MOHD SHAHIZAN BIN OΤΗΜΑΝ

**Submission Date:** May 16, 2025

**Group Members:**
1.  GOH JIALE (A22EA0043)
2.  KOH LI HUI (A22EC0059)
3.  MAISARAH BINTI RIZAL (A22EC0192)
4.  YONG WERN JIE (A22EC0121)

---

## 1. Project Overview

This project explores the application of high-performance computing (HPC) techniques to optimize a data processing pipeline involving large-scale web-scraped data. The primary objective was to design and develop a system to:
1.  Scrape a substantial dataset (over 100,000 records) of car listings from a Malaysian e-commerce website (Mudah.my).
2.  Clean and preprocess the raw data into a structured format.
3.  Store the cleaned data in a Supabase (PostgreSQL) database.
4.  Implement and execute five distinct analytical queries on this dataset.
5.  Compare the performance of four different data processing approaches for these queries:
    * Sequential Processing (Baseline using Pandas)
    * Multithreading (using Python's `concurrent.futures` with Pandas)
    * Multiprocessing (using `joblib` with Pandas)
    * Distributed Computing (using Apache Spark/`pyspark`)
6.  Evaluate these techniques based on execution time, CPU usage, memory usage, and throughput.

This project provided hands-on experience in web scraping, data cleaning, database management, and applying various optimization strategies to handle data-intensive tasks efficiently.

## 2. System Architecture

The project follows a multi-stage data pipeline:

1.  **Data Acquisition (Web Scraping):**
    * Car listing data was scraped from **Mudah.my** using **Selenium** for browser automation and **BeautifulSoup** for HTML parsing.
    * Techniques included dynamic URL management, pagination handling, rate-limiting (1.5s delay), and error handling with retries.
    * Initial cleaning (e.g., price conversion) was performed during scraping.
    * Raw scraped data was staged in a Supabase table (`cars_before_clean`).
2.  **Detailed Data Cleaning & Preparation:**
    * Data from `cars_before_clean` was further processed using **Pandas**.
    * Tasks included mileage normalization, engine capacity conversion, handling missing values, and duplicate removal.
3.  **Cleaned Data Storage:**
    * The fully cleaned and validated dataset (115,001 records after cleaning the initial 121,520 scraped records) was stored in a Supabase table (`cars_clean`).
4.  **Data Analysis & Optimization Implementations:**
    * Five analytical queries were performed on the `cars_clean` dataset using the four processing approaches mentioned above.
    * All approaches (except Spark, which used its own DataFrame) involved fetching data globally into a Pandas DataFrame before processing.
5.  **Performance Evaluation:**
    * Metrics were collected for each query under each processing strategy to compare their effectiveness.

**(Refer to the `HPDP Project 1.pdf` report in this repository for a detailed architectural diagram in Section 2.1, Page 7.)**
![web crawler diagram](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/CrawlOps/img/SystemArchitecture.png)

## 3. Tools and Frameworks Used

* **Python:** Primary programming language.
* **Selenium & BeautifulSoup4:** For web scraping.
* **Supabase (`supabase-py`):** Cloud PostgreSQL database for data storage.
* **Pandas:** For data manipulation, cleaning, and core logic in Sequential, Multithreading, and Multiprocessing approaches.
* **NumPy:** For numerical operations, including assistance in creating balanced data chunks for multiprocessing.
* **`concurrent.futures.ThreadPoolExecutor`:** For implementing the multithreading approach.
* **`joblib`:** For implementing the multiprocessing approach.
* **Apache Spark (`pyspark`):** For the distributed computing approach (run in local mode).
* **`psutil`:** For collecting system CPU and memory usage metrics.
* **`memory_profiler`:** Used for memory profiling in the Spark context.
* **`PrettyTable`:** For formatting console output in some scripts.
* **Visual Studio Code:** Development environment for the web scraping component.
* **Google Colab:** Development environment for data processing and analysis scripts.

## 4. Repository Structure

This repository contains all deliverables for the project:

- **`/data`**:
  - `cleaned_Data.csv`: The final cleaned dataset used for analysis (115,001 records).
  - `raw_data.csv`: The raw dataset collected before cleaning.

- **`/img`**:
  - `SystemArchitecture.png`: Visual representation of the system architecture.
  - `Throughput.png`: Graph showing throughput evaluation.
  - `cpuUsage.png`: CPU usage comparison chart.
  - `memoryUsage.png`: Memory usage comparison chart.
  - `querytime.png`: Query execution time comparison chart.

- **`/p1`**: Scripts and notebooks related to the main data pipeline and optimization methods.
  - `mainCrawler.py`: Web scraping script for collecting raw data.
  - `clean_data.ipynb`: Data cleaning script.
  - `before_optimized_pipeline.ipynb`: Baseline sequential query processing.
  - `multithreaded_supabase_queries.ipynb`: Multithreading-based query processing.
  - `optimized_pipeline_multiprocessing.ipynb`: Multiprocessing optimization using `joblib`.
  - `optimize_pipeline_distributed_computing.ipynb`: Distributed computing optimization using Spark.

- **`/p2`**: Evaluation results and comparative analysis.
  - `Before_Optimization_Sequential.csv`: Output from the baseline sequential query processing.
  - `After_Optimization_Multithreading.csv`: Output from multithreaded query processing.
  - `After_Optimization_Multiprocessing.csv`: Output from multiprocessing approach.
  - `After_Optimization_Distributed_Computing.csv`: Output from distributed (Spark) processing.
  - `evaluation_charts.pdf`: Charts and comparative graphs summarizing performance metrics.

- **`/report`**:
  - `HPDP Project 1 - Group CrawlOps report.pdf`: Final project report including background, methodology, results, and conclusions.
  - `Presentation Slide.pdf`: Slide deck used during the project presentation.

- `README.md`: This file.

*(Please adjust the file paths and names above to match your actual repository structure.)*

## 5. Key Findings & Performance

The project evaluated four different processing strategies. Our performance analysis (detailed in Section 6 of the report) showed the following ranking for overall efficiency on our specific dataset and queries:

1.  **Multithreading (`concurrent.futures` with Pandas)**
2.  **Sequential Processing (Baseline with Pandas)**
3.  **Multiprocessing (`joblib` with Pandas)**
4.  **Distributed Computing (Apache Spark)**

Multithreading demonstrated the best performance, significantly reducing query execution times and achieving the highest throughput. This was attributed to its effective overlap of I/O-bound operations (initially) and efficient handling of concurrent Pandas tasks on the pre-fetched dataset, where many Pandas operations release the Python Global Interpreter Lock (GIL).

Distributed computing (Spark), while powerful for very large datasets, incurred overhead that made it less performant for our dataset size (approx. 115,000 records) compared to single-machine concurrent approaches.

*(Refer to Section 6 "Performance Evaluation" and Section 8.1 "Summary of findings" in the `HPDP Project 1.pdf` for detailed metrics, charts, and discussion.)*

![Query Time Diagram](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/CrawlOps/img/querytime.png)

![Memory Usage Diagram](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/CrawlOps/img/memoryUsage.png)

![CPU Usage Diagram](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/CrawlOps/img/cpuUsage.png)

![Throughput Diagram](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/CrawlOps/img/Throughput.png)

## 6. Challenges and Limitations

Key challenges included:
* Ensuring web scraping reliability against website layout changes.
* Hardware limitations during extensive scraping sessions.
* Managing Supabase API rate limits and latencies with a growing dataset.
* Achieving expected performance gains consistently across all optimization techniques due to factors like Python's GIL and the overhead of more complex frameworks on moderately sized data.

Limitations include the scalability constraints of Supabase for high-throughput analytics on very large datasets (beyond what was tested) and the manual intervention required for scraping error recovery.

*(Refer to Section 7 "Challenges & Limitations" in the `HPDP Project 1.pdf` for a full discussion.)*

## 7. Conclusion

This project successfully demonstrated the development of a web scraping and data processing pipeline, alongside a comparative evaluation of different optimization techniques. The findings underscore that the choice of optimization strategy is highly dependent on the specific workload, data size, and system architecture, with multithreading proving most effective for our particular use case and dataset scale.

---
