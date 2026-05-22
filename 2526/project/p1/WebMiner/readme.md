<h1 align="center"> 
  Group WebMiner - Web Scraping Carlist using Playwright
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
<img src='https://playwright.dev/img/playwright-logo.svg' height=150 width=150 alt='Playwright Logo'>
</div>
<br>
<p>
  Playwright is a powerful Python library designed for automated browser control and web scraping. Unlike traditional parsing libraries, Playwright launches headless or headed browsers (Chromium, Firefox, and WebKit) to interact with web pages exactly like a human user. This allows it to easily handle modern, JavaScript-heavy websites, bypass basic bot detection, manage cookies, and wait for dynamic content to render completely. Using Playwright's robust locator and selector API, we can efficiently target HTML elements, extract text, and capture attributes from complex web structures. The website targeted for this project is https://www.carlist.my/.

  This website is a premier automotive marketplace in Malaysia. It provides a comprehensive platform for buying and selling vehicles, featuring extensive catalogs for used, new, and reconditioned cars. The website includes detailed information about each vehicle listing, such as pricing, mileage, vehicle specifications, and seller locations. Additionally, the website provides automotive news, car reviews, and resources for buyers and dealerships. The platform is operated by iCar Asia, one of the leading automotive classifieds networks in the Malaysian market.  

  We plan to obtain data from the website by extracting its vehicle listings, specifically targeting the core details of the cars available for sale. By analyzing the website's underlying DOM structure, we will locate the individual car listing elements and extract data by targeting their specific CSS selectors and XPath expressions (such as those containing the price, mileage, and location data). We will utilize Playwright to handle the pagination and dynamic content loading, feeding the scraped records directly into the pandas library for structured data manipulation. Finally, we will compile and clean the obtained data, converting it into a CSV file for high-performance analysis. In summary, we will efficiently retrieve large-scale automotive records from Carlist.my using these modern automation tools.
</p>


### 📅 **Timeline & Checklist**

| Week | Task | Responsible Member(s) | Status ✅ |
|------|------|------------------------|:-----------:|
| Week 1 | Form a diverse group (4 members) | All | ✅ |
| Week 1 | Choose a Malaysian website & get approval | Group Leader | ✅ |
| Week 1 | Identify target data fields (≥100,000 records) | Data Analyst | ✅ |
| Week 1 | Design system architecture (crawler + pipeline) | Architect | ✅ |
| Week 2 | Develop and test web crawler (initial batch) | Coder | ✅ |
| Week 2 | Begin collecting real data (progressive storage) | All | ✅ |
| Week 3 | Process and clean dataset (remove duplicates, standardize) | Data Analyst | ✅ |
| Week 3 | Apply optimization (Multiprocessing and Polars) | HPC Specialist | ✅ |
| Week 3 | Benchmark performance (before vs after) | Evaluator | ✅ |
| Week 4 | Compile results, charts, and graphs | HPC Specialist | ✅ |
| Week 4 | Write final report | All (shared) | ☐ |
| Week 4 | Submit report to Turnitin (by 16 May) | Group Leader | ☐ |
| Week 4 | Submit code, dataset, and slides | All | ☐ |
| Week 4 | Present final project (10 minutes) | All | ☐ |

