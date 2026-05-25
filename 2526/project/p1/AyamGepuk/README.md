<h1 align="center"> 
  Ayam Gepuk - News Analysis
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD NAIM BIN ABDULLAH</td>
    <td>A23CS0134</td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD MUKHRITZ AL IMAN BIN MOHD RAFFI</td>
    <td>A23CS0250</td>
  </tr>
  <tr>
    <td width=80%>SYARIFAH DANIA BINTI SYED ABU BAKAR</td>
    <td>A23CS0183</td>
  </tr>
</table>

<div align="center">

| File Name | Description | Link |
|-----------|-------------|------|
| **Raw Dataset (The Edge and The Sun)** | Raw scraped data from Edge Malaysia | [Click Here]([data/Theedgeandthesun.zip]) |
| **Master Dataset** | Final merged and deduplicated 100k dataset | [Click Here](data/FINAL_MASTER_100K.zip) |
| **Optimization Code** | Benchmark pipeline for Pandas, Dask, and Polars | [Click Here](p1/Optimization.ipynb) |
| **Google Colab Notebook** | Full project notebook on Google Colab | [Click Here](https://colab.research.google.com/drive/13Qil79Rb99kBmJA5-DcrDE2fPYp0KmJb#scrollTo=AKfiHYBx-XLt) |
| **Project Report** | Final documentation | [Click Here](report/REPORT%20PROJECT%201%20AYAM%20GEPUK.pdf) |
| **Presentation Slides** | Presentation slides for project presentation | [Click Here](report/Presentation_Slides.pptx) |
| **TurnitIn Report** | TurnItIn generated report | [Click Here](report/REPORT%20PROJECT%201%20(AyamGepuk)%20turnitin.pdf.pdf) |

</div>

## 1.0 Introduction
### 1.1 Background of the Project
Online news platforms have become an important source of information on a wide range of topics including business, finance, politics, social issues, and events happening around the world. With the increasing availability of public data on news websites, web scraping is a powerful tool to automate the collection of large volumes of content for purposes such as sentiment analysis, trend detection, and content archiving.

This project uses web scraping techniques to extract news articles from two established Malaysian online news portals  **Edge Malaysia** and **The Sun**  by leveraging a high-performance asynchronous scraping pipeline. The end goal is to gather at least 100,000 news article records for further data processing and performance benchmarking.

### 1.2 Objectives
- To develop a web scraper capable of collecting over 100,000 news article records from two target websites.
- To extract specific data elements such as article ID, title, author, source, summary, link, and publication date.
- To store the extracted data in a structured CSV format for processing and performance analysis.
- To clean and preprocess the merged dataset to ensure data quality.
- To compare three data processing libraries, Pandas, Dask, and Polars across multiple performance metrics.
- To optimize the data processing pipeline and evaluate performance improvements.

### 1.3 Target Website and Data
The websites targeted for this web scraping project are:
- **Edge Malaysia** (`https://theedgemalaysia.com`), a leading Malaysian financial and business news portal, scraped via its internal category API.
- **The Sun** (`https://thesun.my`), a Malaysian daily newspaper, scraped via its WordPress REST API.

The specific data fields extracted from each article are:
- **article_id:** A unique identifier prefixed with `EDGE_` or `SUN_` depending on source.
- **category:** The main topic area of the article.
- **sub-category:** A secondary classification label.
- **title:** The headline of the article.
- **author:** The article's author or reporter.
- **source:** The originating publication.
- **summary:** A short excerpt or description of the article content.
- **link:** The full URL of the article.
- **created date:** The publication date and time (standardized to D/M/YYYY H:MM:SS AM/PM).
- **updated date:** The last modified date and time.

## 2.0 System Design & Architecture

### 2.1 Description of Architecture
This system architecture illustrates the workflow of the web scraping and data preprocessing pipeline that extracts, cleans, and stores structured news data from Edge Malaysia and The Sun. The system follows a **Data Flow Architecture Pattern** where data moves through a linear sequence of stages such as Input, Intermediate Processing, and Output. The architecture consists of:

**1. Web Pages / APIs**<br/>
The system begins with requests to the Edge Malaysia category API and The Sun WordPress REST API. These endpoints serve as the seed inputs to the respective scrapers.

**2. Asynchronous Web Crawler**<br/>
Both scrapers use `asyncio` and `aiohttp` for asynchronous HTTP requests, allowing dozens of pages to be fetched simultaneously. Concurrency is controlled via `asyncio.Semaphore` (50 for The Edge, 10 for The Sun) to avoid overloading servers. An exponential backoff retry mechanism handles HTTP 429 (Too Many Requests) errors gracefully.

**3. Raw Data Storage**<br/>
The Edge data is written in append-mode batches directly to `theedge.csv` to manage memory during large-scale collection. The Sun data is collected in memory and saved to `thesun.csv` after deduplication.

**4. Data Merging & Cleaning**<br/>
Both raw CSVs are merged using `pd.concat`, deduplicated on the `link` column, and cleaned using HTML stripping, entity decoding, and missing value imputation before being saved as `FINAL_MASTER_100K.csv`.

**5. Optimization & Performance Benchmarking**<br/>
The same ETL pipeline is re-implemented in Pandas (baseline), Dask, and Polars. Each library is run 3 times on the 100,000-row master dataset and evaluated on execution time, memory usage, CPU utilization, and throughput.

**6. Data Storage**<br/>
The final cleaned and benchmarked dataset is saved in CSV format, ready for downstream tasks.

### 2.2 Tools and Frameworks Used
* asyncio
* aiohttp
* Pandas
* Dask
* Polars
* psutil (resource monitoring)
* Matplotlib / Seaborn (visualization)

### 2.3 Roles of the Team Members

| Team Member | Roles |
|-------------|-------|
| MUHAMMAD NAIM BIN ABDULLAH | Group Leader, Coder |
| MUHAMMAD MUKHRITZ AL IMAN BIN MOHD RAFFI | Architect, Coder |
| SYARIFAH DANIA BINTI SYED ABU BAKAR | Data Analyst, Documentation Lead, Coder |

## 3.0 Data Collection
### 3.1 Crawling Method (Pagination, Rate-Limiting, Async)
Data collection was performed using two custom-built asynchronous scrapers, one for Edge Malaysia and one for The Sun, both implemented with `asyncio` and `aiohttp`.

**Edge Malaysia Scraper:**
- Targets the internal REST API endpoint: `https://theedgemalaysia.com/api/loadMoreCategories?offset={offset}&categories={category}&limit={limit}`
- Scrapes 44 categories (e.g. corporate, economy, malaysia, world, politics, court, lifestyle, tech, property, etc.)
- Up to **50 concurrent requests** controlled via `asyncio.Semaphore`
- Data is saved in batches of 100 records directly to CSV (append mode) to manage RAM for large-scale collection
- Exponential backoff (`asyncio.sleep(2 ** attempt)`) handles rate limit errors

**The Sun Scraper:**
- Targets the WordPress REST API: `https://thesun.my/wp-json/wp/v2/posts`
- Fetches 150 pages at 50 records per page
- Up to **10 concurrent requests** to respect the server's stricter limits

**Common strategies:**
- Timestamps are normalized at extraction time, UNIX milliseconds (The Edge) and ISO strings (The Sun) are both converted to a standardized `D/M/YYYY H:MM:SS AM/PM` format
- HTML tags are stripped and HTML entities decoded using `re.sub` and `html.unescape()` during extraction

### 3.2 Number of Records Collected

| Source | Records Collected |
|--------|------------------|
| Edge Malaysia | 93,378 unique records |
| The Sun | 7,500 unique records |
| **Final Master Dataset (after deduplication)** | **100,887 unique records** |

Edge Malaysia was scraped across **44 categories** including corporate, economy, malaysia, world, politics, court, markets, stocks, lifestyle, tech, property, sports, education, automotive, features, and more. Total scraping time for The Edge was approximately **365 seconds**.

### 3.3 Ethical Considerations
The web scrapers were developed with adherence to ethical guidelines to ensure responsible data collection:

- **Respect site rules:** Only publicly accessible API endpoints and pages were accessed to ensure scraping did not violate the websites' terms of service.
- **Rate limiting:** Concurrency limits (Semaphore) and exponential backoff mimic responsible API usage, reducing the risk of server overload or IP bans.
- **Non-commercial use:** The data collected is used solely for academic and research purposes. No redistribution of scraped content is intended.

## 4.0 Data Processing
### 4.1 Cleaning Methods

**a. HTML Cleaning (Applied During Extraction)**<br/>
Raw API responses contain HTML markup. A `clean_text()` / `clean_html()` function is applied immediately during scraping:

```python
def clean_text(text):
    if not isinstance(text, str): return ""
    text = re.sub(r'<.*?>', '', text)   # Remove HTML tags
    text = html.unescape(text)          # Decode &amp;, &quot; etc.
    return re.sub(r'\s+', ' ', text).strip()
```

**b. Handle Duplicate Data**<br/>
Articles may appear under multiple categories or in overlapping API results. Duplicates are removed based on the unique article `link`:

```python
master_df.drop_duplicates(subset=['link'], keep='first', inplace=True)
```

**c. Handle Missing Data**<br/>
Empty cells are filled with `"N/A"` to produce a clean, production-ready dataset:

```python
master_df.fillna("N/A", inplace=True)
```

### 4.2 Data Structure
- Raw data from each source is saved independently as CSV: `theedge.csv`, `thesun.csv`
- Both sources are merged using Pandas:

```python
master_df = pd.concat([edge_df, sun_df], ignore_index=True)
```

- The final cleaned master dataset is saved as:

```python
master_df.to_csv("FINAL_MASTER_100K.csv", index=False)
```

### 4.3 Transformation and Formatting

**Timestamp Normalization:**<br/>
The Edge provides UNIX millisecond timestamps, The Sun provides ISO 8601 strings. Both are converted to a consistent format (`D/M/YYYY H:MM:SS AM/PM`):

```python
# The Edge — UNIX milliseconds
dt = datetime.fromtimestamp(ms / 1000, tz=UTC)
return f"{dt.day}/{dt.month}/{dt.year} {dt.strftime('%I:%M:%S %p').lstrip('0')}"

# The Sun — ISO string
dt = datetime.fromisoformat(iso_date_str)
return f"{dt.day}/{dt.month}/{dt.year} {dt.strftime('%I:%M:%S %p').lstrip('0')}"
```

**Unique Article ID:**<br/>
Each record is assigned a prefixed unique ID at extraction time to distinguish source after merging:

```python
# The Edge
"article_id": f"EDGE_{item.get('nid', '00000')}"

# The Sun
"article_id": f"SUN_{post.get('id', '00000')}"
```

## 5.0 Optimization Techniques
### 5.1 Methods Used
This project benchmarks three data processing libraries on the same 5-task ETL pipeline applied to the 100,000-row master dataset:

| Library | Explanation |
|---------|-------------|
| **Pandas** | The industry-standard Python data library. Uses **eager execution**, loads the entire dataset into RAM at once and processes operations sequentially on a **single thread**. Susceptible to memory bottlenecks on large datasets. Used as the **baseline**. |
| **Dask** | A parallel computing library that scales Pandas workflows. Constructs a **directed acyclic graph (DAG)** of deferred tasks and executes them in parallel across multiple CPU cores via its task scheduler. Designed for **out-of-core (larger-than-RAM)** datasets. |
| **Polars** | A modern high-performance DataFrame library built in **Rust**. Uses **lazy evaluation** with query optimization (e.g. projection pushdown), and natively parallelizes execution across all CPU cores, bypassing Python's GIL. |

### 5.2 Benchmark Pipeline (5 Tasks)
The same pipeline is implemented identically in each library:

#### Task 1 — Data Ingestion (I/O)
Load the master CSV from disk:
```python
# Pandas
df = pd.read_csv(FILE_PATH)

# Dask
ddf = dd.read_csv(FILE_PATH)

# Polars (Lazy)
q = pl.scan_csv(FILE_PATH)
```

#### Task 2 — Feature Engineering
Create a new `title_length` column based on string length:
```python
# Pandas / Dask
df['title_length'] = df['title'].str.len()

# Polars
.with_columns([pl.col("title").str.len_chars().alias("title_length")])
```

#### Task 3 — Data Standardization
Normalize the `category` column to uppercase:
```python
# Pandas / Dask
df['category'] = df['category'].str.upper()

# Polars
.with_columns([pl.col("category").str.to_uppercase()])
```

#### Task 4 — Type Casting & Date Parsing
Convert the `created date` string column to datetime objects:
```python
# Pandas
df['created date'] = pd.to_datetime(df['created date'], format='%d/%m/%Y %I:%M:%S %p', errors='coerce')

# Dask
ddf['created date'] = dd.to_datetime(ddf['created date'], format='%d/%m/%Y %I:%M:%S %p', errors='coerce')

# Polars
.with_columns([pl.col("created date").str.to_datetime("%d/%m/%Y %I:%M:%S %p", strict=False)])
```

#### Task 5 — Multi-Dimensional Aggregation
Group by `source` and `category`, then compute mean title length and article count:
```python
# Pandas
result = df.groupby(['source', 'category']).agg({
    'title_length': 'mean', 'article_id': 'count'
}).reset_index()

# Dask (triggers parallel execution)
result = ddf.groupby(['source', 'category']).agg({
    'title_length': 'mean', 'article_id': 'count'
}).compute()

# Polars
.group_by(["source", "category"]).agg([
    pl.col("title_length").mean().alias("avg_len"),
    pl.len().alias("count")
])
result = q.collect()
```

## 6.0 Performance Evaluation
### 6.1 Before vs After Optimization
The baseline pipeline (Pandas) operates on a single thread with eager execution. The same pipeline was re-implemented in Dask and Polars to measure improvement. Each library was run **3 times** on the 100,000-row master dataset, with memory cleared between runs (`gc.collect()`) to ensure isolation. Performance metrics were averaged across all runs.

### 6.2 Detailed Results Per Run

| Library | Run | Execution Time (s) | Memory Used (MB) | CPU Util (%) | Throughput (rows/s) |
|---------|-----|--------------------|------------------|--------------|---------------------|
| Pandas  | 1   | 1.6060             | 42.93            | 99.62        | 62,265.55           |
| Pandas  | 2   | 1.8461             | 30.43            | 97.50        | 54,167.80           |
| Pandas  | 3   | 1.5362             | 28.46            | 100.25       | 65,094.36           |
| Dask    | 1   | 1.3147             | 12.56            | 100.40       | 76,063.58           |
| Dask    | 2   | 1.3303             | 0.00             | 100.73       | 75,168.35           |
| Dask    | 3   | 1.7315             | 9.88             | 98.18        | 57,751.97           |
| Polars  | 1   | 0.1104             | 3.77             | 154.04       | 906,101.38          |
| Polars  | 2   | 0.0942             | 0.25             | 191.12       | 1,061,776.64        |
| Polars  | 3   | 0.0916             | 1.66             | 196.43       | 1,091,275.95        |

### 6.3 Averaged Summary

| Library | Execution Time (s) | Memory Used (MB) | CPU Util (%) | Throughput (rows/s) |
|---------|--------------------|------------------|--------------|---------------------|
| Pandas  | 1.6628             | 33.94            | 99.12        | 60,509              |
| Dask    | 1.4588             | 7.48             | 99.77        | 69,661              |
| **Polars**  | **0.0987**     | **1.89**         | **180.53**   | **1,019,718**       |

### 6.4 Charts and Graphs
To visually summarize the performance differences between Pandas, Dask, and Polars, a series of bar charts were generated based on the averaged performance metrics as shown in Figure 5. 

#### 1. Comparison of Execution Time
Polars completed the pipeline in under **0.1 seconds** on average, approximately **17× faster** than Pandas and **15× faster** than Dask. Dask recorded a modest improvement over Pandas.

#### 2. Comparison of Memory Usage
Polars used the least memory (~1.89 MB average), attributed to its lazy evaluation engine and projection pushdown which avoids loading unnecessary data into RAM. Dask also performed well (~7.48 MB) by processing data in partitions. Pandas consumed the most RAM (~33.94 MB) as it loads the entire dataset eagerly.

#### 3. Comparison of CPU Utilization
Polars achieved CPU utilization exceeding **180%**, demonstrating effective use of multi-core parallelism via its Rust engine, bypassing Python's Global Interpreter Lock (GIL). Pandas and Dask both stayed near 100%, indicating single-core or lightly parallel execution.

#### 4. Comparison of Throughput
Polars processed over **1 million rows per second**, compared to ~69,661 rows/s for Dask and ~60,509 rows/s for Pandas, a **16.9× improvement** over the Pandas baseline.

## 7.0 Challenges & Limitations

1. **Anti-Scraping Measures:** Both Edge Malaysia and The Sun employ server-side protections. HTTP 429 errors were encountered during The Edge scraping. This was mitigated with exponential backoff (`asyncio.sleep(2 ** attempt)`) and concurrency caps, but such measures can limit data collection speed.

2. **Scale and Memory Management:** Collecting 93,249 records from The Edge required writing data in append-mode batches directly to CSV rather than holding all records in RAM, since loading hundreds of thousands of rows in memory simultaneously is infeasible in a Colab environment.

3. **Data Quality and Inconsistency:** API responses from the two sources had different structures, timestamp formats (UNIX milliseconds vs ISO strings), and HTML-encoded content. Normalizing these at extraction time required separate transformation logic per source.

4. **Merging Data from Multiple Sources:** Aligning schemas between Edge Malaysia and The Sun required careful mapping. Since both sources were independently scraped, post-merge deduplication on the `link` column was necessary to ensure exactly 100,000 distinct rows in the final dataset.

5. **Dask Scheduler Overhead on Medium Data:** For a 100,000-row dataset, Dask's task graph construction and scheduler overhead reduced its advantage over Pandas. Dask's strength is better realized on datasets that exceed available RAM.

## 8.0 Conclusion & Future Work
### 8.1 Summary of Findings
This project successfully designed and built a high-performance asynchronous web scraping pipeline using `asyncio` and `aiohttp` to collect over **100,000 news article records** from Edge Malaysia and The Sun. The Edge Malaysia scraper leveraged its internal category API across 44 categories, while The Sun scraper used the WordPress REST API, collecting 93,249 and 7,500 records respectively within minutes.

After merging, deduplication, and cleaning, the master dataset (`FINAL_MASTER_100K.csv`) was used as the benchmark input for comparing three data processing libraries. Pandas served as the single-threaded eager baseline. Dask offered modest improvement through parallel task scheduling, with lower memory consumption (~7.48 MB vs ~33.94 MB). Polars delivered exceptional results, processing over 1 million rows per second at under 0.1 seconds, using minimal memory and achieving 180%+ CPU utilization through its native Rust multi-threading engine. The results confirm that choosing the right processing library has a dramatic impact on performance at scale.

### 8.2 What Could Be Improved

* **Save collected data into a database**<br/>
Currently, data is persisted as CSV files. Storing data in a database such as PostgreSQL or MongoDB would enable more efficient querying, better indexing, and scalable storage for growing datasets.

* **Expand The Sun collection**<br/>
Only 150 pages were fetched from The Sun's API (7,500 records). Pagination can be extended further, or additional category endpoints explored, to gather a larger and more balanced dataset from that source.

* **Use distributed scraping across machines**<br/>
Deploying scrapers across multiple machines or cloud workers simultaneously would allow collection to scale far beyond what a single Colab session supports, particularly for The Edge's 40+ categories.

* **Improve fault tolerance with checkpointing**<br/>
If the Colab session times out mid-scrape, all progress is lost. Implementing periodic checkpoint saves (e.g., every 10,000 records) would ensure long-running scrapes are resilient to interruptions.

* **Benchmark on larger datasets**<br/>
The 100,000-row dataset did not fully expose Dask's strengths. Testing all three libraries on datasets of 1M+ rows or datasets exceeding available RAM  would provide a more comprehensive picture of Dask's distributed computing advantage.

## References
- Dask. (n.d.). Dask: Scale the Python tools you love. https://docs.dask.org/
- IBM. (2024, July 9). HPC. IBM. https://www.ibm.com/think/topics/hpc
- NetApp. (n.d.). What is high-performance computing (HPC)? How it works. NetApp. https://www.netapp.com/data-storage/high-performance-computing/what-is-hpc/
- Perez, M. (2019, August 6). What is web scraping and what is it used for? ParseHub Blog. https://www.parsehub.com/blog/what-is-web-scraping/
- Polars. (n.d.). User guide. https://docs.pola.rs/
- Rocklin, M. (2015). Dask: Parallel computation with blocked algorithms and task scheduling. Proceedings of the 14th Python in Science Conference (SciPy 2015), 130–136. -- https://doi.org/10.25080/Majora-7b98e3ed-013
- VanderPlas, J. (2016). Python data science handbook: Essential tools for working with data. O'Reilly Media. https://jakevdp.github.io/PythonDataScienceHandbook/
- Wikipedia contributors. (2019, October 4). Web scraping. Wikipedia. https://en.wikipedia.org/wiki/Web_scraping

## Appendices

### 📊 Performance Benchmark Code

| Figure | Description | Preview |
|--------|-------------|---------|
| **Figure 1** | Pandas Benchmark Pipeline | <img width="1053" height="439" alt="image" src="https://github.com/user-attachments/assets/b5943d20-4dd3-4de1-b5ee-0bbab6cde09f" /> |
| **Figure 2** | Dask Benchmark Pipeline | <img width="1058" height="459" alt="image" src="https://github.com/user-attachments/assets/edaa92d2-2e9c-4db1-bdf0-d0b224cc22f0" /> |
| **Figure 3** | Polars Lazy Benchmark Pipeline | <img width="927" height="586" alt="image" src="https://github.com/user-attachments/assets/a812fc0f-5fdc-4834-adb4-cc427461ab4a" /> |
| **Figure 4** | Benchmark Execution Engine & Results Tables | <img width="585" height="725" alt="image" src="https://github.com/user-attachments/assets/b08a371a-7da0-4cd7-9a0b-f3dee301fa40" /> |

---

### 📈 Performance Evaluation Charts
| Figure | Description | Preview |
|--------|-------------|---------|
| **Figure 5** | Performance Benchmark | <img width="595" height="526" alt="image" src="https://github.com/user-attachments/assets/235982a5-edac-419b-8644-ff990bd41a4d" /> |

---

### 🖥️ Output Screenshots

| Figure | Description | Preview |
|--------|-------------|---------|
| **Figure 6** | The Edge Scraper Terminal Output (93,378 records, 365s) | <img width="329" height="68" alt="image" src="https://github.com/user-attachments/assets/4321f532-98c0-4722-91a7-938f4b35b03f" /> |
| **Figure 7** | The Sun Scraper Output Preview (7,500 records) | <img width="379" height="52" alt="image" src="https://github.com/user-attachments/assets/07ae8040-7a61-41ee-a786-2ed69c870bbe" /> |
| **Figure 8** | Final Master Dataset Preview (100,887 records) | <img width="402" height="79" alt="image" src="https://github.com/user-attachments/assets/e3629056-1b14-469a-8c5c-ea2a3fe2458a" /> |
