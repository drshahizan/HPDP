<h1 align="center"> 
  Group E - News Analysis
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>DANIAL HARRIZ BIN MOHD ASINEH @MOHD ASNEH</td>
    <td>A22EC0152</td>
  </tr>
  <tr>
    <td width=80%>CHAI YU TONG</td>
    <td>A22EC0145</td>
  </tr>
  <tr>
    <td width=80%>KOH SU XUAN</td>
    <td>A22EC0060</td>
  </tr>
  <tr>
    <td width=80%>TIEW CHUAN RONG</td>
    <td>A22EC0112</td>
  </tr>
</table>


## 1.0 Introduction
### 1.1 Background of the Project
Online news platforms have become an important source of information on a wide range of topics which includes politics, economics, social issues, and also events that are happening around the world. With the increasing availability of public data on news websites, web scraping is a powerful tool to automate the collection of large volumes of content for different purposes such as sentiment analysis, trend detection, and content archiving.

This project uses web scraping techniques to extract news articles from an established Malaysian online news portal by leveraging a high-performance scraping pipeline. The end goal is to gather relevant news data for further processing and performance analysis.

### 1.2 Objectives
- To develop a web scraper that is capable of collecting up to 100,000 news article records from a target website.
- Extracting specific data elements such as article title, URL, teaser, and category.
- To store the extracted data in a structured CSV format that will be used for tasks such as processing and performance analysis.
- Clean the data collected from web scrape.
- Compare the three libraries (Pandas, Polars and Modin) for data processing.
- Optimize data processing methods to get better performance.

### 1.3 Target Website and Data
The website that is targeted for this web scraping project is the New Straits Times (NST) under the “News” section. It is accessible via https://www.nst.com.my/news/. This section displays updated news articles that are related to the national developments in Malaysia.

The specific data fields that will be extracted from each article are: 
- **Title:** The headline/main title of the article.
- **URL:** The full web link/URL of the article.
- **Teaser:** A short description from the article content.
- **Category:** The label that describes the main topic area of the article.

