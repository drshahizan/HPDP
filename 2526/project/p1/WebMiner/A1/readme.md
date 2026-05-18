<h1 align="center"> 
  Group WebMiner - Web Scraping Carlist using BeautifulSoup
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD AFIQ DANISH BIN MOHD HAZNI</td>
    <td>A23CS0118</td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD SYAHMI FARIS BIN RUSLI</td>
    <td>A23CS0138</td>
  </tr>
  <tr>
    <td width=80%>NG YU HIN</td>
    <td>A23CS0148</td>
  </tr>
</table>
<br>
<div align='center'>
<img src='https://www.jeveuxetredatascientist.fr/wp-content/uploads/2022/06/BeautifulSoup.jpg' height=200 width=300 alt='beautiful soup'>
</div>
<br>
<p>
  Beautiful Soup is a Python library that is used for web scraping. It allows you to parse HTML or XML documents into a readable, tree-like format, and then extract data from the tree based on its structure. With Beautiful Soup, you can easily navigate through the document, search for specific tags, and extract the text or attributes of those tags. It is often used in combination with other libraries, such as requests or Playwright, to programmatically access web pages and extract data from them. The website that we will be using is https://www.motortrader.com.my/.

  This website is a premier automotive marketplace in Malaysia. It provides a comprehensive platform for buying and selling vehicles, featuring extensive catalogs for used, new, and reconditioned cars. The website includes detailed information about each vehicle listing, such as pricing, mileage, vehicle specifications, and seller locations. Additionally, the website provides automotive news, car reviews, and resources for buyers and dealerships. The platform is operated by Motor Trader, one of the leading automotive classifieds networks in the Malaysian market.  

  We plan to obtain data from the website by extracting its vehicle listings, specifically targeting the core details of the cars available for sale. By analyzing the website's underlying code, we will locate the individual car listing elements and access them by targeting their specific HTML tags and CSS classes (such as those containing the price, mileage, and location data). We will then utilize the pandas library alongside the Beautiful Soup package to extract and structure the parsed information from the HTML format. Finally, we will compile and clean the obtained data, converting it into a CSV file for high-performance analysis. In summary, we will efficiently retrieve large-scale automotive records from the website using these data extraction tools.
</p>


### 📅 **Timeline & Checklist**

| Week | Task | Responsible Member(s) | Status ✅ |
|------|------|------------------------|:-----------:|
| Week 1 | Form a diverse group (4 members) | All | ☐ |
| Week 1 | Choose a Malaysian website & get approval | Group Leader | ☐ |
| Week 1 | Identify target data fields (≥100,000 records) | Data Analyst | ☐ |
| Week 1 | Design system architecture (crawler + pipeline) | Architect | ☐ |
| Week 2 | Develop and test web crawler (initial batch) | Coder | ☐ |
| Week 2 | Begin collecting real data (progressive storage) | All | ☐ |
| Week 3 | Process and clean dataset (remove duplicates, standardize) | Data Analyst | ☐ |
| Week 3 | Apply optimization (threading, Spark, Dask, etc.) | HPC Specialist | ☐ |
| Week 3 | Benchmark performance (before vs after) | Evaluator | ☐ |
| Week 4 | Compile results, charts, and graphs | Documentation Lead | ☐ |
| Week 4 | Write final report | All (shared) | ☐ |
| Week 4 | Submit report to Turnitin (by 16 May) | Group Leader | ☐ |
| Week 4 | Submit code, dataset, and slides | All | ☐ |
| Week 4 | Present final project (10 minutes) | All | ☐ |
