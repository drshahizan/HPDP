# GRAB Big Data Analysis - Project Overview

## Project Information

| Item       | Details                                   |
| :--------- | :---------------------------------------- |
| Course     | SECP3133 High Performance Data Processing |
| Assignment | Assignment 2: Mastering Big Data Handling |
| Group Name | **Group DaPro**                         |
| Member 1   | **LAU YAN KAI (A23CS0098)**              |
| Member 2   | **CHEW CHIU XIAN (A23CS0061)**      |

---

## 📌 Project Overview
This repository contains our submission for Assignment 2: Mastering Big Data Handling. The objective of this project is to explore, apply, and evaluate various big data handling strategies using Python. We performed a comparative analysis between traditional in-memory processing (`Pandas`) and modern scalable data processing libraries (`Dask` and `Polars`) to process a 1.98 GB dataset effectively without exhausting system memory.

## 📊 Dataset Information
* **Name:** Grab Safe Driver Telematics
* **Source:** [Kaggle](https://www.kaggle.com/datasets/vancharmlab/grabai)
* **Size:** 1.98 GB (10 Partitioned CSV files)
* **Dimensions:** 16,135,561 rows × 11 columns
* **Description:** Contains high-frequency telematics sensor readings (accelerometer, gyroscope, GPS speed, bearing, accuracy) from Grab drivers' mobile devices.

## 🛠️ Tools & Libraries Evaluated

| Library    | Details                                                                    |
| :--------- | :------------------------------------------------------------------------- |
| Pandas     | Used as the baseline (single-threaded, eager execution).                   |
| Dask       | Used for out-of-core, parallel distributed processing.                     |
| Polars     | Used for high-performance, vectorized lazy evaluation via its Rust backend |

## 🚀 Key Big Data Strategies Implemented
To prevent Out-Of-Memory (OOM) kernel crashes when dealing with the massive dataset, the following optimization strategies were applied:
* **Loading Less Data:** Filtering unneeded columns utilizing the `usecols` parameter.
* **Chunking:** Iterating through data in smaller blocks (`chunksize=100000`) to manage peak RAM usage.
* **Data Type Optimization:** Downcasting 64-bit numeric types to 32-bit floats/integers to immediately reduce memory footprint by ~50%.
* **Sampling:** Implementing randomized row-skipping during the load phase for lightweight Exploratory Data Analysis (EDA).
* **Parallel Processing & Lazy Evaluation:** Utilizing Polars' and Dask's query planners to simultaneously read and aggregate multiple files across available CPU cores.

## 📂 Repository Structure
* `readme.md`: This document, providing a high-level overview of the project.
* `big_data.md`: The comprehensive final report detailing our methodology, comparative analysis, and reflections on pipeline scalability.
* `big_data.ipynb`: The fully executed Jupyter Notebook (Google Colab) containing all source code, profiling metrics, and data visualizations.
* `images/`: Folder containing the exported charts generated during our comparative analysis (Execution Time and Peak Memory Usage).

## 🏆 Summary of Findings
Our comparative analysis revealed that **Polars** is the most efficient tool for single-machine data pipelines at this scale (~2 GB). By leveraging lazy evaluation and a Rust-optimized backend, Polars processed the entire dataset in just **2.67 seconds**, compared to Dask (10.93s) and Pandas (12.15s).
Furthermore, we mapped out a scalability framework concluding that while Polars/Dask are ideal for the 1 GB – 100 GB range, transitioning to distributed cloud-native ecosystems (e.g., Apache Spark, Google BigQuery) is strictly necessary for enterprise-scale data (> 100 GB).

## ⚙️ How to Run the Code
1. Open `big_data.ipynb` in Google Colab or your local Jupyter environment.
2. Ensure you have the dataset downloaded and the path configured correctly in the notebook (e.g., mapped to your Google Drive).
3. Install required profiling and processing dependencies if running locally:
   ```
   bash
   pip install pandas dask polars matplotlib seaborn memory_profiler
   ```
4. Click "Run All" to execute the pipeline from data inspection to comparative analysis plotting.
