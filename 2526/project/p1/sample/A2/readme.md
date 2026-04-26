<h1>Air Flight Analysis  <img width=50px; height=50px src="https://user-images.githubusercontent.com/120556342/215304943-6df48d0a-d866-4f2c-91bf-263d47579dc2.png"></h1>

<p align="center">
  <img width=1000px; height=500px src="https://user-images.githubusercontent.com/120556342/215265584-6f73a09a-ac06-48db-b53c-58bcd370c320.png">
</p>

<h2>Group Members <img width=30px; height=30px src="https://user-images.githubusercontent.com/120556342/215398734-609ba04a-88e5-44b5-9eaa-239ac8edd091.png"></h2>
<table>
  <tr>
    <th>Name</th>
    <th>Matric</th>
  </tr>
  <tr>
    <th>ADAM WAFII BIN AZUAR</th>
    <th>A20EC0003</th>
  </tr>
  <tr>
    <th>HONG PEI GEOK</th>
    <th>A20EC0044</th>
  </tr>
    <tr>
    <th>MIKHEL ADAM BIN MUHAMMAD EZRIN</th>
    <th>A20EC0237</th>
  </tr>
    <tr>
    <th>QAISARA BINTI ROHZAN</th>
    <th>A20EC0133</th>
  </tr>
</table>

<h2>Introduction <img width=30px; height=30px src="https://user-images.githubusercontent.com/120556342/215426682-d651a56a-0d03-45db-82cc-2095910c24c0.png"></h2>
This project aims to investigate the Air Flight in 2022. The dataset consists of 61 columns and 4078318 rows. It is considered as big data and occupies 1.42GB of memory. The dataset is obtained from Kaggle which contains many kinds of dataset ranging from agriculture to education. We have selected this dataset because we like to analyze the flight status. We will perform a series of steps like data processing, data cleaning and visualization on this dataset. Google Colab will be used in this project. Other than that, there will be three libraries related to big data processing which are Pandas, Dask and Koalas being used in this project. At the end, we will compare the processing results from these libraries.

<h2>Libraries <img width=30px; height=30px src="https://user-images.githubusercontent.com/120556342/215421439-3196e80a-14de-47f0-8419-9ce6df02d01a.png"></h2>
<table>
  <tr>
    <th>Library</th>
    <th>Reason</th>
  </tr>
  <tr>
    <td>Pandas<br><img src='https://user-images.githubusercontent.com/120556342/215506067-3b45c1fd-e560-4532-a46c-9ef7c4c0bcce.png'></td>
    <td>
      <ul>
        <li>Pandas is the most straightforward and easy-to-library when working with structured data in-memory.</li>
        <li>Has a large community and plenty of learning documentations. You will find it easy to learn new techniques & find solution to problems.</li>
        <li>You will be provided with ample of convenient functions that will ease your journey in cleaning, transforming and aggregating data.</li>
        <li>Great for prototyping and exploratory data analysis.</li>
      </ul>  
     </td>
  </tr>
  <tr>
    <td>Dask<br><img src='https://user-images.githubusercontent.com/120556342/215506695-0589400d-09cd-4fb3-9d8a-2bc6ee1e342f.png'></td>
    <td>
      <ul>
        <li>Designed specifically for handling big datasets that can't fit into memory.</li>
        <li>Equipped with parallel processing capabilities, makes it faster than Pandas for large datasets.</li>
        <li>Good for use in distributed computing environments such as cloud computing.</li>
        <li>Suitable for use in high-performance and scientific computing.</li>
      </ul>  
     </td>
  </tr>
    <tr>
    <td>Koalas<br><img src='https://user-images.githubusercontent.com/120556342/215507119-4e958236-1d0a-452d-bbe9-5d298eddf049.png'></td>
    <td>
      <ul>
        <li>Provides a Pandas-like interface to work with big datasets.</li>
        <li>Combines the simplicity and ease of use of Pandas with the performance of Dask.</li>
        <li>Good for use in a distributed computing environment, but with less complexity than using Dask directly.</li>
      </ul>  
     </td>
  </tr>
</table>

<h2>Dataset  <img width=30px; height=30px src="https://user-images.githubusercontent.com/120556342/215398064-79c751ea-35b9-4958-a262-0cb56a0c4c31.png"></h2>

