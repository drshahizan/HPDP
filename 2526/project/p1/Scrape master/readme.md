# Optimizing High Performance Data Processing for Large-Scale Web Crawlers

**Course:** High Performance Data Processing — Project 1
**Submission date:** 25 May 2026

## Group members

| Role | Name | Matric No. |
|------|------|------------|
| Group Leader & Data Engineer | MUHAMMAD ADAM BIN RAZALI | A23CS0116 |
| HPC & Performance Specialist | _<fill in>_ | _<fill in>_ |
| Analyst & Documentation Lead | _<fill in>_ | _<fill in>_ |

## Overview

This project builds a complete data pipeline that

1. **crawls** ~200,000 product listings from the Malaysian marketplace **Carousell.com.my**,
2. **cleans and standardises** the raw scrape into a structured dataset, and
3. **benchmarks five data-processing operations** across four libraries — **Pandas, Polars, Multiprocessing, and PySpark** — to quantify the speed-up delivered by each optimisation technique.

Each operation is run **5 times per library** and averaged so the comparison is not skewed by a single run.

## Repository layout

```
hpdp_project_1/
├── data/
│   ├── raw_data.csv              # ~289k raw rows from Carousell.com.my
│   └── cleaned_data.csv          # 198,429 cleaned rows (12 columns)
├── p1/
│   ├── main_crawler.ipynb        # Selenium + threaded crawler
│   ├── clean_data.ipynb          # baseline pandas cleaning pipeline
│   └── optimize_pipeline.ipynb   # 5 operations × 4 libraries × 5 runs benchmark
├── p2/
│   ├── performance_before.csv    # baseline (Pandas) metrics
│   ├── performance_after.csv     # optimized (Polars / MP / PySpark) metrics
│   └── evaluation_charts.ipynb   # bar charts + speedup heatmap + per-run variance
├── report/
│   ├── Final_Report.pdf
│   └── Presentation_Slides.pptx
├── cleaners.py                   # shared cleaning functions (4 engines)
├── worker.py                     # multiprocessing chunk worker for cleaning
├── workloads.py                  # the 5 benchmarked operations × 4 engines
├── benchmark_utils.py            # benchmark harness (time / CPU / memory / throughput)
├── README.md
└── requirements.txt
```

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
| **Polars** | Rust-backed columnar engine with SIMD and built-in multi-threading; vectorised operators bypass the Python interpreter entirely |
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

Charts and the full speed-up heatmap live in `p2/evaluation_charts.ipynb` and in the PNGs at the repo root (`fig_workload_time.png`, `fig_workload_throughput.png`, `fig_workload_memory.png`, `fig_workload_cpu.png`, `fig_speedup_heatmap.png`, `fig_workload_runs.png`).

## How to reproduce

### Prerequisites

- Python 3.11 or 3.13
- Java 11 or 17 with `JAVA_HOME` set (PySpark only)
- Chrome installed (for the crawler)

### Install

```bash
python -m venv .venv
.venv\Scripts\activate         # Windows
# source .venv/bin/activate    # Linux/Mac
pip install -r requirements.txt
```

### Run order

1. `p1/main_crawler.ipynb`        — scrapes Carousell.com.my → `data/raw_data.csv`
2. `p1/clean_data.ipynb`          — cleans the raw CSV → `data/cleaned_data.csv`
3. `p1/optimize_pipeline.ipynb`   — benchmarks 5 operations × 4 libraries × 5 runs → `p2/performance_*.csv`
4. `p2/evaluation_charts.ipynb`   — renders comparison charts and the speed-up heatmap → `fig_*.png`

Each notebook is structured top-to-bottom; restart the kernel between major notebooks for clean memory measurements.

## Ethical scraping

The crawler honours `robots.txt`-style restraint through:

- realistic per-request delays via `time.sleep` between page loads;
- a bounded thread pool that limits concurrent requests to the target site;
- progressive saving so a single run never holds the full dataset only in memory.

## Tools used

| Category | Tools |
|---|---|
| Crawling | `undetected_chromedriver`, `selenium`, `beautifulsoup4`, `threading`, `concurrent.futures` |
| Cleaning | `pandas`, `numpy` |
| HPC | `polars`, `multiprocessing`, `pyspark` |
| Benchmarking | `psutil`, `tracemalloc`, `time.perf_counter` |
| Visualisation | `matplotlib`, `seaborn` |

## Known caveats

- `tracemalloc` only sees Python-allocated memory, so **PySpark's JVM memory is under-reported** in the peak-memory chart. This is noted in the report's "Challenges and Limitations" section.
- Multiprocessing pays a substantial fixed startup cost (`Pool` spawn) that dominates short workloads. It only wins on long-running CPU-bound tasks, which is why its speed-up numbers look modest on small operations.
- Spark's CSV reader is configured with `multiLine=True, escape='"'` so multi-line quoted fields are parsed identically to Pandas/Polars; otherwise row counts diverge.

## License

Submitted for academic assessment in the *High Performance Data Processing* course; not for commercial use.
