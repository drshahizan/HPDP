<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: BYTE NAVIGATORS

### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | ------------- |
| LOO ZHI YUAN            |A21EC0197      |Data Preprocessing|
| SOO WAN YING              |A21EC0227      |Documentation      |
| LAU YEE CHI              |A21EC0042      |Visualization     |

### Table of Contents
+ [Import Dataset](#dataset_import)
+ [Data Processing](#data_processing)
+ [Dashboard](#dashboard)
+ [Contributions](#contribution)

## Import Dataset <a name = "dataset_import"></a>
1. Import the Dataset1.txt to Google Sheets, click on the **"File"** menu and select **"Import"**.
<p align="center"><img align="center" alt="Coding" width="400" src="import.jpeg"></p>

2. Click on the **"Upload"** and select the file to import from computer.
<p align="center"><img align="center" alt="Coding" width="400" src="importselectfile.jpeg"></p>  

3. Click **"Import data"** button after configuring the setting.
<p align="center"><img align="center" alt="Coding" width="400" src="importfile.jpeg"></p>   

4. The data was imported sucessfully.
<p align="center"><img align="center" alt="Coding" width="400" src="afterimport.png"></p>  

## Data Processing <a name = "data_processing"> </a>
1. Use formula **"=UNIQUE(range, by_column, exactly_once)"** to get return of the rows in the order in which they first appear, same procedure apply to sales person, product, sales region, customer, sales year, sales month, and sales qtr.
<p align="center"><img align="center" alt="Formula" width="400" src="unique.png"></p>  
<p align="center"><img align="center" alt="Coding" width="400" src="uniquedone.png"></p>  

2. Use **"data validation"** to build the dropdown menu.
<p align="center">
  <img src="dropdown.png" width="200" />
  <img src="dropdowndatavalidation.png" width="200" />
</p>
<p align="center"><img align="center" alt="Coding" width="400" src="dropdowndatarange.png"></p>  
<p align="center"><img align="center" alt="Table" width="400" src="dropdowndone.gif"></p>  

3. Use formula **"=QUERY(data, query, [headers])"** to retrieve the data.
<p align="center"><img align="center" alt="Formula" width="400" src="query.png"></p>  

4. Use formula **"IF(logical_expression, value_if_true, value_if_false)"** to combine with **QUERY function** to filter or query data based on specific criteria.
<p align="center"><img align="center" alt="Formula" width="400" src="if.png"></p>  

6. Use formula **"=CONCATENATE(string1, [string2, ...])"** to combine the cells without losing data.
<p align="center"><img align="center" alt="Formula" width="400" src="concatenate.png"></p>  

7. Repeat step 3 to step 6 with sales region, sales product, sales person, customers, and month.

8. The completed dropdown menu.
<p align="center"><img align="center" alt="Table" width="500" src="filterdone.gif"></p>  

## Dashboard  <a name = "dashboard"> </a>
<p align="center"><img align="center" alt="Table" width="500" src="dashboard.gif"></p>  

## Contribution 🛠️  <a name = "contribution"> </a>
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
