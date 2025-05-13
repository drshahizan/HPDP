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
- [1.3 Target Website and Data To Be Extracted](#13-target-website-and-data-to-be-extracted)

### 2.0 System Design & Architecture
- [2.1 Description of Architecture](#21-description-of-architecture)
- [2.2 Tools and Frameworks Used](#22-tools-and-frameworks-used)
- [2.3 Roles of Team Members](#23-roles-of-team-members)

### 3.0 Data Collection
- [3.1 Crawling Method](#31-crawling-method)
- [3.2 Number of Records Collected](#32-number-of-records-collected)
- [3.3 Ethical Considerations](#33-ethical-considerations)

### 4.0 Data Processing
- [4.1 Cleaning Methods](#41-cleaning-methods)
- [4.2 Data Structure](#42-data-structure)
- [4.3 Transformation and Formatting](#43-transformation-and-formatting)

### 5.0 Optimization Techniques
- [5.1 Methods Used: Multithreading, Multiprocessing, Spark, Etc.](#51-methods-used-multithreading-multiprocessing-spark-etc)
- [5.2 Code Overview or Pseudocode of Techniques Applied](#52-code-overview-or-pseudocode-of-techniques-applied)

### 6.0 Performance Evaluation
- [6.1 Before VS After Optimization](#61-before-vs-after-optimization)
- [6.2 Comparison of Code Execution Time, Peak Memory Usage, CPU Usage and Throughput](#62-comparison-of-code-execution-time-peak-memory-usage-cpu-usage-and-throughput)
- [6.3 Charts and Graphs](#63-charts-and-graphs)

### 7.0 Challenges & Limitations
- [7.1 What Didn’t Go As Planned](#71-what-didnt-go-as-planned)
- [7.2 Any Limitations of Your Solution](#72-any-limitations-of-your-solution)

### 8.0 Conclusion & Future Work
- [8.1 Summary of Findings](#81-summary-of-findings)
- [8.2 What Could Be Improved](#82-what-could-be-improved)

### References
- [References](#references)

### Appendices
- [Sample code snippets](#sample-code-snippets)
- [Screenshots of output](#screenshots-of-output)
- [Links to full code repo or dataset](#links-to-full-code-repo-or-dataset)

<br>

### 1.0 Introduction 
#### 1.1 Background of The Project 
<p style="text-align: justify; hyphens: auto;">
In the era of big data, high-performance computing (HPC) plays a critical role in enabling the efficient processing of vast volumes of information from web sources. Web data extraction, or web scraping, has become a fundamental technique for data collection in fields such as e-commerce analysis, sentiment analysis and market research. However, handling large-scale web data introduces significant challenges, including performance bottlenecks, ethical scraping practices and managing crawl delays. To address these challenges, modern scraping systems increasingly incorporate multithreading, multiprocessing and distributed processing techniques to enhance scalability and efficiency.
  
This project is designed to provide students with practical, hands-on experience in large-scale web data processing using HPC principles. By designing, developing and optimising a web crawler capable of extracting at least 100,000 structured records, students gain insight into real-world technical and ethical challenges associated with web scraping. Furthermore, the project emphasises the importance of system optimisation, particularly through the comparison of different data processing frameworks, thus strengthening critical thinking skills essential for data science professionals.
</p>

##### 1.1.1 Web Scraping
<p style="text-align: justify; hyphens: auto;">
This project focuses on collecting and preparing product data from Lazada Malaysia, specifically targeting women-related categories such as Beauty & Skincare, Health & Wellness, Home & Living, Home Appliances, Mother & Baby, Stationery, and Women’s Fashion. The main objective is to obtain a clean and structured dataset that can later be used for further analysis or machine learning tasks.

The first step involves web scraping, where product data is automatically collected from the selected subcategories on Lazada. Each subcategory's data is then stored separately in seven Excel files for better organisation. There are a total of 115090 rows of data that have been collected. Once the data is collected, it is uploaded to Google Colab for preprocessing.
</p>

##### 1.1.2 Data Processing
<p style="text-align: justify; hyphens: auto;">
In the preprocessing phase, the first task is data integration, where all seven Excel files are combined into a single dataset. To ensure consistency, all string-based fields such as product names are standardised to uppercase formatting. This helps avoid issues caused by inconsistent capitalization during analysis, such as “lotion" and "Lotion" being treated as different items.

Next, we convert important numerical fields like quantity sold and total reviews into numeric data types. This step is crucial because numeric values are required for proper data analysis, such as outlier detection and calculation needed for grouping items into categories.

After ensuring that all data is in the correct format and structure, we handle missing values. For string fields, missing values are filled with "N/A" to clearly indicate unavailable information, while missing numeric fields are filled with 0. This approach ensures that the dataset remains complete without causing errors in future computations. For example, a missing review count is more safely treated as zero than left blank.
  
Duplicate records are then detected and removed to avoid repetition and ensure data accuracy. Once all the cleaning steps are completed, the final, clean dataset is exported into a CSV file, ready for the optimisation process.
</p>

##### 1.1.3 Optimisation Process 
<p style="text-align: justify; hyphens: auto;">
The second phase of the project focuses on optimising the cleaned dataset obtained from the initial preprocessing stage. The objective of this phase is to group and analyse products based on pricing tiers, popularity levels, and market performance by location in order to derive meaningful insights and support further analytical tasks.

The first optimisation step involves the categorisation of products into four pricing tiers, which are budget-friendly, affordable, mid-range and premium. Prior to grouping, all records with a price value of RM0 were removed, as such entries are considered illogical or erroneous. Outliers within the price field were then identified. Upon evaluation, these outliers were deemed plausible and were therefore retained. The minimum and maximum prices (excluding outliers) were calculated and used to define the thresholds for each pricing group. Subsequently, all products, including those with outlier prices, were assigned to the appropriate pricing category based on the established range.
  
The second optimization focuses on product popularity, measured by the total number of reviews. In this stage, outliers were detected and removed to minimise distortion in the analysis. The adjusted minimum and maximum review counts were then used to determine suitable group boundaries. Products were classified into four popularity levels, which are least popular, below average, above average and most popular, based on their total review count.

The final optimization step involves evaluating product performance by location. Products were grouped according to their listed locations, with relevant attributes such as product price and quantity sold. For each location, the average product price and total quantity sold were computed. These figures were used to estimate market performance, calculated by multiplying the average price by the total quantity sold. Locations were then ranked from highest to lowest based on this performance indicator, enabling identification of regions with the strongest sales activity.
</p>

#### 1.2 Objectives
<p style="text-align: justify; hyphens: auto;">
The main objectives of this project are as follows:

- To develop a web crawler capable of extracting a minimum of 100,000 structured records from a targeted Malaysian e-commerce website.
- To apply high-performance computing techniques, including multithreading, multiprocessing and distributed processing, to optimise the efficiency and scalability of the web crawling and data processing systems.
- To implement ethical web scraping practices by respecting crawl delays and website usage policies.
- To conduct a comparative performance analysis of different data processing frameworks (Pandas, Polars and PySpark) based on the time consumed during data processing.
- To enhance students' technical proficiency, critical thinking in system optimization and collaborative skills in a diverse team environment.
</p>

#### 1.3 Target Website and Data To Be Extracted
<p style="text-align: justify; hyphens: auto;">
For this project, Lazada Malaysia (https://www.lazada.com.my/) was selected as the target website. Lazada is one of the leading e-commerce platforms in Southeast Asia, offering a wide range of products across multiple categories. The focus of the data extraction is on products under the "Women" category, which includes the following subcategories: Women's Fashion, Stationery, Mother and Baby, Home and Living, Health and Wellness and Beauty and Care. The fields extracted for each product are:
  
- <b>Product Name:</b> The title or description of the product as displayed on the website.
- <b>Location:</b> The seller's or product's listed location.
- <b>Quantity Sold:</b> The number of units sold, indicating the popularity of the product.
- <b>Price:</b> The listed selling price of the product.
- <b>Total reviews:</b> The total number of customer ratings received by the product.

Data scraping was carried out by applying a mix of Python libraries and tools such as BeautifulSoup, Selenium, Requests for complete data extraction. The stocks of data collected were then manipulated using pandas polars and PySpark, the processing time compared to evaluate performance enhancement in varied optimisation techniques.

</p>

### 2.0 System Design & Architecture
#### 2.1 Description of Architecture
#### 2.2 Tools and Frameworks Used
#### 2.3 Roles of Team Members

### 3.0 Data Collection
#### 3.1 Crawling Method
#### 3.2 Number of Records Collected
#### 3.3 Ethical Considerations

### 4.0 Data Processing
#### 4.1 Cleaning Methods
#### 4.2 Data Structure
#### 4.3 Transformation and Formatting

### 5.0 Optimization Techniques
#### 5.1 Methods Used: Multithreading, Multiprocessing, Spark, Etc.
<p style="text-align: justify; hyphens: auto;">
To optimize the data processing step, three python libraries were utilized; Pandas, polars and Pyspark libraries. Pandas was initially used as a benchmark because it is straightforward, and has many powerful data manipulation abilities. However, as Pandas functions in a single threaded approach it was found to have limitations with large datasets. To ensure a faster process, Polars was introduced. Polars supports multithreading and lazy evaluation which means that operations can compute across several CPU cores at once, and consequently are faster than Pandas.
  
Finally, for distributed processing an experimental and open source framework written in Python that runs on top of Apache Spark called PySpark was used. PySpark allows processing data at parallel across several cores or machines hence amazingly suitable for very large datasets. Its distributed architecture and native optimisation properties enabled large scale data transformation to work efficiently. Using Pandas (single-threaded), and the multithreaded variant of Polars and PySpark (distributed), the project evaluated the performance and scalability of various optimisation methods for processing data web-scraped.
</p>

#### 5.2 Code Overview or Pseudocode of Techniques Applied
<p>
  <b>Code Overview of Pandas Part 1</b>
</p>
<br>
<div style="text-align: center;">
  <img src="PandasPart1-Colab-05-13-2025_11_05_PM.png" 
       alt="Code Overview of Pandas Part 1"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>
<br>
<p>
  <b>Code Overview of Pandas Part 2</b>
</p>
<br>
<div style="text-align: center;">
  <img src="PandasPart1-Colab-05-13-2025_11_26_PM.png" 
       alt="Code Overview of Pandas Part 2"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>

### 6.0 Performance Evaluation
#### 6.1 Before VS After Optimization
#### 6.2 Comparison of Code Execution Time, Peak Memory Usage, CPU Usage and Throughput
#### 6.3 Charts and Graphs

### 7.0 Challenges & Limitations
#### 7.1 What Didn’t Go As Planned
#### 7.2 Any Limitations of Your Solution

### 8.0 Conclusion & Future Work
#### 8.1 Summary of Findings
#### 8.2 What Could Be Improved

### References

### Appendices
### Sample code snippets
### Screenshots of output
### Links to full code repo or dataset


