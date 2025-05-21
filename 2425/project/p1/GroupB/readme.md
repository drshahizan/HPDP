<h1 align="center"> 
  Data Drillers - Carlist.my
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>ALIATUL IZZAH BINTI JASMAN</td>
    <td>A22EC0136</td>
  </tr>
  <tr>
    <td width=80%>MULYANI BINTI SARIPUDDIN </td>
    <td> A22EC0223 </td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD ANAS BIN MOHD PIKRI </td>
    <td> A21SC0464 </td>
  </tr>
  <tr>
    <td width=80%>THEVAN RAJU A/L JEGANATH </td>
    <td>A22EC0286</td>
  </tr>
</table>

# 🚗 Carlist.my Web Scraper

A Python-based web scraper that extracts car listings from [Carlist.my](https://www.carlist.my/cars-for-sale/malaysia) and saves the data into a structured CSV file. Built for simplicity, performance, and reliability.

---
## 📂 Project Files

| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **Raw Dataset**              | Cleaned and raw data with URLs             | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1eK8V7xZXzvBDPVBAppC2TzItXCjdHnkr/view?usp=sharing) |
| **Clean Dataset**            | Preprocessed data ready for use            | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1KVVZ2WM5iz2jZFF2iFwH8Gn16O9gvoxw/view?usp=sharing) |
| **Web Crawler Script**       | Python script to scrape Carlist.my         | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](p1/main_crawler.ipynb) |
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

| Library | Description |
|--------|-------------|
| <img src="https://github.com/user-attachments/assets/0e15833e-c5f8-4976-afbe-03a8125beca1" width="48"/> `BeautifulSoup` | Web scraping & HTML parsing |
| <img src="https://github.com/user-attachments/assets/db6ed60d-ea8d-4cad-afc5-3c4de59eaaf7" width="48"/> `requests` | Sends HTTP requests to access web pages |


### ⚙️ Data Processing & Optimization Libraries

| Library | Description |
|--------|-------------|
| <img src="https://github.com/user-attachments/assets/e2eaa0ff-2214-43b7-90e1-b20a9e37ce28" width="48"/> `pandas` | A flexible and powerful library used for data analysis, transformation, and cleaning of structured datasets in Python. Ideal for exploratory data analysis and preprocessing. |
| <img src="https://github.com/user-attachments/assets/da096b58-28d4-4562-9fea-05b612f91aa9" width="48"/> `duckdb` | A fast, in-process SQL OLAP database engine designed for efficient querying and analytical operations on large datasets, often used as a drop-in replacement for pandas SQL workflows. |
| <img src="https://github.com/user-attachments/assets/6bbc160f-7b0e-47d9-9d90-0a8453cc2115" width="48"/> `polars` | A high-performance DataFrame library built in Rust, optimized for speed and low memory usage—great for large-scale data wrangling and lightning-fast computations. |

---
## 🛠️ System Architecture
![SystemArchitecture-Page-1 drawio](https://github.com/user-attachments/assets/704c2c3a-7942-4cfd-a69b-c9602e1bb285)
<br>
## 🔧 Architecture of Tools and Frameworks Used
![SystemArchitecture-Page-2 drawio (1)](https://github.com/user-attachments/assets/4ad1e7af-f32c-4bb5-a4a4-7a0f56d68bc1)

## 🔗 Data Details

  - Original dataset containing **175,545 rows** and **17 columns**. Includes some missing values in `location`, `fuel type`, and `body type`.

  - Cleaned version of the dataset with missing values replaced and invalid URL entries removed. Final shape: **175,545 rows × 16 columns**.

---

## 📊 Dataset Overview

This dataset contains car listings from various regions in Malaysia. The dataset includes key attributes such as car name, price, location, brand, year of manufacture, and more. It provides valuable insights for car buyers, sellers, and analysts interested in the automotive market.
## 📊 Data Description

| Column Name        | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `car_name`         | The car’s title or name on the listing                                   |
| `price`            | Asking price for the car                                                 |
| `location`         | City or locality where the car is sold                                   |
| `region`           | Malaysian state or territory                                             |
| `brand`            | Car manufacturer                                                         |
| `model`            | Car model type                                                           |
| `year`             | Manufacturing year                                                       |
| `mileage`          | Driven distance (in kilometres)                                          |
| `fuel_type`        | Fuel type, such as petrol or diesel                                      |
| `color`            | The body colour of the car                                               |
| `body_type`        | Car type, such as hatchback, sedan, etc.                                 |
| `seating_capacity` | The seating number in the car                                            |
| `condition`        | Vehicle condition, such as used or new                                   |
| `image`            | Vehicle image link to identify the car                                   |
| `description`      | Seller’s description of the car                                          |
| `url`              | Full link to the listing                                                 |

## 🚀 Performance Benchmark

We performed three test runs for each optimization stage using **Pandas**, **DuckDB**, and **Polars**, and tracked four key performance metrics:

- 🕒 **Total Processing Time (seconds)**
- 🧠 **CPU Usage (%)**
- 💾 **Memory Usage (MB)**
- ⚡ **Throughput (records/second)**

These measurements help compare how efficiently each method performed under similar conditions.

---

### 🕒 Total Processing Time (seconds)

| Optimization Stage   | Run 1 | Run 2 | Run 3 | **Average** |
|----------------------|-------|-------|-------|-------------|
| Pandas Optimization  | 5.35  | 3.49  | 3.44  | **4.09**    |
| DuckDB Optimization  | 0.45  | 0.89  | 0.43  | **0.59**    |
| Polars Optimization  | 0.43  | 0.26  | 0.61  | **0.43**    |

---

### 🧠 CPU Usage (%)

| Optimization Stage   | Run 1 | Run 2 | Run 3 | **Average** |
|----------------------|-------|-------|-------|-------------|
| Pandas Optimization  | 14.67 | 16.67 | 3.60  | **11.65**   |
| DuckDB Optimization  | 19.80 | 50.00 | 46.20 | **38.67**   |
| Polars Optimization  | 83.10 | 36.20 | 14.80 | **44.70**   |

---

### 💾 Memory Usage (MB)

| Optimization Stage   | Run 1  | Run 2  | Run 3  | **Average** |
|----------------------|--------|--------|--------|-------------|
| Pandas Optimization  | 102.34 | 119.98 | 125.80 | **116.04**  |
| DuckDB Optimization  | 65.79  | 98.83  | 81.64  | **82.09**   |
| Polars Optimization  | 28.63  | 3.81   | 129.63 | **54.02**   |

---

### ⚡ Throughput (records/second)

| Optimization Stage   | Run 1     | Run 2     | Run 3     | **Average** |
|----------------------|-----------|-----------|-----------|-------------|
| Pandas Optimization  | 32,827.06 | 50,356.60 | 51,003.49 | **44,729.0** |
| DuckDB Optimization  | 390,337.6 | 196,502.9 | 406,446.43| **331,095.6** |
| Polars Optimization  | 412,467.7 | 676,460.87| 289,688.39| **459,539.0** |

---

## ✅ Conclusion
The best library is Polars. While Pandas is easy to use, DuckDB and Polars significantly outperform it in terms of speed and efficiency—especially Polars in throughput and DuckDB in low memory usage.
## 🥇 Winner
<p align="center">
  <img src="https://github.com/user-attachments/assets/6bbc160f-7b0e-47d9-9d90-0a8453cc2115" width="300px"/>
</p>
