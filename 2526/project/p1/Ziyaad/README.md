<h1 align="center">
  iProperty Malaysia
  <br>
  High Performance Data Processing for Large-Scale Web Crawlers
  <br>
</h1>

<p align="center">
  <b>SECP 3133 — High Performance Data Processing</b><br>
  Project 1: Optimizing High Performance Data Processing for Large-Scale Web Crawlers<br>
  Universiti Teknologi Malaysia · Faculty of Computing
</p>

<table align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width="80%">AHMAD ZIYAAD BIN MOHD ABBAS</td>
    <td>A23CS0206</td>
  </tr>
</table>

<p align="center">
  <b>Lecturer:</b> DR MOHD SHAHIZAN BIN OTHMAN
</p>

---

<div align="center">

| File Name | Description | Link |
|-----------|-------------|------|
| **Raw Dataset** | Raw iProperty Malaysia scraped dataset (≈100,004 records) | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/data/iproperty_data.zip) |
| **Cleaned Dataset** | Final cleaned 100,000-record property dataset | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/data/iproperty_cleaned.zip) |
| **Main Crawler Notebook** | Notebook used to scrape iProperty Malaysia listings | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/p1/iproperty_100k.ipynb) |
| **Data Cleaning Notebook** | Notebook for cleaning, preprocessing, and transformation | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/p1/clean_data.ipynb) |
| **Optimization Notebook** | Benchmarking notebook for pandas, multiprocessing, and Dask | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/p1/optimize_pipeline.ipynb) |
| **Evaluation Charts Notebook** | Notebook used to generate performance comparison charts | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/p2/evaluation_charts.ipynb) |
| **Performance Results** | CSV files containing benchmark results | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/p2/performance_all.csv) |
| **Project Report** | Final project documentation | [Click Here](https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/report/Report_Project1_Ziyaad.pdf) |

</div>


---

## 1.0 Introduction

The rapid growth of online real estate platforms in Malaysia has produced large, continuously updated databases of structured property listings. While this information is valuable for market valuation, price comparison, and academic research, collecting it at scale introduces real engineering challenges in throughput, reliability, and ethical data acquisition.

This project presents an end-to-end web crawling and data processing pipeline built around **iProperty Malaysia**, one of the country's largest property directories. The pipeline scrapes property listings at scale, persists the raw dataset, cleans and transforms the records, performs exploratory data analysis, and benchmarks three different data processing strategies to determine which performs best for this workload.

A central outcome of this study is that parallelization does not automatically improve performance. For the dataset size and transformation workload examined here, a single-threaded sequential pandas pipeline outperformed both multiprocessing and Dask. Rather than treating this as a shortcoming, it is reported as a valid, empirically grounded engineering finding that reinforces a key principle of high-performance computing: optimization must always be justified through measurement.

## 2.0 Project Objectives

The objectives of this project are as follows:

1. To design and implement a large-scale web crawler capable of collecting at least **100,000** valid, structured property records from iProperty Malaysia.
2. To store the collected data in a structured CSV format and apply rigorous cleaning and transformation operations, including duplicate removal, missing-value handling, field standardization, and data-type validation.
3. To implement at least two distinct high-performance computing techniques — **multiprocessing** and **Dask distributed-style processing** — and apply them to the cleaning and transformation workload.
4. To benchmark the baseline and optimized pipelines using objective metrics: execution time, throughput, CPU utilization, and peak memory.
5. To analyze and interpret the performance results honestly, drawing engineering conclusions about when parallelization is and is not worthwhile.

## 3.0 Target Website and Dataset

### 3.1 Target Website

iProperty Malaysia was chosen because it hosts a very large and continuously refreshed inventory of property listings spanning every Malaysian state, comfortably exceeding the 100,000-record threshold required by the project brief.

- **Website:** iProperty Malaysia
- **URL:** `https://www.iproperty.com.my/`

Listings are organized by transaction type (for-sale and for-rent) and by region, and each listing exposes a consistent set of structured attributes suitable for tabular extraction.

### 3.2 Collected Fields

The raw dataset contains **17 fields**:

