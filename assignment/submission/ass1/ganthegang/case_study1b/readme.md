<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: ganthegang

### Group Members

| Name                                     | Matrix Number | 
| :---------------------------------------- | :-------------: | 
| ALIEYA ZAWANIE BINTI A ZAINI | A21EC0156   |  
| YEW RUI XIANG               | A21EC0149   |      	
| WAN AMIRUL HAFIQ BIN WAN HUZAINI      | A21EC0141   |      
| ABDUL MUHAIMIN BIN ABDUL RAZAK | A21EC0002   |      

## Table of Contents
+ [Dataset Information](#dataset_info)
+ [Data Import and Data Preprocessing](#preprocessing)
+ [Data Processing](#processing)
+ [Dashboard](#dashboard)
  
## Dataset Information <a name = "dataset_info"></a>
This dataset is called dataset2.txt. This dataset has nine columns that contain information about Customers, Products, SalesPerson, SalesRegion, SalesYear, SalesMonth, SalesQtr. Table 1 shows the full marks for the data


**Source**: https://docs.google.com/spreadsheets/d/1PwFHJ20W3lQG4J2shN3Iz5JEFXkT9LxH4tVYx5kTJpY/edit?pli=1#gid=335153237

## Data Import and Data Preprocessing <a name = "preprocessing"></a>
1. In the ribbon 'File', click on "Import" to upload the “Dataset2.txt”.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/Screenshot 2023-10-25 013533.png" width=300>
</p>

<div align="center">
  
Figure 1: To import Dataset
</div>

2. Select the 'Upload' and click on 'Browse.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/2.png" width=300>
</p>

<div align="center">
  
Figure 2: Browse To Import The Dataset

</div>


3. Select the 'Dataset2.txt' and then press 'OK'.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/3.png" width=400>
</p>

<div align="center">
  
Figure 3: Select The Dataset

</div>

4. After the file has been loaded into Google Sheets, click on 'Import Data'. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/4.png" width=400>
</p>

<div align="center">
  
Figure 4: Import Dataset

</div>

5. After the file load it should look like Figure 5 below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/5.png" width=300>
</p>

<div align="center">
  
Figure 5: Selecting The Data

</div>

## Data Processing <a name = "processing"></a>
### Pivot Table

1. Click on any of the columns, then press Ctrl+A to select all. Then on the ribbon, click Insert then select pivot table.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/6.png" width=300>
</p>

<div align="center">  
Figure 7: Select all
</div>
<br>
2. After that, make sure it is inserted into a new sheet and then press ‘Create’.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/7.png" width=300>
</p>

<div align="center">  
Figure 8:  Create a pivot table
</div>
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/8.png" width=300>
</p>

<div align="center">  
Figure 9:   Pivot table
</div>
<br>

### Sales Region

3. On the right side click on ‘Rows’ and ‘Add, and select ‘Sales Region’ 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/9.png" width=300>
</p>
<div align="center">  
Figure 10: Creating a table for sales region
</div>
<br>

4. Then click on ‘Add’ at Values and select ‘Sales’.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/10.png" width=400>
</p>
<div align="center">  
Figure 11: Select Value
</div>
<br>

5. Then there should be a complete table of Sales Region and Sum of Sales. 

   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/11.png" width=400>
</p>
<div align="center">  
Figure 12: Sale region table
</div>
<br>

6. Click Insert and choose Chart then, in the Chart editor;
      - Chart type: 3D pie chart
      - Data range: select the pivot table of the region
      - Label: Sales Region
      - Values: Sum of Sales
      - Close Chart editor
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/Screenshot 2023-10-26 011900.png" width=400>
</p>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/13.png" width=400>
</p>
<div align="center">  
Figure 13: Sales region pie chart
</div>
<be>

### Customer

7. Next to create another table for customers, click on empty cells and click ‘Insert’ at the ribbon and select ‘Pivot Table’. Then the pop-up window ‘create pivot table’ will appear. Select data range by clicking the square icon on the right then select the dataset on the first sheet. Next on the Insert select the ‘Existing Sheet’ and below that make sure to select the empty cell location and press ‘Create’.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/15.png" width=400>
</p>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/16.png" width=400>
</p>
<div align="center">  
Figures 14  and 15: Creating Pivot Table for Customer.
</div>
<br>

8. In the Pivot table editor;

      - Rows: click/drag Customer
      - Values: click/drag Products
      - Close the Pivot table editor


<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/17.png" width=400>
</p>
<div align="center">  
Figure 16: Pivot table editor for customer.
  <br>
  <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/18.png" width=400>
</p></div>
<div align="center">  
Figure 17: Pivot Table Customer
</div>
<br>

 
9. Click Insert and choose Chart then, in the Chart editor;
     - Chart type: 3D pie chart
     - Data range: select the pivot table of the region
     - Label: Customer
     - Values: Count Of Products
     - Close Chart editor

<p align="center">
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/19.png" width=500>
</p>
<div align="center">  
Figure 18: Pie chart for Customer
</div>
<be>
  
### Sales Trend

10. Click Insert then choose pivot table and Select the data range from the dataset2 sheet. Insert the pivot table into the existing sheet name as Dashboard then click Create in the Pivot table editor;
In the Pivot table editor;

      - Rows: click/drag Sales Year, Sales Month
      - Values: click/drag Sales
      - Close the Pivot table editor

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/20.png" width=300>
</p>
<div align="center">  
Figure 19:  Pivot editor for Sales Trend
  
</div>
<be>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/21.png" width=300>
</p>
<div align="center">  
Figure 20:  Pivot Table for Sales Trend
  
</div>
<br>

11. Click Insert and select Chart

    In Chart editor;
      - Chart type: 3D pie chart
      - Data range: select the pivot table of the region
      - Label: Sales Month`
      - Values: Sum of Sales
      - Close Chart editor


<p align="center">
     <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/22.png" width=300>
</p>
<div align="center"> 
Figure 21: Chart editor for sale trend
</div> 
<br>
    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/saLETREND.png" width=700>
</p>
<div align="center"> 
Figure 22: Sale Trend Smooth line graph
</div>  
<br>

### Monthly Sales

12. Click Insert and choose pivot table
        In the Pivot table editor;
              - Rows: click/drag Sales Month
              - Values: click/drag Sales and Target
              - Close the Pivot table editor

  

    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/23.png" width=300>
</p>
<div align="center"> 
Figure 23: Pivot table editor for Monthly sales
</div>  
<br>
<p align="center">

  <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/24.png" width=300>
</p>
<div align="center"> 
Figure 24: Pivot table for Monthly sales
</div>  
<br>
<p align="center">
  
13. Click Insert and choose Chart

      In Chart editor;
          - Chart type: Stacked area chart
          - Stacking: Standard
          - Data range: select the pivot table of Monthly Sales
          - X-axis: Sales Month
          - Series: Sum of Target and Sum of Month
          - Close Chart editor

  

    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/26.png" width=300>
</p>
<div align="center"> 
Figure 25: Chart editor for Monthly sales
</div>  
<br>
   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/30.png" width=300>
</p>
<div align="center"> 
Figure 26: Graph for Monthly sales
</div>  
<br>

### Sales Person

14. Click Insert and choose pivot table then select the data range from the dataset2 sheet and insert the pivot table into the existing sheet name as Dashboard. Click Create
      In the Pivot table editor;
          - Rows: click/drag Sales Person
          - Columns: click/drag Product
          - Values: click/drag Sales
          - Close the Pivot table editor


  

    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/28.png" width=300>
</p>
<div align="center"> 
Figure 27: Pivot Table editor for Sales Person.
</div>  
<br>
   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/29.png" width=300>
</p>
<div align="center"> 
Figure 28: Table for Sales Person
</div>  
<br>

15. Click Insert and choose chart

    In Chart editor;
        - Chart type: Stacked column chart
        - Stacking: Standard
        - Data range: select the pivot table of the salesperson
        - X-axis: Sales Person
        - Series: Cooking Oil, Flour, Milk, Sugar
        - Close Chart editor


    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/31.png" width=300>
</p>
<div align="center"> 
Figure 27: Chart editor for Sales Person.
</div>  
<br>
   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/32.png" width=300>
</p>
<div align="center"> 
Figure 28: Chart for Sales Person
</div>  
<br>
  
16.  Create Slicer: Sales Year, Sales Region, Sales Products, Customer, Sales Person
         - Click Data at ribbon then select Slicer

<p align="center">
   <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/slicer 1.png" width=300>
</p>

<br>
   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/slicer2.png" width=300>
</p>
<div align="center"> 
Figure 29: Slicer editor
</div>  
<br>
   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/slicer3.png" width=800>
</p>
<div align="center"> 
Figure 30: Slicer for Sales Year, Products, Sales Region, Customer, Sales Person.
</div>  
<br>

## Dashboard <a name = "dashboard"></a>
### Data visualization
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/Screenshot 2023-10-26 025000.png" width=1000>
</p>

1. Create **"New sheet"** with name **"dashboard"** in another sheet by pressing the "+" button at the bottom left corner.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/33.png" width=800>
</p>
<div align="center"> 
Figure 31: Creating a new sheet for the dashboard
</div>
<br>

2. At the beginning, selecting "Insert">"Chart" to create a pie chart for the showing the sales in each or selected region. The chart type is selected with **"pie chart"** and the data range is filled with **"Dataset2!A1:I324"** which cover the whole table of Dataset2.
<br>

3. The label is selected with **"Sales Region"** column. Then the "aggregated" and use "row 1 as header" are checked.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/34.png" width=250>
</p>
<div align="center"> 
Figure 32: Setup of "Region" pie chart
</div>
<br> 

4. The similar step is applied on the "Customer" pie chart with the only different setup at the label which is changed to "Customer".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/35.png" width=250>
</p>
<div align="center"> 
Figure 33: Setup of "Customer" pie chart
</div>
<br> 

5. For visualizing the sales made by each sales person, a **"Stacked column chart"** is creeated with a **"Standard"** stacking. The data range is filled with **"AF1:AJ10"** which is the pivot table created before in the Figure 27. Choose the **"Sales person"** under the "X-axis" and select the "Series" with those product for stacking purpose.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/36.png" width=250>
</p>
<div align="center"> 
Figure 34: Setup of "Sales person" stacked column chart
</div>
<br> 

6. Check "use row 1 as header" and "use column AF as labels".

7. The "Sales trend" line chart is also constructed with the following setup as shown in the Figure 35.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/37.png" width=250>
</p>
<div align="center"> 
Figure 35: Setup of "Sales trend" smooth line chart
</div>
<br>    

8. Customize the line chart with naming the horizontal and vertical axis title as **"SALES MONTH"** and **"SUM OF SALES"**.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/38.png" width=250>
</p>
<div align="center"> 
Figure 36: Customize horizontal axis title of "Sales trend" smooth line chart
</div>
<br>

9. A **"Stacked area chart"** with **"Standard"** stacking is setup for visualizing the comparasion between the actual sales and the target sales.
<br>

10. The data range is filled with the value of **"W12:Y24"** which cover the pivot table constructed on the Figure 23. The "X-axis" is selected as the **"SALES MONTH"** while the "Series" is selected with **"SUM of Target"** and **"SUM of Sales"**. Some box at the below are also checked as shown in the figure below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1b/HPDP dataset2/39.png" width=250>
</p>
<div align="center"> 
Figure 37: Setup of "Monthly Sales" stacked area chart
</div>
<br>

11. At the end, all the chart is customized to make it look good. For each chart, the chart title is specified and designed with different styles or colours. The title of the dashboard is also placed in the upper position.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



