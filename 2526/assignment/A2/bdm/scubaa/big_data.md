```python
# Standard
import os, time, gc, psutil, threading, random

# Core libraries
import pandas as pd
import dask.dataframe as dd
import pyarrow as pa
import pyarrow.csv as pa_csv
import pyarrow.parquet as pq

# Visualisation
from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import numpy as np

print("All libraries imported successfully")
```

    All libraries imported successfully
    


```python
FILE = "final_animedataset.csv"

def inspect(FILE: str, nrows: int = 5, chunksize: int = 10000):

    # Data collection
    df_sample   = pd.read_csv(FILE, nrows=nrows)
    total_rows  = 0
    null_counts = pd.Series(0, index=df_sample.columns)

    for chunk in pd.read_csv(FILE, chunksize=chunksize):
        total_rows  += len(chunk)
        null_counts += chunk.isnull().sum()

    # 1. File summary
    print("File Summary")
    display(pd.DataFrame({
        "Property" : ["File", "Total Rows", "Total Columns"],
        "Value"    : [FILE, f"{total_rows:,}", len(df_sample.columns)]
    }).set_index("Property"))

    # 2. Schema & null counts
    print("\nSchema & Null Counts")
    display(pd.DataFrame({
        "Dtype"  : df_sample.dtypes,
        "Nulls"  : null_counts,
        "Null %" : (null_counts / total_rows * 100).round(1)
    }))

    # 3. Sample rows
    print(f"\nSample Rows (first {nrows})")
    display(df_sample)


inspect(FILE)
```

    File Summary
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Value</th>
    </tr>
    <tr>
      <th>Property</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>File</th>
      <td>final_animedataset.csv</td>
    </tr>
    <tr>
      <th>Total Rows</th>
      <td>35,305,695</td>
    </tr>
    <tr>
      <th>Total Columns</th>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>


    
    Schema & Null Counts
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dtype</th>
      <th>Nulls</th>
      <th>Null %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>username</th>
      <td>str</td>
      <td>256</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>anime_id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>my_score</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>user_id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>gender</th>
      <td>str</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>title</th>
      <td>str</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>type</th>
      <td>str</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>source</th>
      <td>str</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>score</th>
      <td>float64</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>scored_by</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>rank</th>
      <td>float64</td>
      <td>751970</td>
      <td>2.1</td>
    </tr>
    <tr>
      <th>popularity</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>genre</th>
      <td>str</td>
      <td>2267</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>


    
    Sample Rows (first 5)
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>username</th>
      <th>anime_id</th>
      <th>my_score</th>
      <th>user_id</th>
      <th>gender</th>
      <th>title</th>
      <th>type</th>
      <th>source</th>
      <th>score</th>
      <th>scored_by</th>
      <th>rank</th>
      <th>popularity</th>
      <th>genre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>karthiga</td>
      <td>21</td>
      <td>9</td>
      <td>2255153</td>
      <td>Female</td>
      <td>One Piece</td>
      <td>TV</td>
      <td>Manga</td>
      <td>8.54</td>
      <td>423868</td>
      <td>91.0</td>
      <td>35</td>
      <td>Action, Adventure, Comedy, Super Power, Drama,...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>karthiga</td>
      <td>59</td>
      <td>7</td>
      <td>2255153</td>
      <td>Female</td>
      <td>Chobits</td>
      <td>TV</td>
      <td>Manga</td>
      <td>7.53</td>
      <td>175388</td>
      <td>1546.0</td>
      <td>188</td>
      <td>Sci-Fi, Comedy, Drama, Romance, Ecchi, Seinen</td>
    </tr>
    <tr>
      <th>2</th>
      <td>karthiga</td>
      <td>74</td>
      <td>7</td>
      <td>2255153</td>
      <td>Female</td>
      <td>Gakuen Alice</td>
      <td>TV</td>
      <td>Manga</td>
      <td>7.77</td>
      <td>33244</td>
      <td>941.0</td>
      <td>1291</td>
      <td>Comedy, School, Shoujo, Super Power</td>
    </tr>
    <tr>
      <th>3</th>
      <td>karthiga</td>
      <td>120</td>
      <td>7</td>
      <td>2255153</td>
      <td>Female</td>
      <td>Fruits Basket</td>
      <td>TV</td>
      <td>Manga</td>
      <td>7.77</td>
      <td>167968</td>
      <td>939.0</td>
      <td>222</td>
      <td>Slice of Life, Comedy, Drama, Romance, Fantasy...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>karthiga</td>
      <td>178</td>
      <td>7</td>
      <td>2255153</td>
      <td>Female</td>
      <td>Ultra Maniac</td>
      <td>TV</td>
      <td>Manga</td>
      <td>7.26</td>
      <td>9663</td>
      <td>2594.0</td>
      <td>2490</td>
      <td>Magic, Comedy, Romance, School, Shoujo</td>
    </tr>
  </tbody>
