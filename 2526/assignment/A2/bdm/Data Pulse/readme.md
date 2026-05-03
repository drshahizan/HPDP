# Assignment 2: Mastering Big Data Handling

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

## Project Files

| File Name        | Description                                                                 | Link |
|-----------------|-----------------------------------------------------------------------------|------|
| `big_data.md`   | Detailed report including implementation, analysis, and findings            | [View](big_data.md) |
| `big_data.ipynb`| Jupyter Notebook containing full code, execution results, and experiments   | [Open](big_data.ipynb) |

---

## Introduction

In modern data-driven industries such as aviation, large volumes of data are generated from flight operations, including departure schedules, arrival times, delays, and airline performance metrics. Processing such datasets efficiently requires appropriate data handling strategies to overcome memory limitations and improve execution performance.

This project focuses on applying and evaluating scalable big data handling techniques using the Carrier On-Time Performance Dataset. Since the dataset contains over 2 million records and 109 columns, direct loading and processing can be inefficient. Therefore, multiple strategies and libraries were used to optimise performance and analyse their effectiveness.

---

## Dataset Overview

- **Name**: Carrier On-Time Performance Dataset  
- **Source**: https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset  
- **Domain**: Airline / Transportation Analytics  
- **File Size**: 841.30 MB  
- **Shape**: 2,000,000 rows × 109 columns  

The dataset contains detailed flight records, including airline information, route details, departure and arrival times, delay metrics, and operational performance indicators.

---

## Description

Each row in the dataset represents a single flight record. The dataset includes key information such as airline carrier, origin and destination airports, scheduled and actual departure and arrival times, and delay-related metrics.

For this project, a subset of 8 relevant columns was selected to improve efficiency while maintaining meaningful analysis. Based on the processed data, 859,554 flights were identified as delayed, representing approximately 42.98% of the dataset.

---

## Strategies Applied

The following strategies were implemented to improve data processing performance:

- Load Less Data: Selecting only required columns to reduce unnecessary data loading  
- Chunking: Processing the dataset in smaller parts to reduce memory usage  
- Data Type Optimisation: Converting columns into efficient data types  
- Sampling: Using a subset of data for faster testing and exploration  
- Parallel Processing: Using Dask for scalable computation  
- High-Performance Processing: Using Polars for faster execution  

---

## Library Comparison

Three libraries were used and compared based on execution time and memory usage:

- Pandas: Provides simple and reliable data processing but requires loading data into memory  
- Dask: Supports parallel processing and is suitable for larger datasets  
- Polars: Offers high-performance execution with optimized query processing  

---

## Key Findings

The results show clear differences in performance between the strategies and libraries:

- Polars achieved the fastest execution time at 1.56 seconds  
- Sampling used the least memory due to processing a smaller dataset  
- Chunking provided a balanced approach for processing the full dataset with low memory usage  
- Data type optimisation reduced memory usage by over 90%  
- Pandas provided a reliable baseline but was slower than optimised methods  
- Dask was slower in this experiment due to overhead but remains useful for distributed systems  

All methods produced consistent analytical results, confirming that the choice of strategy affects performance but not correctness.

---

## Conclusion

This project demonstrates that different big data handling strategies are suitable for different scenarios. Polars is the best option when execution speed is the priority, while chunking is effective for memory-constrained environments. Data type optimisation is essential for reducing memory usage, and sampling is useful for quick analysis.

Pandas remains a practical and easy-to-use option, while Dask is more suitable for larger-scale or distributed processing tasks. The key takeaway is that selecting the appropriate strategy depends on dataset size, system resources, and performance requirements.

---

## References

- Kaggle Dataset:  
  https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset  

- Pandas Documentation:  
  https://pandas.pydata.org/pandas-docs/stable/  

- Dask Documentation:  
  https://docs.dask.org/en/latest/  

- Polars Documentation:  
  https://docs.pola.rs/
