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
This system architecture illustrates the workflow of our web scraping and data preprocessing pipeline that extracts, cleans, and stores structured news data from the NewStraitsTimes(https://www.nst.com.my/news). This system follows a Data Flow Architecture Pattern where data flows through a linear sequence of processing stages of Input, Intermediate Processing and Output. The architecture consists of:
1. Web Pages <br/>
  The system begins with a crawl request for URLs under 4 categories i.e. nation,  politics,  crime-courts and government-public-policy. These URLs serve as the seed input to the crawler.
2. Web Crawler<br/>
We use BeautifulSoup and Playwright to build the crawler. There is URL seed, URL frontier to manage and maintain the list of URLs to be crawled. The HTML downloader is to fetch and download HTML pages from the URLs and the content parser is to parse the downloaded HTML to extract the target data field.
3. Raw Data Storage<br/>
The content which has been parsed is saved as raw data in a CSV file to be processed afterward.
4. Big Data Processing<br/>
The content which has been parsed is saved as raw data in a CSV file to be processed afterward.
5. Optimization & Performance Evaluation<br/>
This project uses Pandas as a benchmarking library and optimization libraries which are Polars and Modin to evaluate the efficiency of data processing in large-scale settings.
6. Data Storage<br/>
The cleaned and processed data is saved in a structured CSV format. 

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