</table>
</div>


# 5. Strategies

## Function for measure performance

This functions asdjksbadbkajdkajsdawd


```python
def evaluate_performance(
    strategy_fn,
    strategy_name: str = "UnknownStrategy",
    *args,
    **kwargs
) -> dict:
    process = psutil.Process(os.getpid())

    # Baseline memory before
    baseline_memory = process.memory_info().rss
    peak_memory     = baseline_memory
    monitoring      = True

    def monitor_memory():
        nonlocal peak_memory
        while monitoring:
            mem = process.memory_info().rss
            peak_memory = max(peak_memory, mem)
            time.sleep(0.05)

    monitor_thread = threading.Thread(target=monitor_memory, daemon=True)
    monitor_thread.start()

    t0     = time.time()
    result = strategy_fn(*args, **kwargs)
    if hasattr(result, "compute"):
        result = result.compute()
    t1 = time.time()

    monitoring = False
    monitor_thread.join()

    # Capture after del
    after_memory = process.memory_info().rss

    peak_memory_mb  = max(0, (peak_memory    - baseline_memory) / (1024 ** 2))
    before_mb       = baseline_memory / (1024 ** 2)
    after_mb        = after_memory    / (1024 ** 2)

    del result
    gc.collect()
    time.sleep(2)

    metrics = {
        "name"                    : strategy_name,
        "total_time_s"            : round(t1 - t0, 4),
        "before_memory_mb"        : round(before_mb, 2),
        "after_memory_mb"         : round(after_mb, 2),
        "peak_memory_usage_mb"    : round(peak_memory_mb, 2)
    }

    print(f"\n{'='*40}")
    print(f"  Strategy              : {strategy_name}")
    print(f"  Total time            : {metrics['total_time_s']:.2f} seconds")
    print(f"  Before memory         : {metrics['before_memory_mb']:,.1f} MB")
    print(f"  After memory          : {metrics['after_memory_mb']:,.1f} MB")
    print(f"  Peak memory usage     : {metrics['peak_memory_usage_mb']:,.1f} MB")
    print(f"{'='*40}")

    return metrics
```


```python
def evaluate_performance_avg(
    strategy_fn,
    strategy_name: str = "UnknownStrategy",
    n: int = 3,
    *args,
    **kwargs
) -> dict:
    runs = []
    for i in range(n):
        print(f"  Run {i+1}/{n}...")
        metrics = evaluate_performance(strategy_fn, strategy_name, *args, **kwargs)
        runs.append(metrics)
        time.sleep(2)

    avg_metrics = {
        "name"                 : strategy_name,
        "total_time_s"         : round(sum(r["total_time_s"]          for r in runs) / n, 4),
        "before_memory_mb"     : round(sum(r["before_memory_mb"]      for r in runs) / n, 2),
        "after_memory_mb"      : round(sum(r["after_memory_mb"]       for r in runs) / n, 2),
        "peak_memory_usage_mb" : round(sum(r["peak_memory_usage_mb"]  for r in runs) / n, 2),
    }

    print(f"\n{'='*40}")
    print(f"  AVG RESULT ({n} runs) : {strategy_name}")
    print(f"  Avg time              : {avg_metrics['total_time_s']:.2f} seconds")
    print(f"  Avg before memory     : {avg_metrics['before_memory_mb']:,.1f} MB")
    print(f"  Avg after memory      : {avg_metrics['after_memory_mb']:,.1f} MB")
    print(f"  Avg peak memory       : {avg_metrics['peak_memory_usage_mb']:,.1f} MB")
    print(f"{'='*40}")

    return avg_metrics
```


