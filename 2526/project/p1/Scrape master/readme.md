# Optimizing High Performance Data Processing for Large-Scale Web Crawlers

**Course:** High Performance Data Processing — Project 1
**Submission date:** 25 May 2026

## Group members

| Role | Name | Matric No. |
|------|------|------------|
| Group Leader & Data Engineer | MUHAMMAD ADAM BIN RAZALI | A23CS0116 |
| HPC & Performance Specialist | AFIF SHAQIR IRFAN BIN ARQAM | A23CS0204 |
| Analyst & Documentation Lead | PRAVINRAJ A/L SIVABATHI | A23CS0171 |

## Overview

This project builds a complete data pipeline that

1. **crawls** ~200,000 product listings from the Malaysian marketplace **Carousell.com.my**,
2. **cleans and standardises** the raw scrape into a structured dataset, and
3. **benchmarks five data-processing operations** across four libraries — **Pandas, Polars, Multiprocessing, and PySpark** — to quantify the speed-up delivered by each optimisation technique.

Each operation is run **5 times per library** and averaged so the comparison is not skewed by a single run.

## Data

| File | Rows | Columns | Notes |
|---|---|---|---|
| `data/raw_data.csv` | ~289,000 lines (~209k logical records) | 13 | Direct scrape output |
| `data/cleaned_data.csv` | 198,429 | 12 | Deduped, normalised, typed |

**Columns after cleaning:** `listing_id, product, price, condition, seller, time_posted, likes, listing_url, source_url, category, buyer_protection, delivery_info, posted_at`

## Optimization techniques

Three genuinely-different HPC techniques are compared against a single-threaded Pandas baseline:

| Technique | Why it's different |
|---|---|
| <img width="747" height="403" alt="image" src="https://github.com/user-attachments/assets/43f41c01-b465-4dd5-881d-53abaa12db4b" />
 | Rust-backed columnar engine with SIMD and built-in multi-threading; vectorised operators bypass the Python interpreter entirely |
| **Multiprocessing** | Splits the DataFrame across all CPU cores using `multiprocessing.Pool`; each worker runs the same Pandas code in its own OS process to bypass the GIL |
| **PySpark** | Distributed DataFrame engine (`local[*]`) that compiles operations to a JVM execution plan with hash-join + broadcast-join + shuffle |

## Benchmarked operations

| # | Operation | What it does |
|---|---|---|
| 1 | **Category Summary**    | Group by `category × condition`; compute 13 aggregations including mean / median / p25 / p75 / p90 / std of price, mean / max / sum of likes, unique sellers, unique products |
| 2 | **Find Popular Listings** | Filter to listings priced RM100–RM10,000 with at least 5 likes and condition `brand new` or `like new` |
| 3 | **Top 10 per Category** | Pick the 10 most-liked listings inside each category (sort + window) |
| 4 | **Keyword Search**      | Find listings whose title matches `gaming|laptop|phone|ssd|ram` (case-insensitive regex) |
| 5 | **Add Seller Stats**    | Compute each seller's avg price / total listings / total likes and inner-join back to every row |

## Tools used

| Category | Tools |
|---|---|
| Crawling | `undetected_chromedriver`, `selenium`, `beautifulsoup4`, `threading`, `concurrent.futures` |
| Cleaning | `pandas`, `numpy` |
| HPC | `polars`, `multiprocessing`, `pyspark` |
| Benchmarking | `psutil`, `tracemalloc`, `time.perf_counter` |
| Visualisation | `matplotlib`, `seaborn` |

## License

Submitted for academic assessment in the *High Performance Data Processing* course; not for commercial use.
