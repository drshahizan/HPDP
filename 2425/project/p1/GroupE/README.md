<h1 align="center"> 
  Group E 
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>TIEW CHUAN RONG</td>
    <td>A22EC0112</td>
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
![web crawler diagram](https://github.com/user-attachments/assets/314304d8-271e-472f-9926-29e3a289f493)

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

### Ethical Considerations
The web scraper was developed with adherence to the ethical guidelines to ensure responsible data collection was done:

- **Respect site rules:** Only publicly accessible content was accessed. This is to ensure that the scraping did not violate the website’s terms of service (TOS).
- **Human-like interaction:** Rate-limiting and random delays implementation mimics human browsing patterns which reduces the risk of server overload.
- **Non-commercial use:** The data collected will only be used for academic and research purposes. No redistribution of the scraped content is intended.

## Data Processing
### 4.1 Cleaning methods
a. Handle Duplicate Data
Some of the news might have more than one tag, hence we might scrap the same news under different categories. To solve this, any duplicate rows from the dataset are removed to avoid redundant data.
`df_cleaned = rd.drop_duplicates()`

b. Handle Missing Data
Some rows may have missing values in the key column (Teaser). Removed using dropna() to maintain data quality.
`df_cleaned = df_cleaned.dropna()`

### 4.2 Data structure (CSV/JSON/database)
The initial data is read from a Microsoft Excel file.
`rd = pd.read_excel("NST_News_Articles.xlsx")`
The final data is exported in CSV format.
`sorted_df.to_csv('finalData.csv',index=False)`

### 4.3 Transformation and formatting
In the place column, it has city names.
- Converts all text to uppercase. Standardize the format so “kuala lumpur” and “KUALA LUMPUR” are treated the same.
- Splits the value on the ; to keep only the first part.
- Removes any non-alphabetic characters to ensure the values only contain clean, readable city names. <br/>
`df_cleaned['Place'] = df_cleaned['Place'].str.upper()`
`df_cleaned['Place'] = df_cleaned['Place'].str.split(',').str[0]`
`df_cleaned['Place'] = df_cleaned['Place'].str.replace(r'[^a-zA-Z\s]+','',regex=True)`

## 5.0 Optimization Techniques
### 5.1 Methods used: multithreading, multiprocessing, Spark, etc
In this project, the Pandas library is used for traditional data processing without any optimization. Pandas is a widely used tool for data processing in Python. On the other hand, Polars and Modin are modern libraries that are selected to optimize the process of data processing. Both these libraries have the capabilities to use multithreading and multiprocessing to distribute tasks into smaller tasks and run them in multiple CPU cores. In this part, we would like to compare these three libraries on how they perform optimization techniques in handling large datasets. Below are the introductions of the three libraries that we used to process data:

| Library  | Explanation |
| ------------- | ------------- |
| ![pandas](https://github.com/user-attachments/assets/a03befb7-f366-49ec-9682-3163ffcd9aa8) | - a traditional, simple and easy language that is used by many people to handle data in python. <br/> - Good for small and medium sized dataset  <br/> - does not support parallel processing, it uses only one CPU core to process that data.  <br/> - runs in a single process and on a single thread only.|
