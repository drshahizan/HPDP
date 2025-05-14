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

<p align="center">
  <img src="./Images/WebCrawlerSystemArchitecture.png" 
       alt="Web Crawler System Architecture" width="60%">
</p>

<p align="center">
  <em>Figure 1: Architecture of the Web Crawler System</em>
</p>

This project describes the design and implementation of a web crawler system for data extraction mechanisation, cleaning, optimisation, and analysis. In this project, data was acquired from Lazada Malaysia with a particular focus on the Women’s category. The obtained dataset is titled **“Women’s Purchase Analysis”**.

The system begins by sending a request to the target website and receiving the corresponding response. The **Crawler** component traverses the web pages in an organized manner to gather pertinent data. The **Parser**, using libraries such as **BeautifulSoup** and **Selenium**, extracts structured data from the gathered web content.

The extracted data is saved to a CSV file for subsequent processes.

**Following data extraction:**

- **Data cleaning and transformation** are performed to remove inconsistencies, handle missing values, and standardize the dataset to ensure quality and consistency.
- Cleaned data is stored in a structured format separately.

**For performance enhancement:**

- Three libraries — **Pandas**, **Polars**, and **PySpark** — are used to optimize data processing speed.
- A performance analysis is conducted to compare the effectiveness of these optimization methods.

**Finally:**

- Cleaned and optimized data is made available for user queries.
- Users can interact with the system by sending queries, and the system generates requested analysis results based on the processed dataset.

This system enables a full workflow from data acquisition to meaningful data retrieval, offering an insightful analysis of women’s purchase trends on Lazada.

#### 2.2 Tools and Frameworks Used

The following tools and frameworks were used during the project:

- **BeautifulSoup**  
  A Python library used for parsing HTML and XML documents. It simplified the process of retrieving targeted information from Lazada web pages during the web scraping phase.

- **Selenium**  
  A web automation tool used to interact with dynamic pages. It handled content that required user interaction (such as scrolling and clicking) to fully load before extraction.

- **Python**  
  The primary programming language used for implementing web scraping, data cleaning, and data analysis functionalities.

- **Pandas**  
  A powerful Python library for data manipulation and analysis. It was used for cleaning, transforming, and processing the extracted data effectively.

- **Polars**  
  A high-performance DataFrame library written in Rust, serving as an alternative to Pandas when working with larger datasets that require more speed.

- **PySpark**  
  The Python API for Apache Spark, used to optimize the processing of large datasets. It enabled distributed data operations, improving performance and scalability while reducing errors.

#### 2.3 Roles of Team Members

<div align="center">
| Team Member              | Roles and Contributions                                                                 |
|--------------------------|------------------------------------------------------------------------------------------|
| **Bernice Lim Jing Xuan** | - Project planning and management<br>- Developed optimization code using Pandas          |
| **Kek Jesslyn**           | - Web crawling and scraping<br>- Developed scrapers using BeautifulSoup and Selenium<br>- Conducted performance comparison testing using laptop |
| **Navachander Navasantar**| - Developed optimization code using PySpark<br>- Assisted in report documentation       |
| **Tan Jun Yuan**          | - Developed optimization code using Polars<br>- Assisted in report work planning and documentation |
</div>
<p align="center">
  <em>Table 1: Roles of Team Members</em>
</p>

### 3.0 Data Collection
#### 3.1 Crawling Method
<p style="text-align: justify; hyphens: auto;">
The web scraping script functioned with Python tools that used Selenium to control browsers and BeautifulSoup to extract HTML data. Our scraping solution undertook multiple page operations in female-oriented Lazada product sections including fashion and skincare along with wellness and home and baby and stationery selections.

- The scraping system detected page count through pagination components before it automatically visited all accessible pages in each category.
- The scraper included rate-limiting functions that simulated human behaviors by introducing random sleep time between 2.5 and 5 seconds when triggering actions such as page loading or "next" button clicks.
- The scraper relies on async handling while using Selenium's WebDriverWait to monitor page element load times as a method to avoid incomplete content during processing. Manual detection occurs when CAPTCHAs appear since a temporary stop occurs for user confirmation.

</p>

#### 3.2 Number of Records Collected
<p style="text-align: justify; hyphens: auto;">
A total of 115090 records were obtained from 36 distinct URLs that covered multiple pricing segments and sections including Women’s Fashion, Beauty Skincare, Health Wellness, Home Living, Home Appliances, Mother & Baby and Stationery. Each record consists of:

- Product name
- Price
- Seller location
- Quantity sold
- Total reviews

</p>