| Field | Description |
|-------|-------------|
| `listing_id` | Unique listing identifier |
| `listing_type` | `for-sale` or `for-rent` |
| `title` | Listing headline / property name |
| `price` | Listed price (RM) |
| `location` | Sub-locality |
| `region` | State-level region |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `car_parks` | Number of car parks |
| `size_sqft` | Built-up / land area in square feet |
| `property_type` | Raw property classification |
| `tenure` | Freehold / leasehold status |
| `furnishing` | Furnishing status |
| `agent` | Listing agent |
| `listing_url` | Source listing URL |
| `source` | Source identifier |
| `url_type` | URL classification |

### 3.3 Dataset Volume

| Metric | Count |
|--------|-------|
| Raw records collected | ≈ 100,004 |
| For-sale listings | 64,173 |
| For-rent listings | 35,827 |
| **Final cleaned dataset** | **100,000 valid structured records** |

## 4.0 System Design and Architecture

The system follows a modular, **three-stage pipeline** architecture. Each stage is implemented as a separate Jupyter notebook to keep concerns isolated and to ease reproducibility and grading.

**Stage 1 — Acquisition**
- Scrape property listing pages from iProperty Malaysia.
- Traverse by listing type and region.
- Paginate through result pages.
- Extract structured listing attributes.
- Save progress continuously to CSV.

**Stage 2 — Processing**
- Clean and standardize raw property data.
- Remove duplicate listings.
- Parse prices into numeric values.
- Normalize fields such as listing type, region, furnishing, and tenure.
- Validate numeric fields.
- Generate derived fields such as price per square foot where data is available.

**Stage 3 — Optimization and Evaluation**
- Run the same processing workload under three strategies: baseline sequential pandas, multiprocessing via `concurrent.futures.ProcessPoolExecutor`, and Dask distributed-style processing using `dask.dataframe` with a `LocalCluster`.
- Compare execution time, throughput, CPU utilization, memory usage, and speedup.

<p align="center">
  <img src="assets/system_architecture.png" width="800"/>
  <br>
  <i>Figure 1: System Architecture of the iProperty Malaysia Data Processing Pipeline</i>
</p>

### 4.1 Tools and Frameworks

| Category | Tools Used |
|----------|------------|
| Crawling | Python, HTTP client, parsing libraries |
| Data Processing | pandas, NumPy |
| Parallelism | `concurrent.futures.ProcessPoolExecutor` (multiprocessing) |
| Distributed-Style | Dask (`dask.dataframe` + `LocalCluster`) |
| Benchmarking | `time`, `psutil` (CPU & memory sampling thread) |
| Visualization | Matplotlib |
| Environment | Jupyter Notebook, CSV file storage |

## 5.0 Web Crawling Methodology

The crawler was implemented in `main_crawler.ipynb`. It traverses iProperty listing pages by transaction type and region, paginating through result sets and extracting the structured fields described in Section 3. To reach the 100,000-record target reliably, the crawler incorporates pagination handling, error recovery, and progressive saving so that partial progress is never lost in the event of a network or parsing failure.

The crawling workflow proceeds as follows:

1. Seed and enumerate listing pages by region and listing type.
2. For each page, parse listing cards and extract structured attributes.
3. Append records progressively to disk (CSV) rather than buffering everything in memory.
4. Apply crawl delays and retry-with-backoff on transient failures.
5. Continue until at least 100,000 valid records are collected.

### 5.1 Ethical Crawling Considerations

Responsible data collection was treated as a first-class design requirement. The crawler was built to minimize its impact on iProperty's infrastructure and to respect the site's policies.

- Only **publicly visible** listing data was collected; no authentication or restricted pages were accessed or bypassed.
- A deliberate **crawl delay** and **retry-with-backoff** handling were applied to avoid generating load resembling a denial-of-service pattern.
- Progress was **saved incrementally** to disk to avoid unnecessary repeated scraping.
- Request rates were kept modest to minimize unnecessary load on the website.
- No personal data beyond publicly displayed agent names was retained.
- The dataset is used strictly for **academic purposes** and is not redistributed commercially.

## 6.0 Data Cleaning and Transformation

Cleaning and transformation were performed in `clean_data.ipynb`. The raw export exhibited substantial missingness in several detail fields, which directly informed the cleaning strategy.

