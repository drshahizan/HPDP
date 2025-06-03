<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# 📘 Assignment 2: Mastering Big Data Handling


**Due Date**: **4 June 2025 5:00 PM**

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
| wns & YX | Pandas | Dask | Polars | [2019 Airline Delays w/Weather and Airport Detail](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations?resource=download) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/sample/A2) |
| Mainecoon | Pandas | Dask | Polars | [NYC Parking Tickets](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets?select=Parking_Violations_Issued_-_Fiscal_Year_2014__August_2013___June_2014_.csv) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/sample/A2) |
| n & t | Pandas | Polars | Dask | [Spotify Charts](https://www.kaggle.com/datasets/dhruvildave/spotify-charts) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/sample/A2) |
| DANS | Pandas | Polars | Dask | [Anime Dataset 2023](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/sample/A2) |
| MasterData | Pandas | Polars | Dask | [Amazon Books Reviews](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?select=Books_rating.csv) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/MasterData) |
| KKK | Pandas | Polars | Dask | [School Donations](https://www.kaggle.com/datasets/perkymaster/school-donations?select=Projects.csv) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/KKK) |
| LCLY | Pandas | Polars | Dask | [UK Housing Prices Paid](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/LCLY/lcly.md) |
| MAS | Pandas | Polars | Dask | [eCommerce behavior data from multi category store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/MAS) |
| BingChiling | Pandas|Polars|Dask | [IMDB Review](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/BingChiling) |
|Transformer|Pandas|Polars|Dask| [Transactions Data](https://www.kaggle.com/datasets/ismetsemedov/transactions?select=synthetic_fraud_data.csv)| [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/Transformer) |
| GHIS | Pandas | Polars | PyArrow | [GitHub Issues](https://www.kaggle.com/datasets/davidshinn/github-issues/data) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](p1/sample/A2) |
| ID | Pandas | Polars | Dask | [Data Expo 2009: Airline On Time Data](https://www.kaggle.com/datasets/wenxingdi/data-expo-2009-airline-on-time-data) | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](A2/bdm/ID) |
| Solo Squad | Pandas | Polars | Dask | [Data Expo 2009: Airline On Time Data]() | [![Open in GitHub]() |





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


