<h1 align="center"> 
  Group scubscub - Web Scraping using BeautifulSoup
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>IMAN ABADI BIN MOHD NIZWAN</td>
    <td>A23CS0084</td>
  </tr>
  <tr>
    <td width=80%>MOHAMED ALIF FATHI BIN ABDUL LATIF</td>
    <td>A23CS0112</td>
  </tr>
  <tr>
    <td width=80%>DHESHIEGHAN A/L SARAVANA MOORTHY</td>
    <td>A23CS0072</td>
  </tr>
</table>
<br>

<h3 align="center">Libraries Used</h3>
<div align='center'>
  <img src='https://www.jeveuxetredatascientist.fr/wp-content/uploads/2022/06/BeautifulSoup.jpg' height=90 alt='BeautifulSoup'>
  &nbsp;&nbsp;&nbsp;
  <img src='https://curl.se/logo/curl-logo.svg' height=90 alt='curl_cffi'>
</div>

<br>

<p align="justify">
  Beautiful Soup is a Python library that is used for web scraping. It allows you to parse HTML or XML documents into a readable tree-like structure and extract data based on the document's elements and tags. With Beautiful Soup, users can easily navigate through webpages, search for specific classes or tags and retrieve important information such as text, links and attributes. It is commonly used together with libraries such as <code>requests</code> (or <code>curl_cffi</code> for browser impersonation) and <code>pandas</code> to automate data collection from websites.

The website that we will be using is from BookXcess. (https://www.bookxcess.com/)

BookXcess is one of the largest bookstore chains in Malaysia, well known for offering a massive catalogue of books across every genre often at heavily discounted prices. Their online store hosts an extensive product inventory with detailed information for each title, including the product ID, book title, author (listed as the vendor), product type (genre/category), SKU (ISBN), current price, original compare-at price, currency, weight in grams, tags, full HTML description, cover image and the date the product was created.
</p>

<p align="justify">
We plan to obtain data from the website by traversing its XML sitemap index, which links to multiple product sub-sitemaps containing every product URL on the site. By parsing these sitemaps with BeautifulSoup (using the <code>lxml</code> XML parser), we will collect all product page URLs and then fetch each product's structured data via its public <code>.json</code> endpoint. To handle the scale (over 150,000 products) we use <code>curl_cffi</code> with Chrome impersonation, a <code>ThreadPoolExecutor</code> with 40 concurrent workers, exponential-backoff retries on transient errors (429/503/etc.) and periodic partial CSV flushing to avoid data loss on long runs. Finally, we will consolidate everything into a clean CSV file using <code>pandas</code>. In summary, we will efficiently retrieve the full BookXcess product inventory and its associated metadata using these tools.
</p>
