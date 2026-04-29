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

In today’s data driven urban environments, large volumes of information are being generated continuously through public report systems, administrative processes, and community interactions in big cities. Advanced tools and techniques are required to handle and anlyze such large-scale of dataset to process beyond typical memory constraints.

This project aims to develop skills in scalable big data processing using tools like Pandas, Dask, and Polars. We applied various optimisation methods to efficiently load and process a large real-world housing dataset, followed by performance benchmarking to evaluate memory usage, execution time, CPU utilisation, and overall processing efficiency.

---

## 👮 Dataset Overview

- **Name**: UK Housing Prices Paid
- **Source**: [Kaggle-hm-land-registry](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid)
- **Domain**: Housing
- **File Size**: 2.41 GB
- **Shape**: 22,489,348 rows × 11 columns

### 📘 Description

This dataset contains comprehensive records of all registered property sales in England and Wales that were sold for full market value. It captures details of reported transactions, legal ownership types, property classifications, and geographical markers. This dataset provide a valuable insights into economic trends, purchasing behaviours, and regional distribution of property values which makes it well-suited for time-series analysis, geospatial mapping, and categorical market trend analysis.

### 🔍 Key Features

- Price: The total sales amount that is essential for valuation and economic modeling.
- Date of Transfer: The specific transaction date, which is ideal for longitudinal time-series analysis.
- Property Type: Classification (Detached, Semi, Terraced, Flat) for comparing market sectors
- Old/New Build: A marker for new construction versus established residential stock.
- Tenure: Indicates ownership type (Freehold/Leasehold), reflecting legal property status.
- Address Hierarchy: Granular location data from Postcode to Country.

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
