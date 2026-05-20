<h1 align="center"> 
  Fast&Furious - mudah.my
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>Goe Jie Ying</td>
    <td> A23CS0224 </td>
  </tr>
  <tr>
    <td width=80%> Nawwarah Auni binti Nazrudin </td>
    <td> A23CS0143 </td>
  </tr>
  <tr>
    <td width=80%> Yasmin Batrisyia Binti Zahiruddin </td>
    <td> A23CS0201 </td>
  </tr>
</table>

# 🏘️ mudah.my Web Scraper

A Python-based web scraper developed to collect property listings from [mudah.my](https://www.mudah.my/) across all states in Malaysia. The scraper extracts relevant property information from each listing and stores the data into separate CSV files by state, which are later combined into a complete consolidated dataset.

---
## 📂 Project Files

| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **Raw Dataset**              | Cleaned and raw data with URLs             | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](p1/data/raw_data.csv) |
| **Clean Dataset**            | Preprocessed data ready for use            | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](p1/data/cleaned_data.csv) |
| **Web Crawler Script**       | Python script to scrape mudah.my       | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](p1/main_crawler.ipynb) |
| **Data Cleaning Code**       | Script to clean and preprocess the data    | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](p1/clean_data.ipynb) |
| **Optimization Code**        | Performance-optimized transformation code  | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](p1/performances_after.ipynb) |
| **Optimization Record Part 1** | Benchmark results part 1                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)](p2/performance_after_part1.csv) |
| **Optimization Record Part 2** | Benchmark results part 2                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)](p2/performance_after_part2.csv) |
| **Optimization Record Part 3** | Benchmark results part 3                 | [![Open](https://img.shields.io/badge/View-CSV-orange?logo=csv)](p2/performance_after_part3.csv) |
| **Evaluation Chart**         | Visual comparison of optimization results  | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](p2/evaluation_charts.ipynb) |
| **Project Report**           | Final detailed documentation               | [![Download](https://img.shields.io/badge/Download-PDF-red?logo=adobe-acrobat-reader)](report/Final_Report.pdf) |
| **Presentation Slides**      | Slides for project presentation            | [![Download](https://img.shields.io/badge/Download-PDF-red?logo=adobe-acrobat-reader)](report/PresentationSlide.pdf) |


---

## 📚 Libraries Used

### 🕸️ Web Scraping Libraries


---
### ⚙️ Data Processing & Optimization Libraries


---
## 🛠️ System Architecture

## 🔧 Architecture of Tools and Frameworks Used
#### Architecture Workflow:

#### 1.  Data Collection
Google Colab runs **BeautifulSoup** to scrape data from **mudah.my**, producing raw data.

#### 2.  Data Cleaning
The raw data is passed into **Pandas** for cleaning and transformation, producing clean data.

#### 3.  Parallel Processing (Before & After Optimization)
Three tools process the clean data in parallel:

| Pipeline | Tool | Status | Output File |
|----------|------|--------|-------------|
| Baseline | Pandas | Before optimization | `performance_before.csv` |
| Optimized | Pandas | After optimization | `performance_after.csv` |
| Optimized | Polars | After optimization | `performance_after.csv` |
| Optimized | DuckDB | After optimization | `performance_after.csv` |

 All four CSV outputs are saved into a central database.

#### 4. Analysis & Visualization
The database flows into **data metrics analysis**, then into **data visualization** to show charts and graphs for insights.

#### 5. Upload to GitHub
The clean data and final outputs are pushed to **GitHub** for version control and sharing.

![image](https://github.com/yAsmin241/HPDP-Project/blob/cdfd3a9f632e7e9e35931d36cfaeaf0391b13fba/Architecture%20and%20Framwork.drawio%20(2).png)


## 🔗 Data Details


---

## 📊 Dataset Overview
---
## 📊 Data Description

---
## 🚀 Performance Benchmark

---

### 🕒 Total Processing Time (seconds)

---

### 🧠 CPU Usage (%)

---

### 💾 Memory Usage (MB)

---

### ⚡ Throughput (records/second)


---

## ✅ Conclusion

