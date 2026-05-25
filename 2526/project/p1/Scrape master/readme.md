# Scrape Master - Carousell

## Group members

| Role | Name | Matric No. |
|------|------|------------|
| Group Leader & Data Engineer | MUHAMMAD ADAM BIN RAZALI | A23CS0116 |
| HPC & Performance Specialist | AFIF SHAQIR IRFAN BIN ARQAM | A23CS0204 |
| Analyst & Documentation Lead | PRAVINRAJ A/L SIVABATHI | A23CS0171 |

## Overview

This project builds a complete data pipeline that

1. **crawls** 200,034 product listings from the Malaysian marketplace **Carousell.com.my**,
2. **cleans and standardises** the raw scrape into a structured dataset, and
3. **benchmarks five data-processing operations** across four libraries — **Pandas, Polars, Multiprocessing, and PySpark**.
4. **Execution order** - main_crawler.pdf, cleaned_data.ipynb, optimized_pipeline.ipynb, evaluation_charts.ipynb

Each operation is run **5 times per library** and averaged so the comparison is not skewed by a single run.

## Project files

The pipeline is implemented across **four notebooks**, each owning one stage of the project. They are designed to be run top-to-bottom in order; the supporting `.py` modules at the repo root hold reusable functions that the notebooks import.

| Notebook | Description | Link |
|---|---|---|
| `data/raw_data.csv` | **Raw Data** | [Raw Data](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/data/raw_data.csv) |
| `data/cleaned_data.csv` | **Clean Data** | [Clean Data](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/data/clean_data.csv)
| `p1/main_crawler.ipynb` | **Scrape** |[Scrape](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/p1/main_crawler.ipynb) |
| `p1/cleaned_data.ipynb` | **Clean and Transform** | [Clean](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/p1/cleaned_data.ipynb) |
| `p1/optimized_pipeline.ipynb` | **Benchmark** | [Benchmark](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/p1/optimized_pipeline.ipynb) |
| `p2/evaluation_charts.ipynb`   | **Visualise** | [Visualize](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/p2/evaluation_charts.ipynb) |
| `report/report.pdf`            | **Final Report** | [Report](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/report/final_report.pdf) |
| `Presentation Slides.pptx` | **Presentation** | [Presentation Slides](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Scrape%20master/Presentation%20Slides.pptx) |


## Data

| File | Rows | Columns |
|---|---|---|
| `data/raw_data.csv` | 200,034 | 13 |
| `data/cleaned_data.csv` | 198,429 | 12 |

**Columns after cleaning:** `listing_id, product, price, condition, seller, time_posted, likes, listing_url, source_url, category, buyer_protection, delivery_info, posted_at`

### Cleaned dataset schema

`data/cleaned_data.csv` has 13 columns. Every row represents one Carousell listing.

| # | Column | Type | Description |
|---|---|---|---|
| 1  | `listing_id`        | int64        | Carousell's primary key for the listing — unique per row after de-duplication |
| 2  | `product`           | string       | Listing title as displayed on the website |
| 3  | `price`             | float64      | Selling price in Malaysian Ringgit (MYR) |
| 4  | `condition`         | string       | Lower-cased condition label |
| 5  | `seller`            | string       | Seller's display name on Carousell |
| 6  | `time_posted`       | string       | Original relative-time phrase as scraped |
| 7  | `likes`             | Int64        | Number of times the listing was liked|
| 8  | `listing_url`       | string       | Canonical product URL on Carousell |
| 9  | `source_url`        | string       | Category page the listing was crawled from |
| 10 | `category`          | string       | Hierarchical category breadcrumb|
| 11 | `buyer_protection`  | string       | buyer protection availability |
| 12 | `delivery_info`     | string       | Free-text delivery note from the seller |
| 13 | `posted_at`         | datetime64   | Absolute timestamp computed from `time_posted` |

## Optimization techniques

Three HPC techniques are compared against a single-threaded Pandas baseline:

| Technique | Description |
|---|---|
| <img width="120" alt="Pandas" src="https://github.com/user-attachments/assets/f5ca61ec-3504-431e-9ffb-361b03e49af9" /> | (Baseline) Traditional single-threaded Python DataFrame library; easy to use and highly compatible with the data science ecosystem, but limited by the Global Interpreter Lock (GIL) for CPU-bound workloads |
| <img width="120" alt="Polars" src="https://github.com/user-attachments/assets/43f41c01-b465-4dd5-881d-53abaa12db4b" /> | Rust-backed columnar engine with SIMD and built-in multi-threading; vectorised operators bypass the Python interpreter entirely |
| <img width="120" alt="Multiprocessing" src="https://github.com/user-attachments/assets/3c716e2a-963f-4fe2-ac84-5088977625a0" /> | Splits the DataFrame across all CPU cores using `multiprocessing.Pool`; each worker runs the same Pandas code in its own OS process to bypass the GIL |
| <img width="120" alt="PySpark" src="https://github.com/user-attachments/assets/eacb9172-399a-4074-81ed-af8817c6e120" /> | Distributed DataFrame engine (`local[*]`) that compiles operations to a JVM execution plan with hash-join + broadcast-join + shuffle |


## System Architecture

<img width="1276" height="1233" alt="image13" src="https://github.com/user-attachments/assets/33947673-d64d-4153-8c97-4b014788d110" />

## Tools and Framework Diagram