<p align="center">
  <img src="assets/missing_values.png" width="700"/>
  <br>
  <i>Figure 2: Missing Values by Column in the Raw Dataset</i>
</p>

Fields such as `bathrooms`, `bedrooms`, `size_sqft`, and `car_parks` were almost entirely missing in the raw export, while `agent` and `tenure` were missing for the overwhelming majority of listings. `furnishing` had comparatively low missingness. The cleaning pipeline therefore prioritized retaining every listing as a valid record while standardizing the fields that were reliably populated.

The following operations were applied:

1. **Duplicate removal** — exact and key-based duplicate listings were dropped.
2. **Field standardization** — `price` was parsed into a numeric value, a derived price-per-square-foot field was computed where size was available, and `listing_type`, `region`, `furnishing`, and `tenure` values were normalized to consistent labels.
3. **Property categorization** — free-text `property_type` was mapped to a standardized `property_category` (e.g., Terrace House, Apartment, Condominium); unmatched values were labeled `Unknown`.
4. **Type validation** — numeric fields were coerced to numeric dtypes, with invalid values nulled rather than dropped.
5. **Final selection** — the cleaned dataset was reduced to well-defined columns and exactly **100,000 valid records**.

> **Transparency note on residual missingness:** Because the source export populated certain fields sparsely, some columns in the cleaned dataset remain largely empty by design. The corresponding EDA results in Section 7 are therefore reported only over the subset of listings for which each field is available.

## 7.0 Exploratory Data Analysis

Exploratory analysis was conducted on the cleaned dataset to characterize the property market and to validate the cleaning process. Where a chart is computed over a sparsely populated field, the analysis is restricted to the listings for which that field is available.

### 7.1 Listing Type and Regional Distribution

For-sale listings outnumber for-rent listings (**64,173** versus **35,827**). Selangor dominates listing volume, followed by Kuala Lumpur, Johor, and Penang — consistent with these being the most economically active regions in Malaysia.

<p align="center">
  <img src="assets/listing_type_regions.png" width="800"/>
  <br>
  <i>Figure 3: Listing Type Distribution and Top Regions by Listing Count</i>
</p>

### 7.2 Price by Region

Among for-sale listings, Kuala Lumpur records the highest median sale price at approximately **RM 1.55 million**, with Penang and Selangor also comparatively high. This pattern aligns with expected urban price premiums.

<p align="center">
  <img src="assets/price_by_region.png" width="700"/>
  <br>
  <i>Figure 4: Median Sale Price by Region</i>
</p>

### 7.3 Price Distribution

The raw price distribution is heavily **right-skewed**, with a long tail of very high-value listings. Applying a base-10 logarithmic transform produces a far more interpretable, approximately bell-shaped distribution, which is the preferred representation for any downstream modeling.

<p align="center">
  <img src="assets/price_distribution.png" width="800"/>
  <br>
  <i>Figure 5: Raw and Log-Transformed Price Distribution</i>
</p>

### 7.4 Furnishing and Tenure

Among listings reporting furnishing, **partially furnished** and **fully furnished** properties dominate, with unfurnished listings least common. Among the smaller subset reporting tenure, **freehold** listings vastly outnumber leasehold.

<p align="center">
  <img src="assets/furnishing_tenure.png" width="800"/>
  <br>
  <i>Figure 6: Furnishing Status and Tenure Type Distribution</i>
</p>

### 7.5 Property Categories

Among listings with a resolved category, **terrace houses** are the most common, followed by apartments, flats, bungalows, townhouses, semi-detached houses, serviced residences, and condominiums.

<p align="center">
  <img src="assets/property_categories.png" width="700"/>
  <br>
  <i>Figure 7: Top Property Categories in the Cleaned Dataset</i>
</p>

> **Coverage caveat:** Several detail fields — including `bedrooms`, `bathrooms`, `size_sqft`, `car_parks`, `tenure`, and `agent` — had high missingness in the source data. The analyses for these fields are therefore limited to the available records only and should be interpreted within that bound.

## 8.0 High Performance Optimization Techniques

