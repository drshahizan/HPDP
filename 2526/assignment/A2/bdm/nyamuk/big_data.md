# Assignment 2: Mastering Big Data Handling

## Group Members:
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

## 1. Dataset Description
- **Name:** UK Housing Prices Paid </p>
- **Source:** [Kaggle-hm-land-registry](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid) </p>
- **File size:** 2.41 GB </p>
- **Domain:** Housing </p>
- **Shape:** 22,489,348 rows × 11 columns  </p>

### 📖 Description
This dataset contains comprehensive records of all registered property sales in England and Wales that were sold for full market value. It captures details of reported transactions, legal ownership types, property classifications, and geographical markers. This dataset provide a valuable insights into economic trends, purchasing behaviours, and regional distribution of property values which makes it well-suited for time-series analysis, geospatial mapping, and categorical market trend analysis.

## 2. Library Choices
Chosen libraries: </p>
| Library 1 | Library 2 | Library 3 |
|--------- | -----------| ---------- |
| Pandas | Dask | Polars |

Brief explanation why select Library 2 and Library 3..

## 3. Data Loading and Inspection
<h4> 🔷Load Strategy </h4>
<h4> 🔷Data Inspection </h4>
Show your initial loading code and the results of your data inspection. 

## 4. Big Data Handling Strategies (For each strategy: explanation, code snippet, output or screenshot, and discussion )
### 4.1 Load Less Data
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>

### 4.2 Chunking
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>

### 4.3 Data Type Optimisation
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>


### 4.4 Sampling
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>


### 4.5 Parallel Processing
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>

## 5. Comparative Analysis
### 5.1 Comparison of Optimized Loading Strategies
<h4> Summary Table </h4>

| Strategy | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| --------- | --------------- | ------------------| ------------| -------------------------|
| Load Less Data |  |  |  |  |
| Chunking |  |  |  |  |
| Optimized Data Types |  |  |  |  |
| Sampling |  |  |  |  |
| Parallel with <Dask> |  |  |  |  |

<h4> Visual Comparison </h4>


<h4> Interpretation </h4>
Cth: Optimize Data Types performed best in overall.


### 5.2 Comparison Between Libraries
Compare between Pandas, Dask, and Polars </p>

<h4> Summary Table </h4>

| Library | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| --------|-----------------|---------------------| ----------- | ------------------------ |
| Pandas |  |  |  |  |
| Dask |  |  |  |  |
| Polars |  |  |  |  |

<h4> Visual Comparison </h4>

<h4> Interpretation: </h4>
Explain satu2 Pandas, Polars, Dask

## 6. Conclusion and Reflection
<h4> 🔷Summary of key observations </h4>
<h4> 🔷Discussion of scalability </h4>
<h4> 🔷Personal reflection on learning </h4> 
 

## References
Afzal, A. (2020). _Los Angeles Crime Data 2020-2026_. Kaggle.com. https://www.kaggle.com/datasets/aliafzal9323/los-angeles-crime-data-2020-2026 

The Pandas Development Team. (2024). _pandas-dev/pandas: Pandas 2.2.2_. Zenodo. https://doi.org/10.5281/zenodo.3509134 

Dask Development Team. (2022). _Dask: Library for dynamic task scheduling_. https://dask.org 

Polars Development Team. (2024). _Polars: Fast multi-threaded, hybrid-streaming DataFrame library in Rust | Python_. https://pola.rs 

Google. (n.d.). _Google Colaboratory_. https://colab.research.google.com 