```python
# Strategy 1: Load Less Data

def strategy_select_cols() -> pd.DataFrame:
    return pd.read_csv(FILE, usecols=['anime_id', 'title', 'score'])

# Strategy 2: Chunking

def strategy_chunked() -> pd.DataFrame:
    chunks = pd.read_csv(FILE, chunksize=500000)
    return pd.concat(chunks, ignore_index=True)

# Strategy 3: Data Type Optimisation

def strategy_optimized_dtypes() -> pd.DataFrame:
    dtype_map = {
        "anime_id" : "int32",
        "score"    : "float32",
        "episodes" : "Int16",
    }
    return pd.read_csv(FILE, dtype=dtype_map)

# Strategy 4: Sampling

def strategy_sampling() -> pd.DataFrame:
    skip_logic = lambda i: i > 0 and random.random() > 0.01
    return pd.read_csv(FILE, skiprows=skip_logic)

# Strategy 5: Parallel Processing with Scalable Libraries

# Pandas (for comparison)
def strategy_baseline_pandas() -> pd.DataFrame:
    return pd.read_csv(FILE, low_memory=False)

# Dask
def strategy_baseline_dask() -> dd.DataFrame:
    return dd.read_csv(FILE)

# PyArrow
def strategy_baseline_pyarrow() -> pa.Table:
    return pa_csv.read_csv(FILE)


```


```python
results = []
results_parallel = []
```

# Pandas baseline for comparison


```python
metrics = evaluate_performance_avg(strategy_baseline_pandas, "Baseline (Pandas)", n=3)
results.append(metrics)
results_parallel.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy              : Baseline (Pandas)
      Total time            : 105.36 seconds
      Before memory         : 198.1 MB
      After memory          : 5,469.0 MB
      Peak memory usage     : 12,064.3 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy              : Baseline (Pandas)
      Total time            : 91.60 seconds
      Before memory         : 141.3 MB
      After memory          : 5,976.1 MB
      Peak memory usage     : 12,391.6 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy              : Baseline (Pandas)
      Total time            : 87.19 seconds
      Before memory         : 140.9 MB
      After memory          : 6,378.7 MB
      Peak memory usage     : 12,339.3 MB
    ========================================
    
    ========================================
      AVG RESULT (3 runs) : Baseline (Pandas)
      Avg time              : 94.72 seconds
      Avg before memory     : 160.1 MB
      Avg after memory      : 5,941.3 MB
      Avg peak memory       : 12,265.0 MB
    ========================================
    

## 5.1 Strategy 1: Load Less Data


```python
print("Warming up disk cache...")
_ = pd.read_csv(FILE, nrows=1000)
del _             
gc.collect()      
time.sleep(3)     

metrics = evaluate_performance_avg(strategy_select_cols, "Load Less Data (Pandas)", n=3)

results.append(metrics)
```

    Warming up disk cache...
      Run 1/3...
    
    ========================================
      Strategy              : Load Less Data (Pandas)
      Total time            : 28.36 seconds
      Before memory         : 145.1 MB
      After memory          : 1,910.9 MB
      Peak memory usage     : 2,138.9 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy              : Load Less Data (Pandas)
      Total time            : 27.76 seconds
      Before memory         : 313.9 MB
      After memory          : 1,922.8 MB
      Peak memory usage     : 1,970.0 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy              : Load Less Data (Pandas)
      Total time            : 27.82 seconds
      Before memory         : 328.1 MB
      After memory          : 1,928.2 MB
      Peak memory usage     : 1,958.8 MB
    ========================================
    
    ========================================
      AVG RESULT (3 runs) : Load Less Data (Pandas)
      Avg time              : 27.98 seconds
      Avg before memory     : 262.4 MB
      Avg after memory      : 1,920.6 MB
      Avg peak memory       : 2,022.6 MB
    ========================================
    

## 5.2 Strategy 2: Chunking


```python
metrics = evaluate_performance_avg(strategy_chunked, "Chunking (Pandas)", n=3)
results.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy              : Chunking (Pandas)
      Total time            : 53.84 seconds
      Before memory         : 320.5 MB
      After memory          : 6,526.0 MB
      Peak memory usage     : 8,049.8 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy              : Chunking (Pandas)
      Total time            : 54.20 seconds
      Before memory         : 170.4 MB
      After memory          : 6,525.4 MB
      Peak memory usage     : 8,134.1 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy              : Chunking (Pandas)
      Total time            : 53.75 seconds
      Before memory         : 170.6 MB
      After memory          : 6,525.5 MB
      Peak memory usage     : 8,140.9 MB
    ========================================
    
    ========================================
      AVG RESULT (3 runs) : Chunking (Pandas)
      Avg time              : 53.93 seconds
      Avg before memory     : 220.5 MB
      Avg after memory      : 6,525.6 MB
      Avg peak memory       : 8,108.2 MB
    ========================================
    

