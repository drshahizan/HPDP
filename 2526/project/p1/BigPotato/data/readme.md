# 📂 Data Folder

This folder contains the datasets used in the **BigPotato JobStreet High Performance Data Processing Pipeline** project.

The data was collected from **JobStreet Malaysia** and processed for cleaning, transformation, and performance benchmarking.

---

## 📁 Files in This Folder

| File Name          | Description                                                                  |
| ------------------ | ---------------------------------------------------------------------------- |
| `raw_data.json`    | Raw job listing data collected from JobStreet Malaysia before cleaning       |
| `cleaned_data.csv` | Cleaned and transformed dataset used for analysis and performance evaluation |
| `readme.md`        | Documentation for the data folder                                            |

---

## 🌐 Data Source

**Website:** JobStreet Malaysia
**URL:** https://my.jobstreet.com/
**Data Type:** Public job listing data

The crawler extracted job listings from multiple JobStreet job classifications.

---

## 📊 Dataset Summary

| Description                 |              Value |
| --------------------------- | -----------------: |
| Raw records collected       |            105,094 |
| Job classifications crawled |                 30 |
| Final cleaned records       |             25,209 |
| Raw data file               |    `raw_data.json` |
| Cleaned data file           | `cleaned_data.csv` |

---

## 🗂️ Raw Dataset

### `raw_data.json`

This file contains the original job listing records collected from JobStreet Malaysia.

Main fields include:

* `job_title`
* `company`
* `location`
* `classification`
* `salary`

The raw dataset was kept to preserve the original scraped data before any cleaning or transformation steps were applied.

---

## ✅ Cleaned Dataset

### `cleaned_data.csv`

This file contains the cleaned and structured version of the dataset.

The cleaned dataset includes the following columns:

| Column           | Description                             |
| ---------------- | --------------------------------------- |
| `job_title`      | Title of the job position               |
| `company`        | Name of the hiring company              |
| `location`       | Job location                            |
| `classification` | Job category or industry classification |
| `salary`         | Original salary text from the listing   |
| `salary_min`     | Extracted minimum salary value          |
| `salary_max`     | Extracted maximum salary value          |

---

## 🧹 Data Cleaning Process

The raw data was cleaned before being used for analysis and benchmarking.

Cleaning steps include:

* Removing duplicate job records
* Handling missing values
* Standardizing text formatting
* Cleaning classification names
* Extracting salary ranges into numeric columns
* Standardizing location names
* Validating data types
* Rearranging columns into a structured format

---

## ⚠️ Notes

* `raw_data.json` should be treated as the original source dataset.
* `cleaned_data.csv` is the final dataset used for processing and performance evaluation.
* The dataset is used for academic purposes only.
* The data was collected from publicly accessible job listings.

