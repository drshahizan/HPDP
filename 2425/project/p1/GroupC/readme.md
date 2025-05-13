<h1 align="center"> 
  Group C - Women's Purchase Analysis
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>BERNICE LIM JING XUAN</td>
    <td>A22EC0038</td>
  </tr>
  <tr>
    <td width=80%>KEK JESSLYN</td>
    <td>A22EC0057</td>
  </tr>
  <tr>
    <td width=80%>TAN JUN YUAN</td>
    <td>A22EC0107</td>
  </tr>
  <tr>
    <td width=80%>NAVACHANDER NAVASANTAR</td>
    <td>A22EC0226</td>
  </tr>
</table>

<br>

## Table of Contents

### 1.0 Introduction
- [1.1 Background of The Project](#11-background-of-the-project)
  - [1.1.1 Web Scraping](#111-web-scraping)
  - [1.1.2 Data Processing](#112-data-processing)
  - [1.1.3 Optimisation Process](#113-optimisation-process)
- [1.2 Objectives](#12-objectives)
- [1.3 Target website and data to be extracted](#13-target-website-and-data-to-be-extracted)

### 2.0 System Design & Architecture
- [2.1 Description of architecture](#21-description-of-architecture)
- [2.2 Tools and frameworks used](#22-tools-and-frameworks-used)
- [2.3 Roles of team members](#23-roles-of-team-members)

### 3.0 Data Collection
- [3.1 Crawling method](#31-crawling-method)
- [3.2 Number of records collected](#32-number-of-records-collected)
- [3.3 Ethical considerations](#33-ethical-considerations)

### 4.0 Data Processing
- [4.1 Cleaning methods](#41-cleaning-methods)
- [4.2 Data structure](#42-data-structure)
- [4.3 Transformation and formatting](#43-transformation-and-formatting)

### 5.0 Optimization Techniques
- [5.1 Methods used: multithreading, multiprocessing, Spark, etc.](#51-methods-used-multithreading-multiprocessing-spark-etc)
- [5.2 Code overview or pseudocode of techniques applied](#52-code-overview-or-pseudocode-of-techniques-applied)

### 6.0 Performance Evaluation
- [6.1 Before vs after optimization](#61-before-vs-after-optimization)
- [6.2 Comparison of Code Execution Time, Peak Memory Usage, CPU usage and Throughput](#62-comparison-of-code-execution-time-peak-memory-usage-cpu-usage-and-throughput)
- [6.3 Charts and graphs](#63-charts-and-graphs)

### 7.0 Challenges & Limitations
- [7.1 What didn’t go as planned](#71-what-didnt-go-as-planned)
- [7.2 Any limitations of your solution](#72-any-limitations-of-your-solution)

### 8.0 Conclusion & Future Work
- [8.1 Summary of findings](#81-summary-of-findings)
- [8.2 What could be improved](#82-what-could-be-improved)

### References
- [References](#references)

### Appendices
- [Sample code snippets](#sample-code-snippets)
- [Screenshots of output](#screenshots-of-output)
- [Links to full code repo or dataset](#links-to-full-code-repo-or-dataset)

<br>

## 1.0 Introduction 
### 1.1 Background of The Project 
<p>
  In the era of big data, high-performance computing (HPC) plays a critical role in enabling the efficient processing of vast volumes of information from web sources. Web data extraction, or web scraping, has become a fundamental technique for data collection in fields such as e-commerce analysis, sentiment analysis and market research. However, handling large-scale web data introduces significant challenges, including performance bottlenecks, ethical scraping practices and managing crawl delays. To address these challenges, modern scraping systems increasingly incorporate multithreading, multiprocessing and distributed processing techniques to enhance scalability and efficiency.
  
  This project is designed to provide students with practical, hands-on experience in large-scale web data processing using HPC principles. By designing, developing and optimising a web crawler capable of extracting at least 100,000 structured records, students gain insight into real-world technical and ethical challenges associated with web scraping. Furthermore, the project emphasises the importance of system optimisation, particularly through the comparison of different data processing frameworks, thus strengthening critical thinking skills essential for data science professionals.
</p>

#### 1.1.1 Web Scraping
<p>
  This project focuses on collecting and preparing product data from Lazada Malaysia, specifically targeting women-related categories such as Beauty & Skincare, Health & Wellness, Home & Living, Home Appliances, Mother & Baby, Stationery, and Women’s Fashion. The main objective is to obtain a clean and structured dataset that can later be used for further analysis or machine learning tasks.

  The first step involves web scraping, where product data is automatically collected from the selected subcategories on Lazada. Each subcategory's data is then stored separately in seven Excel files for better organisation. There are a total of 115090 rows of data that have been collected. Once the data is collected, it is uploaded to Google Colab for preprocessing.
</p>

#### 1.1.2 Data Processing
<p>
  In the preprocessing phase, the first task is data integration, where all seven Excel files are combined into a single dataset. To ensure consistency, all string-based fields such as product names are standardised to uppercase formatting. This helps avoid issues caused by inconsistent capitalization during analysis, such as “lotion" and "Lotion" being treated as different items.

  Next, we convert important numerical fields like quantity sold and total reviews into numeric data types. This step is crucial because numeric values are required for proper data analysis, such as outlier detection and calculation needed for grouping items into categories.

  After ensuring that all data is in the correct format and structure, we handle missing values. For string fields, missing values are filled with "N/A" to clearly indicate unavailable information, while missing numeric fields are filled with 0. This approach ensures that the dataset remains complete without causing errors in future computations. For example, a missing review count is more safely treated as zero than left blank.
  
  Duplicate records are then detected and removed to avoid repetition and ensure data accuracy. Once all the cleaning steps are completed, the final, clean dataset is exported into a CSV file, ready for the optimisation process.
</p>

#### 1.1.3 Optimisation Process 
<p>
  The second phase of the project focuses on optimising the cleaned dataset obtained from the initial preprocessing stage. The objective of this phase is to group and analyse products based on pricing tiers, popularity levels, and market performance by location in order to derive meaningful insights and support further analytical tasks.

  The first optimisation step involves the categorisation of products into four pricing tiers, which are budget-friendly, affordable, mid-range and premium. Prior to grouping, all records with a price value of RM0 were removed, as such entries are considered illogical or erroneous. Outliers within the price field were then identified. Upon evaluation, these outliers were deemed plausible and were therefore retained. The minimum and maximum prices (excluding outliers) were calculated and used to define the thresholds for each pricing group. Subsequently, all products, including those with outlier prices, were assigned to the appropriate pricing category based on the established range.
  
  The second optimization focuses on product popularity, measured by the total number of reviews. In this stage, outliers were detected and removed to minimise distortion in the analysis. The adjusted minimum and maximum review counts were then used to determine suitable group boundaries. Products were classified into four popularity levels, which are least popular, below average, above average and most popular, based on their total review count.

  The final optimization step involves evaluating product performance by location. Products were grouped according to their listed locations, with relevant attributes such as product price and quantity sold. For each location, the average product price and total quantity sold were computed. These figures were used to estimate market performance, calculated by multiplying the average price by the total quantity sold. Locations were then ranked from highest to lowest based on this performance indicator, enabling identification of regions with the strongest sales activity.
</p>

### 1.2 Objectives

The main objectives of this project are as follows:

- To develop a web crawler capable of extracting a minimum of 100,000 structured records from a targeted Malaysian e-commerce website.
- To apply high-performance computing techniques, including multithreading, multiprocessing and distributed processing, to optimise the efficiency and scalability of the web crawling and data processing systems.
- To implement ethical web scraping practices by respecting crawl delays and website usage policies.
- To conduct a comparative performance analysis of different data processing frameworks (Pandas, Polars and PySpark) based on the time consumed during data processing.
- To enhance students' technical proficiency, critical thinking in system optimization and collaborative skills in a diverse team environment.