Two genuinely distinct high-performance computing techniques were applied to the cleaning and transformation workload and compared against a sequential pandas baseline. All three strategies process the same 100,000-row dataset and perform the same set of transformation tasks, ensuring a fair comparison.

### 8.1 Baseline — Sequential pandas

The baseline executes all transformation tasks sequentially in a single thread using vectorized pandas operations. It serves as the reference point against which speedup is measured.

### 8.2 Technique 1 — Multiprocessing (`ProcessPoolExecutor`)

The first optimization uses `concurrent.futures.ProcessPoolExecutor` to distribute the workload across multiple CPU-bound worker processes, configured as the number of available cores minus one (**7 workers** on the test machine). Multiprocessing sidesteps Python's Global Interpreter Lock by running independent processes, making it well-suited in principle to CPU-bound work.

### 8.3 Technique 2 — Dask Distributed-Style Processing

The second optimization uses `dask.dataframe` with a `LocalCluster`, partitioning the dataset into **28 partitions** (workers × 4) and executing transformations lazily across a distributed-style scheduler. Dask is designed to scale to datasets larger than memory and across multiple machines.

## 9.0 Performance Evaluation

Each strategy was benchmarked on the same dataset and hardware. CPU utilization and peak memory were sampled by a background `psutil` monitor thread, execution time was measured with wall-clock timing, and throughput is derived as 100,000 rows divided by execution time. The consolidated results are shown below.

| Metric | Baseline pandas | Multiprocessing (7 workers) | Dask (28 partitions) |
|--------|-----------------|-----------------------------|----------------------|
| Execution Time (s) | **0.21** | 0.45 | 9.74 |
| Throughput (rows/s) | **477,675** | 224,685 | 10,272 |
| Avg CPU Utilization (%) | 16.1 | 17.8 | 76.2 |
| Peak Memory (MB) | **308** | 327 | 543 |
| Speedup vs Baseline | **1.00×** | 0.47× | 0.02× |

<p align="center">
  <img src="assets/performance_comparison.png" width="800"/>
  <br>
  <i>Figure 8: Performance Comparison Between Baseline, Multiprocessing, and Dask</i>
</p>

<p align="center">
  <img src="assets/speedup_over_baseline.png" width="700"/>
  <br>
  <i>Figure 9: Speedup Relative to the Baseline pandas Pipeline</i>
</p>

## 10.0 Discussion of Results

The results are clear and, at first glance, counter-intuitive: the **sequential pandas baseline was the fastest strategy by a wide margin**, completing in 0.21 seconds, while multiprocessing took 0.45 seconds (0.47× the baseline speed) and Dask took 9.74 seconds (0.02× the baseline speed). Throughput followed the same ordering, with the baseline processing 477,675 rows per second against Dask's 10,272.

This outcome is explained by the relationship between workload size and parallelization overhead. At 100,000 rows, the cleaning and transformation operations are already vectorized and complete in a fraction of a second. The fixed costs of parallelization — spawning worker processes, serializing and shipping data between processes (inter-process communication), partition scheduling, and, for Dask, distributed-style task-graph coordination — substantially exceed the actual compute time saved. In short, for this workload the parallel frameworks spend more time coordinating than computing.

