
# Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>CHEN PYNG HAW</td>
    <td>A22EC0042</td>

</table>

## Dataset Description

-   **Dataset**: IMDB Review Dataset
    
-   **Source**: Kaggle ([https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset))
    
-   **Size**: ~1.07 GB uncompressed
    
-   **Records**: Over 1 million reviews
    
-   **Domain**: Movie review data including review text, ratings, reviewer info, and spoiler tags
    

The dataset is selected to test various big data strategies due to its rich structure and large volume.


## Task 1: Load and Inspect Data

We used Pandas, Polars, and Dask to load and inspect the dataset. Column types, shape, and sample records were examined.


## Task 2: Apply Big Data Handling Strategies

### Part 1
This part focuses on comparing five data handling strategies using primarily Pandas and Dask:

 **1. Load Less Data** 

Loaded only 5 important columns (`review_id`, `reviewer`, `movie`, `rating`, `spoiler_tag`) instead of all 9, which reduced memory usage and improved load time.

**2. Use Chunking**

-   **Pandas**: Used `read_json(chunksize=...)` to load 200k rows per chunk.
    
-   **Polars**: Used `.lazy().slice()` to simulate chunked reads.
    
-   **Dask**: Chunking done through partitions with `blocksize`, and `map_partitions()` was used to process all in parallel.
    

**3. Optimize Data Types**

Converted columns to types like `category`, `float32`, `int8`, and `datetime`. This drastically reduced memory footprint.

**4. Sampling**

-   **Pandas and Polars**: Performed 10% sampling using `.sample(frac=0.1)`.
    
-   **Dask**: Sampling not performed because Dask lacks native global row-wise sampling.
    

**5. Parallel Processing with Dask**

Used `df.compute()` to load the full dataset using Dask's internal partitioning. Although Dask handles data in chunks, the `.compute()` method materializes the entire DataFrame into memory, providing parallel execution but with higher memory usage comparable to Pandas.
    

### Part 2
This part compares the performance of the three libraries (Pandas, Polars, and Dask) for the Normal Load strategy, to understand overall performance differences between libraries.



## Task 3: Comparative Analysis

This part includes two comparisons:

-   A strategy-level comparison across Pandas and Dask for Load Less Data, Chunking, Type Optimization, Sampling, and Dask parallel load.
    
-   A library-level comparison (Pandas vs Polars vs Dask) focused only on the Normal Load performance.

### Part 1: Comparison of Data Handling Techniques (Pandas + Dask) and Normal Load Performance Across Libraries


| Technique | Execution Time (s) | Memory Usage (MB) |
| :------------------------ | :----------------- | :---------------- |
| Load Less Data | 16.92 | 235.14 |
| Use Chunking | 16.37 | 301.95 |
| Optimize Data Types | 20.66 | 1249.70 |
| Sampling | 0.07 | 138.07 |
| Parallel Processing (Dask)| 23.62 | 967.74 |

    

### Part 2: Comparative Analysis of Libraries

This part highlights the overall performance of Pandas, Polars, and Dask for full dataset loading without diving into specific strategies. It serves to showcase how each library handles a typical loading task with respect to memory and time.
| Library | Execution Time (s) | Memory Usage (MB) |  
|---------|---------------------|--------------------|  
| Pandas | 16.52 | 1370.75 |  
| Polars | 2.19 | 906.20 |  
| Dask | 22.78 | 967.74 |



## Task 4: Conclusion & Reflection

### Summary of Findings

-   **Polars** performed best in both time and memory due to its optimized engine.
    
-   **Dask** is useful for distributed or larger-than-memory datasets but introduces overhead when `.compute()` is forced.
    
-   **Pandas** is easiest to use but is slow and memory-intensive at large scale.
    

### Benefits

-   **Load Less Data** and **Type Optimization** were most effective in reducing memory.
    
-   **Dask Parallel Processing** is powerful when correctly implemented.
    

### Limitations

-   Dask sampling was skipped as it doesn't support global `.sample()` without loading the full dataset.
    

### Learning Reflection

This assignment provided deep insights into how memory, performance, and parallelism vary between data libraries. We now better understand which tools to use based on dataset size and task type.



## Screenshots & Code

Refer to `big_data.ipynb` for annotated code, plots, and screenshots.



## Submission Info

**Folder**: `bdm/BingChiling/`

-   `big_data.md`
    
-   `big_data.ipynb`
    
-   `readme.md`
    


## References

-   Kaggle: [IMDB Dataset](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset)
    
-   Dask Docs: [https://docs.dask.org](https://docs.dask.org/)
    
-   Polars Docs: [https://docs.pola.rs/user-guide/io/json/](https://docs.pola.rs/user-guide/io/json/)
