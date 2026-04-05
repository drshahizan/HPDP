# 📘 Assignment 2: Mastering Big Data Handling  
### Group Members:
| Name              | Matric No       |
|-------------------|-----------------|
| CHE MARHUMI BIN CHE AB RAHIM   | A22EC0147      |

📅 **Submission Date:** 4 June 2025  

## 📌 Overview

This repository contains our submission for **Assignment 2: Mastering Big Data Handling**, where we explored strategies for efficiently working with large datasets that exceed traditional memory limits.

We used Python tools like **Pandas**, **Dask**, and **Polars** to process a dataset larger than 700MB, and compared performance across methods.

Our focus was on the **MyAnimeList final_animedataset.csv**, which includes rich data about users, anime titles, genres, and ratings — ideal for exploring big data handling techniques.


## 🧾 Dataset Used

| Property | Description |
|---------|-------------|
| **Name** | [MyAnimeList Dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset) |
| **Source** | Kaggle |
| **File Used** | `final_animedataset.csv` |
| **Size** | ~4.5 GB (full file), ~3+ GB usable data |
| **Columns Used** | `username`, `anime_id`, `my_score`, `genre`, `type`, `score` |
| **Domain** | Anime user reviews, ratings, and metadata |

---

## 🔍 Applied Strategies

We applied and benchmarked five key big data handling strategies:

1. **Load Less Data** – Load only necessary columns
2. **Use Chunking** – Process in batches using Pandas chunking
3. **Optimize Data Types** – Reduce memory usage with appropriate dtypes
4. **Sampling** – Use random sampling for fast prototyping
5. **Parallel Processing with Dask** – Leverage lazy evaluation and parallelism

---

## 📁 Folder Structure

| File           | Description | Link                          |
|----------------|-------------|-------------------------------|
| `big_data.md`  | Complete Markdown report showing dataset details, applied strategies, memory and time metrics, and final reflection | [![View Report](https://img.shields.io/badge/View-Report-brightgreen?logo=markdown&logoColor=white)](big_data.md) |
| `big_data.ipynb` | Fully working Google Colab notebook with all strategies implemented | [![Jupyter](https://img.shields.io/badge/Open-Jupyter-F37626?logo=jupyter&logoColor=white)](https://colab.research.google.com/drive/1VTU_URXoo4UkVCz3YLNsNDDwbUj16tqx?usp=sharing) |

---


## 📁 Repository Link

🔗 [GitHub Project Page](https://github.com/drshahizan/HPDP/tree/main/2425/assignment/A2/bdm/Solo%20Squad)

---

## 🧑‍💻 Developed by

**Solo Squad**  
A single-member team working on high-performance data processing using modern tools.

---

📌 *Made with ❤️ for HPDP Class — C.Mrhumi*

---