## 5.3 Strategy 3: Data Type Optimisation


```python
metrics = evaluate_performance_avg(strategy_optimized_dtypes, "Data Type Optimization (Pandas)", n=3)
results.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy              : Data Type Optimization (Pandas)
      Total time            : 53.14 seconds
      Before memory         : 170.5 MB
      After memory          : 6,438.1 MB
      Peak memory usage     : 8,387.9 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy              : Data Type Optimization (Pandas)
      Total time            : 54.72 seconds
      Before memory         : 323.2 MB
      After memory          : 6,479.9 MB
      Peak memory usage     : 8,233.1 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy              : Data Type Optimization (Pandas)
      Total time            : 54.56 seconds
      Before memory         : 357.0 MB
      After memory          : 6,513.9 MB
      Peak memory usage     : 8,201.1 MB
    ========================================
    
    ========================================
      AVG RESULT (3 runs) : Data Type Optimization (Pandas)
      Avg time              : 54.14 seconds
      Avg before memory     : 283.6 MB
      Avg after memory      : 6,477.3 MB
      Avg peak memory       : 8,274.0 MB
    ========================================
    

## 5.4 Strategy 4: Sampling


```python
metrics = evaluate_performance_avg(strategy_sampling, "Sampling (Pandas)", n=3)
results.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy              : Sampling (Pandas)
      Total time            : 22.46 seconds
      Before memory         : 366.7 MB
      After memory          : 417.2 MB
      Peak memory usage     : 51.3 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy              : Sampling (Pandas)
      Total time            : 22.78 seconds
      Before memory         : 351.9 MB
      After memory          : 366.8 MB
      Peak memory usage     : 15.8 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy              : Sampling (Pandas)
      Total time            : 21.91 seconds
      Before memory         : 304.2 MB
      After memory          : 356.8 MB
      Peak memory usage     : 73.6 MB
    ========================================
    
    ========================================
      AVG RESULT (3 runs) : Sampling (Pandas)
      Avg time              : 22.38 seconds
      Avg before memory     : 340.9 MB
      Avg after memory      : 380.3 MB
      Avg peak memory       : 46.9 MB
    ========================================
    

## 5.5 Strategy 5: Parallel Processing with Scalable Libraries

# 5.5.1 : Dask


```python
metrics = evaluate_performance_avg(strategy_baseline_dask, "Baseline (Dask)", n=3)
results_parallel.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy              : Baseline (Dask)
      Total time            : 40.02 seconds
      Before memory         : 290.3 MB
      After memory          : 6,871.3 MB
      Peak memory usage     : 8,653.4 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy              : Baseline (Dask)
      Total time            : 38.85 seconds
      Before memory         : 244.6 MB
      After memory          : 6,859.7 MB
      Peak memory usage     : 8,635.7 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy              : Baseline (Dask)
      Total time            : 37.75 seconds
      Before memory         : 233.7 MB
      After memory          : 6,857.8 MB
      Peak memory usage     : 8,710.0 MB
    ========================================
    
    ========================================
      AVG RESULT (3 runs) : Baseline (Dask)
      Avg time              : 38.87 seconds
      Avg before memory     : 256.2 MB
      Avg after memory      : 6,862.9 MB
      Avg peak memory       : 8,666.3 MB
    ========================================
    

# 5.5.1 : PyArrow


```python
metrics = evaluate_performance_avg(strategy_baseline_pyarrow, "Baseline (Pyarrow)", n=3)
results_parallel.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy              : Baseline (Pyarrow)
      Total time            : 15.68 seconds
      Before memory         : 233.2 MB
      After memory          : 160.6 MB
      Peak memory usage     : 10,602.6 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy              : Baseline (Pyarrow)
      Total time            : 13.43 seconds
      Before memory         : 190.7 MB
      After memory          : 213.4 MB
      Peak memory usage     : 11,798.6 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy              : Baseline (Pyarrow)
      Total time            : 12.64 seconds
      Before memory         : 198.9 MB
      After memory          : 965.7 MB
      Peak memory usage     : 12,001.4 MB
    ========================================
    
    ========================================
      AVG RESULT (3 runs) : Baseline (Pyarrow)
      Avg time              : 13.92 seconds
      Avg before memory     : 207.6 MB
      Avg after memory      : 446.6 MB
      Avg peak memory       : 11,467.5 MB
    ========================================
    


