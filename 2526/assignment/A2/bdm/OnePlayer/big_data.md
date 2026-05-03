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