<a href="https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022?select=Combined_Flights_2022.csv">Kaggle: Air Flight Dataset</a><br>
<h4>Attribute Information:</h4>
<table>
  <tr>
    <th>Acronym</th>
    <th>Description</th>
  </tr>
  <tr>
    <th>FlightDate</th>
    <td>Flight Date (yyyymmdd)</td>
  </tr>
    <tr>
    <th>Airline</th>
    <td>Name of Airline</td>
  </tr>
    <tr>
    <th>OP_CARRIER_FL_NUM</th>
    <td>Flight Number</td>
  </tr>
    <tr>
    <th>Origin</th>
    <td>Origin Airport</td>
  </tr>
    <tr>
    <th>Dest</th>
    <td>Destination Airport</td>
  </tr>
    <tr>
    <th>Cancelled</th>
    <td>Cancelled Flight Indicator (1=Yes)</td>
  </tr>
    <tr>
    <th>Diverted</th>
    <td>Diverted Flight Indicator (1=Yes)</td>
  </tr>
    <tr>
    <th>CRSDepTime</th>
    <td>CRS Departure Time (local time: hhmm)</td>
  </tr>
    <tr>
    <th>DepTime</th>
    <td>Actual Departure Time (local time: hhmm)</td>
  </tr>
    <tr>
    <th>DepDelayMinutes</th>
    <td>Difference in minutes between scheduled and actual departure time. Early departures set to 0.</td>
  </tr>
    <tr>
    <th>DepDelay</th>
    <td>Difference in minutes between scheduled and actual departure time. Early departures show negative numbers.</td>
  </tr>
    <tr>
    <th>ArrTime</th>
    <td> Actual Arrival Time (local time: hhmm)</td>
  </tr>
    <tr>
    <th>ArrDelayMinutes</th>
    <td>Difference in minutes between scheduled and actual arrival time. Early arrivals set to 0.</td>
  </tr>
    <tr>
    <th>AirTime</th>
    <td>Flight Time, in Minutes</td>
  </tr>
    <tr>
    <th>CRSElapsedTime</th>
    <td>CRS Elapsed Time of Flight, in Minutes</td>
  </tr>
    <tr>
    <th>ActualElapsedTime</th>
    <td>Elapsed Time of Flight, in Minutes</td>
  </tr>
    <tr>
    <th>Distance</th>
    <td>Distance between airports (miles)</td>
  </tr>
    <tr>
    <th>Year</th>
    <td>Year</td>
  </tr>
    <tr>
    <th>Quarter</th>
    <td>Quarter (1-4)</td>
  </tr>
    <tr>
    <th>Month</th>
    <td>Month</td>
  </tr>
    <tr>
    <th>DayofMonth</th>
    <td>Day of Month</td>
  </tr>
    <tr>
    <th>DayOfWeek</th>
    <td>Day of Week</td>
  </tr>
</table> 
<h2>Contents&nbsp;<img width=30px; height=30px src="https://user-images.githubusercontent.com/120556342/215428150-7c7e817f-3efb-40ac-8675-4c49740784c0.png"></h2>
1. Data Preparation and Cleaning<br>
<ul>
  <li>Remove unwanted columns</li>
  <li>Remove null values</li>
  <li>Use efficient data types</li>
  <li>Drop duplicate rows</li>
</ul>  
2. Exploratory Analysis and Visualization<br>
<ul>
  <li>Statistic</li>
  <li>Histogram</li>
  <li>Scatter Plot</li>
  <li>Line Chart</li>
  <li>Bar Chart</li>
</ul>  
3. Asking and Answering Questions<br>

<h2>Conclusion</h2>
In conclusion when performing the Exploratory Data Analysis (EDA), Dask is the fastest choice if you're working with large datasets. In comparison to Dask and Pandas, it is believed that Dask is 500% times faster than Pandas. Koalas are a good alternative to Pandas if you prefer their simplicity and use, but with a small performance penalty. In general, Dask is faster than Koalas as it operates directly on the data and does not have the overhead of the Pandas-like interface.<br><br>

To put it in simpler words for the performance comparison between the libraries:

> **Dask > Koalas > Pandas**

<br>

🌟<b>For more information: </b><br>
| Open in Colab |  Open in GitHub |
|  ------ | :------: | 
|<a href="https://colab.research.google.com/drive/1AbXa171YIE-AINYH1U1sw7-zNH32AJFd?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|[:octocat:](https://github.com/drshahizan/Python-big-data/blob/main/Project/AdMiPeQa/Project_big_data_AdMiPeQa.ipynb)|