```python
df = pd.DataFrame(results)

colors = np.random.rand(len(df), 3)

plt.figure()
plt.bar(df['name'], df['total_time_s'], color=colors)
plt.title('Execution Time Comparison')
plt.xticks(rotation=20)
plt.show()

plt.figure()
plt.bar(df['name'], df['peak_memory_usage_mb'], color=colors)
plt.title('Peak Memory Usage Comparison')
plt.xticks(rotation=20)
plt.show()
```


    
![png](output_23_0.png)
    



    
![png](output_23_1.png)
    



```python
df = pd.DataFrame(results_parallel)

colors = np.random.rand(len(df), 3)

plt.figure()
plt.bar(df['name'], df['total_time_s'], color=colors)
plt.title('Execution Time Comparison')
plt.xticks(rotation=20)
plt.show()

plt.figure()
plt.bar(df['name'], df['peak_memory_usage_mb'], color=colors)
plt.title('Peak Memory Usage Comparison')
plt.xticks(rotation=20)
plt.show()
```


    
![png](output_24_0.png)
    



    
![png](output_24_1.png)
    



```python
display(pd.DataFrame(results))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>total_time_s</th>
      <th>before_memory_mb</th>
      <th>after_memory_mb</th>
      <th>peak_memory_usage_mb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Baseline (Pandas)</td>
      <td>94.7182</td>
      <td>160.13</td>
      <td>5941.26</td>
      <td>12265.05</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Load Less Data (Pandas)</td>
      <td>27.9799</td>
      <td>262.36</td>
      <td>1920.62</td>
      <td>2022.58</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chunking (Pandas)</td>
      <td>53.9318</td>
      <td>220.51</td>
      <td>6525.64</td>
      <td>8108.25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Data Type Optimization (Pandas)</td>
      <td>54.1405</td>
      <td>283.55</td>
      <td>6477.31</td>
      <td>8274.03</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sampling (Pandas)</td>
      <td>22.3840</td>
      <td>340.93</td>
      <td>380.30</td>
      <td>46.88</td>
    </tr>
  </tbody>
</table>
</div>



```python
display(pd.DataFrame(results_parallel))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>total_time_s</th>
      <th>before_memory_mb</th>
      <th>after_memory_mb</th>
      <th>peak_memory_usage_mb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Baseline (Pandas)</td>
      <td>94.7182</td>
      <td>160.13</td>
      <td>5941.26</td>
      <td>12265.05</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Baseline (Dask)</td>
      <td>38.8737</td>
      <td>256.19</td>
      <td>6862.93</td>
      <td>8666.34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Baseline (Pyarrow)</td>
      <td>13.9153</td>
      <td>207.59</td>
      <td>446.61</td>
      <td>11467.52</td>
    </tr>
  </tbody>
</table>
</div>


# Comparative Analysis


```python
def evaluate_performance_library(
    load_fn,
    process_fn,
    strategy_name: str = "UnknownStrategy",
    *args,
    **kwargs
) -> dict:
    process = psutil.Process(os.getpid())

    baseline_memory = process.memory_info().rss
    peak_memory     = baseline_memory
    monitoring      = True

    def monitor_memory():
        nonlocal peak_memory
        while monitoring:
            mem = process.memory_info().rss
            peak_memory = max(peak_memory, mem)
            time.sleep(0.05)

    monitor_thread = threading.Thread(target=monitor_memory, daemon=True)
    monitor_thread.start()

    # --- Load ---
    t0     = time.time()
    data   = load_fn(*args, **kwargs)
    t1     = time.time()

    # --- Process ---
    t2     = time.time()
    result = process_fn(data)
    if hasattr(result, "compute"):
        result = result.compute()
    t3     = time.time()

    monitoring = False
    monitor_thread.join()

    after_memory        = process.memory_info().rss
    peak_memory_mb      = max(0, (peak_memory - baseline_memory) / (1024 ** 2))
    before_mb           = baseline_memory / (1024 ** 2)
    after_mb            = after_memory    / (1024 ** 2)
    load_time_s         = round(t1 - t0, 4)
    process_time_s      = round(t3 - t2, 4)
    total_time_s        = round(t3 - t0, 4)

    del data, result
    gc.collect()
    time.sleep(2)

    metrics = {
        "name"                 : strategy_name,
        "load_time_s"          : load_time_s,
        "process_time_s"       : process_time_s,
        "total_time_s"         : total_time_s,
        "before_memory_mb"     : round(before_mb, 2),
        "after_memory_mb"      : round(after_mb, 2),
        "peak_memory_usage_mb" : round(peak_memory_mb, 2),
    }

    print(f"\n{'='*40}")
    print(f"  Strategy          : {strategy_name}")
    print(f"  Load time         : {load_time_s:.2f} seconds")
    print(f"  Process time      : {process_time_s:.2f} seconds")
    print(f"  Total time        : {total_time_s:.2f} seconds")
    print(f"  Before memory     : {before_mb:,.1f} MB")
    print(f"  After memory      : {after_mb:,.1f} MB")
    print(f"  Peak memory       : {peak_memory_mb:,.1f} MB")
    print(f"{'='*40}")

    return metrics
```


