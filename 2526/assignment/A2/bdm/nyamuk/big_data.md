# Assignment 2: Mastering Big Data Handling

## Group Members:
<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Nabil Aflah Boo Binti Mohd Yosuf Boo Yong Chong</td>
    <td>A23CS0252</td>
  </tr>
  <tr>
    <td>Yasmin Batrisyia Binti Zahiruddin</td>
    <td>A23CS0201</td>
  </tr>
</table> 

## 1. Dataset Description
- **Name:** UK Housing Prices Paid </p>
- **Source:** [Kaggle-hm-land-registry](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid) </p>
- **File size:** 2.41 GB </p>
- **Domain:** Housing </p>
- **Shape:** 22,489,348 rows × 11 columns  </p>

### 📖 Description
This dataset contains comprehensive records of all registered property sales in England and Wales that were sold for full market value. It captures details of reported transactions, legal ownership types, property classifications, and geographical markers. This dataset provide a valuable insights into economic trends, purchasing behaviours, and regional distribution of property values which makes it well-suited for time-series analysis, geospatial mapping, and categorical market trend analysis.

## 2. Library Choices
Chosen libraries: </p>
| Library 1 | Library 2 | Library 3 |
|--------- | -----------| ---------- |
| Pandas | Dask | Polars |

- Dask is chosen besides Pandas as it enables to process the data through parallel processing and distributed processing of datasets which divides them into a smaller segments for simultaneous processing. It uses lazy evaluation as it performs calculations only when necessary which leads to reduced memory consumption and increased system operational capacity.

- Polars is chosen as it is a high-performance DataFrame library that is written in Rust which allows to execute the programs more faster while using less memory consumptions. It uses multi-threading method which enables it to perform data operations at a speed that exceeds Pandas when handling large datasets.

## 3. Data Loading and Inspection
<h4> 🔷Load Strategy </h4>
The following steps are taken to efficiently load the dataset in Google Colab: </p>
1. kaggle.json is imported using Google Colab import files feature. </p>

``` python
  from google.colab import files
  files.upload()
```

2. Configured Kaggle API Credentials. </p>

```bash
  !mkdir -p ~/.kaggle
  !cp kaggle.json ~/.kaggle/
  !chmod 600 ~/.kaggle/kaggle.json
```

3. Download the dataset from Kaggle using Kaggle CLI to retrieve dataset directly into Colab. </p>

```bash
  !kaggle datasets download -d hm-land-registry/uk-housing-prices-paid
```

4. Unzipped the dataset file. </p>

```bash
  !unzip uk-housing-prices-paid.zip
```

5. Loaded sample of rows using pd.read_csv() and display first 5 rows of the dataset. </p>

```bash
  df = pd.read_csv('price_paid_records.csv', low_memory=False)
  display(df.head())
  df.info()
```

<h4> 🔷Data Inspection </h4>
Show your initial loading code and the results of your data inspection. 

## 4. Big Data Handling Strategies (For each strategy: explanation, code snippet, output or screenshot, and discussion )
### 4.1 Load Less Data
**Explain:** </p>
This strategy uses the ``` cols ``` parameter within ``` pd.read_csv() ``` function to restrict to only necessary data to be loaded into the environment. The selected columns are ``` Price, Date of Transfer, Property Type, Old/New, Duration, and Town/City ```. By filtering these columns, the system able to avoids the overhead of parsing and storing irrelevant columns, which also directly minimize the initial memory used.

</p>

**Code:** </p>
```python
  file_path="price_paid_records.csv"

  def load_less_data_pandas(file_path):
    cols = [
        'Price', 'Date of Transfer', 'Property Type', 'Old/New', 'Duration',   'Town/City'
    ]
    return pd.read_csv(file_path, usecols=cols)
  
  
  performance_less_data, df_less_data = measure_performance(
      load_less_data_pandas,
      description="Load Less Data with Pandas",
      file_path=file_path
  )
  
  display(pd.DataFrame([performance_less_data]))

```
</p>