#### 3.3 Ethical Considerations
<p style="text-align: justify; hyphens: auto;">
The data scraping operation abided by all ethical standards throughout the process.
- Research and academic needs formed the sole basis for the scraping activities.
- The company Lazada has not declared any restrictions on data scraping for our collected data so we protected their server by delaying requests while managing concurrent requests at a moderate level.
- The researchers manually dealt with CAPTCHA interruptions to prevent any security bypassing situations.
- Our data scraping operations did not involve any wishes of personalized user information.
- We would either have accessed the Lazada API or attempted to obtain permission through clear terms if the platform provided either option.

</p>

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
  <b><u>Code Overview of Pandas Part 1</u></b>
</p>
<div style="text-align: center;">
  <img src="Images/PandasPart1-Colab-05-13-2025_11_05_PM.png" 
       alt="Code Overview of Pandas Part 1"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>
<br>
<p>
  <b><u>Code Overview of Pandas Part 2</u></b>
</p>
<div style="text-align: center;">
  <img src="Images/PandasPart2-Colab-05-13-2025_11_26_PM.png" 
       alt="Code Overview of Pandas Part 2"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>
<br>
<p>
  <b><u>Code Overview of Polars Part 1</u></b>
</p>
<div style="text-align: center;">
  <img src="Images/P1_POLARS_CPU_MEMORY_ExecutionTime_PROCESSING-ipynb-Colab-05-13-2025_11_50_PM.png" 
       alt="Code Overview of Polars Part 1"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>
<br>
<p>
  <b><u>Code Overview of Polars Part 2</u></b>
</p>
<div style="text-align: center;">
  <img src="Images/P2_POLARS_CPU_MEMORY_ExecutionTime_PROCESSING-ipynb-Colab-05-13-2025_11_52_PM.png" 
       alt="Code Overview of Polars Part 2"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>
<br>
<p>
  <b>Code Overview of PySpark Part 1:</b>
</p>
<div style="text-align: center;">
  <img src="Images/PySpark_Part1.png" 
       alt="Code Overview of PySpark Part 1"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>
<br>
<p>
  <b>Code Overview of PySpark Part 2:</b>
</p>
<div style="text-align: center;">
  <img src="Images/PySpark_Part2.png" 
       alt="Code Overview of PySpark Part 2"
       style="border: 2px solid #ccc; border-radius: 8px; max-width: 60%; height: auto;">
</div>

### 6.0 Performance Evaluation
#### 6.1 Before VS After Optimization
#### 6.2 Comparison of Code Execution Time, Peak Memory Usage, CPU Usage and Throughput
#### 6.3 Charts and Graphs

### 7.0 Challenges & Limitations
#### 7.1 What Didn’t Go As Planned
<p style="text-align: justify; hyphens: auto;">
Initially, the project intended to use only Requests and BeautifulSoup for web scraping. However, Lazada’s dynamic JavaScript-driven content made it impossible to retrieve the necessary information with these tools alone. Therefore, Selenium was incorporated to handle the dynamic loading of data. However, using Selenium brought new issues, particularly the need for ChromeDriver installation. Since Google Colab could not successfully run ChromeDriver, the team had to shift the environment to Visual Studio Code on local machines. This transition increased the setup time and complexity.
  
Another major challenge was Lazada’s frequent CAPTCHA verifications. The team had to manually solve CAPTCHAs during the scraping process, which greatly slowed down data collection. Scraping had to be done during weekends, requiring long hours in front of the computer to monitor and complete the verification steps.

During the data processing stage, differences in library capabilities also posed problems. For example, Polars could not directly read Excel files. To resolve this, the data was first read into Pandas and then converted into a Polars DataFrame, adding extra steps and minor inefficiencies to the workflow.
</p>

#### 7.2 Any Limitations of Your Solution
<p style="text-align: justify; hyphens: auto;">
Despite overcoming many challenges, some limitations remained. The most significant was the reliance on manual CAPTCHA handling, which prevented full automation and reduced scraping efficiency. Running Selenium locally on Visual Studio Code also restricted collaboration, as each member needed to configure their own environment separately. This limited the flexibility that cloud platforms like Colab would have provided.
  
In addition, extra conversion steps between data formats affected the purity of the performance comparisons between Pandas, Polars and PySpark. Although functional, it introduced slight variations in the benchmarking results.
  
Finally, the need for manual oversight and longer scraping times meant that the project could not easily scale to even larger datasets or implement more advanced scraping strategies like headless browsing or automated CAPTCHA solving.
</p>

### 8.0 Conclusion & Future Work
#### 8.1 Summary of Findings
<p style="text-align: justify; hyphens: auto;">
This project sought to improve high-efficiency data processing for massive web crawling of Lazada Malaysia's Women category. Our group collected over 115,000 product listings by utilising the tools named Selenium and BeautifulSoup to navigate the site and pull out information such as product titles, price, number sold, seller locations, and customer reviews. We filtered and arranged the data once it was gathered, prepared for analysis. 
  