<img width="1576" height="998" alt="image18" src="https://github.com/user-attachments/assets/14c6f03e-3858-4659-b7fa-7ded99d710f4" />

## Benchmarked operations

| # | Operation | Description |
|---|---|---|
| 1 | **Category Summary**    | Group by `category × condition`; compute 13 aggregations including mean / median / p25 / p75 / p90 / std of price, mean / max / sum of likes, unique sellers, unique products |
| 2 | **Find Popular Listings** | Filter to listings priced RM100–RM10,000 with at least 5 likes and condition `brand new` or `like new` |
| 3 | **Top 10 per Category** | Pick the 10 most-liked listings inside each category (sort + window) |
| 4 | **Keyword Search**      | Find listings whose title matches `gaming|laptop|phone|ssd|ram` (case-insensitive regex) |
| 5 | **Add Seller Stats**    | Compute each seller's avg price / total listings / total likes and inner-join back to every row |

## Benchmark result files (`p2/`)

The benchmark stage writes six CSV files into the `p2/` folder. The master file contains every run; the five per-operation files are split-and-averaged views of the master file for easier scanning.

| File | Brief description | Link |
|---|---|---|
| `performance_comparison.csv`                            | **Master file.** Every metric for every (operation × library × run) — 120 rows total. Includes `Speedup vs Pandas` per row and a `Winner` flag on the average rows only. | [p2/performance_comparison.csv](p2/performance_comparison.csv) |
| `performance_comparison_categorysummary.csv`            | **Category Summary** operation only. One row per library showing the average over 5 runs. | [p2/performance_comparison_categorysummary.csv](p2/performance_comparison_categorysummary.csv) |
| `performance_comparison_findpopularlistings.csv`        | **Find Popular Listings** operation only. One row per library showing the average over 5 runs. | [p2/performance_comparison_findpopularlistings.csv](p2/performance_comparison_findpopularlistings.csv) |
| `performance_comparison_top10percategory.csv`           | **Top 10 per Category** operation only. One row per library showing the average over 5 runs. | [p2/performance_comparison_top10percategory.csv](p2/performance_comparison_top10percategory.csv) |
| `performance_comparison_keywordsearch.csv`              | **Keyword Search** operation only. One row per library showing the average over 5 runs. | [p2/performance_comparison_keywordsearch.csv](p2/performance_comparison_keywordsearch.csv) |
| `performance_comparison_addsellerstats.csv`             | **Add Seller Stats** operation only. One row per library showing the average over 5 runs. | [p2/performance_comparison_addsellerstats.csv](p2/performance_comparison_addsellerstats.csv) |

Every file uses the same friendly column names: `Library, [Run #,] Time (s), CPU (%), Peak Memory (MB), Process Memory (MB), Records Returned, Throughput, Speedup vs Pandas, Winner`. (`Run #` and `Operation` only appear in the master file.)

## Tools used

| Category | Tools |
|---|---|
| Crawling | `undetected_chromedriver`, `selenium`, `beautifulsoup4`, `threading`, `concurrent.futures` |
| Cleaning | `pandas`, `numpy` |
| HPC | `polars`, `multiprocessing`, `pyspark` |
| Benchmarking | `psutil`, `tracemalloc`, `time.perf_counter` |
| Visualisation | `matplotlib`, `seaborn` |

## Key results (averaged over 5 runs)

**Wall time (seconds):**

| Operation | Pandas | Polars | Multiprocessing | PySpark |
|---|---:|---:|---:|---:|
| Category Summary        | 5.368 | **0.109** | 4.232 | 1.490 |
| Find Popular Listings   | **0.023** | 0.083 | 2.088 | 1.168 |
| Top 10 per Category     | 0.157 | **0.131** | 2.378 | 1.423 |
| Keyword Search          | 0.954 | **0.087** | 2.203 | 1.425 |
| Add Seller Stats        | 0.230 | **0.124** | 3.384 | 2.176 |

**Speed-up vs Pandas baseline** (`>1` = faster than Pandas):

| Operation | Polars | Multiprocessing | PySpark |
|---|---:|---:|---:|
| Category Summary        | **49.3×** | 1.27× | 3.60× |
| Find Popular Listings   | 0.28× | 0.01× | 0.02× |
| Top 10 per Category     | 1.20× | 0.07× | 0.11× |
| Keyword Search          | **11.0×** | 0.43× | 0.67× |
| Add Seller Stats        | 1.85× | 0.07× | 0.11× |

## Conclusion — Best Library

<p align="center"><img width="400" alt="Polars" src="https://github.com/user-attachments/assets/43f41c01-b465-4dd5-881d-53abaa12db4b" /></p>

**Polars is the clear winner for the workload size and operation mix in this project.** It is the fastest library in **4 of the 5 operations**, including the heaviest one (Category Summary, where it is **~49× faster than Pandas**) and the text-search operation (Keyword Search, **~11× faster than Pandas**). It also keeps memory use comparable to or lower than the other libraries.

| Operation               | Winner   | 
|---|---|
| Category Summary        | **Polars**  |
| Find Popular Listings   | **Pandas**  | 
| Top 10 per Category     | **Polars**  |
| Keyword Search          | **Polars**  |
| Add Seller Stats        | **Polars**  |


## License

Submitted for academic assessment in the *High Performance Data Processing* course; not for commercial use.
