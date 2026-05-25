<h1 align="center"> 
  Group scubscub — Web Scraping using BeautifulSoup
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>IMAN ABADI BIN MOHD NIZWAN</td>
    <td>A23CS0084</td>
  </tr>
  <tr>
    <td width=80%>MOHAMED ALIF FATHI BIN ABDUL LATIF</td>
    <td>A23CS0112</td>
  </tr>
  <tr>
    <td width=80%>DHESHIEGHAN A/L SARAVANA MOORTHY</td>
    <td>A23CS0072</td>
  </tr>
</table>
<br>

<h3 align="center">Libraries Used</h3>
<div align='center'>
  <img src='https://www.jeveuxetredatascientist.fr/wp-content/uploads/2022/06/BeautifulSoup.jpg' height=90 alt='BeautifulSoup'>
  &nbsp;&nbsp;&nbsp;
  <img src='https://curl.se/logo/curl-logo.svg' height=90 alt='curl_cffi'>
</div>

<br>

<p align="justify">
  Beautiful Soup is a Python library that is used for web scraping. It allows you to parse HTML or XML documents into a readable tree-like structure and extract data based on the document's elements and tags. With Beautiful Soup, users can easily navigate through webpages, search for specific classes or tags and retrieve important information such as text, links and attributes. It is commonly used together with libraries such as <code>requests</code> (or <code>curl_cffi</code> for browser impersonation) and <code>pandas</code> to automate data collection from websites.

The website that we will be using is from BookXcess. (https://www.bookxcess.com/)

BookXcess is one of the largest bookstore chains in Malaysia, well known for offering a massive catalogue of books across every genre often at heavily discounted prices. Their online store hosts an extensive product inventory with detailed information for each title, including the product ID, book title, author (listed as the vendor), product type (genre/category), SKU (ISBN), current price, original compare-at price, currency, weight in grams, tags, full HTML description, cover image and the date the product was created.
</p>

<p align="justify">
We plan to obtain data from the website by traversing its XML sitemap index, which links to multiple product sub-sitemaps containing every product URL on the site. By parsing these sitemaps with BeautifulSoup (using the <code>lxml</code> XML parser), we will collect all product page URLs and then fetch each product's structured data via its public <code>.json</code> endpoint. To handle the scale (over 150,000 products) we use <code>curl_cffi</code> with Chrome impersonation, a <code>ThreadPoolExecutor</code> with 40 concurrent workers, exponential-backoff retries on transient errors (429/503/etc.) and periodic partial CSV flushing to avoid data loss on long runs. Finally, we will consolidate everything into a clean CSV file using <code>pandas</code>. In summary, we will efficiently retrieve the full BookXcess product inventory and its associated metadata using these tools.
</p>

# Files in this folder

| File | Purpose |
|------|---------|
| [`main_crawler.ipynb`](main_crawler.ipynb) | End-to-end BookXcess scraper — sitemap traversal, concurrent product fetch, raw CSV output. |
| [`clean_data.ipynb`](clean_data.ipynb) | Cleans and validates `raw_data.csv`, producing the analysis-ready `cleaned_data.csv`. |
| [`optimize_pipeline.ipynb`](optimize_pipeline.ipynb) | Benchmarks six operations across Pandas, Polars, and PyArrow on the cleaned dataset. |

---

## 1. `main_crawler.ipynb` — BookXcess full inventory scraper

The full crawl is split into four sequential steps inside the notebook.

| Step | What it does |
|------|--------------|
| **Connection Test** | Sends a single `curl_cffi` request with Chrome impersonation to confirm BookXcess responds with a 200 before launching the full crawl. |
| **Step 1 — Collect every product URL** | Fetches the XML sitemap index, then each product sub-sitemap, parsing them with `BeautifulSoup` + `lxml` to harvest every product URL on the site. |
| **Step 2 — Concurrent product scrape** | Uses a `ThreadPoolExecutor` with **40 worker threads** to hit each product's public `.json` endpoint. Includes exponential-backoff retries on transient errors (429, 503, etc.) and periodic partial-CSV flushing so long runs don't lose data if interrupted. |
| **Step 3 — Save final CSV** | Consolidates all scraped product rows with `pandas` and writes the final `raw_data.csv`. |
| **Optional — Re-scrape failed URLs** | A retry pass over any URLs that did not return a successful response in Step 2. |

**Output**: `raw_data.csv` (~180 MB, 100,000+ products) — see [`../data/readme.md`](../data/readme.md) for the Google Drive link.

## 2. `clean_data.ipynb` — Data cleaning and validation

Transforms the raw CSV into the analysis-ready `cleaned_data.csv`. The notebook is organised as a numbered checklist:

1. **Load the raw CSV and audit for nulls** — sanity-check column counts and missing values.
2. **Rename columns and prep datatypes** — standardise column names and cast numerics.
3. **Strip HTML tags from the product description** — `BeautifulSoup` removes embedded markup so descriptions are plain text.
4. **Remove `[Bargain Corner]` prefix from titles** — common marketing prefix dropped for clean titles.
5. **Clean recurring `?` characters and stray whitespace** — applied across all text fields; empty strings normalised to `None`.
6. **Validate `author` and `publisher`** — strip dangling punctuation and reject obviously invalid names.
7. **Calculate discount and drop illogical price rows** — computes `discount_pct` and removes rows where `compare_price < current_price`.
8. **Final checks and save** — hard assertions on schema integrity, then writes `cleaned_data.csv`.

**Output**: `cleaned_data.csv` (~160 MB, 100,000+ valid rows). Final schema is documented in the last cell of the notebook.

## 3. `optimize_pipeline.ipynb` — Pandas vs Polars vs PyArrow benchmark

Runs the same six operations across three libraries to compare their performance on the cleaned dataset.

**Libraries benchmarked**: `pandas`, `polars`, `pyarrow`.

**Operations** (each executed in all three libraries):

1. Filter high-discount books
2. GroupBy publisher aggregation
3. String extract price tier (regex; PyArrow uses a named capture group)
4. Calculate savings (derived column)
5. Sort by discount and price
6. Top authors by average discount

**Metrics captured per run** (via `time` + `psutil`):

- Execution time (s)
- CPU utilisation — initial and final (%)
- Memory used (MB)
- Throughput (rows/s)

Each (library, operation) pair runs **3 times** and an `average` row is appended. Results are written to [`../p2/performance_before.csv`](../p2/performance_before.csv) (baseline Pandas) and [`../p2/performance_after.csv`](../p2/performance_after.csv) (optimised pipeline with all three libraries). Visualisations live in [`../p2/evaluation_charts.ipynb`](../p2/evaluation_charts.ipynb).


