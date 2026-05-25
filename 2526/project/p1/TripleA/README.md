<h1 align="center"> 
  TripleA - Maukerja Job Scraping and Data Processing Benchmark
  <br>
</h1>

<table align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>LAM YOKE YU</td>
    <td>A23CS0233</td>
  </tr>
  <tr>
    <td width=80%>NABIL AFLAH BOO BINTI MOHD YOSUF BOO YONG CHONG</td>
    <td>A23CS0252</td>
  </tr>
  <tr>
    <td width=80%>ANIS SAFIYYA BINTI JANAI</td>
    <td>A23CS0049</td>
  </tr>
</table>
<br>

# Project Overview
The system is a data processing pipeline consisting of four main stages: web scraping, data preprocessing and cleaning, data processing using multiple libraries and frameworks, and performance visualisation.

The objective of the system is to collect job postings from the [Maukerja](https://www.maukerja.my/) website and to evaluate and compare the performance of different data processing libraries, namely Pandas, Polars, and PySpark.

# Project Architecture
```mermaid
flowchart TD

    A["🌐 Maukerja Website"] --> B["🕷️ Web Scraping Layer
    BeautifulSoup
    Requests
    Regex Extraction"]

    B --> C["💾 Raw Data Storage
    maukerja_compiled_with_description.csv"]

    C --> D["🧹 Data Preprocessing Layer
    Deduplication
    Cleaning
    Transformation
    Pandas"]

    D --> E["📦 Cleaned Dataset
    maukerja_cleaned.csv"]

    E --> F1["Pandas Benchmark"]
    E --> F2["Polars Benchmark"]
    E --> F3["PySpark Benchmark"]

    F1 --> G["📊 Visualization Layer
    Matplotlib
    Seaborn"]

    F2 --> G
    F3 --> G
```

# Tools and Framework Used
| Purpose           | Framework and Libraries                               | 
|------------------------------|--------------------------------------------|
| Core programming language | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| Data storage | ![CSV](https://img.shields.io/badge/CSV-000000?style=for-the-badge) ![GZIP](https://img.shields.io/badge/GZIP-000000?style=for-the-badge) |
| Web Scraping libraries| ![BeautifulSoup](https://img.shields.io/badge/beautiful_soup-000000?style=for-the-badge) ![Requests](https://img.shields.io/badge/requests-000000?style=for-the-badge) |
| Data manipulation libraries | ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![polars](https://img.shields.io/badge/polars-0075FF?style=for-the-badge&logo=polars&logoColor=white) |
| Distributed processing framework | ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white) |
| Data visualisation libraries | ![Matplotlib](https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge) ![Seaborn](https://img.shields.io/badge/seaborn-4C72B0?style=for-the-badge) |
| Version control and coordination | ![Github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) |


# Project Structure
📁 TripleA  
│  
├── 📁 data/  
│   ├── 📁 [raw_data_compiled](https://github.com/drshahizan/HPDP/tree/main/2526/project/p1/TripleA/data/raw_data_compiled) - Job listing scraped from the Maukerja website  
│   ├── 📄 [maukerja_compiled.gz](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/data/maukerja_compiled.gz) - Deduplicated job listings  
│   ├── 📄 [maukerja_compiled_with_description.gz](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/data/maukerja_compiled_with_description.gz) - Job listings with extracted descriptions  
│   └── 📄 [maukerja_cleaned.gz](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/data/maukerja_cleaned.gz) - Cleaned and normalised dataset     
│  
├── 📁 p1/  
│   ├── 📓 [main_crawler.ipynb](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p1/main_crawler.ipynb) - Scrapes job listing pages   
│   ├── 📓 [description_crawler.ipynb](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p1/description_crawler.ipynb) - Scrapes job descriptions using job URLs    
│   ├── 📓 [scraped_file_handler.ipynb](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p1/scraped_file_handler.ipynb) - Merges and separates datasets for processing        
│   ├── 📓 [maukerja_clean.ipynb](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p1/maukerja_clean.ipynb) - Data cleaning and standardisation   
│   └── 📓 [optimize_pipeline.ipynb](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p1/optimize_pipeline.ipynb) - Benchmarking pipeline for selected libraries    
│  
├── 📁 p2/  
│   ├── 📄 [performance_before.csv](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p2/performance_before.csv)  
│   ├── 📄 [performance_after.csv](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p2/performance_after.csv)  
│   └── 📓 [evaluation_charts.ipynb](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/p2/evaluation_charts.ipynb) - Visualises performance metrics    
│  
├── 📁 report/  
│   └── 📄 [Final_Report.pdf](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/TripleA/report/Final_Report.pdf)  
│  
├── 📄 README.md  
└── 📄 requirements.txt  

# Execution Flow
The pipeline was executed in the following order:

1. `main_crawler.ipynb`
   - Scrape job listing pages
2. `scraped_file_handler.ipynb`
   - Merge and deduplicate datasets
3. `description_crawler.ipynb`
   - Scrape detailed job descriptions
4. `scraped_file_handler.ipynb`
   - Recombine datasets
5. `maukerja_clean.ipynb`
   - Cleans and standardises data
6. `optimize_pipeline.ipynb`
   - Execute Pandas, Polars, and PySpark benchmarks
7. `evaluation_charts.ipynb`
   - Generate performance charts

# Data Scraping
- **Source Website**: [Maukerja](https://www.maukerja.my/)
- **Total Records Collected**: 106,080 job postings

# Benchmarking
### Libraries compared:   
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![polars](https://img.shields.io/badge/polars-0075FF?style=for-the-badge&logo=polars&logoColor=white) ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)

### Benchmark Metrics:
- Execution time (seconds)
- CPU utilisation (%)
- Memory usage (MB)
- Throughput (records/second)

### Benchmarking Results:
![Benchmarking results](/2526/project/p1/TripleA/p2/evaluation_charts.png)

### Benchmarking Summary
Polars achieved the best overall performance in terms of execution time and throughput, making it highly efficient for single-machine data processing tasks.

The optimised Pandas implementation significantly improved performance compared to the baseline version, particularly in execution time and memory efficiency.

PySpark, while designed for distributed computing environments, exhibited higher execution time in a single-machine setup, indicating that its advantages are more apparent in cluster-based architectures.
