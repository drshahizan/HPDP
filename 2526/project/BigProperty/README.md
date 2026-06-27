# SECP3133 Project 1: Optimizing High-Performance Data Processing for Large-Scale Web Crawlers

Welcome to our repository for the High Performance Data Processing group project.

## 👥 Group Information

| Item            | Details                                   |
| :-------------  | :---------------------------------------- |
| **Course**      | SECP3133 High Performance Data Processing |
| **Lecturer:**   | DR. SEAH CHOON SEN                        |
| **Group Name**  | Group BigProperty                         |
| **Member 1**    | LAU YAN KAI (A23CS0098)                   |
| **Member 2**    | NEO LI XIN (A23CS0253)                    |
| **Member 3**    | ELIJAH SHE YU SHENG (A23CS0073)           |
| **Member 4**    | CHEW CHIU XIAN (A23CS0061)                |

---

## 📌 Project Overview
This project focuses on designing, developing, and optimizing a large-scale data engineering pipeline for property listing data from **iProperty Malaysia**. The primary objective is to transition a traditional sequential, single-threaded processing engine into high-performance computing (HPC) architectures using macro-parallelism (Process Pool Multiprocessing) and micro-vectorization. 

The optimization layer benchmarks execution profiles by performing calculation assignments to determine an engineering feature (`investment_tier`) over **95,004 records**.

---

## 🎯 Project Objectives
* Develop a browser-automated web crawler capable of collecting at least 100,000 raw property records ethically.
* Parse, clean, deduplicate, and enforce rigid schemas on unstructured web text blocks.
* Implement and evaluate multiple parallel computing frameworks to address bottlenecks caused by Python's Global Interpreter Lock (GIL) and row-by-row interpreter abstraction loops.
* Conduct empirical multi-run benchmarks analyzing Latency, Peak Memory, CPU Load, and Record Throughput.

---

## 🌐 Target Website & Dataset Profile

### Data Ingestion Summary
* **Target Portal:** [iProperty Malaysia](https://www.iproperty.com.my) (Property Listings for Sale)
* **Total Raw Records Ingested:** 102,502
* **Unique Property Listings (Deduplicated):** 95,004
* **Overlapping/Duplicate Records Removed:** 7,498
* **Storage Matrix Format:** structured CSV

### Data Attributes Schema

| Column | Data Type | Structural Purpose / Description |
| :--- | :--- | :--- |
| `listing_url` | string | Unique resource identifier (Acts as Primary Key) |
| `property_type`| string | Standardized category mapping (e.g., Condominium, Terrace/Link) |
| `price_rm` | float64 | Total financial asset cost in Malaysian Ringgit (MYR) |
| `price_psf` | float64 | Valuation density metric (Price per square foot) |
| `built_up_sqft`| float64 | Total indoor usable floor dimensions |
| `land_area_sqft`| float64 | Geometric plot area boundary footprint size (otherwise `NaN`) |
| `furnishing` | string | Normalized furnishing layout status (Unfurnished, Fully, etc.) |
| `scraped_at` | DateTime | Standardized temporal stamp of ingestion processing |
| `investment_tier`| string | Engineered feature generated via optimization processing rules |

---

## 🚀 Optimization Architectures Evaluated
Performance metrics are sampled over **3 independent execution runs per model** to prevent environmental anomalies, calculating exact averages for final system plotting:

1. **Baseline Model (Before Optimization):** A control implementation utilizing a single-threaded interpreter execution thread. It iterates row-by-row via `.iterrows()`, introducing high context-switching and instruction overhead.
2. **Technique 1 (MP Pool):** Macro-parallel framework utilizing `concurrent.futures.ProcessPoolExecutor` to split data shards horizontally into distinct OS worker processes, bypassing the Python GIL.
3. **Technique 2 (Hybrid Vectorized):** Advanced high-performance setup pairing process-level sharding with underlying pre-compiled NumPy/Pandas array masking (`np.select`). Bypasses worker-level row loops entirely, driving operations down to native machine code levels.

---

## ⚙️ Core Tools & Dependencies
* **Web Crawling:** Selenium (Browser automation driver stability) & BeautifulSoup (HTML parsing)
* **High Performance Engine:** Python Concurrent Futures (`ProcessPoolExecutor`) & NumPy
* **Data Processing Layer:** Pandas DataFrames (Vector operations)
* **Hardware Telemetry Profilers:** `psutil` (Active CPU utilization tracking) & `tracemalloc` (Peak memory space tracing)
* **Visualization Suite:** Matplotlib & Seaborn

---

## 📁 Repository Folder Structure
```text
p1/[your_group_name]/
│
├── data/
│   ├── raw_data.json                 # Unprocessed initial crawled text lines
│   └── cleaned_data.csv              # Deduplicated and schema-enforced dataset
│
├── p1/
│   ├── main_crawler.ipynb            # Automated browser crawler engine
│   ├── clean_data.ipynb              # Token extraction & cleaning pipeline
│   ├── optimise_pipeline.ipynb       # 3-run averaging hardware benchmark suite
│   ├── performance_before.csv        # Logged metrics for unoptimized baseline run
│   ├── performance_after.csv         # Logged metrics for optimized frameworks (Tech 1 & 2)
│   └── evaluation_charts.ipynb       # Automated parsing and plotting notebook
│
├── report/
│   ├── Final_Report.pdf              # Comprehensive technical submission report
│   └── Presentation_Slides.pptx      # Slide deck summarizing empirical findings
│
├── README.md                         # Project roadmap and documentation
└── requirements.txt                  # Python dependencies manifest file

```


## 🔒 Ethical and Operational Bounds
* Collected exclusively public, non-authenticated real estate cards.
* Enforced randomized crawl delays (random.uniform(3, 6)) to preserve target server health.
* Zero security circumvention, bypass scripts, or CAPTCHA injection methods were deployed.
* Structured operational logs maintained historical transparency for failures and recoveries.