# 📘 Project 1 
## Optimizing High Performance Data Processing for Large Scale Web Crawlers

<table border="solid" align="center">
  <tr>
    <th>Role</th>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Group Leader & Data Engineer</td>
    <td>Muhammad Afiq Danial bin Rozaidie</td>
    <td>A23CS0117</td>
  </tr>
  <tr>
    <td>HPC Specialist & Documentation Lead</td>
    <td>Ahmad Adib Zikri bin A.Mazlam</td>
    <td>A23CS0205</td>
  </tr>
</table>

<br>
<div align='center'>
<img src='https://www.jeveuxetredatascientist.fr/wp-content/uploads/2022/06/BeautifulSoup.jpg' height=200 width=300 alt='beautiful soup'>
</div>
<br>

# 📚 Web Scraping Overview Using BeautifulSoup (MPHOnline.com)

## 🌐 Introduction

Web scraping is an automated technique used to extract information from websites for analysis, research, or data collection purposes. In this project, web scraping was conducted using **BeautifulSoup**, a Python library commonly used for parsing HTML and extracting structured data from webpages. BeautifulSoup enables users to navigate webpage structures, identify HTML tags, and retrieve specific information efficiently.

For this project, the selected website is [**MPHOnline.com**](https://mphonline.com/), a Malaysian online bookstore that provides books, stationery, gifts, and educational materials through its e-commerce platform. The website serves as a rich source of publicly available product information, making it suitable for web scraping and dataset creation.

---

## 🎯 Objectives of the Web Scraping Project

The main objective of this web scraping activity is to collect structured data from MPHOnline to support analysis and insight generation. Specifically, the scraping process aims to:

### 1. 📖 Extract Product Information
Collect important product details such as:

- Product title  
- Author name  
- Vendor 
- Created/Updated/Published Date  
- Tags  
- Book Description
- Source URL  

### 2. 📊 Analyze Pricing and Product Trends
Identify patterns in:

- Popular or bestselling categories
- Current trends that on sell  

This helps provide insights into consumer preferences and pricing strategies.

### 3. 🗂️ Create a Structured Dataset
Transform webpage data into a structured dataset (e.g., CSV format) for:

- Data analysis  
- Data visualization  

### 4. ⚡ Improve Data Collection Efficiency
Automate the collection of information from multiple webpages, reducing the time and effort required for manual data gathering.

BeautifulSoup is suitable for this task because MPHOnline displays product information in structured HTML elements, allowing data such as titles, author, and tags/categories to be extracted systematically.

---

## 🗃️ Dataset Identification

The dataset collected from MPHOnline consists of **semi-structured web data**, which originates from HTML webpages and is transformed into a structured format after scraping.

### Expected Dataset Attributes

| 🏷️ Attribute | 📝 Description |
| :--- | :--- |
| **id** | A unique numerical identifier for the item |
| **title** | The full title of the book or product |
| **handle** | A unique, URL-friendly string identifier (slug) representing the title, typically used in website URLs. |
| **vendor** | The publisher or distributor responsible for the product |
| **author** | The name of the author who wrote the book, formatted as Last Name, First Name. |
| **created_at** | The timestamp indicating exactly when the product record was originally created. |
| **updated_at** | The timestamp indicating when the product record was last modified or updated. |
| **published_at**| The timestamp indicating when the product was officially published or made live. |
| **tags** | Classification keywords or labels used to categorize the product (e.g., "Class Code"). |
| **description** | A brief text summary, synopsis, or promotional blurb describing the book's content. |
| **source_url** | The direct URL or API endpoint where the original JSON data for the product is hosted. |

### 📌 Type of Dataset
The dataset is categorized as **semi-structured data** because website content is stored in HTML format and must be parsed before being converted into structured forms such as:

- CSV files  
- Excel spreadsheets  
- Databases  

Since MPHOnline includes multiple categories such as fiction, non-fiction, educational books, children's books, and stationery, the dataset can support various analytical purposes such as:

- 🛒 Consumer preference studies  
- 📚 Category popularity analysis  

---

## ⚖️ Ethical Crawling Considerations

Ethical web scraping is important to ensure that the website is accessed responsibly and without causing disruption. Several ethical considerations should be followed when scraping data from MPHOnline.

### 1. 📜 Respect Website Policies
Before scraping, the website's **Terms of Service** and `robots.txt` file should be reviewed to determine:

- Whether web scraping is allowed  
- Which pages may be restricted from automated access  

### 2. ⏳ Avoid Excessive Requests
Sending too many requests within a short time may overload the website server.

To avoid this:

- Introduce delays between requests using `time.sleep()`  
- Limit scraping frequency  
- Avoid aggressive crawling behavior  

### 3. 🔓 Collect Publicly Available Data Only
Only publicly accessible information should be collected. Sensitive or private information such as customer accounts, payment data, or personal information must **never** be accessed.

### 4. 🎓 Use Data Responsibly
Since this project is intended for **academic and research purposes**, the collected data should be used responsibly and not redistributed for unauthorized commercial purposes.

### 5. 🧩 Handle Dynamic Content Properly
Some website content may be loaded dynamically through JavaScript. Scraping should still be performed responsibly without generating unnecessary server load or bypassing website protections.

---

## ✅ Conclusion

In conclusion, web scraping using **BeautifulSoup** provides an efficient way to collect structured data from **MPHOnline.com** for analytical purposes. The project focuses on extracting product-related information such as book titles, prices, categories, and availability to build a usable dataset. By following ethical crawling practices such as respecting website policies, limiting request frequency, and collecting only public data, the scraping process can be conducted responsibly and effectively. 🚀
