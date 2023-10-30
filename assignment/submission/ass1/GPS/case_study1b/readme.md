<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: GPS (GroupPalingSolid)

## Table of Contents
+ [Dataset Information](#dataset_info)
+ [Importing data](#import_data)
+ [Monthly Sales](#monthly_sales)
+ [Sales Region](#sales_region)
+ [Customer](#customer)
+ [Salesperson](#salesperson)
+ [Sales trend](#sales_trend)
+ [Slicer](#slicer)

## Dataset information <a name = "dataset_info"></a>
This dataset is called Dataset2.txt. This dataset has nine columns which are CUSTOMER, PRODUCTS, SALES PERSON, Sales Region, Target, SALES, SALES YEAR, SALES MONTH	and SALES QTR.

**Source**: https://docs.google.com/spreadsheets/d/1vUogP0glv5RVHAp1kRcJCLvHPztVrFxzTwvV4YZCsiE/edit?usp=sharing

<p align="center">
  <img src="images/0.png" alt="Image Description">
</p> 

### Importing data : <a name = "import_data"></a>
 1. Import the Dataset2.txt into Google Sheets, on the left upper menu bar, choose "File" -> "Import".
<p align="center">
  <img src="images/1.png" alt="Image Description">
</p> 
2. Then, click "Import data"
<p align="center">
  <img src="images/2.png" alt="Image Description">
</p>
3. Add a new column named "Month Index" and insert a formula =IF(H2="Jan", 1, IF(H2="Feb", 2, IF(H2="Mar", 3, IF(H2="Apr", 4, IF(H2="May", 5, IF(H2="Jun", 6, IF(H2="Jul", 7, IF(H2="Aug", 8, IF(H2="Sept", 9, IF(H2="Oct", 10, IF(H2="Nov", 11, IF(H2="Dec", 12, 0)))))))))))) to sort the "SALES MONTH" due to "SALES MONTH" format data is in text.
<p align="center">
  <img src="images/3.png" alt="Image Description">
</p>

## Charts
### Monthly sales chart<a name = "monthly_sales"></a>
1. First of all, select all columns that we just imported click on "Insert" and click on "Pivot Table"
<p align="center">
  <img src="images/4.png" alt="Image Description">
</p>

2. Make sure that the data range is correct and proceed with clicking on Create Table. Just so you know, you can create the table in the same existing sheet.
<p align="center">
  <img src="images/5.png" alt="Image Description">
</p>

3. On Pivot Table Editor, choose "Month Index" and "Sales Month" as Rows. Then, choose "Sales Year" and "Target" as Values and close the editor.
<p align="center">
  <img src="images/6.png" alt="Image Description">
</p>

<p align="center">
  <img src="images/7.png" alt="Image Description">
</p>

4. The output is shown below: 
<p align="center">
  <img src="images/8.png" alt="Image Description">
</p>

5. Select the table we just created, click on "Insert" and click on "Chart".
<p align="center">
  <img src="images/9.png" alt="Image Description">
</p>

6. In Chart Editor, choose "Stacked area chart" and ensure that the data range is correct. Set the X-axis as a "SALES MONTH" column and the Series as "SUM of SALES" and "SUM of Target".
<p align="center">
  <img src="images/10.png" alt="Image Description">
</p>

7. For the Sales Monthly Chart, the chart is shown below:
<p align="center">
  <img src="images/11.png" alt="Image Description">
</p>

### Sales region<a name = "sales_region"></a>
1. Repeat steps 1 and 2 from 'Monthly Sales Chart' to create a pivot table for Sales Region.
2. Add 'Sales Region' as Rows and 'SALES' as Values.
   <p align="center">
     <img width="251" alt="Screenshot 2023-10-26 at 1 17 13 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/85b0e0d9-90b1-40a4-b8ef-ff301a21671a">
</p>
The output is as stated below:
<p align="center"> 
  <img width="205" alt="Screenshot 2023-10-26 at 1 22 33 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/117ff0c9-4537-46f1-8fc6-398a95481919">
</p>
3. Select the pivot table that was created, and click 'Insert' at the ribbon. A pie chart will be automatically created.
<p align="center">
  <img width="503" alt="Screenshot 2023-10-26 at 1 27 21 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/400a5de2-2a63-4fdc-bfa4-91da09870684">
</p>
4. Once the pie chart is created, ensure that the Data range, Label and Value is correct as shown below. 
<p align="center">
  <img width="336" alt="Screenshot 2023-10-26 at 1 29 38 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/550e16b6-c562-4b41-9d13-033d4233ebea">
</p>
5. Customize the chart according to your preferences. The result of the pie chart is attached below:
<p align="center" >
  <img width="336" alt="Screenshot 2023-10-26 at 1 34 46 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/d09c1f00-a3cd-43db-8b75-28022ce13455">
</p>


### Customer<a name = "customer"></a>
1. Repeat steps 1 and 2 from 'Monthly Sales Chart' to create a pivot table for Customer.
2. Add 'CUSTOMER' as Rows and 'SALES' as Values.
   <p align="center">
   <img width="235" alt="Screenshot 2023-10-26 at 1 38 29 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/8366ee88-b602-4277-ad80-aa769130fc26">
   </p>
   The output is shown below:
   <p align="center">
   <img width="206" alt="Screenshot 2023-10-26 at 1 40 53 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/e4243114-336b-4dd9-9621-addb10291019">
   </p>
3. Select the pivot table that was created, and click 'Insert' at the ribbon. A pie chart will be automatically created.
   <p align="center">
     <img width="495" alt="Screenshot 2023-10-26 at 1 42 44 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/d1f8a1d1-519a-47cc-bf62-cd1c58c90bb5">
   </p>
4. Once the pie chart is created, ensure that the Data range, Label and Value is correct as shown below.
   <p align="center">
   <img width="336" alt="Screenshot 2023-10-26 at 1 44 18 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/3cc1b0e3-65ab-4748-8da7-ad3ec2c33080">
   </p> 
5. Customize the chart according to your preferences. The result of the pie chart is attached below:
   <p align="center" >
   <img width="395" alt="Screenshot 2023-10-26 at 1 45 45 PM" src="https://github.com/drshahizan/HPDP/assets/147252849/cf360ffa-a97b-4ef7-8d9b-e14a138a0eb8">
   </p>



### Salesperson<a name = "sales_person"></a>
1. Do the same steps in Monthly sales charts from step 1 until step 3. However, this time choose "Sales Product" and "PRODUCTS" as Rows. Then, choose "Sales". 
<p align="center">
  <img src="images/12.png" alt="Image Description">
</p>
<p align="center">
  <img src="images/13.png" alt="Image Description">
</p>

2. For the filter part, choose SALES, click on "Filter by condition", click on "is not empty" and close the editor.
<p align="center">
  <img src="images/15.png" alt="Image Description">
</p>
<p align="center">
  <img src="images/14.png" alt="Image Description">
</p>

3. The output is shown below:
<p align="center">
  <img src="images/16.png" alt="Image Description">
</p>

4. Select the table we just created, click on "Insert" and click on "Chart".
<p align="center">
  <img src="images/17.png" alt="Image Description">
</p>

5. In Chart Editor, choose "Stacked column chart" and ensure that the data range is correct. Set the X-axis as a "SALES PERSON" column and the Series as "Cooking Oil", "Flour", "Milk" and "Sugar".
<p align="center">
  <img src="images/18.png" alt="Image Description">
</p>

6. For the Salesperson chart, the chart is shown below:
<p align="center">
  <img src="images/19.png" alt="Image Description">
</p>


### Sales Trend<a name = "sales_trend"></a>
1. Do the same steps in Monthly sales charts from step 1 until step 3. However, this time choose "Sales Product" and "PRODUCTS" as Rows. Then, choose "Sales". 
<p align="center">
  <img src="images/20.png" alt="Image Description">
</p>
<p align="center">
  <img src="images/21.png" alt="Image Description">
</p>

2. The output is shown below:
<p align="center">
  <img src="images/22.png" alt="Image Description">
</p>

3. Select the table we just created, click on "Insert" and click on "Chart".
<p align="center">
  <img src="images/23.png" alt="Image Description">
</p>

4. In Chart Editor, choose "Smooth line chart" and ensure that the data range is correct. Set the X-axis as a "SALES MONTH" column and the Series as "SUM of SALES".
<p align="center">
  <img src="images/24.png" alt="Image Description">
</p>

5. For the Sales trend chart, the chart is shown below:
<p align="center">
  <img src="images/25.png" alt="Image Description">
</p>

## Slicer<a name = "slicer"></a>
1. First of all, Slicers provide buttons that you can click to filter tables or PivotTables. In addition to quick filtering, slicers also indicate the current filtering state, which makes it easy to understand what exactly is currently displayed. The image below is what we called Slicer.
<p align="center">
  <img src="images/26.png" alt="Image Description">
</p>

2. To create Slicer, you just need to click on "Data" and click on "Add a slicer".
<p align="center">
  <img src="images/27.png" alt="Image Description">
</p>

3. In a Slicer editor, you can choose any Column that you decide to filter.
<p align="center">
  <img src="images/28.png" alt="Image Description">
</p>



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



