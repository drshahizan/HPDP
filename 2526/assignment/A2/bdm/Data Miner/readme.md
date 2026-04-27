# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Muhammad Syahmi Faris Bin Rusli</td>
    <td>A23CS0138</td>
  </tr>
  <tr>
    <td>Ng Yu Hin</td>
    <td>A23CS0148</td>
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

In the era of smart cities and urban planning, massive datasets are generated daily by transportation networks. Analyzing New York City's taxi trips provides a perfect scenario to practice handling high-volume data that exceeds standard memory limits.

Our project focuses on mastering scalable big data techniques using tools such as **Pandas**, **Dask**, and **Polars**. We applied optimization strategies—including column projection, sampling, and parallel processing—to benchmark memory usage, execution time, CPU utilization, and throughput.

---

## 🚕 Dataset Overview

- **Name**: 🚕 NYC Yellow Taxi Trip Data 🗽
- **Source**: [Kaggle – Elemento](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data)  
- **Domain**: Transportation / Urban Analytics  
- **File Size**: ~1.99 GB (January 2015 subset)  
- **Shape**: ~12.7 Million rows × 19 columns  

### 📘 Description

This dataset contains records of yellow medallion taxicab trips in New York City. The data was collected and provided to the NYC Taxi and Limousine Commission (TLC). Each record includes fields capturing pick-up and drop-off dates/times, locations, distances, itemized fares, rate types, and payment types.

### 🔍 Key Features

- **Temporal**: Pickup and drop-off timestamps.
- **Geospatial**: Longitude and latitude coordinates for trip start and end.
- **Financial**: Fare amount, mta_tax, tip_amount, and total_amount.
- **Trip Metadata**: Passenger count, trip distance, and payment type.

---

## ⚙️ Strategies Applied

- **Strategy 1: Load Less Data** (Column Projection to minimize RAM footprint).
- **Strategy 2: Chunking** (Iterative processing of data segments to bypass RAM limits)
- **Strategy 3: Optimized Data Types** (Downcasting numeric bits and using Categorical encoding to shrink memory overhead)
- **Strategy 4: Sampling** (Probabilistic row skipping for efficient EDA).
- **Strategy 5: Parallel Processing** (Utilizing Dask for multi-core computation).
- **Benchmarking**: Custom performance tracking for CPU and Throughput.

---

## 📊 Library Benchmarking

We evaluated the performance of three popular data-processing libraries:

- **Pandas**: The industry standard for tabular data.
- **Dask**: For parallelizing tasks and handling "Big Data" that doesn't fit in RAM.
- **Polars**: A lightning-fast DataFrame library written in Rust.

Each was compared based on:
- Memory consumption (MB)
- Execution time (s)
- Average CPU usage (%)
- Processing throughput (records/second)

---

## 🎯 Conclusion

By comparing multiple tools and strategies, we gained insights into the trade-offs between processing speed and resource constraints. This project demonstrates how to move beyond basic data loading into professional-grade data engineering workflows, ensuring that large-scale datasets remain manageable and performant.
