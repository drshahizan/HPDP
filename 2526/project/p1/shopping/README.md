<h1 align="center"> 
  Shopping - MalayMail.com
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>NURUL ADRIANA BINTI KAMAL JEFRI</td>
    <td>A23CS0258</td>
  </tr>
  <tr>
    <td width=80%>TAN YI YA</td>
    <td> A23CS0187</td>
  </tr>
  <tr>
    <td width=80%>TEH RU QIAN</td>
    <td>A23CS0191</td>
  </tr>
</table>

---
## 📂 Project Files

| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **Raw Dataset**              | Cleaned and raw data with URLs             | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1KvE0LtZrowNbbN6DWptL_0HpzUySe3qV/view?usp=drive_link) |
| **Clean Dataset**            | Preprocessed data ready for use            | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1Qza60tGcSKJgXykWvQ81tgIjR5OXpc6z/view?usp=drive_link) |
| **Web Crawler Script**       | Python script to scrape Carlist.my         | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p1/Web_Crawler.ipynb) |
| **Data Cleaning and Optimization Code**       | Script to clean, preprocess and performance-optimized transformation |  [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)]() |
| **Optimization Record Pandas** | Benchmark results Pandas                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)]() |
| **Optimization Record Dask** | Benchmark results Dask                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)]() |
| **Optimization Record Polars** | Benchmark results Polars                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)]() |
| **Evaluation Chart**         | Visual comparison of optimization results  | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)]() |
| **Project Report**           | Final detailed documentation               | [![Download](https://img.shields.io/badge/Download-PDF-red?logo=adobe-acrobat-reader)]() |
| **Presentation Slides**      | Slides for project presentation            | [![Download](https://img.shields.io/badge/Download-PDF-red?logo=adobe-acrobat-reader)]() |


---

## 📚 Libraries Used

### 🕸️ Web Scraping Libraries

| Library | Description |
|--------|-------------|
|![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white) `Playwright` | Browser automation and web scraping framework used to extract structured data from dynamic websites. |


### ⚙️ Data Processing & Optimization Libraries

| Library | Description |
|--------|-------------|
| ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) `pandas` | Data analysis and data cleaning library for structured datasets. |
| ![Dask](https://img.shields.io/badge/Dask-FC6E6B?logo=dask&logoColor=white) `dask` | Parallelized Pandas framework for larger-than-memory and multi-core data processing.|
| ![Polars](https://img.shields.io/badge/Polars-CD792C?logo=polars&logoColor=white) `polars` | Rust-based DataFrame library optimized for high-speed, memory-efficient analytics. |

---
## 🛠️ System Architecture
<img src="https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p1/System%20Architecture%20(1).png" width="500"/>

## 🔧 Architecture of Tools and Frameworks Used

<img src="https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p1/Tools.drawio.png" width="500"/>

## 🔗 Data Details
Original dataset containing **121,794** news articles collected. The dataset consists of **9 columns**. Raw data may contain duplicate records, encoding issues, missing values and inconsistent text formatting.

Cleaned version of the dataset with duplicate articles removed, text encoding corrected, author and category fields standardized, missing values handled and location information extracted from article content. The final dataset consists of **10 columns**.

---

## 📊 Dataset Overview
This dataset contains news articles collected from a Malaysian news website across multiple categories. Each record includes key information such as article title, publication details, author, category, content and source URL.

The dataset can be used for news analytics, trend analysis, text mining, natural language processing (NLP), sentiment analysis and large-scale data processing experiments.

## 📊 Data Description

| Column Name        | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `id`               |Unique article identifier                                                 |
| `title`            | News title                                                               |
| `category`         | News category                                   |
| `day`           | Publication day                                             |
| `date`            | Publication date                                                         |
| `time`            | Publication time                                                           |
| `author`             | Author name                                                       |
| `location`          | Extracted article location                                          |
| `content`            | News article content                                               |
| `link`        | Article URL                                 |

## 🚀 Performance Benchmark

We performed three test runs for each optimization stage using **Pandas**, **Dask**, and **Polars**, and tracked four key performance metrics:

- 🕒 **Total Processing Time (seconds)**
- 🧠 **CPU Usage (%)**
- 💾 **Memory Usage (MB)**
- ⚡ **Throughput (records/second)**

These measurements help compare how efficiently each method performed under similar conditions.

---

### 🕒 Total Processing Time (seconds)

| Tools                | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **Average** |
|----------------------|-------|-------|-------|-------|-------|-------------|
| Pandas | | | | | | **0**    |
| Dask | | | | | | **0**    |
| Polars | | | | | | **0**    |

---

### 🧠 CPU Usage (%)

| Tools                | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **Average** |
|----------------------|-------|-------|-------|-------|-------|-------------|
| Pandas | | | | | | **0**    |
| Dask | | | | | | **0**    |
| Polars | | | | | | **0**    |

---

### 💾 Memory Usage (MB)

| Tools                | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **Average** |
|----------------------|-------|-------|-------|-------|-------|-------------|
| Pandas | | | | | | **0**    |
| Dask | | | | | | **0**    |
| Polars | | | | | | **0**    |


---

### ⚡ Throughput (records/second)

| Tools                | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **Average** |
|----------------------|-------|-------|-------|-------|-------|-------------|
| Pandas | | | | | | **0**    |
| Dask | | | | | | **0**    |
| Polars | | | | | | **0**    |


---

## ✅ Conclusion

## 🥇 Winner
<p align="center">
  <img src="" width="300px"/>
</p>