```python
def evaluate_performance_library_avg(
    load_fn,
    process_fn,
    strategy_name: str = "UnknownStrategy",
    n: int = 3,
    *args,
    **kwargs
) -> dict:
    runs = []
    for i in range(n):
        print(f"  Run {i+1}/{n}...")
        metrics = evaluate_performance_library(load_fn, process_fn, strategy_name, *args, **kwargs)
        runs.append(metrics)
        time.sleep(2)

    avg_metrics = {
        "name"                 : strategy_name,
        "load_time_s"          : round(sum(r["load_time_s"]          for r in runs) / n, 4),
        "process_time_s"       : round(sum(r["process_time_s"]       for r in runs) / n, 4),
        "total_time_s"         : round(sum(r["total_time_s"]         for r in runs) / n, 4),
        "before_memory_mb"     : round(sum(r["before_memory_mb"]     for r in runs) / n, 2),
        "after_memory_mb"      : round(sum(r["after_memory_mb"]      for r in runs) / n, 2),
        "peak_memory_usage_mb" : round(sum(r["peak_memory_usage_mb"] for r in runs) / n, 2),
    }

    print(f"\n{'#'*40}")
    print(f"  AVG RESULT ({n} runs) : {strategy_name}")
    print(f"  Avg load time         : {avg_metrics['load_time_s']:.2f} seconds")
    print(f"  Avg process time      : {avg_metrics['process_time_s']:.2f} seconds")
    print(f"  Avg total time        : {avg_metrics['total_time_s']:.2f} seconds")
    print(f"  Avg before memory     : {avg_metrics['before_memory_mb']:,.1f} MB")
    print(f"  Avg after memory      : {avg_metrics['after_memory_mb']:,.1f} MB")
    print(f"  Avg peak memory       : {avg_metrics['peak_memory_usage_mb']:,.1f} MB")
    print(f"{'#'*40}")

    return avg_metrics
```

# Pandas
def load_pandas():
    return pd.read_csv(FILE, low_memory=False)

def process_pandas(df):
    return df.groupby("genre")["score"].mean()

# PyArrow
def load_pyarrow():
    return pv.read_csv(FILE)

def process_pyarrow(table):
    import pyarrow.compute as pc
    # groupby aggregation
    return table.group_by("genre").aggregate([("score", "mean")])


# Dask
def load_dask():
    return dd.read_csv(FILE)

def process_dask(df):
    return df.groupby("genre")["score"].mean().compute()


metrics = evaluate_performance_detailed_avg(load_pandas, process_pandas, "Pandas", n=3)
results.append(metrics)

metrics = evaluate_performance_detailed_avg(load_pyarrow, process_pyarrow, "PyArrow", n=3)
results.append(metrics)

metrics = evaluate_performance_detailed_avg(load_dask, process_dask, "Dask", n=3)
results.append(metrics)


```python
results_library = []
```


```python
# Pandas
def load_pandas():
    return pd.read_csv(FILE, low_memory=False)

def process_pandas(df):
    return df.groupby("genre")["score"].mean()

metrics = evaluate_performance_library_avg(load_pandas, process_pandas, "Pandas", n=3)
results_library.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy          : Pandas
      Load time         : 167.31 seconds
      Process time      : 1.94 seconds
      Total time        : 169.25 seconds
      Before memory     : 332.5 MB
      After memory      : 6,400.5 MB
      Peak memory       : 11,522.8 MB
    ========================================
      Run 2/3...
    


```python
# PyArrow
def load_pyarrow():
    return pa_csv.read_csv(FILE)

def process_pyarrow(table):
    import pyarrow.compute as pc
    # groupby aggregation
    return table.group_by("genre").aggregate([("score", "mean")])

