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
| **Web Crawler Script**       | Python script to scrape Carlist.my         | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p1/main_crawler.ipynb) |
| **Data Cleaning and Optimization Code**       | Script to clean, preprocess and performance-optimized transformation |  [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p1/clean_and_optimization.ipynb) |
| **Optimization Record Pandas** | Benchmark results Pandas                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p2/pandas_performance_results.csv) |
| **Optimization Record Dask** | Benchmark results Dask                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p2/dask_performance_results.csv) |
| **Optimization Record Polars** | Benchmark results Polars                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p2/polars_performance_results.csv) |
| **Evaluation Chart Code**         | Visual comparison of optimization results  | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/shopping/p1/Evaluation_Chart_Code.ipynb) |
| **Project Report**           | Final detailed documentation               | [![Download](https://img.shields.io/badge/Download-PDF-red?logo=adobe-acrobat-reader)](https://github.com/user-attachments/files/28208096/HPDP.Report.P1.pdf) |
| **Presentation Slides**      | Slides for project presentation            | [![Download](https://img.shields.io/badge/Download-PDF-red?logo=adobe-acrobat-reader)](https://github.com/user-attachments/files/28209967/HPDP.Project.1.pdf) |


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
| Pandas | 25.8236 | 25.4457 | 25.7103 | 26.1038 | 24.1501 | **25.6599**    |
| Dask | 154.50050 | 150.52610 | 155.19330 | 148.45820 | 152.90220 | **152.31606**    |
| Polars | 10.89440 | 4.94950 | 5.93880 | 4.74640 | 4.53320 | **6.21246**    |

---

### 🧠 CPU Usage (%)

| Tools                | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **Average** |
|----------------------|-------|-------|-------|-------|-------|-------------|
| Pandas | 61.9 | 63.1 | 54.5 | 60.8 | 53.2 | **59.8**    |
| Dask | 70.10 | 69.70 | 69.10 | 68.90 | 73.10 | **70.18**    |
| Polars | 90.20 | 61.20 | 96.00 | 44.40 | 55.00 | **69.36**    |

---

### 💾 Memory Usage (MB)

| Tools                | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **Average** |
|----------------------|-------|-------|-------|-------|-------|-------------|
| Pandas | 1872.0 | 2276.5 | 2570.5 | 2595.5 | 2609.1 | **2239.7**    |
| Dask | 3876.40 | 4747.00 | 4800.30 | 4652.70 | 4815.40 | **4578.36**    |
| Polars | 5204.00 | 5798.30 | 6174.00 | 6447.80 | 6490.10 | **6022.84**    |


---

### ⚡ Throughput (records/second)

| Tools                | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | **Average** |
|----------------------|-------|-------|-------|-------|-------|-------------|
| Pandas | 4782.0 | 4854.0 | 4804.0 | 4731.0 | 5114.0 | **4813.0**    |
| Dask | 799.0 | 820.0 | 796.0 | 832.0 | 808.0 | **811.0**    |
| Polars | 11336.0 | 24952.0 | 20796.0 | 26020.0 | 27244.0 | **22069.6**    |

### 📈 Performance Visualizations
<img width="619" height="371" alt="execution time chart" src="https://github.com/user-attachments/assets/61303384-3603-4899-b7cd-3015663b2f6f" />

<img width="620" height="367" alt="memory footprint chart" src="https://github.com/user-attachments/assets/807cd5fa-b4ef-4edf-9091-18fa152d6bd0" />

---
## 📈 Performance Comparison between Libraries
<img width="582" height="393" alt="Total Processing Time Chart" src="https://github.com/user-attachments/assets/43a8e711-4908-459b-b989-e44808cd8e55" />
<img width="576" height="393" alt="Peak Memory Usage Chart" src="https://github.com/user-attachments/assets/9fddb04b-0520-4615-b07a-6e680c1b897f" />
<img width="576" height="401" alt="Average CPU Usage Chart" src="https://github.com/user-attachments/assets/a210d82e-7119-415f-b20a-9c077d1a4a75" />
<img width="584" height="392" alt="Throughput Chart" src="https://github.com/user-attachments/assets/ca7682c9-1209-4839-8d98-1518736d7da6" />

---

## ✅ Conclusion
The benchmark results clearly demonstrate the impact of different data processing architectures on pipeline efficiency:

- **Pandas (The Baseline):** Pandas delivered a solid, reliable baseline, processing the dataset in an average of 25.6 seconds with a throughput of 4,813 records/second. Because it relies on single-threaded execution, its CPU utilization was the lowest (~59.8%), and it maintained the lowest memory footprint (2,239 MB).
- **Dask (The Overhead Penalty):** Dask performed significantly slower than the baseline, averaging 152.3 seconds with a throughput of only 811 records/second. While Dask successfully utilized more CPU cores (70.18%), the ~120,000-row dataset was not large enough to benefit from its distributed architecture. The massive scheduling overhead required to partition the data and manage the parallel workers severely bottlenecked the execution speed.
- **Polars (The Speed Multiplier):** Polars drastically outperformed both frameworks. By leveraging its Rust-based engine, lazy evaluation, and Apache Arrow memory format, Polars parallelized the workload perfectly. It processed the entire dataset in just 6.2 seconds, achieving a massive throughput of over 22,069 records/second (a 358% speed increase over Pandas). While this high-speed parallelization resulted in the highest peak memory usage (~6,022 MB), the trade-off was exceptionally worthwhile for the sheer processing speed gained.

## 🥇 Winner
<p align="center">
  <img src="https://raw.githubusercontent.com/pola-rs/polars-static/master/logos/polars-logo-dark.svg" width="300px"/>
</p>

**Polars** is the definitive winner for this pipeline. It maximized our hardware's multi-threading capabilities, sidestepped the single-core limitations of Pandas, and avoided the heavy task-graph overhead of Dask, proving to be the ultimate high-performance solution for medium-to-large web-scraped datasets.
