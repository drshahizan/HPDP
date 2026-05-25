<h1 align="center"> 
  Group 10 - Web Scraping using PlayWright
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>TAN YI YA</td>
    <td>A23CS0187</td>
  </tr>
  <tr>
    <td width=80%>TEH RU QIAN</td>
    <td>A23CS0191</td>
  </tr>
  <tr>
    <td width=80%>NURUL ADRIANA BINTI KAMAL JEFRI</td>
    <td>A23CS0258</td>
  </tr>
</table>
<br>
<div align='center'>
<img width="285" height="177" alt="images" src="https://github.com/user-attachments/assets/4b848fcf-7587-4491-bd14-7b6cbcf567a1" />
</div>
<br>
<p>
  Playwright is an open-source automation library developed by Microsoft, designed for end-to-end testing and web scraping across modern web applications. It supports multiple programming languages, including Python, Node.js, Java, and .NET, allowing developers to automate interactions across Chromium, Firefox, and WebKit browser engines. It provides robust features such as auto-waiting, network intercepting, and headless browser execution, making it a powerful tool for reliably capturing data from complex web architectures. The website that we will be using is from https://www.malaymail.com/.
  
  This website is a prominent Malaysian digital news portal that provides up-to-the-minute coverage of local and international news. It covers a wide range of topics, including national politics, business, lifestyle, sports and entertainment, catering to an English-speaking audience. The website serves as a rich resource for real-time information, opinion pieces and investigative journalism focused on Malaysian current affairs. 
  
  We plan to obtain data from the website by extracting the latest news articles from its main feed or specific category pages. By analyzing the website's dynamic DOM structure, we will use Playwright to wait for the JavaScript content to fully render, ensuring all headlines, publication dates and article URLs are accessible. We will then utilize appropriate CSS selectors or XPath expressions to locate the news grid and extract the relevant text and link attributes. Finally, we will process the gathered content and export it into a structured format of a CSV file for further analysis. In summary, we will efficiently retrieve dynamic news data from the website using these tools.
</p>

### 📅 **Timeline & Checklist**

| Week | Task | Responsible Member(s) | Status ✅ |
|------|------|------------------------|:-----------:|
| Week 1 | Form a diverse group (4 members) | All | ✅ |
| Week 1 | Choose a Malaysian website & get approval | Group Leader |✅ |
| Week 1 | Identify target data fields (≥100,000 records) | Data Analyst | ✅ |
| Week 1 | Design system architecture (crawler + pipeline) | Architect | ✅ |
| Week 2 | Develop and test web crawler (initial batch) | Coder | ✅ |
| Week 2 | Begin collecting real data (progressive storage) | All | ✅ |
| Week 3 | Process and clean dataset (remove duplicates, standardize) | Data Analyst | ✅ |
| Week 3 | Apply optimization (threading, Spark, Dask, etc.) | HPC Specialist | ✅ |
| Week 3 | Benchmark performance (before vs after) | Evaluator | ✅ |
| Week 4 | Compile results, charts, and graphs | Documentation Lead | ✅ |
| Week 4 | Write final report | All (shared) | ✅ |
| Week 4 | Submit report to Turnitin (by 16 May) | Group Leader | ✅ |
| Week 4 | Submit code, dataset, and slides | All | ✅ |
| Week 4 | Present final project (10 minutes) | All | ✅ |