metrics = evaluate_performance_library_avg(load_pyarrow, process_pyarrow, "PyArrow", n=3)
results_library.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy          : PyArrow
      Load time         : 14.90 seconds
      Process time      : 0.47 seconds
      Total time        : 15.37 seconds
      Before memory     : 175.6 MB
      After memory      : 2,101.6 MB
      Peak memory       : 11,791.5 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy          : PyArrow
      Load time         : 14.81 seconds
      Process time      : 0.43 seconds
      Total time        : 15.24 seconds
      Before memory     : 217.2 MB
      After memory      : 2,253.3 MB
      Peak memory       : 11,876.5 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy          : PyArrow
      Load time         : 15.29 seconds
      Process time      : 0.42 seconds
      Total time        : 15.70 seconds
      Before memory     : 219.7 MB
      After memory      : 2,230.6 MB
      Peak memory       : 12,005.4 MB
    ========================================
    
    ########################################
      AVG RESULT (3 runs) : PyArrow
      Avg load time         : 15.00 seconds
      Avg process time      : 0.44 seconds
      Avg total time        : 15.44 seconds
      Avg before memory     : 204.2 MB
      Avg after memory      : 2,195.2 MB
      Avg peak memory       : 11,891.1 MB
    ########################################
    


```python
# Dask
def load_dask():
    return dd.read_csv(FILE)

def process_dask(df):
    return df.groupby("genre")["score"].mean()
    
metrics = evaluate_performance_library_avg(load_dask, process_dask, "Dask", n=3)
results_library.append(metrics)
```

      Run 1/3...
    
    ========================================
      Strategy          : Dask
      Load time         : 0.12 seconds
      Process time      : 99.20 seconds
      Total time        : 99.32 seconds
      Before memory     : 225.1 MB
      After memory      : 302.2 MB
      Peak memory       : 2,821.4 MB
    ========================================
      Run 2/3...
    
    ========================================
      Strategy          : Dask
      Load time         : 0.03 seconds
      Process time      : 98.34 seconds
      Total time        : 98.37 seconds
      Before memory     : 300.2 MB
      After memory      : 302.5 MB
      Peak memory       : 2,544.8 MB
    ========================================
      Run 3/3...
    
    ========================================
      Strategy          : Dask
      Load time         : 0.03 seconds
      Process time      : 97.46 seconds
      Total time        : 97.49 seconds
      Before memory     : 302.5 MB
      After memory      : 304.7 MB
      Peak memory       : 2,608.4 MB
    ========================================
    
    ########################################
      AVG RESULT (3 runs) : Dask
      Avg load time         : 0.06 seconds
      Avg process time      : 98.34 seconds
      Avg total time        : 98.39 seconds
      Avg before memory     : 275.9 MB
      Avg after memory      : 303.1 MB
      Avg peak memory       : 2,658.2 MB
    ########################################
    


```python
display(pd.DataFrame(results_library))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>load_time_s</th>
      <th>process_time_s</th>
      <th>total_time_s</th>
      <th>before_memory_mb</th>
      <th>after_memory_mb</th>
      <th>peak_memory_usage_mb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Pandas</td>
      <td>135.1022</td>
      <td>1.9331</td>
      <td>137.0353</td>
      <td>203.83</td>
      <td>6131.13</td>
      <td>12029.94</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PyArrow</td>
      <td>15.0006</td>
      <td>0.4363</td>
      <td>15.4369</td>
      <td>204.17</td>
      <td>2195.15</td>
      <td>11891.13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Dask</td>
      <td>0.0574</td>
      <td>98.3365</td>
      <td>98.3939</td>
      <td>275.92</td>
      <td>303.12</td>
      <td>2658.21</td>
    </tr>
  </tbody>
</table>
</div>



```python
metrics_to_plot = ["total_time_s", "load_time_s", "process_time_s", "peak_memory_usage_mb"]
labels_map = {
    "total_time_s"         : "Total time (s)",
    "load_time_s"          : "Load time (s)",
    "process_time_s"       : "Process time (s)",
    "peak_memory_usage_mb" : "Peak memory (MB)",
}
colors = ["#534AB7", "#0F6E56", "#993C1D", "#185FA5"]

