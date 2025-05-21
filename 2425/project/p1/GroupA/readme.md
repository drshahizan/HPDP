<h1 align="center"> 
  Group A - Appartment Pricing Analysis
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>LEE YIK HONG</td>
    <td>A21BE0376</td>
  </tr>
  <tr>
    <td width=80%>WONG JUN JI</td>
    <td>A22EC0117</td>
  </tr>
  <tr>
    <td width=80%>CHE MARHUMI BIN CHE AB RAHIM</td>
    <td>A22EC0147</td>
  </tr>
</table>

# 📰 NST News Scraper

A multithreaded Python-based web scraper that extracts over 100,000 articles from the [New Straits Times (NST)](https://www.nst.com.my/) website. The project includes advanced data cleaning and performance benchmarking using Pandas, Dask, and Polars. Built to evaluate high-performance data processing pipelines.

---

## 📂 Project Files

| File Name                    | Description                                 | Link |
|-----------------------------|---------------------------------------------|------|
| **Raw Dataset**             | Combined uncleaned scraped articles         | [📎 Download](https://example.com/raw_dataset.csv) |
| **Clean Dataset (Pandas)**  | Cleaned data using Pandas                   | [📎 Download](https://example.com/cleaned_pandas.csv) |
| **Clean Dataset (Dask)**    | Cleaned data using Dask                     | [📎 Download](https://example.com/cleaned_dask.csv) |
| **Clean Dataset (Polars)**  | Cleaned data using Polars                   | [📎 Download](https://example.com/cleaned_polars.csv) |
| **Web Scraper Script**      | Multithreaded Selenium crawler              | [🔍 View](src/nst_scraper.py) |
| **Data Cleaning Scripts**   | Pipelines for Pandas, Dask, and Polars      | [🔍 View](src/data_cleaning.py) |
| **Performance Chart**       | Benchmark charts for all libraries          | [🔍 View](notebooks/performance_charts.ipynb) |
| **Project Report**          | Full documentation and evaluation           | [📄 PDF](report/HDPD_01_Group1.pdf) |
| **Presentation Slides**     | Summary slides for academic presentation    | [📄 PDF](report/PresentationSlide.pdf) |

---

## ⚙️ Tools & Libraries Used

### Web Scraping

| Tool | Purpose |
|------|---------|
| `Selenium` | Automates interaction with dynamically loaded pages |
| `threading` | Allows concurrent scraping with multiple threads |
| `Queue` | Efficient task distribution across threads |

### Data Processing

| Library | Function |
|---------|----------|
| `pandas` | Data transformation, cleaning (baseline) |
| `dask` | Parallelized data handling and transformation |
| `polars` | Ultra-fast, multithreaded data wrangling |
| `psutil` | Monitors CPU and memory usage |
| `matplotlib` | Visualizes performance benchmarks |

---

## 🗂️ Extracted Data Fields

| Column Name | Description |
|-------------|-------------|
| `category`  | News section (Business, World, ASEAN) |
| `headline`  | Article title |
| `summary`   | Short description |
| `date`      | Publication date |
| `place`     | Location derived from summary |
| `year`      | Year extracted from date |
| `month`     | Month extracted from date |

---

## 🚀 Performance Evaluation

| Metric                  | Pandas | Dask | Polars |
|-------------------------|--------|------|--------|
| ⏱ Time Elapsed (s)      | 1.30   | 1.56 | **0.19** |
| 🧠 Avg. CPU Usage (%)   | **31.03** | 27.37 | 28.90 |
| 💾 Peak Memory Usage (%)| 71.5   | 73.6 | 73.3 |
| ⚡ Throughput (rec/sec)  | 77,550 | 64,766 | **529,123** |

> ✅ **Conclusion:** Polars dominates in speed and throughput. While Pandas is simple and stable, Polars is far more efficient for large-scale data operations. Dask performs reasonably but doesn’t outshine the others for in-memory datasets.

---

## 👨‍💻 Team Members

| Name                     | Role                         |
|--------------------------|------------------------------|
| Lee Yik Hong             | Group Leader, Evaluator      |
| Wong Jun Ji              | System Architect, Evaluator  |
| Che Marhumi bin Che Ab Rahim | Developer, Optimizer   |

---

## 📌 Future Improvements

- Integrate real-time scraping and streaming pipelines.
- Replace CSV with database storage (e.g., PostgreSQL or MongoDB).
- Use distributed scrapers with Playwright or headless Chromium clusters.
- Deploy as a scalable microservice.

---

## 📖 License

This project is intended for academic use and research only. All content scraped complies with [NST’s](https://www.nst.com.my/) publicly accessible data policies and ethical scraping guidelines.

