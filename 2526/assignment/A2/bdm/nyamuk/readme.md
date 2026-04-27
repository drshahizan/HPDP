# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Nabil Aflah Boo Binti Mohd Yosuf Boo Yong Chong</td>
    <td>A23CS0252</td>
  </tr>
  <tr>
    <td>Yasmin Batrisyia Binti Zahiruddin</td>
    <td>A23CS0201</td>
  </tr>
</table>

---

## 🗂️ Project Files

| File Name        | Description                                                               | Link |
|-----------------|---------------------------------------------------------------------------|------|
| `big_data.md`   | Markdown file with detailed write-up for Assignment 2                     | [![Open](https://img.shields.io/badge/View-Markdown-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb`| Colab notebook exploring various data loading and optimization techniques  | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data.ipynb) |

---

## 📖 Introduction

In today’s data driven urban environments, large volumes of information are being generated continuously through public report systems, administrative processes, and community interactions in big cities. To handle and analyze such large-scale data, it requires advanced tools and techniques to process beyond typical memory constraints.

This project aims to develop skills in scalable big data processing using tools like Pandas, Dask, and Polars. We applied various optimisation methods to efficiently load and process a large real-world crime dataset, followed by performance benchmarking to evaluate memory usage, execution time, CPU utilisation, and overall processing efficiency.

---

## 👮 Dataset Overview

- **Name**: Los Angeles Crime Data 2020-2026
- **Source**: [Kaggle – aliafzal9323](https://www.kaggle.com/datasets/aliafzal9323/los-angeles-crime-data-2020-2026)
- **Domain**: Criminal
- **File Size**: 12.63 GB
- **Shape**: 5,348,822 rows × 44 columns

### 📘 Description

This dataset contains comprehensive records of crime incidents that are reported in Los Angeles from 2020 to 2026, sourced from open public data platforms. It captures details of reported incidents, responsible agencies, types of reported problems, and so on. This dataset provides valuable insights into crime patterns, reporting behaviours, and regional distribution of incidents which makes it well suited for time-series analysis, geospatial mapping, and categorical crime trend analysis.

### 🔍 Key Features

- Temporal details: created date and time of reported incidents
- Agency information: department responsible for handling cases
- Incidents categories: type of problem or complaint reported
- Case status: current progress (in progress, closed)
- Regional data: areas of where the incident took placed
- Geolocation data: latitude and longitude coordinates for mapping

### ⚠️ Notes

- Some records may contain missing or null values, especially in location or status fields.
- Data entries may show inconsistencies across agencies or reporting formats.
- Certain cases might be categorised under general labels.
- The dataset is best for time-series, categorical, and geospatial analysis.

---

## ⚙️ Strategies Used

- **Strategy 1: Load Less Data** (filter using usecols to reduce memory usage)
- **Strategy 2: Chunking** (handle large data in smaller batches)
- **Strategy 3: Data Type Optimization** (downcasting numeric types and converting strings to categories to save memory)
- **Strategy 4: Sampling** (use smaller subset of data for faster testing and analysis)
- **Strategy 5: Parallel Processing with Scalable Libraries** (use Dask and Polars to speed up process with multi-core execution)

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

This project demonstrates how large-scale crime data can be efficiently processed using scalable big data techniques. By applying the strategies, we are able to significantly improve the memory efficiency and processing performance. The comparison of different libraries between Pandas, Dask, and Polars also demonstrates that we need to choose the appropriate tools according to dataset size and computational requirements. Overall, this project shows that data processing optimization methods enable efficient handling of actual large datasets in a real-world environment.
