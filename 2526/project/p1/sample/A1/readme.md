<h1 align="center"> 
  Group 10 - Web Scraping using BeautifulSoup
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>FARAH IRDINA BINTI AHMAD BAHARUDIN</td>
    <td>A20EC0035</td>
  </tr>
  <tr>
    <td width=80%>LOW JUNYI</td>
    <td>A20EC0071</td>
  </tr>
  <tr>
    <td width=80%>NURFARRAHIN BINTI CHE ALIAS</td>
    <td>A20EC0121</td>
  </tr>
  <tr>
    <td width=80%>YONG ZHI YAN</td>
    <td>A20EC0172</td>
  </tr>
</table>
<br>
<div align='center'>
<img src='https://www.jeveuxetredatascientist.fr/wp-content/uploads/2022/06/BeautifulSoup.jpg' height=200 width=300 alt='beautiful soup'>
</div>
<br>
<p>
  Beautiful Soup is a Python library that is used for web scraping. It allows you to parse the HTML or XML documents into a readable tree-like format, and then extract data from the tree based on its structure. With Beautiful Soup, you can easily navigate through the document, search for specific tags, and extract the text or attributes of those tags. It is often used in combination with other libraries such as requests to programmatically access web pages and extract data from them. The website that we will be using is from https://www.studymalaysia.com/education/top-stories/list-of-universities-in-malaysia.
  
  This website is a resource for individuals interested in higher education in Malaysia. It provides a comprehensive list of universities in Malaysia, including both public and private institutions. The website also includes information about the universities' locations, programs offered, and contact information. Additionally, the website provides articles and news related to education and universities in Malaysia, as well as resources for students and parents. The website appears to be operated by StudyMalaysia Group, which is a provider of education and career guidance in Malaysia.
  
  We plan to obtain data from the website by extracting one of its tables, specifically the list of 20 Public Universities in Malaysia. By analyzing the website's code, we will locate the table and access it using the 'full boxed' class. We will then utilize the pandas library and the BeautifulSoup package to extract the information from the table in html format. Finally, we will convert the obtained data into a CSV file. In summary, we will efficiently retrieve various tables and contents from the website using these tools.
</p>
