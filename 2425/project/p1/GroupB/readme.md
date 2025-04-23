<h1 align="center"> 
  Data Drillers - Carlist.my
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>ALIATUL IZZAH BINTI JASMAN</td>
    <td>A22EC0136</td>
  </tr>
  <tr>
    <td width=80%>MULYANI BINTI SARIPUDDIN </td>
    <td> A22EC0223 </td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD ANAS BIN MOHD PIKRI </td>
    <td> A21SC0464 </td>
  </tr>
  <tr>
    <td width=80%>THEVAN RAJU A/L JEGANATH </td>
    <td>A22EC0286</td>
  </tr>
</table>

# 🚗 Carlist.my Web Scraper

A Python-based web scraper that extracts car listings from [Carlist.my](https://www.carlist.my/cars-for-sale/malaysia) and saves the data into a structured CSV file. Built for simplicity, performance, and reliability using a sequential (single-threaded) approach.

---

## 🔧 Features

- Extracts car listing details like price, mileage, fuel type, color, etc.
- Parses structured data (`JSON-LD`) from each listing
- Writes listings one-by-one to CSV (no multithreading)
- Retries on failed pages with configurable delay
- Tracks scraping speed, duration, and file size

---

## 📚 Libraries Used

| Library          | Purpose                                         |
|------------------|--------------------------------------------------|
| `requests`       | Sends HTTP GET requests                          |
| `beautifulsoup4` | Parses and extracts HTML content                 |
| `json`           | Parses structured JSON-LD embedded in pages     |
| `csv`            | Writes extracted data into a CSV file            |
| `time`           | Manages delays and measures performance          |
| `os`             | Handles file size check and system operations    |

### Install Required Libraries

```bash
pip install requests beautifulsoup4