The CPU and memory metrics corroborate this interpretation. Multiprocessing and especially Dask drove higher average CPU utilization (17.8% and 76.2% versus the baseline's 16.1%), confirming that more cores were genuinely engaged. However, this additional activity did not translate into shorter runtimes, and it came at a memory cost: Dask's peak memory rose to 543 MB against the baseline's 308 MB, reflecting partition management and scheduler overhead.

Crucially, this does **not** indicate that the parallel techniques are defective. Multiprocessing and Dask are designed to win on workloads where per-row computation is expensive or where the dataset exceeds available memory. For datasets that are orders of magnitude larger, or for heavier transformations such as geocoding, text processing, or model inference, the compute time would dominate the fixed overhead and the ordering would be expected to reverse. The experiment therefore demonstrates the correct engineering lesson: **parallelization must be justified by the workload, and benchmarking is the only reliable way to confirm it.**

## 11.0 Challenges and Limitations

- **Source data sparsity:** Several detail fields (`bedrooms`, `bathrooms`, `size_sqft`, `car_parks`, `tenure`, and `agent`) were largely missing in the raw export, limiting the depth of some EDA and requiring an `Unknown` category for unresolved property types.
- **Crawling fragility:** Pagination behavior, intermittent network instability, and possible rate limiting required defensive error handling and progressive saving.
- **Benchmark scale:** 100,000 rows satisfied the project requirement but is too small for Dask to demonstrate its true distributed advantage; the transformation completes sub-second under pandas, leaving little headroom for parallel speedup.
- **Single-machine constraint:** Dask was run on a `LocalCluster` rather than a true multi-node cluster, so its distributed-scaling advantages could not be fully realized.
- **Overhead dominance:** Parallel processing is not always faster — for small or medium workloads, coordination overhead can dominate and outweigh any computational gain.

## 12.0 Conclusion

This project successfully delivered a complete, end-to-end high-performance data pipeline: a large-scale crawler that collected over 100,000 iProperty Malaysia listings, a robust cleaning and transformation stage that produced exactly 100,000 valid structured records, and a rigorous benchmarking study comparing a sequential baseline against multiprocessing and Dask. The exploratory analysis produced coherent, market-consistent insights into regional listing volumes, prices, and property characteristics.

The performance evaluation produced a clear and honestly reported result: for this dataset size and workload, the sequential pandas baseline was the fastest and most memory-efficient strategy, and the parallel techniques introduced overhead that outweighed their benefit. Far from undermining the project, this finding satisfies its core intent — to measure, compare, and interpret performance — and yields a transferable engineering principle: parallelization is a tool whose value depends on workload characteristics, and it must be validated empirically rather than assumed.

## 13.0 Future Work

- Re-run the benchmark on a substantially larger dataset (e.g., **5–50 million rows**) to identify the crossover point where multiprocessing and Dask overtake the baseline.
- Introduce heavier per-row transformations such as **geocoding, text processing, or machine learning feature extraction** to make the workload compute-bound and favorable to parallelism.
- Deploy Dask on a genuine **multi-node cluster** to evaluate distributed scaling.
- Evaluate alternative high-performance dataframe engines such as **Polars** or **DuckDB**, which often outperform pandas on a single machine without distributed overhead.
- Store records in a database such as **PostgreSQL** or **MongoDB** instead of flat CSV files for more efficient querying and scalable storage.
- Improve crawler **checkpointing and resume functionality** to harden long-running scrapes against interruptions.

## 14.0 References

1. pandas development team. (n.d.). *pandas documentation.* https://pandas.pydata.org/docs/
2. Dask development team. (n.d.). *Dask documentation.* https://docs.dask.org/en/stable/
3. Python Software Foundation. (n.d.). *concurrent.futures — Launching parallel tasks.* In Python 3 documentation. https://docs.python.org/3/library/concurrent.futures.html
4. Rodolà, G. (n.d.). *psutil documentation.* https://psutil.readthedocs.io/en/latest/
5. iProperty Malaysia. (n.d.). *iProperty.com.my* [Property listings website]. https://www.iproperty.com.my/

## 15.0 Appendices

### Appendix A — Figure Index

| Figure | Description |
|--------|-------------|
| **Figure 1** | System Architecture |
| **Figure 2** | Missing Values by Column |
| **Figure 3** | Listing Type Distribution and Top Regions |
| **Figure 4** | Median Sale Price by Region |
| **Figure 5** | Price Distribution (Raw and Log-Transformed) |
| **Figure 6** | Furnishing and Tenure Distribution |
| **Figure 7** | Property Categories |
| **Figure 8** | Performance Comparison |
| **Figure 9** | Speedup Over Baseline |

### Appendix B — Repository and Dataset Links

- **GitHub repository:** `https://github.com/drshahizan/HPDP/tree/main/2526/project/p1/Ziyaad`
- **Cleaned dataset (`iproperty_cleaned.csv`):** `https://github.com/drshahizan/HPDP/blob/main/2526/project/p1/Ziyaad/data/iproperty_cleaned.zip`

> Replace the repository placeholders above with your actual GitHub paths before submission.

