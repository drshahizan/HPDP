<h1 align="center"> 
  Group G - Malaysia News Analysis
</h1>

<table border="1" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>CHEN PYNG HAW</td>
    <td>A22EC0042</td>
  </tr>
  <tr>
    <td>MUHAMMAD DANIAL BIN AHMAD SYAHIR</td>
    <td>A22EC0206</td>
  </tr>
  <tr>
    <td>LOW JIE SHENG</td>
    <td>A22EC0075</td>
  </tr>
  <tr>
    <td>NADHRAH NURSABRINA BINTI ZULAINI</td>
    <td>A22EC0224</td>
  </tr>
</table>

<br>


# The Edge Malaysia Web Scraper

A high-performance web crawler to extract over 100,000 articles from [The Edge Malaysia](https://theedgemalaysia.com/). Using the site's public API, the team collected news data from the "Malaysia" section, cleaned and structured it, then applied optimization techniques like multithreading, Dask, and Polars to enhance processing speed and efficiency. The project concludes with a performance comparison before and after optimization.


## 📂 Project Files

| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **Raw Dataset**              | Cleaned and raw data with URLs             | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](data/theedge_articles.csv)|
| **Clean Dataset**            | Preprocessed data ready for use            | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://drive.google.com/file/d/1KVVZ2WM5iz2jZFF2iFwH8Gn16O9gvoxw/view?usp=sharing) |
| **Web Crawler**       | Python script to scrape The Edge Malaysia         | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1 ) |
| **Data Cleaning Code**       | Script to clean and preprocess the data    | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/theedge_cleaning_pandas.py) |
| **Optimization Code**        | Performance-optimized transformation code  | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/performances_after.ipynb) 
| **Evaluation Chart**         | Visual comparison of optimization results  | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p2) |
| **Project Report**           | Final detailed documentation               | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](report/HPDP_GroupG_FinalReport.pdf) |
| **Presentation Slides**      | Slides for project presentation            | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](report/HPDP_GroupG_Slide.pdf) |


---

## 📚 Libraries Used

### 🕸️ Web Scraping Libraries

| Library | Description |
|--------|-------------|
| `requests` | Sends HTTP requests to access web pages |


### ⚙️ Data Processing & Optimization Libraries

| Library | Description |
|--------|-------------|
| `pandas` | A flexible and powerful library used for data analysis, transformation, and cleaning of structured datasets in Python. Ideal for exploratory data analysis and preprocessing. |
|  `dask` | Dask is an open-source Python library for parallel computing. It scales Python code from multi-core local machines to large distributed clusters in the cloud. Dask provides a familiar user interface by mirroring the APIs of other libraries in the PyData ecosystem including: Pandas, scikit-learn and NumPy. |
| `polars` | A high-performance DataFrame library built in Rust, optimized for speed and low memory usage—great for large-scale data wrangling and lightning-fast computations. |

---
## 🛠️ System Architecture


## 🔧 Architecture of Tools and Frameworks Used



## 📊 Dataset Overview

- **Source Website**: [The Edge Malaysia](https://theedgemalaysia.com/)
- **Target Section**: Malaysia news category
- **Total Records Collected**: 110,000 articles
- **Format**: CSV (UTF-8 encoded)

## 📊 Data Description

| **Attribute**        | **Description**                                                      |
|----------------------|----------------------------------------------------------------------|
| `Category`             | Main domain of the article                                           |
| `Sub-category`         | Specific classification under the main category                     |
| `Title`                | The headline of the news article                                     |
| `Author`               | Name(s) of the person(s) who wrote the article                       |
| `Source`               | Origin of the article                                                |
| `Summary`              | A brief summary of the article’s content                             |
| `Created date`         | The original publication date of the article                         |
| `Updated date`         | The date when the article was last updated                           |

## 🧹 Cleaning & Transformation:

- Removed duplicate articles based on `title`
- Filled missing values (`author`, `source`) with "Unknown"
- Dropped articles with no `summary`
- Converted date fields to datetime format
- Trimmed whitespaces from text fields
- Structured categories into multiple subfields

## 🧪 Optimization Libraries Used:

- **Pandas** (baseline)
- **Pandas + Threading**
- **Dask** (distributed processing)
- **Polars** (Rust-based high-performance DataFrame)

> Cleaned datasets were saved separately for each framework for benchmarking and evaluation.
> 
## 🚀 Performance Benchmark

We performed three test runs for each optimization stage using **Pandas with threading**, **Dask**, and **Polars**, and tracked four key performance metrics:

- 🕒 **Total Processing Time (seconds)**
- 🧠 **CPU Usage (%)**
- 💾 **Memory Usage (MB)**
- ⚡ **Throughput (records/second)**

These measurements help compare how efficiently each method performed under similar conditions.

---

### 🕒 Total Processing Time (seconds)

| Library             | Before Optimization (s) | After Optimization (s) |
|---------------------|--------------------------|-------------------------
| Pandas              | 4.31                     | 1.07                   |
| Pandas + Threading  | 4.70                     | 1.08                   |
| Dask                | 11.37                    | 1.32                   |
| Polars              | 1.17                     | 0.96                   |

---

### 🧠 CPU Usage (%)

| Library             | Before Optimization (%) | After Optimization (%) |
|---------------------|--------------------------|-------------------------|
| Pandas              | 87.90                    | 97.71                   |
| Pandas + Threading  | 87.91                    | 89.47                   |
| Dask                | 92.97                    | 89.71                   |
| Polars              | 66.39                    | 98.60                   |

---

### 💾 Memory Usage (MB)

| Library             | Before Optimization (MB) | After Optimization (MB) |
|---------------------|---------------------------|--------------------------|
| Pandas              | 1237.40                   | 1275.09                  |
| Pandas + Threading  | 1263.07                   | 1274.09                  |
| Dask                | 1407.42                   | 1275.30                  |
| Polars              | 1275.69                   | 1273.69                  |

---

### ⚡ Throughput (records/second)

| Library             | Before Optimization (record/s) | After Optimization (record/s) |
|---------------------|----------------------------------|-------------------------------|
| Pandas              | 25115.66                        | 103236.63                     |
| Pandas + Threading  | 23255.58                        | 102188.66                     |
| Dask                | 9528.43                         | 82263.68                      |
| Polars              | 95919.64                        | 112545.89                     |



## ✅ Conclusion
- Polars is the fastest 
 - Pandas with threading was slightly better than normal Pandas 
 - Dask is better for very big data, not for this small scale

## 🥇 Winner
<p align="center">
  <img src="https://github.com/user-attachments/assets/6bbc160f-7b0e-47d9-9d90-0a8453cc2115" width="300px"/>
</p>

</table>