names  = [r["name"] for r in results_library]
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, metric in enumerate(metrics_to_plot):
    values = [r[metric] for r in results]
    bars   = axes[i].barh(names, values, color=colors[i], alpha=0.85)
    axes[i].set_title(labels_map[metric], fontsize=12, fontweight="bold", pad=10)
    axes[i].set_xlabel(labels_map[metric], fontsize=10)
    axes[i].invert_yaxis()
    axes[i].bar_label(bars, fmt="%.2f", padding=4, fontsize=9)
    axes[i].spines[["top", "right"]].set_visible(False)
    axes[i].grid(axis="x", alpha=0.2)

plt.suptitle("Benchmark Comparison", fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig("benchmark.png", dpi=150, bbox_inches="tight")
plt.show()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[28], line 16
         14 for i, metric in enumerate(metrics_to_plot):
         15     values = [r[metric] for r in results]
    ---> 16     bars   = axes[i].barh(names, values, color=colors[i], alpha=0.85)
         17     axes[i].set_title(labels_map[metric], fontsize=12, fontweight="bold", pad=10)
         18     axes[i].set_xlabel(labels_map[metric], fontsize=10)
    

    File ~\anaconda3\envs\myenv\Lib\site-packages\matplotlib\axes\_axes.py:2834, in Axes.barh(self, y, width, height, left, align, data, **kwargs)
       2704 r"""
       2705 Make a horizontal bar plot.
       2706 
       (...)   2831 :doc:`/gallery/lines_bars_and_markers/horizontal_barchart_distribution`.
       2832 """
       2833 kwargs.setdefault('orientation', 'horizontal')
    -> 2834 patches = self.bar(x=left, height=height, width=width, bottom=y,
       2835                    align=align, data=data, **kwargs)
       2836 return patches
    

    File ~\anaconda3\envs\myenv\Lib\site-packages\matplotlib\__init__.py:1524, in _preprocess_data.<locals>.inner(ax, data, *args, **kwargs)
       1521 @functools.wraps(func)
       1522 def inner(ax, *args, data=None, **kwargs):
       1523     if data is None:
    -> 1524         return func(
       1525             ax,
       1526             *map(cbook.sanitize_sequence, args),
       1527             **{k: cbook.sanitize_sequence(v) for k, v in kwargs.items()})
       1529     bound = new_sig.bind(ax, *args, **kwargs)
       1530     auto_label = (bound.arguments.get(label_namer)
       1531                   or bound.kwargs.get(label_namer))
    

    File ~\anaconda3\envs\myenv\Lib\site-packages\matplotlib\axes\_axes.py:2583, in Axes.bar(self, x, height, width, bottom, align, **kwargs)
       2580     if yerr is not None:
       2581         yerr = self._convert_dx(yerr, y0, y, self.convert_yunits)
    -> 2583 x, height, width, y, linewidth, hatch = np.broadcast_arrays(
       2584     # Make args iterable too.
       2585     np.atleast_1d(x), height, width, y, linewidth, hatch)
       2587 # Now that units have been converted, set the tick locations.
       2588 if orientation == 'vertical':
    

    File ~\anaconda3\envs\myenv\Lib\site-packages\numpy\lib\_stride_tricks_impl.py:577, in broadcast_arrays(subok, *args)
        570 # nditer is not used here to avoid the limit of 64 arrays.
        571 # Otherwise, something like the following one-liner would suffice:
        572 # return np.nditer(args, flags=['multi_index', 'zerosize_ok'],
        573 #                  order='C').itviews
        575 args = [np.array(_m, copy=None, subok=subok) for _m in args]
    --> 577 shape = _broadcast_shape(*args)
        579 result = [array if array.shape == shape
        580           else _broadcast_to(array, shape, subok=subok, readonly=False)
        581                           for array in args]
        582 return tuple(result)
    

    File ~\anaconda3\envs\myenv\Lib\site-packages\numpy\lib\_stride_tricks_impl.py:452, in _broadcast_shape(*args)
        447 """Returns the shape of the arrays that would result from broadcasting the
        448 supplied arrays against each other.
        449 """
        450 # use the old-iterator because np.nditer does not handle size 0 arrays
        451 # consistently
    --> 452 b = np.broadcast(*args[:64])
        453 # unfortunately, it cannot handle 64 or more arguments directly
        454 for pos in range(64, len(args), 63):
        455     # ironically, np.broadcast does not properly handle np.broadcast
        456     # objects (it treats them as scalars)
        457     # use broadcasting to avoid allocating the full array
    

    ValueError: shape mismatch: objects cannot be broadcast to a single shape.  Mismatch is between arg 2 with shape (5,) and arg 3 with shape (3,).



    
![png](output_36_1.png)
    



```python

```