## 2.0 System Design & Architecture
![web crawler diagram (1)](https://github.com/user-attachments/assets/43d99f04-c044-4df7-841d-8f5a918db6e1)

### 2.1 Description of architecture 
This system architecture illustrates the workflow of our web scraping and data preprocessing pipeline that extracts, cleans, and stores structured news data from the NewStraitsTimes(https://www.nst.com.my/news). This system follows a Data Flow Architecture Pattern where data flows through a linear sequence of processing stages of Input, Intermediate Processing and Output. The architecture consists of:<br/><br/>
**1. Web Pages** <br/>
  The system begins with a crawl request for URLs under 4 categories i.e. nation,  politics,  crime-courts and government-public-policy. These URLs serve as the seed input to the crawler.<br/><br/>
**2. Web Crawler**<br/>
We use BeautifulSoup and Playwright to build the crawler. There is URL seed, URL frontier to manage and maintain the list of URLs to be crawled. The HTML downloader is to fetch and download HTML pages from the URLs and the content parser is to parse the downloaded HTML to extract the target data field.<br/><br/>
**3. Raw Data Storage**<br/>
The content which has been parsed is saved as raw data in a CSV file to be processed afterward.<br/><br/>
**4. Big Data Processing**<br/>
The content which has been parsed is saved as raw data in a CSV file to be processed afterward.<br/><br/>
**5. Optimization & Performance Evaluation**<br/>
This project uses Pandas as a benchmarking library and optimization libraries which are Polars and Modin to evaluate the efficiency of data processing in large-scale settings.<br/><br/>
**6. Data Storage**<br/>
The cleaned and processed data is saved in a structured CSV format. <br/>

### 2.2 Tools and frameworks used 
* Beautiful Soup
* Playwright
* Asyncio
* Pandas
* Polars
* Modin

### 2.3 Roles of the team members

| Team Member  | Roles |
| ------------- | ------------- |
| DANIAL HARRIZ BIN MOHD ASINEH @MOHD ASNEH  | Group Leader, Coder  |
| TIEW CHUAN RONG  | Architect, Coder  |
| CHAI YU TONG  | Data Analyst, Documentation Lead, Coder  |
| KOH SU XUAN  | HPC Specialist, Evaluator, Coder  |

## 3.0 Data Collection
### 3.1 Crawling method (pagination, rate-limiting, async)
The collection of data was performed using a custom-built asynchronous web scraper that was developed using Playwright, which is a browser automation library. The scraper navigates through the pages of the NST News in each subcategory section, where each page lists 20 news articles.<br/>

The strategies employed to ensure efficient and robust data collection are: 
* **Pagination:** URLs were generated in the format of `https://www.nst.com.my/news/{subcategory}?page={page_number}`
* **Asynchronous Processing:** The scraper utilizes asynchronous processing with Playwright and asyncio, where up to 8 concurrent pages are run to handle multiple pages in parallel, improving efficiency.
* **Rate Limiting and Random Delays:** To reduce server load and mimic human behavior, random delays are set between requests. In addition, a retry mechanism was implemented to ensure robustness.

### 3.2 Number of records collected
The number of records collected was **110,642** across four distinct subcategories under the News section of the New Straits Times: 

* Crime & Courts
* Nation
* Government/Public Policy
* Politics

Each subcategory was crawled independently, where each of the members in our group was responsible for scraping one or two subcategories. The same data fields are scraped to ensure that the data collected are uniform and can be merged.

### 3.3 Ethical Considerations
The web scraper was developed with adherence to the ethical guidelines to ensure responsible data collection was done:

- **Respect site rules:** Only publicly accessible content was accessed. This is to ensure that the scraping did not violate the website’s terms of service (TOS).
- **Human-like interaction:** Rate-limiting and random delays implementation mimics human browsing patterns which reduces the risk of server overload.
- **Non-commercial use:** The data collected will only be used for academic and research purposes. No redistribution of the scraped content is intended.

## 4.0 Data Processing
### 4.1 Cleaning methods
a. Handle Duplicate Data
Some of the news might have more than one tag, hence we might scrap the same news under different categories. To solve this, any duplicate rows from the dataset are removed to avoid redundant data.
`df_cleaned = rd.drop_duplicates()`

b. Handle Missing Data
Some rows may have missing values in the key column (Teaser). Removed using dropna() to maintain data quality.
`df_cleaned = df_cleaned.dropna()`

### 4.2 Data structure (CSV/JSON/database)
The initial data is read from a Microsoft Excel file.<br/>
`rd = pd.read_excel("NST_News_Articles.xlsx")`<br/>
The final data is exported in CSV format.<br/>
`sorted_df.to_csv('finalData.csv',index=False)`

### 4.3 Transformation and formatting
In the place column, it has city names.
- Converts all text to uppercase. Standardize the format so “kuala lumpur” and “KUALA LUMPUR” are treated the same.
- Splits the value on the ; to keep only the first part.
- Removes any non-alphabetic characters to ensure the values only contain clean, readable city names. <br/>
`df_cleaned['Place'] = df_cleaned['Place'].str.upper()`<br/>
`df_cleaned['Place'] = df_cleaned['Place'].str.split(',').str[0]`<br/>
`df_cleaned['Place'] = df_cleaned['Place'].str.replace(r'[^a-zA-Z\s]+','',regex=True)`

## 5.0 Optimization Techniques
### 5.1 Methods used: multithreading, multiprocessing, Spark, etc
In this project, the Pandas library is used for traditional data processing without any optimization. Pandas is a widely used tool for data processing in Python. On the other hand, Polars and Modin are modern libraries that are selected to optimize the process of data processing. Both these libraries have the capabilities to use multithreading and multiprocessing to distribute tasks into smaller tasks and run them in multiple CPU cores. In this part, we would like to compare these three libraries on how they perform optimization techniques in handling large datasets. Below are the introductions of the three libraries that we used to process data:

| Library  | Explanation |
| ------------- | ------------- |
| ![pandas](https://github.com/user-attachments/assets/a03befb7-f366-49ec-9682-3163ffcd9aa8) | - a traditional, simple and easy language that is used by many people to handle data in python. <br/> - Good for small and medium sized dataset  <br/> - does not support parallel processing, it uses only one CPU core to process that data.  <br/> - runs in a single process and on a single thread only.|
| ![polars](https://github.com/user-attachments/assets/b32b54ef-63a5-4f4b-81dd-db2dbbfe31c1)| - Polars is a modern tool that is built with Rust.<br/>- Best for big data that needs optimization and performance.<br/> - Polars use parallel processing, it uses all CPU cores in the computer to process a lot of data at same time.<br/> - Polars uses multiprocessing and multithreading to split tasks and run them in parallel.|
| ![modin](https://github.com/user-attachments/assets/940ebb94-b9b5-446a-a599-348d1fd43f85) | - Modin can speed up workflows by scaling pandas.<br/>- Modin works well on larger datasets.<br/>- Modin uses parallel processing, it uses multiple CPU cores in the computer to handle the task.<br/>- Modin speeds up pandas work without rewriting the whole code.<br/>- Modin uses Ray or Dask, which break work into chunks and run them across the CPU core for multiprocessing.|

### 5.2 Code overview or pseudocode of techniques applied
#### 1. Import library
Import the Pandas, Polars, Modin libraries seperately with other libraries for monitoring the performance. <br/>
| Pandas | Polars | Modin |
|--------------|--------------|--------------|
| ![Screenshot 2025-05-14 212428](https://github.com/user-attachments/assets/1e09a188-1b58-4a89-8ab2-4bcbb99f26a3)|![Screenshot 2025-05-15 190735](https://github.com/user-attachments/assets/bbee7862-e3b1-4529-b5fd-e74b50ce7284)|![Screenshot 2025-05-15 190756](https://github.com/user-attachments/assets/771ad78f-6e09-4331-bd85-42f4405030d7)|

#### 2. Load data
Load the raw dataset from the NST_News_Articles.csv file using pd.read_excel.<br/>
| Pandas | Polars | Modin |
|--------|--------|--------|
| ![Screenshot 2025-05-14 212556](https://github.com/user-attachments/assets/4d93d061-f382-4bf8-a2d7-49dfa1ccbd84) | ![Screenshot 2025-05-15 191213](https://github.com/user-attachments/assets/ef186eda-13d8-4780-883a-e2ff758c13ef) | ![Screenshot 2025-05-15 191231](https://github.com/user-attachments/assets/f9ed8bb1-330a-4cc0-8bf7-e662ebe2727e) |

#### 3. Remove duplicated data
Remove duplicate rows from the table
| Pandas | Polars | Modin |
|--------|--------|--------|
|![image](https://github.com/user-attachments/assets/90eafd5a-655e-4bdd-8eb5-7998841ac569)| ![image](https://github.com/user-attachments/assets/25d18edb-21d4-46ee-9f61-8fdfa6b43e97)| ![image](https://github.com/user-attachments/assets/01ebf7fa-84a7-4486-b55e-2fbd06758424)|

#### 4. Remove missing data
 Drop rows with missing values in the columns
| Pandas | Polars | Modin |
|--------|--------|--------|
|![image](https://github.com/user-attachments/assets/f3300cbe-c16d-4bad-810e-2a522b78a5b5)| ![image](https://github.com/user-attachments/assets/f2b5c52d-3961-429a-9600-3e7cc7a724a8)| ![image](https://github.com/user-attachments/assets/31685590-2aed-419c-926a-931b8c5fe719)|

#### 5. Clean the teaser column
Clean the teaser column by removing unwanted characters
| Pandas | Polars | Modin |
|--------|--------|--------|
|![image](https://github.com/user-attachments/assets/536ba9ae-5bcf-4919-9d3e-a2871a4e3eeb)|![image](https://github.com/user-attachments/assets/c4f08a16-5254-4665-867b-94f343c45ac3)| ![image](https://github.com/user-attachments/assets/b104f14e-567d-46cb-b875-1513833fc3e7)|

#### 6. Splitting the place from the teaser column
Get the place from the teaser column
| Pandas | Polars | Modin |
|--------|--------|--------|
|![image](https://github.com/user-attachments/assets/22dffeed-98d1-45d6-8b73-7623c5679da9)| ![image](https://github.com/user-attachments/assets/c4c80a19-377e-4cf9-a11a-5df6f8e4d3c8)| ![image](https://github.com/user-attachments/assets/689fef7d-1528-4b37-a823-17319e54858e)|

#### 7. Standardize place names
Standardize the place names, convert them to uppercase, and remove any country names or other non-relevant information
| Pandas | Polars | Modin |
|--------|--------|--------|
|![image](https://github.com/user-attachments/assets/1ea178c2-dd32-4388-9a0e-5eff202f781b)|![image](https://github.com/user-attachments/assets/5d752ae3-5d26-41aa-9c1d-6265b234eb9f) ![image](https://github.com/user-attachments/assets/9f1902d1-02b9-4458-a760-14e2e1e68c8e)| ![image](https://github.com/user-attachments/assets/3decb654-6a5d-4d96-bdac-2d3c8b44175a) ![image](https://github.com/user-attachments/assets/cd1ed6e5-d373-4601-a098-9acbe96ec9bb)|

#### 8. Extract date from URL
Extract the date in YYYY/MM format from the URL and add it as a separate column in the dataset
| Pandas | Polars | Modin |
|--------|--------|--------|
|![image](https://github.com/user-attachments/assets/58878f7f-7905-4be3-bd2e-cdb7f4e02d27)|![image](https://github.com/user-attachments/assets/e9b38608-52e4-4162-9661-f51950c9c650)|![image](https://github.com/user-attachments/assets/044cbf41-f628-4732-a398-992824bc3b57)|

## 6.0 Performance Evaluagtion
### 6.1 Before vs After Optimization
Data processing was first performed using Pandas, which operates in a single-threaded manner. Although Pandas offers a user-friendly API, its lack of parallelism leads to performance bottlenecks with large datasets. Tasks such as data loading, duplicate removal, missing value handling, string cleaning, column splitting, place name standardization and date extraction were used to establish baseline metrics. The same tasks were re-executed using Polars and Modin. Polars offers high performance through efficient memory use and native multi-core parallelism while Modin speeds up Pandas workflows by distributing tasks across CPU cores. Performance improvements were measured by comparing how each library processed the same large-scale dataset with the average calculated from three measurements.

### 6.2 Processing time, CPU usage, memory usage and throughput
#### 1. Load data
| Performance Metrics             | Pandas    | Polars    | Modin     |
|---------------------------------|-----------|-----------|-----------|
| Total Processing Time (seconds) | 1.1660    | 1.0009    | 1.0010    |
| Initial CPU Usage (%)           | 38.20     | 58.10     | 57.13     |
| Final CPU Usage (%)             | 23.07     | 46.27     | 58.20     |
| Memory Usage (%)                | 21.37     | 21.80     | 21.97     |
| Throughput (records/sec)        | 94922.15  | 110547.61 | 110531.92 |

#### 2. Handle Duplicated Data
| Performance Metrics             | Pandas    | Polars    | Modin    |
|---------------------------------|-----------|-----------|----------|
| Total Processing Time (seconds) | 1.1372    | 1.0006    | 1.0733   |
| Initial CPU Usage (%)           | 10.20     | 12.33     | 74.47    |
| Final CPU Usage (%)             | 5.17      | 5.37      | 5.50     |
| Memory Usage (%)                | 21.33     | 21.77     | 22.03    |
| Throughput (records/sec)        | 93631.39  | 106407.09 | 99201.30 |

#### 3. Handle Missing Data
| Performance Metrics             | Pandas    | Polars    | Modin    |
|---------------------------------|-----------|-----------|----------|
| Total Processing Time (seconds) | 1.1954    | 1.0005    | 1.0723   |
| Initial CPU Usage (%)           | 6.90      | 4.87      | 25.70    |
| Final CPU Usage (%)             | 4.90      | 6.20      | 4.70     |
| Memory Usage (%)                | 21.33     | 21.77     | 22.00    |
| Throughput (records/sec)        | 88167.97  | 105335.91 | 98292.13 |

#### 4. Clean the Teaser Column
| Performance Metrics             | Pandas    | Polars    | Modin     |
|---------------------------------|-----------|-----------|-----------|
| Total Processing Time (seconds) | 1.1826    | 1.0006    | 1.0007    |
| Initial CPU Usage (%)           | 5.07      | 4.70      | 47.97     |
| Final CPU Usage (%)             | 4.87      | 5.20      | 4.40      |
| Memory Usage (%)                | 21.33     | 21.77     | 22.03     |
| Throughput (records/sec)        | 89118.82  | 105331.54 | 105321.33 |

| Performance Metrics             | Pandas    | Polars    | Modin    |
|---------------------------------|-----------|-----------|----------|
| Total Processing Time (seconds) | 1.1944    | 1.0006    | 1.0445   |
| Initial CPU Usage (%)           | 10.70     | 5.23      | 46.37    |
| Final CPU Usage (%)             | 29.37     | 4.53      | 5.03     |
| Memory Usage (%)                | 21.30     | 21.77     | 21.97    |
| Throughput (records/sec)        | 86350.94  | 103003.67 | 98679.35 |

#### 5. Splitting the place from 'Teaser' column
| Performance Metrics             | Pandas    | Polars    | Modin     |
|---------------------------------|-----------|-----------|-----------|
| Total Processing Time (seconds) | 1.2424    | 1.0005    | 1.0007    |
| Initial CPU Usage (%)           | 41.60     | 5.53      | 10.30     |
| Final CPU Usage (%)             | 31.47     | 28.30     | 38.43     |
| Memory Usage (%)                | 21.37     | 21.77     | 21.97     |
| Throughput (records/sec)        | 83065.61  | 103011.94 | 102997.50 |

#### 6. Extract and Standardize Place Names
| Performance Metrics             | Pandas    | Polars    | Modin   |
|---------------------------------|-----------|-----------|---------|
| Total Processing Time (seconds) | 1.1889    | 1.0007    | 1.0010  |
| Initial CPU Usage (%)           | 5.03      | 39.80     | 100.00  |
| Final CPU Usage (%)             | 5.03      | 8.70      | 100.00  |
| Memory Usage (%)                | 21.33     | 21.83     | 21.97   |
| Throughput (records/sec)        | 86694.45  | 103000.17 | 102964.66 |

| Performance Metrics             | Pandas    | Polars    | Modin    |
|---------------------------------|-----------|-----------|----------|
| Total Processing Time (seconds) | 1.1886    | 1.0006    | 1.0609   |
| Initial CPU Usage (%)           | 4.93      | 5.57      | 38.77    |
| Final CPU Usage (%)             | 5.20      | 4.33      | 28.70    |
| Memory Usage (%)                | 21.33     | 21.80     | 21.37    |
| Throughput (records/sec)        | 86463.74  | 102698.85 | 96861.25 |

| Performance Metrics             | Pandas    | Polars    | Modin    |
|---------------------------------|-----------|-----------|----------|
| Total Processing Time (seconds) | 1.1917    | 1.0006    | 1.1003   |
| Initial CPU Usage (%)           | 6.07      | 5.70      | 76.27    |
| Final CPU Usage (%)             | 6.00      | 5.50      | 55.57    |
| Memory Usage (%)                | 21.33     | 21.80     | 21.60    |
| Throughput (records/sec)        | 86237.43  | 102698.47 | 93389.56 |

#### 7. Extract Date from URL
| Performance Metrics             | Pandas    | Polars    | Modin     |
|---------------------------------|-----------|-----------|-----------|
| Total Processing Time (seconds) | 1.2322    | 1.0008    | 1.0007    |
| Initial CPU Usage (%)           | 22.50     | 6.43      | 54.40     |
| Final CPU Usage (%)             | 41.43     | 4.67      | 5.90      |
| Memory Usage (%)                | 21.40     | 21.80     | 21.30     |
| Throughput (records/sec)        | 83463.20  | 102673.35 | 102680.96 |

### 6.3 Charts and Graphs
To visually summarize the performance differences between Pandas, Polars and Modin, a series of bar charts were generated based on the aggregated performance metrics measured during the data processing.
<br/>
#### 1. Comparison of Total Processing Time
<p align="center">
  <img src="https://github.com/user-attachments/assets/2dbe905f-a43a-4906-b8f9-fd1f5f2a29b2" width="600" height="450">
</p>
The chart clearly indicates that Polars completed the entire set of data processing tasks in the shortest time followed by Modin and Pandas. This highlights the efficiency gains from the parallel processing capabilities inherent in Polars and utilized by Modin's backend, compared to the single-threaded execution model of Pandas.
<br/>

#### 2. Comparison of Average Final CPU Usage
<p align="center">
  <img src="https://github.com/user-attachments/assets/f8034c77-cdf9-4c01-85e4-4d6543b49f31" width="600" height="450">
</p>
The chart shows Modin achieving the highest average final CPU usage. This suggests that Modin effectively utilized multiple CPU cores for its parallel tasks. Meanwhile, Pandas has the next highest average final CPU usage. Since it is single-threaded in nature, this suggests the active core was likely working intensively during processing, even though the overall system usage stayed low. Although Polars is the fastest library, it showed the lowest average final CPU usage among the three libraries. This indicates that Polars' operations are not only parallel but also highly optimized in which it achieves significant speedups without needing as many CPU resources as Modin.
<br/>

#### 3. Comparison of Average Memory Usage
<p align="center">
  <img src="https://github.com/user-attachments/assets/d4459581-a580-441b-bea9-5b8c8d5aecb6" width="600" height="450">
</p>
The chart shows Pandas has the lowest average memory usage. Polars was next, followed by Modin, which had the highest average memory usage. While Polars' efficiency is likely due to its Rust backend and Arrow-based memory layout, the aggregated average here is very close to Pandas. Even though Pandas does not use parallel processing, it has a mature and generally efficient memory model for data processing. The slightly higher figures for Polars and Modin in this averaged context could be due to the memory overhead of their respective backends, management of data partitions across cores and parallel execution. All three libraries used memory within a relatively tight range when processing the dataset.
<br/>

#### 4. Comparison of Average Throughput
<p align="center">
  <img src="https://github.com/user-attachments/assets/b9aa825e-75b6-44a6-a674-0d1e30de39d7" width="600" height="450">
</p> 
The chart shows Polars has the highest average throughput. Modin followed with a strong throughput while Pandas had the lowest. Throughput is directly related to processing speed. Thus, libraries that process data faster will naturally have a higher throughput. Both Polars and Modin significantly outperformed Pandas in terms of the number of records processed per second.

## 7.0 Challenges & Limitations
During this project, several challenges were encountered and certain limitations of the developed solution were identified: <br/>

1. Initial Target Website Infeasibility: Originally, the project aimed to scrape the Lazada website due to its extensive and valuable data. However, we encountered significant difficulties in successfully scraping Lazada. This challenge, along with the fact that another group had also chosen Lazada, led to a strategic decision to switch our target to the New Straits Times (NST) website. <br/>

2. Tooling and Environment Constraints: We initially considered using Scrapy, a powerful web scraping framework. However, we found that Scrapy was not fully compatible with Google Colab, our preferred development environment, because processing a large dataset (aiming for over 100,000 records) on local systems will have a potential resource constraint. Therefore, we aimed to overcome it by using a cloud-based environment. As a result, we opted to use Beautiful Soup (in conjunction with Playwright and Asyncio) for scraping. <br/>

3. Anti-Scraping Measures: Websites often employ anti-scraping measures to protect their content. While our implemented strategies such as rate-limiting and human-like interaction patterns aimed to navigate these on the NST website, such defenses are indeed a challenge in web scraping. They can limit the speed of data collection and require ongoing adjustments if the target website modifies its protective mechanisms. <br/>

4. Data Quality and Inconsistency: The NST website, particularly the older articles from 2014 to 2019, has data quality issues. These included human typographical errors, non-standardized data formats and inconsistencies in how information was presented such as the variations in place names like "Johor Baharu". This data noisiness required more intensive effort during the data cleaning phase and represents a limitation in the raw data's initial quality.

## 8.0 Conclusion & Future Work
### 8.1 Summary of Findings
To conclude, in this project we had successfully designed and built a web scraper by using tools like Playwright, Beautiful Soup and Asyncio to collect more than 110,000 news article data from pages of the New Straits Times website. For web scraping, Playwright is used to automate browsers, navigate to web pages and click buttons to get the HTML pages. Beautiful Soup is used to parse the HTML page and extract the data like title, teaser, URL and category by searching the HTML page. Asyncio is used to improve the process of web scraping by handling many tasks concurrently. <br/>

After collecting the data, we clean and process the data to make it more organized, as the data collected from web scraping is raw and not organized. We had used 3 libraries and tools, which are Pandas, Polars and Modin in Python, to process the data. We then compared these 3 different libraries and tools in time, memory, CPU usage and throughput. We use Pandas as our traditional library for data processing and Polars and Modin libraries to provide optimization methods like multithreading and multiprocessing to improve the speed and performance of data processing. As for Pandas, it works slower with large datasets as it processes data in a single thread. For Polars, it is the fastest way as it uses multithreading to handle many tasks at a time. Lastly, Modin also improved performance by using multiprocessing to split tasks across multiple CPU cores. As a result, Polars and Modin are better choices for handling large data compared to pandas. This is because Polars and Modin provide optimization methods that can improve the performance of data processing. So, using the correct tools is important as the optimized tools help to improve the performance and reduce the time to process big data.

### 8.2 What could be improved
In this project, we learned many skills in web scraping and data processing and faced many problems and challenges while handling the data. The challenges that we faced were website restriction, inconsistent data and technical issues with the tools that we used in Google Colab. There are still many things that can be improved in this project. The improvements are: <br/>

* **Save the collected and cleaned data into a database**
Now we save the data into CSV files for simple storage.  But it would be better to store the data in databases like PostgreSQL, MongoDB and NoSQL. This is because databases can handle large data efficiently and with better organization. <br/>

* **Use distributed computing for web scraping**
This is to run multiple scrapers at the same time across many different machines. For example, we can use the Scrapy cluster to run many tasks in parallel. <br/>

* **Improve fault tolerance in web scraping**
If the code suddenly crashes or stops running in the middle due to some external factor, all the progress might be lost. So, saving progress frequently is important for scraping for a long time. <br/>

* **Process data in chunks**
Loading large CSV files at one time could be heavy. So, processing the data in chunks by setting the chunk size could improve the performance of data processing.

## References
- IBM. (2024, July 9). HPC. Ibm.com. https://www.ibm.com/think/topics/hpc
- NetApp. (n.d.). What Is High-Performance Computing (HPC)? How It Works | NetApp. Www.netapp.com. https://www.netapp.com/data-storage/high-performance-computing/what-is-hpc/
- Perez, M. (2019, August 6). What is Web Scraping and What is it Used For? | ParseHub. ParseHub Blog. https://www.parsehub.com/blog/what-is-web-scraping/
- Wikipedia Contributors. (2019, October 4). Web scraping. Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Web_scraping

## Appendices
#### Sample Code Snippets

### 📂 Web Scraper Source Code

| Figure | Description | Preview |
|--------|-------------|---------|
| **Figure 7** | Web Scraper Source Code – Part 1 | ![Figure 7](https://github.com/user-attachments/assets/73c86009-3978-4d3e-bf04-9dd1b5db0ac1) |
| **Figure 8** | Web Scraper Source Code – Part 2 | ![Figure 8](https://github.com/user-attachments/assets/b2695688-96a2-4e9a-84df-f2e13c9b10b6) |

---

### 📊 Performance Evaluation Charts

| Figure | Description | Preview |
|--------|-------------|---------|
| **Figure 9** | Performance Evaluation – Chart 1 | ![Chart 1](https://github.com/user-attachments/assets/79cf5340-8187-4b7c-80b5-9ad978be8dc9) |
| **Figure 10** | Performance Evaluation – Chart 2 | ![Chart 2](https://github.com/user-attachments/assets/3dbb508a-efff-4c72-b4de-9031f4f57bd9) |

---

### 🖥️ Output Screenshots

| Figure | Description | Preview |
|--------|-------------|---------|
| **Figure 11** | Web Scraper Output Screenshot | ![Output](https://github.com/user-attachments/assets/07212559-c02f-4665-9202-f356c5aa89cb) |
| **Figure 12** | Performance Evaluation – Chart 1 | ![Chart](https://github.com/user-attachments/assets/35175eb9-6eb6-4069-b583-e66a0a586ded) |
| **Figure 13** | Performance Evaluation – Chart 2 | ![Chart](https://github.com/user-attachments/assets/c2826b01-7b72-4a44-afd6-fe18b181f2ad) |
| **Figure 14** | Performance Evaluation – Chart 3 | ![Chart](https://github.com/user-attachments/assets/951a2aa0-bf18-4e61-99ea-ad341e400c23) |




