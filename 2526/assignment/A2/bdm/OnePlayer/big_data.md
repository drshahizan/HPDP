# 📘 Assignment 2: Mastering Big Data Handling

**Group Information**
- Group Name: OnePlayer

| Name | Matric Number |
|---|---|
| Muhammad Afiq Danish bin Mohd Hazni | A23CS0118 |

---

## 📝 1. Dataset Description

### 📌 Dataset Overview

* **Dataset Name**: *Cell Towers Worldwide: Location Data by Continent (Asia)*
* **Source**: [Kaggle - zakariaeyoussefi](https://www.kaggle.com/datasets/zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent) 
* **File**: *Asia towers.csv*
* **File Size**: *~1.46 GB*
* **Domain**: *Telecommunications / Network Infrastructure*
* **Number of Records**: *13.38 million rows × 18 columns* 

This dataset contains geographical and technical information of cell towers located across Asia.
It is sourced from OpenCelliD, the world's largest open database of cell towers, and is 
well-suited for large-scale data processing analysis due to its size and diversity of column 
types including integers, floats, strings, and categorical values.

### 🔍 Key Features
- Over 13 million cell tower records across Asia
- Covers multiple radio technologies including GSM, LTE, UMTS and NR
- Contains both geographical coordinates and network metadata
- Includes categorical columns suitable for data type optimisation
- Rich enough for exploratory analysis including groupby, aggregation and filtering operations

### 📊 Column Descriptions

| Column | Data Type | Description |
|---|---|---|
| **Radio** | object | The generation of broadband cellular network technology (e.g., LTE, GSM) |
| **MCC** | int64 | Mobile Country Code, a unique identifier for each country in the mobile network |
| **MNC** | int64 | Mobile Network Code, identifying the mobile network within a country |
| **TAC** | int64 | Location Area Code, Tracking Area Code, or Network Identifier |
| **CID** | int64 | Unique identifier for each Base Transceiver Station (BTS) or sector |
| **LON** | float64 | Geographic coordinate specifying the east-west position |
| **LAT** | float64 | Geographic coordinate specifying the north-south position |
| **RANGE** | int64 | Approximate area within which the cell coverage extends (in meters) |
| **SAM** | int64 | Number of measures processed to derive the data point |
| **changeable** | int64 | Indicates if the cell location was determined through sample processing (1) or directly obtained from the telecom firm (0) |
| **created** | int64 | Timestamp indicating when the cell was first added to the database (UNIX format) |
| **updated** | int64 | Timestamp indicating when the cell was last seen or updated in the database (UNIX format) |
| **averageSignal** | int64 | Represents the averaged signal strength of the cell location |
| **Country** | object | The country of the cell tower |
| **Network** | object | The company that owns the cell tower |
| **Continent** | object | The continent of the cell tower |

---

## 📔 2. Library Choices

### Library 1: Pandas
Pandas is the most widely used data manipulation library in Python. It serves as the 
baseline for this assignment, providing a reference point for performance comparison 
against scalable libraries. All strategies are first implemented in Pandas before being 
compared against Dask and Polars.

### Library 2: Dask
Dask was selected as the second library because it mirrors the Pandas API closely, 
making it straightforward to implement equivalent operations. Dask is designed to handle 
datasets that are too large to fit into memory by breaking them into smaller partitions 
and processing them in parallel across multiple CPU cores. This makes it particularly 
suitable for large CSV files like the Asia towers dataset.

### Library 3: Polars
Polars was selected as the third library because of its exceptional performance on large 
datasets. Written in Rust, Polars is designed from the ground up for speed and efficiency. 
It supports lazy evaluation, allowing it to optimise query plans before execution, and 
natively utilises all available CPU cores for parallel processing. Its distinct type system 
and memory management also make it an interesting contrast to both Pandas and Dask.

---

## 📝 Task 2: Load and Inspect Data

### 🔹 2.1 Loading Strategy
To load the dataset efficiently in [Google Colab](https://colab.research.google.com/), the following steps were taken:

**Step 1: Upload Kaggle API Credentials**
The `kaggle.json` file was uploaded via the Colab file upload feature to authenticate 
with the Kaggle API.

```python
from google.colab import files
files.upload()
```

**Step 2: Configure Kaggle API Credentials**
The uploaded file was moved to the `.kaggle` directory and permissions were set.

```python
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
```

**Step 3: Download Dataset from Kaggle**
Only the Asia towers CSV file was downloaded using the `-f` flag to avoid downloading 
all continent files.

```python
!kaggle datasets download \
    -d zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent \
    -f "Asia towers.csv" \
    --force
```

**Step 4: Unzip the Dataset**
The downloaded ZIP file was extracted.

```python
!unzip "Asia%20towers.csv.zip"
```

**Step 5: Save to Google Drive**
The dataset was copied to Google Drive for persistent storage across sessions to avoid 
re-downloading every time the Colab runtime resets.

```python
shutil.copy("Asia towers.csv", "/content/drive/MyDrive/HPDP_A2/Asia towers.csv")
```

**Step 6: Set File Path**
The file path was set to point directly to Google Drive for all subsequent operations.

```python
file_path = "/content/drive/MyDrive/HPDP_A2/Asia towers.csv"
```
### 🔹 2.2 Initial Data Loading
The dataset was loaded using Pandas with `nrows=1000000` for initial inspection to 
avoid excessive memory consumption during the inspection phase.

```python
df = pd.read_csv(file_path, nrows=1000000)
```

### 🔹 2.3 Inspection Results

#### Dataset Shape
```python
print("=== Dataset Shape ===")
print(f"Rows    : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]}")
```
<img width="185" height="60" alt="image" src="https://github.com/user-attachments/assets/a5a5ea1f-db1b-4087-bafc-f38d6f23670a" />

#### Column Names and Data Types
```python
print("=== Column Names and Data Type ===")
print(df.dtypes.to_string())
```
<img width="276" height="338" alt="image" src="https://github.com/user-attachments/assets/8e7ddc63-91a9-4bde-8389-dcf469cdbcc0" />

#### Missing Values Summary
```python
print("=== Missing Values Summary ===")
missing = df.isnull().sum()
print(missing)
```
<img width="254" height="362" alt="image" src="https://github.com/user-attachments/assets/badae365-6b91-4d50-88d5-a1fcd533850c" />

> ✅ The dataset contains **no missing values** across all 18 columns, indicating a 
clean and complete dataset that requires no imputation or missing value handling.

#### First 5 Rows Preview
```python
print("=== First 5 Rows Preview ===")
df.head()
```
<img width="1285" height="222" alt="image" src="https://github.com/user-attachments/assets/63c09bd7-1e5a-4590-905c-ef4b29a842f9" />

---

## 🛠️ Task 3: Apply Big Data Handling Strategies

### 3.1 Performance Measurement Function Setup

Before implementing the strategies, a custom performance measurement function is set up 
to automatically track and record execution time and memory usage for every strategy 
function. The results are auto-saved to Google Drive after every run to prevent data 
loss across sessions.

#### Results Storage Setup
The following code checks if a previous results file exists in Google Drive and loads 
it. If not, it starts a fresh results list.

```python
RESULTS_PATH = "/content/drive/MyDrive/HPDP_A2/performance_results.csv"

if os.path.exists(RESULTS_PATH):
    performance_results = pd.read_csv(RESULTS_PATH).to_dict('records')
    print(f"✅ Loaded {len(performance_results)} existing results from Drive!")
else:
    performance_results = []
    print("✅ Starting fresh performance results!")
```

#### Performance Measurement Decorator
The `measure_performance` decorator is applied to every strategy function. It 
automatically measures and records the following metrics:

```python
def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss / 1024**2

        tracemalloc.start()
        start = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start
        _, mem_peak_traced = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        mem_after = process.memory_info().rss / 1024**2
        mem_peak_traced = mem_peak_traced / 1024**2
        mem_peak = mem_peak_traced if mem_peak_traced > 0 else mem_after

        if isinstance(result, pd.DataFrame):
            df_mem = result.memory_usage(deep=True).sum() / 1024**2
        elif isinstance(result, pl.DataFrame):
            df_mem = result.estimated_size() / 1024**2
        elif isinstance(result, dd.DataFrame):
            df_mem = result.memory_usage(deep=True).sum().compute() / 1024**2
        else:
            df_mem = 0.0

        performance_results.append({
            'Strategy'           : strategy,
            'Library'            : library,
            'Total Time (s)'     : round(total_time, 4),
            'Memory Before (MB)' : round(mem_before, 2),
            'Memory After (MB)'  : round(mem_after, 2),
            'Memory Peak (MB)'   : round(mem_peak, 2) if mem_peak is not None else 'N/A',
            'DataFrame Size (MB)': round(df_mem, 2)
        })

        pd.DataFrame(performance_results).to_csv(RESULTS_PATH, index=False)
        return result
    return wrapper
```

#### Implementation Summary
- **Execution Time**: Measured using `time.time()` before and after the function runs
- **Memory Before**: Actual RAM usage of the Python process before execution using `psutil`
- **Memory After**: Actual RAM usage of the Python process after execution using `psutil`
- **Memory Peak**: Peak memory allocated during execution using `tracemalloc`
- **DataFrame Size**: Memory usage which is the actual size of the resulting DataFrame in memory
- **Auto-save**: Results are saved to Google Drive as `performance_results.csv` after every run
- **Auto-load**: Previous results are loaded from Drive on session reconnect
- **Library Detection**: Library and strategy names are automatically parsed from the function name

### 3.2 Strategy 1: Load Less Data

**Code:**

```python
SELECTED_COLS = ['radio', 'MCC', 'MNC', 'TAC', 'LON', 'LAT', 'RANGE', 'created', 'updated']

@measure_performance
def load_less_data_pandas():
    return pd.read_csv(file_path, usecols=SELECTED_COLS, nrows=1000000)

df_less = load_less_data_pandas()
```

**Explanation:**

When working with large datasets, it is often unnecessary to load all available columns 
into memory. By selecting only the relevant columns using the `usecols` parameter and 
limiting the number of rows to 1,000,000 using `nrows`, both memory usage and load time 
can be significantly reduced compared to loading the full dataset with all 18 columns.

**Implementation Summary:**

- Only 12 out of 18 columns were loaded using `usecols`
- Only the first 1,000,000 rows were read using `nrows`
- Columns loaded from the CSV: `radio`, `MCC`, `MNC`, `TAC`, `LON`, `LAT`, `RANGE`, `created`, `updated`

**Output:**

<img width="908" height="132" alt="image" src="https://github.com/user-attachments/assets/635f7e7b-caaa-46af-90f3-2aea61c9b328" />

### 3.3 Strategy 2: Chunking

**Code:**

```python
@measure_performance
def chunking_pandas():
    chunk_size = 100000
    chunks = []

    for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)
    return df

df_chunked = chunking_pandas()
```

**Explanation:**

Instead of loading the full dataset in a single operation, chunking reads the data in 
smaller manageable portions of 100,000 rows at a time. The `low_memory=False` parameter 
ensures consistent data type inference for `Network` column across all chunks by reading the entire column 
before deciding its type. Each chunk is appended to a list and combined into a single 
DataFrame using `pd.concat()` at the end. This ensures that only a small portion of the 
dataset exists in memory at any one time, making it possible to process files that are 
larger than the available RAM.

**Implementation Summary:**

- Chunk size of 100,000 rows per chunk
- `low_memory=False` is used to ensure consistent data type inference for `Network` column due to its mixed data types
- Each chunk is appended to a list and combined at the end using `pd.concat()`
- Full dataset is loaded without any row limit

**Output:**

<img width="865" height="137" alt="image" src="https://github.com/user-attachments/assets/b9252ccc-f37b-4211-9bfd-606ed62af23b" />

### 3.4 Strategy 3: Data Type Optimisation

**Code:**

**Step 1: Load dataset with default data types to observe column types before optimisation:**
```python
df_before = pd.read_csv(file_path, nrows=1000000)

print("\n=== Data Types Before Optimisation ===")
print(df_before.dtypes.to_string())
```

**Step 2: Define optimised data types for each column:**
```python
OPTIMISED_DTYPES = {
    'Unnamed: 0'   : 'int32',    # Row index — fits in int32
    'radio'        : 'category', # Repeated strings e.g. GSM, LTE, UMTS
    'MCC'          : 'int16',    # Mobile country code — small integer
    'MNC'          : 'int16',    # Mobile network code — small integer
    'TAC'          : 'int16',    # Tracking area code — fits in int16
    'CID'          : 'int32',    # Cell ID — fits in int32
    'unit'         : 'int16',    # Small integer
    'LON'          : 'float32',  # Longitude — float32 sufficient
    'LAT'          : 'float32',  # Latitude — float32 sufficient
    'RANGE'        : 'int16',    # Range in metres — fits in int16
    'SAM'          : 'int16',    # Sample count — fits in int16
    'changeable'   : 'int8',     # Binary-like flag — int8 sufficient
    'created'      : 'int32',    # Timestamp — fits in int32
    'updated'      : 'int32',    # Timestamp — fits in int32
    'averageSignal': 'int16',    # Signal strength — small integer
    'Country'      : 'category', # Repeated country names
    'Network'      : 'category', # Repeated network names
    'Continent'    : 'category', # Repeated continent names
}
```

**Step 3: Load dataset with optimised data types:**
```python
@measure_performance
def data_type_optimisation_pandas():
    df = pd.read_csv(
        file_path,
        dtype=OPTIMISED_DTYPES,
        nrows=1000000
    )
    return df

df_optimised = data_type_optimisation_pandas()

print("\n=== Data Types After Optimisation ===")
print(df_optimised.dtypes.to_string())
```

**Explanation:**

When Pandas loads a CSV file, it assigns default data types to each column which are 
often wasteful. For example, integer columns are stored as `int64` by default even when 
the values are small enough to fit in `int16` or `int8`. Similarly, columns with 
repeated string values such as `radio`, `Country`, `Network` and `Continent` are stored 
as `object` type which consumes significantly more memory than the `category` type. By 
specifying optimised data types using the `dtype` parameter at load time, the memory 
footprint of the dataset is significantly reduced before any processing begins.


**Implementation Summary:**

- Default data types are first observed without performance measurement
- Integer columns downcast from `int64` to `int32`, `int16` or `int8` based on value range
- Float columns downcast from `float64` to `float32` for coordinate columns
- String columns with repeated values converted to `category` type
- Optimised types are applied at load time using the `dtype` parameter
- Performance is only measured after optimisation using `measure_performance`

**Output:**

Before Optimisation:

<img width="322" height="340" alt="image" src="https://github.com/user-attachments/assets/6299619a-16d3-4ad6-9a55-7cdf2c04d1bb" />

After Optimisation:

<img width="955" height="139" alt="image" src="https://github.com/user-attachments/assets/7671b973-667d-4490-b745-0115d2419a3b" />

<img width="300" height="340" alt="image" src="https://github.com/user-attachments/assets/4572bf62-93fc-48f1-ad44-acb42b64e433" />

### 3.5 Strategy 4: Sampling

**Code:**

```python
@measure_performance
def sampling_pandas():
    df = pd.read_csv(file_path, low_memory=False)
    df_sample = df.sample(frac=0.1, random_state=42)
    return df_sample

df_sampled = sampling_pandas()
print(f"Shape: {df_sampled.shape}")
```

**Explanation:**

Instead of working with the full dataset, sampling selects a random representative 
subset for analysis. The full dataset is first loaded using `low_memory=False` to 
ensure consistent data type inference, then 10% of the rows are randomly selected 
using the `sample()` method. The `random_state=42` parameter ensures reproducibility, 
meaning the same sample is selected every time the code is run. This dramatically 
shortens development cycles and makes exploratory analysis feasible even on very 
large datasets.

**Implementation Summary:**

- Full dataset is loaded using `low_memory=False` to avoid mixed type warnings for `Network` column
- 10% of rows are randomly sampled using `frac=0.1`
- `random_state=42` is used to ensure reproducibility
- The sample is large enough to be statistically representative while being small 
enough to process instantly

**Output:**

<img width="868" height="149" alt="image" src="https://github.com/user-attachments/assets/cc9fc733-72b1-4ac8-bc64-815d8da57090" />

### 3.6 Strategy 5: Parallel Processing with Scalable Libraries

Parallel processing involves distributing computational tasks across multiple processor 
cores simultaneously. Unlike standard Pandas which is single-threaded, Dask and Polars 
are built to exploit multiple CPU cores automatically, resulting in faster processing 
times for large datasets. In this strategy, the same five operations are implemented 
across all three libraries to enable a direct performance comparison.


#### Operation 1: Load Full Data

**Code:**

**Pandas:**
```python
@measure_performance
def load_full_data_pandas():
    df = pd.read_csv(file_path, low_memory=False)
    return df

df_pandas_full = load_full_data_pandas()
print(f"Shape: {df_pandas_full.shape}")
```

**Dask:**
```python
@measure_performance
def load_full_data_dask():
    df = dd.read_csv(file_path, assume_missing=True, low_memory=False)
    df = df.compute()
    return df

df_dask_full = load_full_data_dask()
print(f"Shape: {df_dask_full.shape}")
```

**Polars:**
```python
@measure_performance
def load_full_data_polars():
    df = pl.read_csv(file_path)
    return df

df_polars_full = load_full_data_polars()
print(f"Shape: {df_polars_full.shape}")
```

**Explanation:**

The full dataset is loaded using all three libraries to establish a direct performance 
comparison. Pandas loads the file sequentially using a single thread with `low_memory=False` 
to ensure consistent data type inference. Dask splits the file into partitions and processes 
them in parallel using `assume_missing=True` to handle potential missing values across 
partitions, with `.compute()` triggering the actual execution. Polars loads the file 
natively using all available CPU cores without any additional configuration required.

**Implementation Summary:**

- **Pandas** - single-threaded sequential loading with `low_memory=False`
- **Dask** - parallel partitioned loading with `assume_missing=True` and `.compute()` to trigger execution
- **Polars** - native parallel loading with automatic CPU core utilisation
- All three libraries load the full dataset without any row limit

**Output:**

Pandas:

<img width="904" height="113" alt="image" src="https://github.com/user-attachments/assets/2a9b98a8-dfd3-4b52-afe1-7a73d9430483" />

Dask:

<img width="884" height="109" alt="image" src="https://github.com/user-attachments/assets/0b659f9d-4964-4908-8ad6-92ed1d49426d" />

Polars:

<img width="891" height="111" alt="image" src="https://github.com/user-attachments/assets/ba513334-47a3-4627-8009-61cfddf8183c" />

#### Operation 2: Load Less Data

**Code:**

**Dask:**
```python
@measure_performance
def load_less_data_dask():
    df = dd.read_csv(file_path, usecols=SELECTED_COLS, assume_missing=True, low_memory=False)
    df = df.compute()
    return df

df_dask_less = load_less_data_dask()
print(f"Shape: {df_dask_less.shape}")
```

**Polars:**
```python
@measure_performance
def load_less_data_polars():
    df = pl.read_csv(file_path, columns=SELECTED_COLS)
    return df

df_polars_less = load_less_data_polars()
print(f"Shape: {df_polars_less.shape}")
```

**Explanation:**

Only the selected columns are loaded using Dask and Polars to reduce memory consumption. 
Dask uses the same `usecols` parameter as Pandas since it mirrors the Pandas API, while 
Polars uses the `columns` parameter which is specific to its own API. Both libraries 
load only the relevant columns in parallel across multiple CPU cores, resulting in faster 
load times and lower memory usage compared to loading all 18 columns.

**Implementation Summary:**

- **Dask** - uses `usecols` parameter with `assume_missing=True` and `low_memory=False`
- **Polars** - uses `columns` parameter specific to the Polars API
- Both libraries load only the selected columns defined in `SELECTED_COLS`
- Full dataset is loaded without any row limit

**Output:**

Dask:

<img width="889" height="107" alt="image" src="https://github.com/user-attachments/assets/dc502017-b530-4825-b026-2cd5aa0cfe36" />

Polars:

<img width="898" height="108" alt="image" src="https://github.com/user-attachments/assets/a39ecc2b-048d-4a3f-beca-dc021aa5bd63" />

#### Operation 3: Chunking

**Code:**

**Dask:**
```python
@measure_performance
def chunking_dask():
    df = dd.read_csv(file_path, assume_missing=True, low_memory=False, blocksize=10e6) 
    df = df.compute()
    return df

df_dask_chunked = chunking_dask()
```

**Polars:**
```python
@measure_performance
def chunking_polars():
    df = pl.read_csv(file_path, batch_size=100000)
    return df

df_polars_chunked = chunking_polars()
```

**Explanation:**

Unlike Pandas which requires manual chunking by iterating through chunks and combining 
them using `pd.concat()`, both Dask and Polars handle chunking internally and 
automatically. Dask splits the file into partitions of 10 MB each using the `blocksize` 
parameter and processes them in parallel across multiple CPU cores. Polars processes the 
file in batches of 100,000 rows at a time using the `batch_size` parameter, also 
internally managed without any manual intervention. Both libraries return a single 
complete DataFrame at the end without requiring any manual concatenation.

**Implementation Summary:**

- **Dask** - automatically partitions the file into 10 MB partitions using `blocksize=10e6`
- **Polars** - automatically processes the file in batches of 100,000 rows using `batch_size=100_000`
- Neither library requires manual chunk management unlike Pandas
- Both libraries load the full dataset without any row limit

**Output:**

Dask:

<img width="857" height="97" alt="image" src="https://github.com/user-attachments/assets/d2876e6c-df16-4aa5-af8e-d2f456d1ccb1" />

Polars:

<img width="859" height="92" alt="image" src="https://github.com/user-attachments/assets/300739e0-dc6f-49de-8541-80344fa67030" />

#### Operation 4: Sampling

**Code:**

**Dask:**
```python
@measure_performance
def sampling_dask():
    df = dd.read_csv(file_path, assume_missing=True, low_memory=False)
    df_sample = df.sample(frac=0.1, random_state=42)
    df_sample = df_sample.compute()
    return df_sample

df_dask_sampled = sampling_dask()
print(f"Shape: {df_dask_sampled.shape}")
```

**Polars:**
```python
@measure_performance
def sampling_polars():
    df = pl.read_csv(file_path)
    df_sample = df.sample(fraction=0.1, seed=42)
    return df_sample

df_polars_sampled = sampling_polars()
print(f"Shape: {df_polars_sampled.shape}")
```

**Explanation:**

Both Dask and Polars load the full dataset and select a random 10% sample for analysis. 
Dask uses the same `sample()` method as Pandas with `frac=0.1` and `random_state=42` 
for reproducibility, but requires `.compute()` to trigger the actual execution due to 
its lazy evaluation nature. Polars uses its own `sample()` method with `fraction=0.1` 
and `seed=42` for reproducibility, which is executed immediately due to Polars being 
eager by default.

**Implementation Summary:**

- **Dask** — uses `frac=0.1` and `random_state=42` with `.compute()` to trigger execution
- **Polars** — uses `fraction=0.1` and `seed=42` for reproducibility
- Both libraries sample 10% of the full dataset
- `random_state` and `seed` ensure the same sample is selected every time

**Output:**

Dask:

<img width="860" height="107" alt="image" src="https://github.com/user-attachments/assets/f541b8a7-9cd8-4c5e-91af-6253c08884d7" />

Polars:

<img width="861" height="111" alt="image" src="https://github.com/user-attachments/assets/0823e5be-dc34-4923-901b-008755806f52" />

#### Operation 5: Data Type Optimisation

**Code:**

**Dask:**
```python
@measure_performance
def data_type_optimisation_dask():
    df = dd.read_csv(file_path, assume_missing=True, low_memory=False, dtype=OPTIMISED_DTYPES)
    df = df.head(1000000, compute=True)
    return df

df_dask_optimised = data_type_optimisation_dask()
print("\n=== Data Types After Optimisation ===")
print(df_dask_optimised.dtypes.to_string())
```

**Polars:**
```python
POLARS_OPTIMISED_DTYPES = {
    'Unnamed: 0'   : pl.Int32,
    'radio'        : pl.Categorical,
    'MCC'          : pl.Int16,
    'MNC'          : pl.Int16,
    'TAC'          : pl.Int32,
    'CID'          : pl.Int64,
    'unit'         : pl.Int16,
    'LON'          : pl.Float32,
    'LAT'          : pl.Float32,
    'RANGE'        : pl.Int32,
    'SAM'          : pl.Int32,
    'changeable'   : pl.Int8,
    'created'      : pl.Int32,
    'updated'      : pl.Int32,
    'averageSignal': pl.Int16,
    'Country'      : pl.Categorical,
    'Network'      : pl.Categorical,
    'Continent'    : pl.Categorical,
}

@measure_performance
def data_type_optimisation_polars():
    df = pl.read_csv(file_path, schema_overrides=POLARS_OPTIMISED_DTYPES)
    df = df.slice(0, 1000000)
    return df

df_polars_optimised = data_type_optimisation_polars()
print("\n=== Data Types After Optimisation ===")
print(df_polars_optimised.dtypes)
```

**Explanation:**

Both Dask and Polars apply optimised data types at load time to reduce memory footprint. 
Dask reuses the same `OPTIMISED_DTYPES` dictionary as Pandas since it mirrors the Pandas 
API, passing it through the `dtype` parameter. The first 1,000,000 rows are retrieved 
using `.head(1000000, compute=True)` for consistent comparison with the Pandas baseline. 
Polars requires a separate `POLARS_OPTIMISED_DTYPES` dictionary using its own type system 
such as `pl.Int16`, `pl.Float32` and `pl.Categorical`, passed through the 
`schema_overrides` parameter. The first 1,000,000 rows are then selected using 
`.slice(0, 1000000)` for consistent comparison.

**Implementation Summary:**

- **Dask** - reuses `OPTIMISED_DTYPES` dictionary with `dtype` parameter, retrieves first 1,000,000 rows using `.head(1000000, compute=True)`
- **Polars** - uses separate `POLARS_OPTIMISED_DTYPES` dictionary with Polars type system, retrieves first 1,000,000 rows using `.slice(0, 1000000)`
- Both libraries apply optimised types at load time for maximum memory efficiency
- Results are consistent with the Pandas baseline of 1,000,000 rows

**Output:**

Dask:

<img width="942" height="69" alt="image" src="https://github.com/user-attachments/assets/fe61c487-c1bd-4c31-bbe7-d9b68a936e80" />

Polars:

<img width="949" height="89" alt="image" src="https://github.com/user-attachments/assets/bc588cb3-8c99-40a2-b399-aa166c205295" />



