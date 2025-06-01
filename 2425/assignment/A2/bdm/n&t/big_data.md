# 🎧 Big Data Handling Report: Spotify Charts Dataset

## 1. 📁 Dataset Overview  

### 🎵 Dataset: **Spotify Charts - Global & Regional**  
- **Source:** [Kaggle - Spotify Charts Dataset](https://www.kaggle.com/datasets/dhruvildave/spotify-charts)  
- **File Size:** ~3.48 GB  
- **Entries:** `26,173,514` rows and `9` columns  
- **Domain:** Music Streaming, Time Series  
- **Date Range:** Spanning from 2017 onward  

This dataset contains daily rankings for Spotify’s **Top 200** and **Viral 50** charts across multiple regions. Each row represents a song's rank on a specific chart in a specific region on a given date. It is ideal for exploring trends in music popularity and practicing large-scale data handling techniques.

---

### 📊 Dataset Snapshot

| Column Name | Description |
|-------------|-------------|
| `title`     | Name of the song as listed on Spotify. |
| `rank`      | The position of the song on the chart for the specific day and region. |
| `date`      | The chart date (daily granularity). |
| `artist`    | Name of the artist(s) of the song. |
| `url`       | Direct URL to the Spotify track. |
| `region`    | The geographical region (e.g., US, Global, Brazil). |
| `chart`     | The chart type – either **top200** or **viral50**. |
| `trend`     | Indicates if the song’s ranking is **new**, **re-entry**, or unchanged. |
| `streams`   | Number of times the song was streamed on that day in the region. |

> 📌 **Observation:**  
> The dataset includes a mix of categorical (`region`, `chart`, `trend`) and numerical (`rank`, `streams`) data. The text-heavy columns such as `title` and `artist` consume memory due to their string nature.


## 2. ⏱️📊 Measurement Techniques: Time & Memory

To evaluate and compare the performance of various big data handling strategies, we consistently measured both **execution time** and **memory usage**.

### 🧪 Tools Used

- **`time` module** – to track how long each strategy took to run.
- **`pandas.DataFrame.memory_usage(deep=True)`** – to calculate the full memory footprint of the loaded data.

### ⏱️ Time Measurement Snippet

```python
import time

start_time = time.time()
# Data loading or processing code here
end_time = time.time()

print("Time Taken:", (end_time - start_time:.2f), "seconds")
```

### 🧠 Memory Usage Snippet

```python
memory_usage = df.memory_usage(deep=True).sum() / (1024**3)
print("Memory Usage:", (memory_usage:.2f), "GB")
```

These tools were used after each strategy to benchmark improvements in resource efficiency and processing speed.


## 3. 🐼 Traditional Data Load (Baseline)


As a baseline, we loaded the full dataset using the most common method:

```python
import pandas as pd

df = pd.read_csv("spotify_charts.csv")
```

This straightforward approach loads **all columns** and **all rows** into memory with no optimizations. It represents how most users initially interact with CSV data — but it's not suited for very large datasets.

### ⚙️ What This Does:
- Loads 26+ million rows and 9 columns directly into memory.
- No filtering, column selection, or type optimization is applied.
- Used as the **baseline** to compare all optimized strategies.

---

### 📌 Observations:

- **Time Taken:** ~20.92 seconds  
- **Memory Usage:** ~1.88 GB  
- **Ease of Processing:**  
  ❌ Not ideal for machines with <8 GB RAM.  
  ❌ Slower performance when performing downstream operations (e.g., filtering, grouping).  
  ❌ High memory overhead due to default object datatypes for strings.  
  ❌ Not scalable for larger datasets (4GB+ CSVs).

> ⚠️ This traditional approach becomes impractical when working with gigabyte-scale datasets, especially on platforms like Google Colab or limited-memory machines.


## 4. ⚙️ Big Data Handling Strategies

### 4.1 Load Less Data

* **What was done**
* Code snippet
* Time & memory comparison
* Benefit/limitation

### 4.2 Chunking

* Code snippet
* Metrics
* Benefit/limitation

### 4.3 Optimize Data Types

* `astype()` usage (e.g., float32, category)
* Before/after memory usage
* Code snippet
* Benefit/limitation

### 4.4 Sampling

* Strategy (5% sample)
* Code snippet
* Metrics
* Benefit/limitation

## 5. 📊 Comparative Analysis

| Strategy            | Time Taken | Memory Usage | Ease of Processing | Notes |
| ------------------- | ---------- | ------------ | ------------------ | ----- |
| Traditional Load    |            |              |                    |       |
| Load Less Data      |            |              |                    |       |
| Chunking            |            |              |                    |       |
| Optimize Data Types |            |              |                    |       |
| Sampling            |            |              |                    |       |

*(Add chart/bar graph for visual comparison if possible)*

## 6. 🧠 Conclusion & Reflection

* Key takeaways
* Benefits vs limitations
* What you learned from this assignment

