# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>DHESHIEGHAN A/L SARAVANA MOORTHY</td>
    <td>A23CS0072</td>
  </tr>
  <tr>
    <td>PRAVINRAJ A/L SIVABATHI</td>
    <td>A23CS0171</td>
  </tr>
</table>

---

## 🗂️ Project Files

| File Name                | Description                                                                    | Link |
|--------------------------|--------------------------------------------------------------------------------|------|
| `big_data.md`            | Markdown file with detailed write-up for Assignment 2                          | [![Open](https://img.shields.io/badge/View-Markdown-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb`         | Colab notebook exploring various data loading and optimization techniques       | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data.ipynb) |

---

## 📖 Introduction

In the modern aviation industry, massive amounts of data are generated daily from flight operations, including departure schedules, arrival times, delays, cancellations, and airline performance metrics. Handling such large-scale datasets requires efficient data processing techniques to overcome memory and computational limitations.

Our project focuses on mastering scalable big data handling techniques using the **Carrier On-Time Performance Dataset**. Since the dataset is large and contains over 100 columns, traditional data loading approaches can be inefficient.

To address this, we applied optimization strategies using **Pandas**, **Dask**, and **Polars**. These include column projection, chunking, sampling, optimized data types, and parallel processing. We also benchmarked performance based on memory usage, execution time, CPU utilization, and throughput.

---

## ✈️ Dataset Overview

- **Name**: ✈️ Carrier On-Time Performance Dataset  
- **Source**: [Kaggle](https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset)  
- **Domain**: Airline / Transportation Analytics  
- **File Size**: 841 MB
- **Shape**: ~2 Million rows × 109 columns  

---

## 📘 Description

This dataset contains detailed records of airline flight operations in the United States. Each row represents a single flight and includes information such as airline carrier, origin and destination airports, scheduled and actual departure/arrival times, delays, cancellations, and diversion details.

The dataset is widely used for analyzing airline performance, identifying delay patterns, evaluating operational efficiency, and understanding factors affecting flight punctuality.

---

## 🔍 Key Features

- **Flight Information**: Airline carrier, flight number, tail number  
- **Temporal Data**: Flight date, scheduled and actual departure/arrival times  
- **Route Data**: Origin and destination airports and cities  
- **Delay Metrics**: Departure delay, arrival delay, and delay categories (weather, carrier, NAS, etc.)  
- **Flight Status**: Cancellation and diversion indicators  
- **Operational Metrics**: Distance, airtime, elapsed time  

---

## ⚙️ Strategies Applied

- **Strategy 1: Load Less Data** (Column projection to reduce memory usage by selecting only relevant columns)  
- **Strategy 2: Chunking** (Processing the dataset in smaller parts to avoid memory overflow)  
- **Strategy 3: Optimized Data Types** (Downcasting numeric data and converting strings to categorical types)  
- **Strategy 4: Sampling** (Using a subset of data for faster exploratory analysis)  
- **Strategy 5: Parallel Processing** (Using Dask for multi-core computation on large datasets)  
- **Benchmarking**: Measuring memory usage, execution time, CPU usage, and throughput  

---

## 📊 Library Benchmarking

We evaluated the performance of three popular data-processing libraries:

- **Pandas**: The industry standard for structured data analysis  
- **Dask**: Designed for parallel computing and large-scale data processing  
- **Polars**: A high-performance DataFrame library optimized for speed and memory efficiency  

Each was compared based on:
- Memory consumption (MB)  
- Execution time (seconds)  
- Average CPU usage (%)  
- Processing throughput (records per second)  

---

## 🎯 Conclusion

By applying multiple optimization strategies, we successfully handled a large-scale airline dataset efficiently. This project highlights the importance of choosing the right tools and techniques when working with big data.

Pandas is suitable for smaller datasets, while Dask enables parallel processing for larger datasets that exceed memory limits. Polars offers superior performance in terms of speed and memory efficiency.

Overall, this project demonstrates how modern data engineering techniques can significantly improve performance and scalability when dealing with real-world big data scenarios in the transportation domain.
