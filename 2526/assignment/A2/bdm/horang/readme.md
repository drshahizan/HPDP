# 📘 Assignment 2: Mastering Big Data Handling

## 👥 Group Members

| Name | Matric Number |
|------|--------------|
| Goe Jie Ying | A23CS0224 |
| Lam Yoke Yu | A23CS0233 |

---

## 📁 Project Deliverables

| File | Description | Link |
|------|------------|------|
| `big_data.md` | Full written report | [![Open](https://img.shields.io/badge/View-Markdown-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb` | Implementation & experiments | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data.ipynb) |

---

## 🧠 Project Overview

In this era of abundant talent and creative freedom, music and songs have emerged as important mediums for both artists and individuals to express themselves. Consequently, the rapid growth in song production has resulted in large-scale song datasets. Analyzing this data and extracting meaningful insights pose significant challenges, requiring efficient data handling techniques and scalable processing frameworks.

In this assignment，we explores techniques for handling and optimizing large-scale datasets efficiently. We focus on applying scalable data processing strategies using multiple Python libraries, such as Pandas, Dask, Polars and PyArrow to evaluate their performance and analyze how different optimization techniques impact execution efficiency.

---

## 📊 Dataset Information

- **Dataset Name**: Genius Song Lyrics 
- **Source**: [Kaggle - Genius Song Lyrics](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information/data) 
- **Domain**: Music / Entertainment
- **File Size**: 9.07 GB  
- **Dimensions**: 5134856 rows × 11 columns

### 📌 Dataset Description
This dataset contains song-related information collected up to 2022 from Genius, a platform where users contribute and annotate lyrics, poems, and other textual content—primarily music lyrics. The dataset presents several preprocessing challenges. Lyrics are stored in a structured format that often includes metadata enclosed in square brackets within the text. Additionally, the lyrical content preserves line breaks and formatting, resulting in a large number of newline characters that can complicate data loading and text processing. Other attributes, such as audio features and languages, also require cleaning and transformation before analysis.

---

### ⚠️ Data Considerations

- The dataset contains **missing values** in columns such as `title` and language-related fields, which must be handled to ensure smooth processing.  
- The **lyrics column consists of large, unstructured textual data**, including embedded metadata and numerous newline characters. This leads to high memory consumption and increased preprocessing complexity.  
- Due to its size and complexity, the lyrics column was removed to **avoid system instability and reduce computational overhead**.  

---

### 🔑 Important Features

- **Title** – Name of the song  
- **Language Columns (`language`, `language_cld3`, `language_ft`)** – Provide language information detected using different models  
- **Features** – Contains additional metadata about the song, requiring parsing and preprocessing  

---

## ⚙️ Methodology

The following techniques were applied to improve data handling efficiency:

- Technique 1 – Load Less Data 
- Technique 2 – Chunking  
- Technique 3 – Optimize Data Types
- Technique 4 – Sampling 
- Technique 5 – Parallel Processing with Dask, Polars and PyArrow

---

## 🛠️ Tools & Libraries

- **Pandas** 
- **Dask** 
- **Polars**
- **PyArrow**

---

## 📈 Performance Evaluation

We compared the tools based on the following metrics:

- Memory Usage  
- Execution Time  
- CPU Utilization    

---

## 🎯 Conclusion

This project demonstrates how different tools and optimization techniques affect big data processing performance. By analyzing multiple approaches, we identified trade-offs between ease of use, speed, and resource efficiency.

Overall, this assignment provides practical exposure to real-world data engineering challenges and highlights the importance of selecting appropriate tools for large-scale data processing.

---
