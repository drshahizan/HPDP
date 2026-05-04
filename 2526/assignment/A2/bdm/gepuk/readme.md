# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>MUHAMMAD MUKHRITZ AL IMAN BIN MOHD RAFFI</td>
    <td>A23CS0250</td>
  </tr>
  <tr>
    <td>MUHAMMAD NAIM BIN ABDULLAH</td>
    <td>A23CS0134</td>
  </tr>
</table>

---

## 🗂️ Project Files

| File Name | Description | Link |
|---|---|---|
| `big_data.md` | Markdown file with detailed write-up for Assignment 2 | [![Open](https://img.shields.io/badge/View-Markdown-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb` | Colab notebook exploring various data loading and optimization techniques | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data .ipynb) |

---

## 📖 Introduction

In the era of modern aviation and smart transportation systems, millions of flight records are generated daily by airlines across the United States. Analyzing departure delays and cancellations provides a perfect real-world scenario to practice handling high-volume data that exceeds standard memory limits.

Our project focuses on mastering scalable big data techniques using tools such as **Pandas**, **Dask**, and **Polars**. We applied optimization strategies which include the column projection, data type downcasting, chunking, sampling, and parallel processing to benchmark memory usage, execution time, CPU utilization, and throughput across the full 6.5 million row dataset.

---

## ✈️ Dataset Overview

- **Name**: ✈️ 2019 Airline Delays and Cancellations 🛫
- **Source**: [Kaggle – threnjen](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations)
- **Domain**: Transportation / Aviation
- **File Size**: ~754 MB (Zipped) / 1.3+ GB (Uncompressed CSV)
- **Shape**: ~6.5 Million rows × 26 columns

### 📘 Description

This dataset contains records of domestic U.S. airline flights throughout the year 2019, sourced from the Bureau of Transportation Statistics (BTS). Each record captures departure delay indicators, weather conditions, flight schedules, and carrier information — making it an ideal dataset for delay prediction and operational analysis.

### 🔍 Key Features

- **Temporal**: Month, day of week, and departure time blocks.
- **Flight Info**: Carrier name, departing airport, segment number, and distance group.
- **Delay Indicator**: Binary departure delay flag (`DEP_DEL15`) for delays ≥ 15 minutes.
- **Weather**: Precipitation, snowfall, and maximum temperature at departure location.
- **Geospatial**: Latitude and longitude coordinates of the departing airport.

---

## ⚙️ Strategies Applied

- **Strategy 1: Load Less Data** — Column projection using `usecols` to minimize RAM footprint.
- **Strategy 2: Chunking** — Iterative processing of 100,000-row data segments to bypass RAM limits.
- **Strategy 3: Optimized Data Types** — Downcasting numeric columns (`int8`, `float32`) and applying categorical encoding to shrink memory overhead.
- **Strategy 4: Sampling** — Probabilistic row skipping to load a random 5% sample for efficient EDA.
- **Strategy 5: Parallel Processing** — Utilizing Dask for out-of-core, multi-core computation on the full dataset.
- **Benchmarking** — Custom `track_performance` function using `psutil` to capture execution time, memory, CPU, and throughput per strategy.

---

## 📊 Library Benchmarking

We evaluated the performance of three popular data-processing libraries on a full load of the 1.3+ GB dataset:

- **Pandas** — The industry standard for tabular data.
- **Dask** — For parallelizing tasks and handling data that doesn't fit in RAM.
- **Polars** — A lightning-fast DataFrame library written in Rust using the Apache Arrow framework.

Each library was compared based on:

- Memory consumption (MB)
- Execution time (s)
- Average CPU usage (%)
- Processing throughput (MB/s)

---

## 🎯 Conclusion

By comparing multiple tools and strategies against the 6.5 million row Airline Delays dataset, we gained clear insights into the trade-offs between processing speed and resource constraints. Polars consistently outperformed both Pandas and Dask in speed, while Dask proved most resilient against memory overflow. This project demonstrates how to move beyond basic data loading into professional-grade data engineering workflows, ensuring that large-scale datasets remain manageable and performant on standard hardware.
