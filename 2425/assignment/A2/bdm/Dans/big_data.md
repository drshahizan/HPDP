
# Big Data Analysis: Anime Review

## Table of Contents
1. [Introduction](#1-introduction)
2. [Dataset Overview and Inspection](#2-dataset-overview-and-inspection)
3. [Big Data Handling Strategies](#3-big-data-handling-strategies)
4. [Comparative Analysis](#4-comparative-analysis)
5. [Conclusion and Reflection](#5-conclusion-and-reflection)
6. [References](#6-references)

---

## 1. Introduction

### 1.1 Background of the Project
With people creating more content online and using digital platforms, the amount of data in the entertainment industry and especially in anime, has shot up. When data is very large, using Pandas to examine and analyse the information is no longer simple. Handling tasks for millions of rows often takes time and space from a system which may cause it to crash or run slow.
The main goal is to figure out the best techniques for processing big anime datasets using advanced big data technologies. The main goal is to check where Pandas is slow, then enhance its performance with alternative and scalable libraries like Dask and Polars. The data engineering community is adopting them because they allow for working with big data and processing things simultaneously.
This analysis used information on thousands of anime from a dataset such as their genres, types, episode counts, ratings and how popular they are with users. Since streaming platforms, fan analytics and recommendation systems rely on similar datasets in real life, this project gives an opportunity to practice using scalable methods in the entertainment industry.
### 1.2 Objectives
- Benchmark Pandas, Dask, and Polars
- Explore chunking, data type optimization, and parallel processing
- Measure performance in terms of time, memory, and throughput

### 1.3 Dataset Source
- **Dataset**: Anime Review
- **Source**: [Kaggle]( https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset)
- **Size**: ~4GB CSV file

---

## 2. Dataset Overview and Inspection

### 2.1 Dataset Description
The dataset contains records of residential property sales in the UK, including fields like:
- username
- anime_id
- my_score
- user_id
- gender
- title
- type
- source
- score
- scored_by
- rank
- popularity
- genre

### 2.2 Initial Loading
The dataset was too large to load using standard Pandas methods, so we used chunked reading and preprocessing.

### 2.3 Basic Inspection
Initial inspection was done using:
- `nrows` to sample a small portion
- Memory usage and dtype evaluations
- Structure and completeness checks

---

## 3. Big Data Handling Strategies

### 3.1 Pandas Strategies
Implemented:
- **Chunking** using `pd.read_csv(..., chunksize=...)`
- **Data Type Optimization** by converting string/object columns to `category`
- **Sampling** with `skiprows` and `nrows` to simulate a sample-based analysis

### 3.2 Parallel Processing with Dask
Used Dask to:
- Load large CSV using `dd.read_csv()`
- Optimize memory via column selection
- Compute results lazily and in parallel using `.compute()`

### 3.3 Polars for High Performance
Polars was used as a modern, Rust-backed alternative:
- Used `pl.read_csv()` for fast ingestion
- Queried and filtered data using its expression syntax
- Monitored execution speed and memory usage

---

## 4. Comparative Analysis

### 4.1 Metrics Used
- **Processing Time**
- **Memory Usage**

### 4.2 Summary

#### Traditional Pandas (Baseline)
- Handled full dataset successfully
- High memory usage
- Simple syntax, but not scalable

#### Dask
- Handled full dataset successfully
- Slower due to overhead from lazy evaluation
- Moderate memory usage

#### Polars
- Fastest ingestion and processing
- Very low memory footprint
- Requires learning a new API

---

## 5. Conclusion and Reflection

### 5.1 Summary of Findings
| Library  | Time     | Memory  | Notes                        |
|----------|----------|---------|------------------------------|
| Pandas   | 116.48s  | 7.68 GB    | Eager loading failed         |
| Dask     | 138.83s    | 9.34 GB    | Slow but stable              |
| Polars   | 37.52s      | 7.22 GB    | Fastest and most efficient   |

- **Polars** is the most performant for large datasets.
- **Dask** is robust and good for scaling Pandas workflows.
- **Pandas** is suitable for small datasets only.

### 5.2 Benefits & Limitations

| Tool     | Pros                                    | Cons                                  |
|----------|-----------------------------------------|---------------------------------------|
| Pandas   | Easy to use, mature API                 | Poor scalability                      |
| Dask     | Scales well, familiar API               | Slower, requires understanding of lazy eval |
| Polars   | Fast, memory efficient                  | New syntax, not distributed           |

### 5.3 Personal Reflection

#### Author 1
> Processing the anime dataset during this assignment was enjoyable and full of lessons. I’ve loved anime as someone who watches it, but learning about the data behind it made me admire how large and challenging data in media can be. When I began, I did not realize how much memory and processing capability was needed to handle the whole dataset with Pandas. I had problems with slow performance and game crashes. Yet, using sampling and shrinking the kinds of data stored helped clarify how to deal with large files.
Being able to use Dask and Polars introduced me to ways of working with large amounts of data efficiently. It is clear to me from using Dask and Polars that selecting proper tools is very important. Through this, I am better equipped to use big data tools and ready to deal with situations that appear in data analytics.

#### Author 2
> The project let me learn through actions how to deal with large volumes of data and work with the latest libraries in this area. Learning with the anime dataset was interesting because it combined technical topics with my hobby. At the start, I depended on Pandas, but soon I realized they had limitations when I tried to use the entire file. I noticed that making the application more efficient with chunking and selective loading was necessary.
Using Dask and Polars was a huge improvement. Seeing the Polars process the full dataset in seconds made me realize how much faster it is than when Pandas tries to handle only part of it. Considering this made me realize how important it is to use the newest technologies. In general, taking part in this project boosted my knowledge in programming and helped me consider performance, memory and scalability for big data.


