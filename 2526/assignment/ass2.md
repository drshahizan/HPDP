<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# 📘 Assignment 2: Mastering Big Data Handling

**[Student Briefing and Guidance Document](https://liveutm-my.sharepoint.com/:b:/g/personal/shahizan_live_utm_my/IQDruqzF5F8mSrljcx9KS85ZAaCbWKHUnp7OZpTw3vA9ONA?e=L3p80A)**

**Due Date**: **4 May 2025 5:00 PM**

**Group Work**: Yes (2 students per group)

**Submission Platform**: GitHub (via provided structure) and Google Colab


## 📌 Introduction

In the modern data-driven world, organizations face the challenge of managing and extracting insights from *massive datasets* that far exceed the capabilities of traditional data handling tools. This assignment provides hands-on experience in managing such datasets using Python and its scalable libraries.

Students will apply real-world strategies for handling data volumes above **700MB** using techniques such as **chunking**, **sampling**, **type optimization**, and **parallel computing with Dask**.

## 🎯 Learning Outcomes

By the end of this assignment, students should be able to:

1. Identify challenges and limitations in traditional big data processing.
2. Apply strategies to manage and analyze large datasets efficiently.
3. Compare performance between traditional and optimized methods.

## 📝 Assignment Tasks

### Task 1: Dataset Selection

* Choose a dataset **larger than 700MB** from a reliable source (e.g., Kaggle, UCI Repository).
* The dataset should be rich enough for exploratory and performance comparison.
* Mention dataset details (source, size, domain, number of records).

### Task 2: Load and Inspect Data

* Use **Python** (preferably on **Google Colab**) to load the dataset.
* Ensure the loading method accommodates the file size efficiently.
* Include a brief inspection (e.g., shape, column names, datatypes).

### Task 3: Apply Big Data Handling Strategies

Apply the following **five strategies** to your dataset:

1. **Load Less Data**

   * Load only required columns or filter relevant rows during read operation.

2. **Use Chunking**

   * Process the data in small chunks using `pandas.read_csv(chunksize=...)`.

3. **Optimize Data Types**

   * Convert columns to appropriate types (e.g., `category`, `float32`) to reduce memory usage.

4. **Sampling**

   * Apply random or stratified sampling to reduce the dataset size for fast prototyping.

5. **Parallel Processing with Dask**

   * Use **Dask DataFrame** to read and process large files in parallel.

Each strategy must be:

* Clearly **explained**
* **Implemented with code snippets**
* Accompanied by **screenshots of outputs** or **results**

### Task 4: Comparative Analysis

Perform a **comparison** between:

* **Traditional methods** (e.g., full Pandas load)
* **Optimized strategies** above

Measure and discuss:

* **Memory usage**
* **Execution time**
* **Ease of processing**

Use tables or charts to present your analysis if applicable.

### Task 5: Conclusion & Reflection

* Summarize key observations.
* Discuss the **benefits and limitations** of each method.
* Reflect on what was learned from this assignment.

## 📁 File and Folder Structure

Place your files in your respective group folder inside the `bdm/` directory as follows:

```
bdm/your_group/
├── 📄 big_data.md        ← The main Markdown report
├── 📄 readme.md          ← Brief introduction and links
└── 📄 big_data.ipynb     ← Colab Notebook with code
```

> 💡 Use this GitHub structure: [will inform later]()

## 🧑‍🤝‍🧑 Group Work and Submission

* Each group must consist of **2 students** only.

**Submit**:

1. `big_data.md` – the final Markdown write-up
2. `big_data.ipynb` – the annotated Colab notebook with working code
3. Push to the correct folder in GitHub
4. Documentation

## 📌 Important Notes

* Ensure your **Markdown file is clear**, includes explanations and Python code snippets.
* Cite all data sources.
* Late submissions will **not be entertained**.
* **Academic Integrity** is strictly enforced. Cases of plagiarism or code copying will receive **zero marks** and be referred to the disciplinary committee.

## 🔍 Evaluation Rubric (Suggested)

| Criteria                         | Marks   |
| -------------------------------- | ------- |
| Dataset Description              | 5       |
| Strategy Implementations         | 30      |
| Comparative Analysis             | 15      |
| Code Functionality (Notebook)    | 25      |
| Markdown Clarity & Documentation | 10      |
| Conclusion & Reflection          | 10      |
| GitHub Submission                | 5       |
| **Total**                        | **100** |

## Submission

| Team | Library 1 | Library 2 | Library 3 | Dataset |  Open in GitHub |
| ----- | ----- | ------ | ------ |  ------ | :------: | 
| Sample1 | Pandas | Dask | Koalas | Air Flight Analysis | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/sample/A2) |
| Sample2 | Pandas | Dask | Polars | [🎹 960K Spotify Songs With Lyrics data 🎵](https://www.kaggle.com/datasets/bwandowando/spotify-songs-with-attributes-and-lyrics) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/Sample2) |
| sixseven | Pandas | PyArrow | Polars | [Book Recommendation System](https://www.kaggle.com/datasets/kunaloswal/book-recommendation-system) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/sixseven) |
| Sayur | Pandas | Dask | Polars | [Pakistan Carbon monoxide 2022 - 2025](https://www.kaggle.com/datasets/muhammadbilal77511/pakistan-carbon-monoxide-2022-2025) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/tree/main/2526/assignment/A2/bdm/Sayur) |
| DataPulse | Pandas | Dask | Polars | [Carrier on time performance dataset](https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)]() |
| Horang | Pandas | PyArrow | Polars | [Genius Song Lyrics](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)]() |
| nyamuk | Pandas | Dask | Polars | [UK Housing Prices Paid](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/nyamuk) |
| Data Miner | Pandas | Dask | Polars | [NYC Yellow Taxi Trip Data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data?select=yellow_tripdata_2016-03.csv) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/tree/main/2526/assignment/A2/bdm/Data%20Miner) |
| kak ros | Pandas | Dask | Polars | [Airline Delay and Cancellation Data](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018?select=2009.csv) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/tree/main/2526/assignment/A2/bdm/kak%20ros) |
| DuaTiga | Pandas | Dask | Polars | [Amazon Books Reviews](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/tree/main/2526/assignment/A2/bdm/DuaTiga) |
| Ayam | Pandas | Dask | Polars | [NYC Parking Ticket](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)]() |
| gawr-jus | Pandas | PyArrow | Polars | [Flight Delay Dataset — 2024](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)]() |
| gepuk | Pandas | Dask | Polars | [2019-airline-delays-and-cancellations](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations) | |
| group6 | Pandas | Dask | Polars | [NYC Yellow Taxi Trip Data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) | |
| scubaa | Pandas | Dask | PyArrow | [The MOTHER OF ALL MOVIE REVIEW DATASETS](https://www.kaggle.com/datasets/bwandowando/rotten-tomatoes-9800-movie-critic-and-user-reviews) | |
| OnePlayer | Pandas | Dask | Polars | [Cell Towers Worldwide: Location Data by Continent](https://www.kaggle.com/datasets/zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/tree/main/2526/assignment/A2/bdm/OnePlayer) |

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


