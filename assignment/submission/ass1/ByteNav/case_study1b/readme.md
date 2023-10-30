<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

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
+ [Create Dashboard](#create_dashboard)
+ [Dashboard](#dashboard)
+ [Contributions](#contribution)

## Import Dataset <a name = "dataset_import"></a>
1. Click on the **"File"** menu and select **"Import"**.
<p align="center"><img align="center" alt="Coding" width="400" src="import.jpeg"></p>
<p align="center"> <em> Figure 1: Import data </em> </p> 

2. Click on the **"Upload"** and select the file to import from computer.
<p align="center"><img align="center" alt="Coding" width="400" src="importselectfile.jpeg"></p> 
<p align="center"> <em> Figure 2: Upload data </em> </p> 

3. Click **"Import data"** button after configuring the setting.
<p align="center"><img align="center" alt="Coding" width="400" src="importfile.jpeg"></p>
<p align="center"> <em> Figure 3: Import data </em> </p>

4. The data was imported sucessfully.
<p align="center"><img align="center" alt="Coding" width="400" src="afterimport.png"></p>
<p align="center"> <em> Figure 4: Dataset2 was imported sucessfully </em> </p> 

## Data Processing <a name = "data_processing"> </a>
1. Use function **"=UNIQUE(range, by_column, exactly_once)"** to get return of the rows in the order in which they first appear, same procedure apply to sales person, product, sales region, customer, sales year, sales month, and sales qtr.
<p align="center"><img align="center" alt="function" width="400" src="unique.png"></p>
<p align="center"> <em> Figure 5: Use UNIQUE function to get return of the rows in the order in which they first appear </em> </p> 
<p align="center"><img align="center" alt="Coding" width="400" src="uniquedone.png"></p>  
<p align="center"> <em> Figure 6: The filtered data after using UNIQUE function  </em> </p> 

2. Use **"data validation"** to build the dropdown menu.
<p align="center">
  <img src="dropdown.png" width="200" />
  <img src="dropdowndatavalidation.png" width="200" />
</p>
<p align="center"><img align="center" alt="Coding" width="400" src="dropdowndatarange.png"></p>  
<p align="center"> <em> Figure 7 & 8 & 9: Use data validation to build dropdown menu  </em> </p> 
<p align="center"><img align="center" alt="Table" width="400" src="dropdowndone.gif"></p>  
<p align="center"> <em> Gif 1: The built dropdown menu after using data validation </em> </p> 

3. Use function **"=QUERY(data, query, [headers])"** to retrieve the data.
<p align="center"><img align="center" alt="function" width="400" src="query.png"></p> 
<p align="center"> <em> Figure 10: Use QUERY function to retrieve the data  </em> </p> 

4. Use function **"IF(logical_expression, value_if_true, value_if_false)"** to combine with **QUERY function** to filter or query data based on specific criteria.
<p align="center"><img align="center" alt="function" width="400" src="if.png"></p> 
<p align="center"> <em> Figure 11: Use IF function to filter the data  </em> </p> 

6. Use function **"=CONCATENATE(string1, [string2, ...])"** to combine the cells without losing data.
<p align="center"><img align="center" alt="function" width="400" src="concatenate.png"></p>  
<p align="center"> <em> Figure 12: Use CONCATENATE function to combine the cells  </em> </p> 

7. Repeat step 3 to step 6 with sales region, sales product, sales person, customers, and month.
  
8. The completed dropdown menu.
<p align="center"><img align="center" alt="Table" width="500" src="filterdone.gif"></p>
<p align="center"> <em> Gif 2: The completed dropdown menu  </em> </p> 

9. Use function **"=QUERY(data, query, [headers])"** to calculate the sum of sales and target.
<p align="center"><img align="center" alt="function" width="400" src="sum.png"></p> 
<p align="center"> <em> Figure 13: Use QUERY function to select column H and calculate the sum of columns F and E, grouped by column H </em> </p> 
<p align="center"><img align="center" alt="function" width="400" src="sumofsalesandtarget.png"></p> 
<p align="center"> <em> Figure 14: The calculated sum of sales and target</em> </p> 
   
## Create Dashboard  <a name = "create_dashboard"> </a>
1. Click on the **"Insert"** menu and select **"chart"**.
<p align="center"><img align="center" alt="googlesheet" width="400" src="insertchart.png"></p>
<p align="center"> <em> Figure 15: Insert chart</em> </p> 

2. Select **"Line chart"**, and make the following changes:
  + Data range: K11:M22
  + X-axis: K11:M22
  + Series: Sum for L11:M22, and M11:M22
<p align="center"><img align="center" alt="editor" width="400" src="monthlysalesandtarget.png"></p>
<p align="center"> <em> Figure 16: Chart editor for monthly sales and target</em> </p> 
<p align="center"><img align="center" alt="editor" width="400" src="monthlysalesandtargetdone.png"></p>
<p align="center"> <em> Figure 17: Line chart for monthly sales and target</em> </p> 

3. Repeat step 1, and select **"Column chart"**, and make the following changes:
  + Stacking: None
  + Data range: A8:A331
  + X-axis: CUSTOMER
<p align="center"><img align="center" alt="editor" width="400" src="customer.png"></p>
<p align="center"> <em> Figure 18: Chart editor for customer</em> </p> 
<p align="center"><img align="center" alt="editor" width="400" src="customerdone.png"></p>
<p align="center"> <em> Figure 19: Column chart for customer</em> </p>

4. Repeat step 1, and select **"3D pie chart"**, and make the following changes:
  + Data range: D8:D331
  + Label: Sales Region
<p align="center"><img align="center" alt="editor" width="400" src="region.png"></p>
<p align="center"> <em> Figure 20: Chart editor for sales region</em> </p> 
<p align="center"><img align="center" alt="editor" width="400" src="regiondone.png"></p>
<p align="center"> <em> Figure 21: 3D pie chart for sales region</em> </p>

5. Repeat step 1, and select **"Pie chart"**, and make the following changes:
  + Data range: D8:D331
  + Label: SALES PERSON
<p align="center"><img align="center" alt="editor" width="400" src="person.png"></p>
<p align="center"> <em> Figure 22: Chart editor for sales person</em> </p> 
<p align="center"><img align="center" alt="editor" width="400" src="persondone.png"></p>
<p align="center"> <em> Figure 23: Pie chart for sales person</em> </p>

6. Repeat step 1, and select **"Area chart"**, and make the following changes:
  + Stacking: None
  + Data range: K8:L22
  + X-axis: K8:K22
  + Series: Sum for L8:L22 
<p align="center"><img align="center" alt="editor" width="400" src="salestrend.png"></p>
<p align="center"> <em> Figure 24: Chart editor for sales trend</em> </p> 
<p align="center"><img align="center" alt="editor" width="500" src="salestrenddone.png"></p>
<p align="center"> <em> Figure 25: Area chart for sales trend</em> </p>

## Dashboard  <a name = "dashboard"> </a>
<p align="center"><img align="center" alt="Table" width="500" src="dashboard.gif"></p>  
<p align="center"> <em> Gif 3: The completed dashboard  </em> </p> 

## Contribution 🛠️  <a name = "contribution"> </a>
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
