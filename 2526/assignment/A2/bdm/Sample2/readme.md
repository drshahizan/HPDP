# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Goh Jiale</td>
    <td>A22EA0043</td>
  </tr>
  <tr>
    <td>Yong Wern Jie</td>
    <td>A22EC0121</td>
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

In the modern era of music streaming and digital content, large datasets are common in entertainment platforms like Spotify. Efficiently handling this kind of data requires specialized tools and techniques.

Our project focuses on mastering scalable big data techniques using tools such as Pandas, Dask, and Polars. We applied various optimization strategies to load and process a large real-world dataset, then conducted performance benchmarking on memory usage, execution time, CPU utilization, and throughput.

---

## 🎵 Dataset Overview

- **Name**: 🎹 960K Spotify Songs With Lyrics Data 🎵  
- **Source**: [Kaggle – bwandowando](https://www.kaggle.com/datasets/bwandowando/960k-spotify-songs-with-lyrics)  
- **Domain**: Music / Entertainment  
- **File Size**: 1.54 GB  
- **Shape**: 955,320 rows × 17 columns  

### 📘 Description

This dataset is an enriched compilation created by merging several Spotify-related datasets, including:

- Spotify 1M+ Tracks  
- Spotify + Genius Dataset  
- 30K Spotify Songs  
- 6K Spotify Playlists  
- And more...

From over 3.3 million tracks submitted to the Spotify Lyrics API, around 960,000 were matched with usable lyrics. Each record includes audio features (tempo, energy, etc.), metadata (artist, album), and full song lyrics—making it suitable for both **audio analysis** and **natural language processing**.

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

Each was tested and compared based on:

- Memory consumption  
- Execution time  
- Average CPU usage  
- Processing throughput (records/second)  

---

## 🎯 Conclusion

This project allowed us to explore and apply advanced data-handling techniques on a high-volume dataset in a practical scenario. By comparing multiple tools and approaches, we gained insights into the trade-offs between simplicity, speed, and resource usage in large-scale data processing.

Through this assignment, we have taken a step closer to how professional data engineers manage, optimize, and analyze massive datasets in real-world applications.

