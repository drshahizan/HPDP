# 📘 Big Data Management Assignment: Mastering Big Data Handling

**Group Members**:
- Student 1: Ahmad Ziyaad bin Mohd Abbas, A23CS0206

---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: *US Accidents (2016–2023)*
* **Source**: [Kaggle – sobhanmoosavi](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
* **Domain**: *Transportation / Road Safety*
* **File Size**: *3,058.2 MB* (~3.0 GB, confirmed by `os.path.getsize()` on the downloaded file — see Task 2)
* **Shape**: *7,728,394 rows × 46 columns* (full dataset). Benchmark runs in this notebook used a `MAX_ROWS = 500,000` cap so every strategy/library could be tested safely within Colab's free-tier RAM budget — see the note in Task 3.

### 📖 Description

The US Accidents dataset is a countrywide collection of traffic accident records covering 49 US states, collected continuously from February 2016 to March 2023 using multiple traffic APIs (state DOTs, law-enforcement feeds, traffic cameras, and road sensors). This dataset is ideal for big data handling experiments because:

* It comfortably exceeds the 700 MB requirement at ~3 GB uncompressed.
* It contains a genuine mix of data types: numeric (`Temperature(F)`, `Distance(mi)`), boolean road-feature flags (`Crossing`, `Junction`, `Bump`), low/high-cardinality categorical text (`State`, `Weather_Condition`, `City`), and datetime columns (`Start_Time`, `End_Time`).
* It has real, uneven missingness (e.g. `End_Lat`/`End_Lng` are known to be sparsely populated), which is representative of real-world messy data.
* It presents realistic memory and performance challenges when loaded naively with a single `pd.read_csv()` call.

### 🔍 Key Features

* Location data: `Start_Lat`, `Start_Lng`, `End_Lat`, `End_Lng`, `City`, `County`, `State`, `Zipcode`
* Time data: `Start_Time`, `End_Time`, `Weather_Timestamp`, `Sunrise_Sunset` and twilight flags
* Weather attributes: `Temperature(F)`, `Humidity(%)`, `Visibility(mi)`, `Wind_Speed(mph)`, `Precipitation(in)`, `Weather_Condition`
* Road-feature flags (boolean): `Amenity`, `Bump`, `Crossing`, `Give_Way`, `Junction`, `Railway`, `Roundabout`, `Station`, `Stop`, `Traffic_Calming`, `Traffic_Signal`
* Target/severity: `Severity` (1–4 scale)

### 📊 Data Column Description

The full schema has 46 columns; the table below groups them by category and highlights the columns actually used across the benchmarking strategies in Task 3.

| Category | Example Columns | Default Data Type(s) | Used in Benchmarks? |
| :--- | :--- | :--- | :--- |
| Identifiers | `ID`, `Source` | `object` | No |
| Severity | `Severity` | `int64` | ✅ Yes — target column throughout |
| Time | `Start_Time`, `End_Time`, `Weather_Timestamp` | `object` (parsed to datetime) | Partially |
| Location | `Start_Lat`, `Start_Lng`, `End_Lat`, `End_Lng`, `City`, `County`, `State`, `Zipcode` | `float64` / `object` | `State` ✅ |
| Distance | `Distance(mi)` | `float64` | ✅ Yes |
| Weather | `Temperature(F)`, `Humidity(%)`, `Visibility(mi)`, `Wind_Speed(mph)`, `Precipitation(in)`, `Weather_Condition` | `float64` / `object` | ✅ Yes (subset) |
| Road features | `Amenity`, `Bump`, `Crossing`, `Junction`, `Traffic_Signal`, etc. | `bool` | No |
| Daylight | `Sunrise_Sunset`, `Civil_Twilight`, `Nautical_Twilight`, `Astronomical_Twilight` | `object` | No |

---

## 📝 Task 2: Load and Inspect Data

### 🔹 Loading Strategy

The dataset was downloaded in Google Colab using **`kagglehub`**, which handles authentication and caching automatically (no manual `kaggle.json` upload needed once a Kaggle account is linked to the Colab environment):

```python
import kagglehub
path = kagglehub.dataset_download("sobhanmoosavi/us-accidents")
```

A fallback path also supports the classic Kaggle CLI method (`kaggle datasets download ...`) if `kagglehub` isn't available, and — if neither is configured — the notebook generates a schema-matched **synthetic** CSV so every downstream cell still runs for testing purposes. The actual submitted run used the real file, confirmed by the printed output:

```
Using DATA_PATH = /kaggle/input/us-accidents/US_Accidents_March23.csv
File size on disk: 3,058.2 MB
DEMO_MODE = False
```

### 🔹 Dataset Inspection

Rather than loading the full 3 GB file twice (once to "inspect" and again later to benchmark), Task 2 does a **cheap 5,000-row peek** — the expensive full loads are deferred to Task 3 Part 2, where they're properly benchmarked across all three libraries instead of being paid for twice.

```python
peek = pd.read_csv(DATA_PATH, nrows=5000)
print("Shape (5,000-row peek):", peek.shape)
print(peek.dtypes)
print(peek.isna().sum().sort_values(ascending=False).head(10))
```

#### 📐 Shape of the Peek Sample

```
Shape (5,000-row peek): (5000, 46)
```

#### 🏷️ Column Names and Data Types (excerpt)

```
ID                        object
Source                    object
Severity                   int64
Start_Time                object
End_Time                   object
Start_Lat                float64
Start_Lng                float64
End_Lat                  float64
End_Lng                  float64
Distance(mi)             float64
Description               object
Street                    object
City                      object
County                    object
...                          ...
```

#### 📌 First Rows (excerpt)

```
    ID   Source  Severity           Start_Time             End_Time  \
0  A-1  Source2         3  2016-02-08 05:46:00  2016-02-08 11:00:00
1  A-2  Source2         2  2016-02-08 06:07:59  2016-02-08 06:37:59
2  A-3  Source2         2  2016-02-08 06:49:27  2016-02-08 07:19:27
...
```

All 46 columns loaded as pandas' default (unoptimized) types on this peek — exactly the baseline that Strategy 3 (dtype optimization) and the library comparison in Part 2 improve on.

---

## 🛠️ Task 3: Apply Big Data Handling Strategies

> ⚠️ **`MAX_ROWS = 500,000`** was used for this run (out of 7,728,394 total rows) so that all eight loads below (5 strategies + 3 libraries) could run safely within Colab's free-tier RAM. All numbers reported are real, captured outputs from this run — not estimates.

### 🔹 **Part 1: Memory- and Performance-Efficient Techniques**

### 📊 Performance Measurement Setup

The `measure_performance()` function is a shared benchmarking utility used for every strategy and every library, so all eight approaches are compared on identical footing. It wraps a target loading function and, using `psutil`, records the process memory (RSS) delta before/after, wall-clock execution time, average CPU utilization (sampled on a background thread every 0.1s), and throughput (records/second). It also transparently `.compute()`s any Dask result and recognizes both pandas and Polars DataFrames when calculating throughput, so the exact same helper works across all three libraries.

**Code**:
```python
def measure_performance(func, description="", *args, **kwargs):
    process = psutil.Process(os.getpid())
    total_ram = psutil.virtual_memory().total / 1024 / 1024  # MB

    cpu_percent = []
    done = [False]

    def track_cpu():
        while not done[0]:
            cpu_percent.append(process.cpu_percent(interval=0.1))

    cpu_thread = threading.Thread(target=track_cpu)
    cpu_thread.start()

    mem_before = process.memory_info().rss / 1024 / 1024  # MB
    start_time = time.time()

    try:
        result = func(*args, **kwargs)
        success = True
        error_message = None
    except Exception as e:
        result = None
        success = False
        error_message = str(e)

    end_time = time.time()
    mem_after = process.memory_info().rss / 1024 / 1024  # MB
    done[0] = True
    cpu_thread.join()

    exec_time = round(end_time - start_time, 4)
    mem_diff_mb = mem_after - mem_before

    if isinstance(result, dd.DataFrame):
        result = result.compute()

    if isinstance(result, (pd.DataFrame, pl.DataFrame)):
        num_records = len(result)
        throughput = round(num_records / exec_time, 2) if exec_time > 0 else None
    else:
        throughput = None

    performance = {
        "Description": description,
        "Memory Used (MB)": round(mem_diff_mb, 2),
        "Execution Time (s)": exec_time,
        "Success": success,
        "Average CPU (%)": round(sum(cpu_percent) / len(cpu_percent), 2) if cpu_percent else 0.0,
        "Throughput (records/sec)": throughput,
    }
    if not success:
        performance["Error"] = error_message

    return performance, result
```

---

### 1. Load Less Data

**Code**:
```python
def load_less_data(filepath, nrows=None):
    selected_columns = ['Severity', 'State', 'Temperature(F)', 'Humidity(%)',
                         'Weather_Condition', 'Distance(mi)']
    df = pd.read_csv(filepath, usecols=selected_columns, nrows=nrows)
    return df[df['Severity'] >= 3]   # filter during processing

performance_less_data, df_less_data = measure_performance(
    load_less_data, description="Load Less Data with Pandas",
    filepath=DATA_PATH, nrows=MAX_ROWS
)
```

**Explanation**: Only 6 of the 46 columns are read from disk via `usecols`, and rows are filtered to higher-severity accidents (`Severity >= 3`) immediately after. Restricting the CSV parser to a handful of columns means the other 40 never enter RAM at all.

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Load Less Data with Pandas | 4.84 | 2.9494 | True | 43.46 | 63,556.32 |

`Filtered shape (Severity >= 3): (187453, 6)`

---

### 2. Use Chunking

**Code**:
```python
def load_with_chunking(filepath, nrows=None, chunk_size=100_000):
    chunks = []
    rows_read = 0
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        chunk.columns = chunk.columns.str.strip()
        chunks.append(chunk)
        rows_read += len(chunk)
        if nrows is not None and rows_read >= nrows:
            break
    df = pd.concat(chunks, ignore_index=True)
    if nrows is not None:
        df = df.iloc[:nrows]
    return df

performance_chunking, df_chunked = measure_performance(
    load_with_chunking, description="Chunked Load",
    filepath=DATA_PATH, nrows=MAX_ROWS
)
```

**Explanation**: The file is read in 100,000-row chunks (all 46 columns, unlike Strategy 1) and concatenated back together, stopping once the row cap is reached. Peak memory during the read loop never exceeds a single chunk's size, though the final `pd.concat()` briefly holds all chunks plus the merged result.

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Chunked Load | 279.89 | 5.3461 | True | 71.25 | 93,526.12 |

`Shape: (500000, 46)`

---

### 3. Optimize Data Types

**Code**:
```python
def optimized_load(filepath, usecols=None, dtype_map=None, nrows=None):
    df = pd.read_csv(filepath, usecols=usecols, dtype=dtype_map, nrows=nrows)
    return df

load_args = {
    "filepath": DATA_PATH,
    "usecols": ['Severity', 'State', 'Temperature(F)', 'Humidity(%)',
                'Visibility(mi)', 'Distance(mi)', 'Weather_Condition'],
    "dtype_map": {
        'Severity': 'int8', 'State': 'category', 'Temperature(F)': 'float32',
        'Humidity(%)': 'float32', 'Visibility(mi)': 'float32',
        'Distance(mi)': 'float32', 'Weather_Condition': 'category',
    },
    "nrows": MAX_ROWS,
}

performance_optimize_load, df_optimize_load = measure_performance(
    optimized_load, description="Optimized Load with Dtype", **load_args
)
```

**Explanation**: Numeric columns are downcast to `float32`/`int8` and low-cardinality text columns (`State`, `Weather_Condition`) are set to `category`, all specified directly via the `dtype` parameter at read time — avoiding pandas' default `float64`/`object` types entirely rather than converting after the fact.

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Optimized Load with Dtype | 35.71 | 0.9267 | True | 90.68 | 539,548.94 |

```
RangeIndex: 500000 entries, 0 to 499999
Data columns (total 7 columns):
 #   Column             Non-Null Count   Dtype
---  ------             --------------   -----
 0   Severity           500000 non-null  int8
 1   Distance(mi)       500000 non-null  float32
 2   State              500000 non-null  category
 3   Temperature(F)     492750 non-null  float32
 4   Humidity(%)        492085 non-null  float32
 5   Visibility(mi)     489461 non-null  float32
 ...
```

This was by far the **fastest and highest-throughput** strategy of the five — reading fewer columns *and* at their final compact dtype in one pass avoids both excess I/O and a later, separate conversion step.

---

### 4. Sampling

**Code**:
```python
def sampling(filepath, sample_fraction=0.1, usecols=None, dtype_map=None, nrows=None):
    df = pd.read_csv(filepath, usecols=usecols, dtype=dtype_map, nrows=nrows)
    return df.sample(frac=sample_fraction, random_state=42)

performance_sampling, df_sampling = measure_performance(
    sampling, description="Sampling",
    filepath=DATA_PATH, sample_fraction=0.1, nrows=MAX_ROWS
)
```

**Explanation**: All 46 columns of the 500,000-row cap are loaded first, then 10% is randomly sampled with a fixed `random_state` for reproducibility. As expected, the full (capped) load has to happen *before* sampling can occur, so this strategy doesn't avoid the initial read cost.

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Sampling | -9.70 | 5.9647 | True | 96.81 | 8,382.65 |

`Rows: 50000`

*Note on the negative memory figure*: a negative RSS delta means the process's measured memory was lower **after** the call than before — most likely because Python/pandas garbage-collected memory from a previous cell's DataFrame during this call's execution window, rather than this strategy somehow using "negative" memory. This is a known limitation of single-process RSS-delta measurement discussed further in Task 4.

---

### 5. Parallel Processing with Dask

**Code**:
```python
def optimized_load_dask(filepath, usecols=None, dtype_map=None, nrows=None, blocksize='64MB'):
    safe_dtype_map = {col: 'object' for col in dtype_map} if dtype_map else None
    ddf = dd.read_csv(filepath, usecols=usecols, dtype=safe_dtype_map,
                       on_bad_lines="skip", blocksize=blocksize)
    ddf.columns = ddf.columns.str.strip()

    if dtype_map:
        for col, target_type in dtype_map.items():
            ddf[col] = ddf[col].map_partitions(
                lambda s, t=target_type: pd.to_numeric(s, errors='coerce').astype(t)
                if t not in ('category', 'object') else s.astype(t),
                meta=(col, 'float64' if target_type not in ('category', 'object') else 'object')
            )

    if nrows is not None:
        return ddf.head(nrows, npartitions=-1)
    return ddf.compute()

performance_dask_strategy, df_dask_strategy = measure_performance(
    optimized_load_dask, description="Parallel with Dask",
    filepath=DATA_PATH,
    usecols=['Severity', 'State', 'Temperature(F)', 'Humidity(%)', 'Distance(mi)'],
    dtype_map={'Severity': 'int8', 'Temperature(F)': 'float32',
               'Humidity(%)': 'float32', 'Distance(mi)': 'float32'},
    nrows=MAX_ROWS
)
```

**Explanation**: The file is read lazily in 64MB partitions via `dask.dataframe`, with per-partition dtype conversion applied in parallel via `map_partitions`, before materializing the result. Average CPU of **118.88%** (over 100%) confirms genuine multi-core engagement across partitions.

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Parallel with Dask | 38.63 | 32.8425 | True | 118.88 | 15,224.18 |

`Shape: (500000, 5)`

Despite low memory and confirmed parallelism, this was the **slowest** of the five strategies — the task-scheduling and partition-coordination overhead outweighs its benefits at this row count on a single machine.

---

### 🔹 **Part 2: Loading Dataset with Different Libraries**

This part isolates the **library** itself: a plain, unoptimized full load (within the same `MAX_ROWS = 500,000` cap) benchmarked once with each of Pandas, Polars, and Dask.

#### 1. Using **Pandas**

```python
def load_full_pandas(filepath, nrows=None):
    return pd.read_csv(filepath, nrows=nrows)

performance_pandas_full, df_pandas_full = measure_performance(
    load_full_pandas, description="Load with Pandas", filepath=DATA_PATH, nrows=MAX_ROWS
)
```

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Load with Pandas | 279.20 | 2.5808 | True | 96.21 | 193,738.38 |

#### 2. Using **Polars**

```python
def load_full_polars(filepath, n_rows=None):
    return pl.read_csv(filepath, n_rows=n_rows)

performance_polars_full, df_polars_full = measure_performance(
    load_full_polars, description="Load with Polars", filepath=DATA_PATH, n_rows=MAX_ROWS
)
```

**Explanation**: Polars parses CSVs across multiple threads automatically, with no configuration required, and stores data column-by-column internally rather than row-by-row.

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Load with Polars | 7,299.50 | 9.8531 | True | 172.43 | 50,745.45 |

#### 3. Using **Dask**

```python
def load_full_dask(filepath, nrows=None):
    ddf = dd.read_csv(filepath, assume_missing=True, on_bad_lines='skip',
                       dtype=str, blocksize='64MB')
    if nrows is not None:
        return ddf.head(nrows, npartitions=-1)
    return ddf.compute()

performance_dask_full, df_dask_full = measure_performance(
    load_full_dask, description="Load with Dask", filepath=DATA_PATH, nrows=MAX_ROWS
)
```

**Output**:

| Description | Memory Used (MB) | Execution Time (s) | Success | Average CPU (%) | Throughput (records/sec) |
|---|---|---|---|---|---|
| Load with Dask | -3,695.73 | 57.9638 | True | 123.76 | 8,626.07 |

### Summary — Part 2

| Library | Loading Style | Parallelism | Key Parameter |
|---|---|---|---|
| **Pandas** | Eager, single-threaded | None | `pd.read_csv()` |
| **Polars** | Eager, multi-core | Automatic (Rust) | `n_rows=` for row cap |
| **Dask** | Lazy, partition-based | Multi-threaded | `blocksize="64MB"` |

---

## 📊 Task 4: Comparative Analysis

### 🔍 Part 1: Comparison of the Five Strategies

All figures below are for a `MAX_ROWS = 500,000` slice of the 7,728,394-row dataset.

#### Summary Table

| Strategy | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (rec/s) |
|---|---|---|---|---|
| 1 — Load Less Data | 4.84 | 2.9494 | 43.46 | 63,556.32 |
| 2 — Chunking | 279.89 | 5.3461 | 71.25 | 93,526.12 |
| 3 — Dtype Optimization | 35.71 | 0.9267 | 90.68 | 539,548.94 |
| 4 — Sampling | -9.70 | 5.9647 | 96.81 | 8,382.65 |
| 5 — Parallel (Dask) | 38.63 | 32.8425 | 118.88 | 15,224.18 |

*(See the "Task 4" section of `big_data.ipynb` for the live-rendered 2×2 bar charts — Memory, Time, Avg CPU%, Throughput — built directly from these captured values.)*

#### Analysis

- **Strategy 3 (Dtype Optimization)** was the clear standout: lowest execution time (**0.93s**) and by far the highest throughput (**539,549 rec/s**) among the five, while using only **35.71 MB**. Reading fewer columns *and* at their final compact dtype in a single pass avoids both wasted I/O and a later conversion step.
- **Strategy 1 (Load Less Data)** used the least memory of all five (**4.84 MB**) since only 6 of 46 columns were ever parsed, though its throughput (63,556 rec/s) was lower than Strategy 3's because it lacks the dtype optimization on top.
- **Strategy 2 (Chunking)** used substantially more memory (**279.89 MB**) than Strategies 1 and 3 — it reads all 46 columns (unlike Strategy 1) and briefly holds both the individual chunks and the concatenated result at once.
- **Strategy 4 (Sampling)** was the slowest relative to the amount of data actually returned (only 50,000 rows) since the full 500,000-row, 46-column frame has to be loaded *before* `.sample()` can run — the memory/time cost of the initial load dominates.
- **Strategy 5 (Dask)** confirmed genuine multi-core parallelism (**118.88% avg CPU**, i.e. more than one core actively engaged) and used relatively little memory (**38.63 MB**, since only 5 columns were selected), but was the **slowest strategy overall** (**32.84s**) — the task-scheduling and partition-coordination overhead dominates at this scale on a single machine.

#### Interpretation

For a dataset of this size on a single Colab instance, **Dtype Optimization gives the best all-round result** — it doesn't require sacrificing rows (unlike Sampling) or paying a coordination tax (unlike Dask), and it comfortably beats plain column-selection (Load Less Data) once the dtype conversion is folded into the same read call. Chunking and Dask both remain valuable specifically when the *full* file doesn't fit in memory at all — a constraint this 500,000-row slice doesn't actually hit, which is why their overhead shows up here without their main benefit (handling data that genuinely exceeds RAM).

---

### 📊 Part 2: Full-Load Performance Across Libraries

#### Summary Table

| Library | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (rec/s) |
|---|---|---|---|---|
| **Pandas** | 279.20 | 2.5808 | 96.21 | 193,738.38 |
| **Polars** | 7,299.50 | 9.8531 | 172.43 | 50,745.45 |
| **Dask** | -3,695.73 | 57.9638 | 123.76 | 8,626.07 |

*(See the "Task 4" section of `big_data.ipynb` for the corresponding 2×2 bar charts.)*

#### Analysis

- **Pandas** was, somewhat counter-intuitively, both the **fastest** (**2.58s**) and **lowest-memory** (**279.2 MB**) of the three libraries for this particular 500,000-row load. This does **not** match the general expectation that Polars/Dask outperform Pandas — see the interpretation below for why.
- **Polars** reported by far the **highest memory figure** (**7,299.5 MB**) despite processing the same 500,000 rows as Pandas. Its execution time (**9.85s**) and CPU usage (**172.43%**, confirming multi-core activity) were also both higher than Pandas'.
- **Dask** reported a **negative memory delta** (**-3,695.73 MB**) and was the **slowest** of the three (**57.96s**), with CPU usage of **123.76%** confirming parallel execution across partitions.

#### 🧠 Interpretation — reading these results honestly

These particular numbers **do not match the typical pattern** reported in most Pandas-vs-Polars-vs-Dask benchmarks (where Polars is usually fastest and lowest-memory for a full load). Two things are almost certainly happening at once, and both are worth naming explicitly rather than glossing over:

1. **First-call initialization cost.** This was the *first* time Polars and Dask were invoked in the session (aside from the smaller, column-limited Strategy 5 call). Both libraries spin up their own multi-threaded runtimes and memory allocators on first use — Polars' Rust-based thread pool and Dask's task scheduler both carry a one-time setup cost that a single-shot `measure_performance()` call attributes entirely to that one function call, inflating its reported memory and time relative to steady-state, repeated-call performance.
2. **RSS-delta measurement noise across multi-threaded libraries.** `measure_performance()` measures whole-process memory (RSS) before and after each call. For single-threaded Pandas this is a fairly clean signal. For Polars and Dask, background threads/worker processes can allocate and free memory outside the main thread's immediately-visible footprint, and glibc's memory allocator frequently does not return freed memory to the OS immediately — so a large positive spike (Polars) or an apparent large negative drop (Dask, if the OS reclaimed memory from a *previous* call during this call's measurement window) can both appear without reflecting the "true" data footprint of that one load.

**Practical takeaway:** for a fair, general-purpose comparison, each library should ideally be benchmarked with a warm-up call (to absorb one-time initialization costs) and averaged over multiple repeated runs — something worth doing in a follow-up if these results are used for anything beyond this assignment's illustrative purpose. As captured, this run's numbers are a real, honest record of *this specific single execution*, but shouldn't be read as a definitive verdict on which library is "better" in general.

---

## 🧠 Task 5: Conclusion & Reflection

### 🔹 Summary of Observations

Applying five pandas-based strategies and benchmarking three libraries against the US Accidents dataset (3.0 GB, 7,728,394 rows — benchmarked here on a 500,000-row cap for RAM safety) surfaced several concrete lessons:

- **Dtype Optimization** was the best all-round pandas strategy: fastest (0.93s), highest throughput (539,549 rec/s), and low memory (35.71 MB), all without sacrificing any rows.
- **Load Less Data** was the most memory-efficient strategy outright (4.84 MB) by loading only 6 of 46 columns, at the cost of not having those other columns available at all.
- **Chunking** avoided ever holding the *entire* file in memory at once, but for a 500,000-row slice that already fits comfortably in RAM, its `pd.concat()` step meant it used more memory (279.89 MB) than the two strategies above.
- **Sampling** is only as fast as the load it's sampling from — the full capped dataset had to be loaded before the 10% sample could be drawn, so its cost reflects a full load, not a sample-sized one.
- **Dask (Strategy 5)** confirmed genuine multi-core execution (118.88% CPU) but was the slowest strategy, reinforcing that its real advantage is scaling *past* a single machine's RAM, not raw speed on data that already fits.
- Comparing libraries directly for a full load surfaced results that **contradicted the usual "Polars/Dask beat Pandas" expectation** — Pandas was fastest and lowest-memory in this particular run. Rather than conclude Pandas is "better," Task 4 identifies this as most likely a first-call initialization and RSS-measurement artifact specific to Polars/Dask's multi-threaded runtimes, not a general result.

### 🔹 Benefits & Limitations

#### Part 1: Strategies

| Strategy | Benefits | Limitations |
|---|---|---|
| Load Less Data | Simple, lowest memory of the five strategies tested | Only 6/46 columns available; must know requirements upfront |
| Chunking | Never holds the full file in memory during the read loop | `pd.concat()` step still spikes memory; slower than direct optimized reads for data that fits in RAM |
| Dtype Optimization | Best speed/throughput/memory balance among the five strategies; no rows or columns sacrificed | Requires knowing sensible dtypes per column in advance; risk of precision loss if downcast too aggressively |
| Sampling | Fast to iterate on the resulting smaller sample | Full (capped) load still has to happen first; not useful purely as a loading optimization |
| Parallel Processing (Dask) | Confirmed genuine multi-core use; scales to files that don't fit in RAM at all | Task-scheduling overhead makes it the slowest option here; real benefit only appears once data exceeds a single machine's memory |

#### Part 2: Libraries

| Library | Benefits | Limitations |
|---|---|---|
| Pandas | Simplest, most familiar API; fastest and lowest-memory in this specific run | Single-threaded; typically the most memory-hungry library at larger scale/more repeated calls |
| Polars | Multi-threaded by default; pandas-like API | High reported memory/time here, likely inflated by first-call thread-pool initialization overhead |
| Dask | Scales beyond a single machine's RAM; can run on a real cluster | Slowest of the three here; task-graph/scheduling overhead dominates for data that already fits in memory |

### 🔹 Reflection

This assignment made the trade-offs between simplicity, speed, memory, and exactness concrete rather than theoretical. Perhaps the most valuable lesson came from a result that *didn't* match expectations: the library comparison in Task 4 Part 2 showed Pandas outperforming Polars and Dask, which is the opposite of what's usually reported. Rather than discard or "fix" that result, we treated it as real data and reasoned through *why* it might have happened (first-call initialization costs, RSS-measurement noise around multi-threaded runtimes) — which taught us more about how to benchmark responsibly than a "clean" result would have. The broader takeaway is that *which* library and *which* loading strategy are two separate, stackable decisions, and that any single benchmarking run — ours included — should be read as one data point, not a universal verdict.

---

## 📁 Folder Structure

```plaintext
bdm/your_group/
├── big_data.md        ← This file
├── readme.md          ← Brief intro and links
└── big_data.ipynb     ← Code notebook
```