**Output:** </p>
![image](https://github.com/aflahh12/hpdpA2/blob/0633951a2bcd421bec27f10fa8a5c4dc5e1503d8/Screenshot%202026-05-03%20014142.png)

</p>

**Discussion:** </p>
From this strategy, it requires only 1093.57 MB of memory and execution time of 31.8884 seconds. The system also maintain a high throughput of 705251.69 records per seconds which shows that this approach is recommended when the analytical scope is limited to a specific subset of data.

</p>

### 4.2 Chunking
**Explain:** </p>
This strategy uses an interative loading technique to break a large file into smaller parts using discrete segments that is defined by ``` chunksize ``` parameter. This helps to prevent the system crashes by ensuring that only small portions of file, which is ``` 10,000 ``` to be processed in the limited RAM.

</p>

**Code:** </p>
```bash
  def load_with_chunking(file_path):
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=10000):
      chunks.append(chunk)
    df = pd.concat(chunks, ignore_index=True)
    return df
  
  performance_chunking, df_chunked = measure_performance(
      load_with_chunking,
      description="Chuncked Load",
      file_path="price_paid_records.csv"
  )
  
  display(pd.DataFrame([performance_chunking]))
```
</p>

**Output:** </p>
![image](https://github.com/aflahh12/hpdpA2/blob/0633951a2bcd421bec27f10fa8a5c4dc5e1503d8/Screenshot%202026-05-03%20014216.png)

</p>

**Discussion:** </p>
The results show a significant increase in memory usage of 5722.25 MB and execution time of 61.0781 seconds compared to load less data strategy. This performance degradation happened as the code appends all chunks into a list and concatenates them which effectively reconstructcs the entire dataset in memory and using a high computational cost during the final merge.
</p>

### 4.3 Data Type Optimisation
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>


### 4.4 Sampling
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>


### 4.5 Parallel Processing
Explain: </p>
Code: </p>
Output: </p>
Discussion: </p>

## 5. Comparative Analysis
### 5.1 Comparison of Optimized Loading Strategies
<h4> Summary Table </h4>

| Strategy | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| --------- | --------------- | ------------------| ------------| -------------------------|
| Load Less Data | 1093.57 | 31.8884 | 99.12 | 705251.69 |
| Chunking | 5722.25 | 61.0781 | 99.17 | 368206.41 |
| Optimized Data Types | 21.6 | 116.0844 | 102.38 | 193732.73 |
| Sampling | 83.34 | 43.7621 | 96.64 | 51390.02 |
| Parallel with <Dask> | 9.24 | 0.3845 | 17.48 | 260078.02 |

<h4> Visual Comparison </h4>

![image](https://github.com/aflahh12/hpdpA2/blob/61ecc4639aabbe6d8eae8a6e2652e173ade554a9/Screenshot%202026-05-03%20020434.png)

<h4> Interpretation </h4>
From the results, it shows that load less data performed best among others strategies. This is because it achieves the highest throughput and the fastest execution time while maintaining a low memory consumption. By filtered out some unnecessary columns, it minimizes the overhead and allows the CPU to process necessary data with maximum efficiency. 


### 5.2 Comparison Between Libraries
Compare between Pandas, Dask, and Polars </p>

<h4> Summary Table </h4>

| Library | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| --------|-----------------|---------------------| ----------- | ------------------------ |
| Pandas |  |  |  |  |
| Dask |  |  |  |  |
| Polars |  |  |  |  |

<h4> Visual Comparison </h4>

<h4> Interpretation: </h4>
Explain satu2 Pandas, Polars, Dask

## 6. Conclusion and Reflection
<h4> 🔷Summary of key observations </h4>
<h4> 🔷Discussion of scalability </h4>
<h4> 🔷Personal reflection on learning </h4> 
 

## References
_UK Housing Prices Paid_. (n.d.). Www.kaggle.com. https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid 

The Pandas Development Team. (2024). _pandas-dev/pandas: Pandas 2.2.2_. Zenodo. https://doi.org/10.5281/zenodo.3509134 

Dask Development Team. (2022). _Dask: Library for dynamic task scheduling_. https://dask.org 

Polars Development Team. (2024). _Polars: Fast multi-threaded, hybrid-streaming DataFrame library in Rust | Python_. https://pola.rs 

Google. (n.d.). _Google Colaboratory_. https://colab.research.google.com 
