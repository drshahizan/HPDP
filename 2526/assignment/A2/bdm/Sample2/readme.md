# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Najma Shakirah binti Shahrulzaman
</td>
    <td>A23CS</td>
  </tr>
  <tr>
    <td>Syarifah Dania binti Syed Abu Bakar
</td>
    <td>A23CS0183</td>
  </tr>
   <tr>
    <td>Nawwarah Auni binti NazrudinNawarrah Auni
</td>
    <td>A23CS</td>
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

In the era of big data, traditional processing tools often fail when handling large-scale datasets, leading to memory exhaustion and slow execution. This assignment focuses on mastering high-performance data handling techniques by transitioning from theory to practical implementation.  

We utilize the Amazon Books Reviews dataset (approx. 2.9 GB), which is large enough to challenge the limits of standard libraries like Pandas. Our objective is to apply five key strategies which are loading selective data, chunking, data type optimization, sampling, and parallel processing—to ensure efficiency. By comparing Pandas against scalable libraries like PyArrows, Polars and Dask, we evaluate improvements in execution time and memory usage, preparing us for real-world data engineering challenges. 

---

## 🎵 Dataset Overview

- **Name**: Amazon Books Reviews
- **Source**: [Kaggle – [Mohamed Bekheet] (https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews)
- **Domain**: E-commerce / Retail 
- **File Size**: 2.8 GB
- **Shape**: 3000000 rows x 10 columns

### 📘 Description

The Amazon Books Reviews dataset is a large-scale collection of customer feedback and book metadata from the Amazon platform. It is primarily used for analyzing consumer behavior, sentiment analysis, and high-performance data processing tasks due to its significant volume.

### ⚠️ Notes

- Some songs may not have album metadata.  
- A portion of lyrics are missing proper startTimeMs annotations.  
- Not all tracks contain lyrics.  

### 🔍 Key Features

- Track metadata: name, artist(s), album  
- Audio attributes: danceability, energy, loudness, tempo, valence, etc.  
- Full lyrics (some with timestamps)  
- Dataset enriched from multiple Kaggle sources and lyric APIs  

---

## ⚙️ Techniques Used

- Selective data loading  
- Data type downcasting  
- Chunk-based reading  
- Sampling methods  
- Parallel processing with Dask  
- High-performance computing with Polars  

---

## 📊 Library Benchmarking

We evaluated the performance of three popular data-processing libraries:

- **Pandas**
- **Dask**
- **Polars**
- **PyArrows**

Each was tested and compared based on:

- Memory consumption  
- Execution time  
- Average CPU usage  
- Processing throughput (records/second)  

---

## 🎯 Conclusion

This project allowed us to explore and apply advanced data-handling techniques on a high-volume dataset in a practical scenario. By comparing multiple tools and approaches, we gained insights into the trade-offs between simplicity, speed, and resource usage in large-scale data processing.

Through this assignment, we have taken a step closer to how professional data engineers manage, optimize, and analyze massive datasets in real-world applications.

