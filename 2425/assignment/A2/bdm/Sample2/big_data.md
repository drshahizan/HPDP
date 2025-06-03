# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:  
- Student 1: *Goh Jiale, A22EA0043*  
- Student 2: *Yong Wern Jie, A22EC0121*

---

## 📌 Introduction

*Write a brief overview of the importance of big data handling and what this assignment covers.*

---

## 🎯 Learning Outcomes

1. Identify challenges and limitations in traditional big data processing.
2. Apply strategies to manage and analyze large datasets efficiently.
3. Compare performance between traditional and optimized methods.

---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: *🎹 960K Spotify Songs With Lyrics Data 🎵*
* **Source**: [Kaggle – bwandowando](https://www.kaggle.com/datasets/bwandowando/spotify-songs-with-attributes-and-lyrics)
* **Domain**: *Music / Entertainment*
* **File Size**: *1.54 GB*
* **Shape**: *955,320 rows × 17 columns*


### 📖 Description

This dataset is an enriched compilation built by combining multiple large-scale Spotify-related datasets, including:

* *Spotify 1M+ Tracks*,
* *Spotify + Genius Dataset*,
* *30K Spotify Songs*,
* *6K Spotify Playlists*, and more.

From over 3.3 million tracks submitted to the Spotify Lyrics API, about **960,000** were matched with usable lyrics. These tracks include audio attributes (like tempo, energy, and acousticness), metadata (such as artist and album), and lyrical content—making the dataset ideal for both **audio signal processing** and **natural language processing** applications.

> ⚠️ Note:
>
> * Some songs do **not** have album information.
> * A portion of the lyrics lack properly annotated `startTimeMs` values.
> * Not every track contains lyrics.


### 🔍 Key Features

* **Track metadata**: name, artist(s), album
* **Audio features**: danceability, energy, tempo, loudness, valence, etc.
* **Lyrics**: complete song lyrics with optional timestamp annotations
* **Merged sources**: enriched using data from multiple Kaggle contributors and lyric APIs


### 📊 Data Column Description

| Column Name        | Data Type | Description                                                         |
| ------------------ | --------- | ------------------------------------------------------------------- |
| `id`               | object    | Unique Spotify track ID                                             |
| `name`             | object    | Name of the song                                                    |
| `album_name`       | object    | Name of the album (may be missing for some entries)                 |
| `artists`          | object    | Artist(s) who performed the song                                    |
| `danceability`     | float64   | Suitability for dancing (0.0 = low, 1.0 = high)                     |
| `energy`           | float64   | Intensity and activity level (0.0 = calm, 1.0 = energetic)          |
| `key`              | object    | Musical key (e.g., C, D#, F#)                                       |
| `loudness`         | float64   | Loudness in decibels (typically -60 to 0 dB)                        |
| `mode`             | object    | Modality of the song: major or minor                                |
| `speechiness`      | float64   | Presence of spoken words (higher = more speech-like)                |
| `acousticness`     | float64   | Confidence score of acoustic quality (0.0 to 1.0)                   |
| `instrumentalness` | float64   | Likelihood that the track is instrumental (0.0 to 1.0)              |
| `liveness`         | float64   | Probability that the track was performed live                       |
| `valence`          | float64   | Musical positivity (0.0 = sad, 1.0 = happy/upbeat)                  |
| `tempo`            | float64   | Tempo in beats per minute (BPM)                                     |
| `duration_ms`      | float64   | Length of the track in milliseconds                                 |
| `lyrics`           | object    | Full lyrics of the song (may include timestamps like `startTimeMs`) |

---

Here’s a clean and well-structured markdown for your **📝 Task 2: Load and Inspect Data**, including **Loading Strategy** and **Dataset Inspection** sections:

---

## 📝 Task 2: Load and Inspect Data

### 🔹 Loading Strategy

To load the dataset efficiently in [Google Colab](https://colab.research.google.com/), the following steps were taken:

1. **Imported `kaggle.json`**
   Uploaded via the Colab file upload feature:

   ```python
   from google.colab import files
   files.upload()  # Upload kaggle.json
   ```

2. **Configured Kaggle API Credentials**
   Moved the uploaded file to the `.kaggle` directory and set proper permissions:

   ```bash
   !mkdir -p ~/.kaggle
   !cp kaggle.json ~/.kaggle/
   !chmod 600 ~/.kaggle/kaggle.json
   ```

3. **Downloaded Dataset from Kaggle**
   Using Kaggle CLI to fetch the dataset directly into the Colab environment:

   ```bash
   !kaggle datasets download -d bwandowando/spotify-songs-with-attributes-and-lyrics
   ```

4. **Unzipped the Dataset File**
   Extracted the dataset ZIP file:

   ```bash
   !unzip spotify-songs-with-attributes-and-lyrics.zip
   ```

5. **Loaded a Sample (100 Rows) Using `pandas.read_csv()`**
   This is to allow quicker inspection without overloading memory:

   ```python
   import pandas as pd
   df = pd.read_csv('songs_with_attributes_and_lyrics.csv', nrows=1000000)
   ```

---

### 🔹 Dataset Inspection

#### 📌 First 5 Rows

```python
df['lyrics_short'] = df['lyrics'].astype(str).str.slice(0, 100) + '...'

print("First 5 rows of the dataset:")
display(df.drop(columns=['lyrics']).head())
df = df.drop(columns=['lyrics_short'])
```
> ✅ *The `lyrics` column contains very long strings, so we truncated it for display to provide a more concise overview of the dataset’s structure.*

|index|id|name|album\_name|artists|danceability|energy|key|loudness|mode|speechiness|acousticness|instrumentalness|liveness|valence|tempo|duration\_ms|lyrics\_short|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0Prct5TDjAnEgIqbxcldY9|\!|UNDEN\!ABLE|\['HELLYEAH'\]|0\.415|0\.605|7|-11\.157|1|0\.0575|0\.00116|0\.838|0\.471|0\.193|100\.059|79500\.0|He said he came from Jamaica, he owned a couple acres A couple fake visas 'cause he never got his \.\.\.|
|1|2ASl4wirkeYm3OWZxXKYuq|\!\!|NaN|Yxngxr1|0\.788|0\.648|7|-9\.135|0|0\.315|0\.9|0\.0|0\.176|0\.287|79\.998|114000\.0|Fucked a bitch, now she running with my kids And you said I never listen, yeah, yeah Yeah, yeah, y\.\.\.|
|2|69lcggVPmOr9cvPx9kLiiN|\!\!\! - Interlude|Where I Belong EP|\['Glowie'\]|0\.0|0\.0354|7|-20\.151|0|0\.0|0\.908|0\.0|0\.479|0\.0|0\.0|11413\.0|Oh, my God, I'm going crazy \.\.\.|
|3|4U7dlZjg1s9pjdppqZy0fm|\!\!De Repente\!\!|Un Palo Al Agua \(20 Grandes Canciones\)|\['Rosendo'\]|0\.657|0\.882|5|-6\.34|1|0\.0385|0\.0074|1\.27e-05|0\.0474|0\.939|123\.588|198173\.0|Continuamente se extraña la gente si no puede ser verdad que de repente tan fácilmente material sin\.\.\.|
|4|4v1IBp3Y3rpkWmWzIlkYju|\!\!De Repente\!\!|Fuera De Lugar|\['Rosendo'\]|0\.659|0\.893|5|-8\.531|1|0\.0411|0\.0922|1\.91e-05|0\.0534|0\.951|123\.6|199827\.0|Continuamente se extraña la gente si no puede ser verdad que de repente tan fácilmente material sin\.\.\.|
---

#### 📐 Shape of the Dataset

```python
print(f"\nDataset Shape:\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
```

![image](https://github.com/user-attachments/assets/1fb696c5-2295-4e68-bbec-ffd07d719fc4)


---

#### 🏷️ Column Names and Data Types

```python
display(df.dtypes.to_frame(name='Data Type').T)
```
![image](https://github.com/user-attachments/assets/5112b408-7ca5-41de-8339-6b2e3141c67b)

---

#### 📋 Summary Info

```python
df.info()
```

![image](https://github.com/user-attachments/assets/e2610d93-51b2-4d7a-849a-6e085e14f41e)


---


## 🛠️ Task 3: Apply Big Data Handling Strategies

### 1. Load Less Data  
**Explanation**:  
*Describe the idea of only loading required columns or rows.*  

**Implementation Summary**:  
*Mention what columns/rows were selected.*

**Output Summary**:  
*Screenshot or result description.*

---

### 2. Use Chunking  
**Explanation**:  
*Briefly explain chunking and why it's useful.*  

**Implementation Summary**:  
*Chunk size and method.*  

**Output Summary**:  
*Result of processing with chunks.*

---

### 3. Optimize Data Types  
**Explanation**:  
*Importance of reducing memory by adjusting data types.*

**Implementation Summary**:  
*Which columns were optimized and how.*

**Output Summary**:  
*Memory usage before vs after.*

---

### 4. Sampling  
**Explanation**:  
*What sampling was done and why.*

**Implementation Summary**:  
*How sampling was applied (random/stratified/etc.)*

**Output Summary**:  
*Size of sample and representation summary.*

---

### 5. Parallel Processing with Dask  
**Explanation**:  
*How Dask helps in parallelizing the workload.*  

**Implementation Summary**:  
*Which operations were parallelized.*

**Output Summary**:  
*Comparison in performance or output.*

---

## 📊 Task 4: Comparative Analysis

| Metric                | Traditional Pandas | Optimized Strategies |
|-----------------------|--------------------|----------------------|
| Memory Usage          | *e.g., 1.5GB*       | *e.g., 300MB*        |
| Execution Time        | *e.g., 120s*        | *e.g., 40s*          |
| Ease of Processing    | *Subjective score or remarks* | *Remarks* |

*You may include charts, plots, or bullet points here for additional analysis.*

---

## 🧠 Task 5: Conclusion & Reflection

### 🔹 Summary of Observations  
*Summarize the main findings from each strategy.*

### 🔹 Benefits & Limitations  
- **Load Less Data**:  
- **Chunking**:  
- **Data Type Optimization**:  
- **Sampling**:  
- **Dask Parallel Processing**:  

### 🔹 Reflection  
*What did you learn about handling big data, and how will it be useful in the future?*

---

## 📁 Folder Structure

```plaintext
bdm/your_group/
├── big_data.md        ← This file
├── readme.md          ← Brief intro and links
└── big_data.ipynb     ← Code notebook
