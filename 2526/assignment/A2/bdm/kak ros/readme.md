# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Harini A/P Sangaran</td>
    <td>A23CS0081</td>
  </tr>
  <tr>
    <td>Nurul Adriana Binti Kamal Jefri</td>
    <td>A23CS0258</td>
  </tr>
</table>

---

## 🗂️ Project Files

| File Name                     | Description                                                                    | Link |
|------------------------------|--------------------------------------------------------------------------------|------|
| `big_data.md`                | Markdown file with detailed write-up for Assignment 2                          | [![Open](https://img.shields.io/badge/View-Markdown-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb`             | Colab notebook exploring various data loading and optimization techniques      | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data.ipynb) |

---

## 📖 Introduction

In the modern era of global transportation and logistics, the aviation industry generates massive amounts of telemetry and scheduling data every single day. Efficiently handling this scale of data requires specialized tools and techniques that go beyond standard memory limits.

Our project focuses on mastering scalable big data techniques using tools such as Pandas, Dask, and Polars. We applied various optimization strategies to load and process a massive real-world flight dataset, then conducted performance benchmarking to compare memory usage, execution time, and processing efficiency.

---

## 🎵 Dataset Overview

- **Name**: Airline Delay and Cancellation Data, 2009 - 2018  
- **Source**: [Kaggle](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018?select=2009.csv)  
- **Domain**: Transportation  
- **File Size**: 7.62 GB  
- **Shape**: 61,556,964 rows × 28 columns  

### 📘 Description

This dataset is a comprehensive compilation of flight tracking records collected over a ten-year period. It contains millions of flight logs detailing domestic operations across the United States. Each record includes;

- cheduling metadata (airlines, flight numbers, origin, and destination airports)  
- operational timestamps (scheduled vs. actual departure and arrival times)  
- specific delay categorizations  
- And more...

### ⚠️ Notes

- Cancelled or diverted flights will naturally be missing arrival times and airborne durations.  
- Specific delay reason columns (e.g., Weather Delay, Carrier Delay) contain null values if the flight departed on time. 
- The sheer size of the uncompressed data exceeds standard RAM capacities, requiring strategic loading methods.  

### 🔍 Key Features

- Flight Metadata: Date, Airline Carrier Code, Flight Number, Tail Number.  
- Location Data: Origin Airport, Destination Airport, Distance.  
- Time Metrics: Scheduled Departure/Arrival, Actual Departure/Arrival, Taxi In/Out times. 
- Performance Attributes: Departure Delay, Arrival Delay, Cancellation Codes, and specific Delay Breakdown Categories.  

---

## ⚙️ Techniques Used

- Selective data loading: Utilizing usecols to extract only essential features.  
- Chunk-based reading: Iterating through the dataset in manageable portions.  
- Data type downcasting: Converting high-memory defaults (like int64 and object) to optimized types (like int16 and category).  
- Sampling methods: Utilizing randomized subsets for rapid prototyping and exploratory analysis. 
- Parallel processing: Distributing computational workloads across multiple cores using Dask and Polars.   

---

## 📊 Library Benchmarking

We evaluated the performance of three popular data-processing libraries:

- **Pandas**
- **Dask**
- **Polars**

Each was tested and compared based on:

- Memory consumption  
- Execution time  
- Average CPU usage  
- Processing throughput (records/second)  

---

## 🎯 Conclusion

This project allowed us to explore and apply advanced data-handling techniques on a high-volume dataset in a practical scenario. By comparing multiple tools and approaches, we gained measurable insights into the trade-offs between simplicity, execution speed, and memory optimization in large-scale data processing.

Through this assignment, we have taken a step closer to understanding how professional data engineers manage massive datasets in production environments, and we are better equipped to scale these solutions to even larger infrastructure in the future.