We then contrasted and examined three distinct libraries to determine which one was most appropriate to process large-scale data effectively:
- Pandas, though easy to use and effective for small to midsize datasets, showed worsening performance and more memory usage with our large dataset and thus turned out to be less effective for large-scale data processing tasks.
- Polars, with a Rust backend and lazy evaluation approach, exhibited excellent performance gains in speed and memory consumption. It offered a perfect harmony between usability and functionality for moderately sized datasets.
- PySpark was typified by scalability, distributed processing, and appropriateness for large-scale data projects. Still, its configurational complexity and associated overhead rendered it less suitable for small or medium-size projects.

Overall, this project provided our group with hands-on practice, from data collections and cleaning to performance testing of modern data processing tools. Most significantly, we learned how to assess and choose suitable technologies depending on certain requirements such as dataset size, processing time, and memory consumption. This project not only improved our technical expertise in Python and high performance libraries but also improved our critical thinking, collaboration, and problem solving skills, equipping us for upcoming projects in data engineering and data analysis.

#### 8.2 What Could Be Improved
<p style="text-align: justify; hyphens: auto;">
While the current implementation successfully achieved its primary goals, there are several meaningful ways the project can be expanded and enhanced in the future:
  
1. Automate CAPTCHA Handling for seamless handling
Manual CAPTCHA solving during scraping delayed the data collection process. 2Captcha browser extension allows skipping reCAPTCHAs. This extension automates the process of solving reCAPTCHA, making it easier and faster for users to bypass these verifications [1].  Incorporating automated services such as 2Captcha can automate the process with machine learning powered CAPTCHA solvers.
  
2. Make the most of GPU Powered Libraries for better performance
Libraries such as RAPIDS cuDF by NVIDIA can leverage GPUs to greatly accelerate data processing operations. For instance, cuDF accelerates pandas with zero code changes and brings greatly improved performance [2].  This is particularly useful when working with large numeric datasets.

3. Use machine learning for further analysis
The structured data can be utilised to implement machine learning algorithms for customer segmentation. Machine learning methodologies are a great tool for analyzing customer data and finding insights and patterns. Artificially intelligent models are powerful tools for decision-makers. They can precisely identify customer segments, which is much harder to do manually or with conventional analytical methods [3]. For instance, K-Means is efficient machine learning when it comes to solving data cluster problems.

By adopting these improvements, the project has the potential to evolve into a robust, scalable and intelligent data pipeline capable of supporting practical, data-driven decisions in the e-commerce landscape.

### References
[1]  Captcha Solver: reCAPTCHA solver and captcha solving service. Bypass captchas using the best auto captcha solver online API - 2Captcha. (2025). 2captcha.com. [Link](https://2captcha.com/)

‌[2] Open GPU Data Science. (n.d.). RAPIDS. [Link](https://rapids.ai/)

‌[3] Kumar, D. (2021, June 18). Implementing Customer Segmentation Using Machine Learning [Beginners Guide]. Neptune.ai. [Link](https://neptune.ai/blog/customer-segmentation-using-machine-learning)

### Appendices
### Sample code snippets
### Screenshots of output
### Links to full code repo or dataset
1. **Pandas:**
   - [Part 1](Codes/P1_PANDAS.ipynb) [Here to Colab](https://colab.research.google.com/drive/1xi-2SBSYWeEue9q_BF58WCiihWX9j6nN?usp=sharing)
   - [Part 2](Codes/P2_PANDAS.ipynb) [Here to Colab](https://colab.research.google.com/drive/1_StmE7ovcoBiV6SbCMLnO9KXCIxy2tR8?usp=sharing)

2. **Polars:**
   - [Part 1](Codes/P1_POLARS.ipynb) [Here to Colab](https://colab.research.google.com/drive/1Mo98HWNSUhlKcTMXERXbh2yYHhQ4BhvP?usp=sharing)
   - [Part 2](Codes/P2_POLARS.ipynb) [Here to Colab](https://colab.research.google.com/drive/1MjQbbpOWY6xCiv9GxZ842zNhea_vK2YT?usp=sharing)

3. **PySpark:**
   - [Part 1](Codes/P1_PYSPARK.ipynb) [Here to Colab](https://colab.research.google.com/drive/1KUD0RVBLRetTi0Wer8ButoaDxbkJjIcR?usp=sharing)
   - [Part 2](Codes/P1_PYSPARK.ipynb) [Here to Colab](https://colab.research.google.com/drive/1zFGwWiYsAkjxCqtm6u2Y1qsc5w_N72WL?usp=sharing)

4. **Dataset**
   - [Raw Dataset](https://drive.google.com/file/d/1LvokKS7OMZyWrZxFSy82rm7E0IJOgSAn/view?usp=sharing)
   - [Cleaned Dataset](https://drive.google.com/file/d/1d6JlsQBuqvSLAUfd-pEv9-NKANgPHwK-/view?usp=sharing)



