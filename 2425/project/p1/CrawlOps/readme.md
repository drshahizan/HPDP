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

* **`/Report`**:
    * `HPDP Project 1.pdf`: The final project report detailing the background, methodology, results, and conclusions.
* **`/Code`**:
    * `Web_Scraping/`: Contains the script(s) used for scraping data from Mudah.my (e.g., `webScrape.py`). *(Adjust folder/file name as per your actual structure)*
    * `Data_Cleaning/`: Contains the script(s) for cleaning the raw scraped data (e.g., `Data_Cleaning_Script.py` or the initial part of your `All Python code.docx`). *(Adjust folder/file name)*
    * `Sequential_Processing/`: Script for the baseline sequential query processing (e.g., `Sequential_Pandas.ipynb` or `.py`). *(Adjust folder/file name)*
    * `Multithreading/`: Script for the multithreaded query processing (e.g., `Multithreading_Pandas.ipynb` or `.py` - your part). *(Adjust folder/file name)*
    * `Multiprocessing/`: Script for the multiprocessing approach using `joblib` (e.g., `Multiprocessing_Joblib.ipynb` or `.py`). *(Adjust folder/file name)*
    * `Distributed_Computing_Spark/`: Script for the Spark-based query processing (e.g., `Spark_PySpark.ipynb` or `.py`). *(Adjust folder/file name)*
* **`/Dataset`**:
    * `raw_car_data.csv` (or `.json`): The raw dataset collected before cleaning. *(Link or actual file - adjust as needed)*
    * `cleaned_car_data.csv` (or `.json`): The final cleaned dataset (115,001 records) used for analysis. *(Link or actual file - adjust as needed)*
* **`/Presentation`**:
    * `Project_Presentation_Slides.pptx` (or `.pdf`): Slides used for the project presentation. *(Adjust file name)*
* `README.md`: This file.

*(Please adjust the file paths and names above to match your actual repository structure.)*

## 5. How to Run the Code

*(This section should be filled in by your team with specific instructions for each script if they are intended to be runnable by others. Consider including:)*
* Prerequisites (e.g., Python version, Java for Spark).
* How to install dependencies (e.g., `pip install -r requirements.txt`).
* Instructions for setting up Supabase credentials (e.g., updating placeholder variables in the scripts).
* Order of execution if scripts depend on each other (e.g., run cleaning before analysis).
* Example commands to run each script.

**Example for Multithreading Script:**
1.  Ensure Python 3.x is installed along with `pandas`, `supabase`, `psutil`.
2.  Update `SUPABASE_URL` and `SUPABASE_KEY` placeholders in the script (`Multithreading/Multithreading_Pandas.py`).
3.  Run the script from the terminal: `python Multithreading/Multithreading_Pandas.py`

## 6. Key Findings & Performance

The project evaluated four different processing strategies. Our performance analysis (detailed in Section 6 of the report) showed the following ranking for overall efficiency on our specific dataset and queries:

1.  **Multithreading (`concurrent.futures` with Pandas)**
2.  **Sequential Processing (Baseline with Pandas)**
3.  **Multiprocessing (`joblib` with Pandas)**
4.  **Distributed Computing (Apache Spark)**

Multithreading demonstrated the best performance, significantly reducing query execution times and achieving the highest throughput. This was attributed to its effective overlap of I/O-bound operations (initially) and efficient handling of concurrent Pandas tasks on the pre-fetched dataset, where many Pandas operations release the Python Global Interpreter Lock (GIL).

Distributed computing (Spark), while powerful for very large datasets, incurred overhead that made it less performant for our dataset size (approx. 115,000 records) compared to single-machine concurrent approaches.

*(Refer to Section 6 "Performance Evaluation" and Section 8.1 "Summary of findings" in the `HPDP Project 1.pdf` for detailed metrics, charts, and discussion.)*

## 7. Challenges and Limitations

Key challenges included:
* Ensuring web scraping reliability against website layout changes.
* Hardware limitations during extensive scraping sessions.
* Managing Supabase API rate limits and latencies with a growing dataset.
* Achieving expected performance gains consistently across all optimization techniques due to factors like Python's GIL and the overhead of more complex frameworks on moderately sized data.

Limitations include the scalability constraints of Supabase for high-throughput analytics on very large datasets (beyond what was tested) and the manual intervention required for scraping error recovery.

*(Refer to Section 7 "Challenges & Limitations" in the `HPDP Project 1.pdf` for a full discussion.)*

## 8. Conclusion

This project successfully demonstrated the development of a web scraping and data processing pipeline, alongside a comparative evaluation of different optimization techniques. The findings underscore that the choice of optimization strategy is highly dependent on the specific workload, data size, and system architecture, with multithreading proving most effective for our particular use case and dataset scale.

---
