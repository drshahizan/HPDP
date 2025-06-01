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


## 2. 🧪 Initial Data Inspection

* Code snippet for inspecting the data (head, info, etc.)
* Short analysis of what you observed

## 3. 🐼 Traditional Data Load (Baseline)

* Full load using `pd.read_csv()`
* Measure:

  * Load time
  * Memory usage
* Code snippet
* Output metrics (create a table or bar chart)
* Short discussion of baseline issues

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

