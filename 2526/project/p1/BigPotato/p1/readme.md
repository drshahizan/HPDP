
# 📁 P1 Folder

This folder contains the main Jupyter Notebook files used to build the **JobStreet High Performance Data Processing Pipeline** for the BigPotato project.

The notebooks cover the full workflow from data collection, data cleaning, and optimized data processing.

---

## 📌 Folder Purpose

The `p1` folder stores the implementation notebooks for:

* 🌐 Web crawling
* 🧹 Data cleaning
* ⚡ Processing optimization
* 📊 Preparation for performance benchmarking

These notebooks are part of the **SECP3133 High Performance Data Processing** Project 1.

---

## 📂 Files in This Folder

| File Name                 | Description                                                              |
| ------------------------- | ------------------------------------------------------------------------ |
| `main_crawler.ipynb`      | Collects job listing data from JobStreet Malaysia using web crawling     |
| `clean_data.ipynb`        | Cleans and transforms the raw scraped dataset into a structured CSV file |
| `optimize_pipeline.ipynb` | Applies optimized processing techniques using Pandas, Polars, and DuckDB |
| `readme.md`               | Documentation for the `p1` folder                                        |

---

## 🌐 `main_crawler.ipynb`

This notebook is responsible for collecting job listing data from **JobStreet Malaysia**.

### Main Functions

* Access JobStreet Malaysia job listing pages
* Crawl job listings from multiple classifications
* Handle pagination
* Extract job information such as job title, company, location, classification, and salary
* Save the collected raw data into JSON format

### Output

```text
../data/raw_data.json
```

---

## 🧹 `clean_data.ipynb`

This notebook processes the raw dataset and prepares it for analysis and optimization.

### Main Cleaning Steps

* Remove duplicate job records
* Handle missing values
* Standardize text formatting
* Clean job classification values
* Extract salary ranges into numeric columns
* Standardize location names
* Validate data types
* Export the final cleaned dataset

### Output

```text
../data/cleaned_data.csv
```

---

## ⚡ `optimize_pipeline.ipynb`

This notebook focuses on improving the performance of the data processing pipeline.

Three processing approaches are implemented and compared:

### 1. Pandas Optimized Pipeline

* Loads only required columns
* Uses specific data types
* Applies category encoding
* Uses vectorized operations
* Performs efficient grouping and filtering

### 2. Polars Lazy Execution Pipeline

* Uses lazy CSV scanning
* Optimizes query execution
* Supports parallel processing
* Performs fast aggregation

### 3. DuckDB SQL-Based Processing

* Queries CSV data directly
* Uses SQL-based filtering and grouping
* Performs analytical processing efficiently

---

## 🔄 Suggested Notebook Execution Order

Run the notebooks in the following order:

```text
1. main_crawler.ipynb
2. clean_data.ipynb
3. optimize_pipeline.ipynb
```

This order ensures that the raw data is collected first, then cleaned, and finally used for optimized processing.

---

## 📊 Related Data Files

The notebooks in this folder are linked to the `data` folder.

| Data File                  | Purpose                                              |
| -------------------------- | ---------------------------------------------------- |
| `../data/raw_data.json`    | Raw scraped JobStreet dataset                        |
| `../data/cleaned_data.csv` | Cleaned dataset used for processing and benchmarking |

---

## 🛠️ Tools Used

| Tool / Framework | Usage                                  |
| ---------------- | -------------------------------------- |
| Python           | Main programming language              |
| Playwright       | Web crawling                           |
| BeautifulSoup    | HTML parsing                           |
| AsyncIO          | Asynchronous crawling                  |
| Pandas           | Data cleaning and optimized processing |
| Polars           | Lazy execution and parallel processing |
| DuckDB           | SQL-based analytical processing        |
| Google Colab     | Notebook development and testing       |

---

## 📌 Note

This folder contains the implementation notebooks for academic purposes only. The collected data is used for learning, data processing practice, and performance evaluation under the SECP3133 High Performance Data Processing course.
