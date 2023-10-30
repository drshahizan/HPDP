<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales Performance

### Group Name: ohSheet
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | ------------- |
| MIKHAIL BIN YASSIN                       |  A21EC0053       |      Pre-processing |
| FAUZAN AQIL BIN AZMAN                    |    A21EC0174     |    Data Transformation           |
| YASMEEN NATASHA BINTI HAFIZ SHAHREL      |     A21EC0147    |     Documentation|   
| MUHAMMAD ADAM FAHMI BIN MOHD TAUFIQ      |      A21EC0061   |       Visualization         |     

## Table of Contents
+ [About](#about)
+ [Getting Started](#import)
+ [Creating a Dynamic Dashboard](#dashboard)
+ [Contributing](../CONTRIBUTING.md)


## About <a name="about"></a>

The main goal of this project is to utilize Google Sheets to process and present data, with a specific focus on a case study related to examination results. The project involves tasks such as calculating statistics, creating charts, and generating meaningful insights from the examination results.

We were given **Dataset2** where information about **CUSTOMER**, **PRODUCTS**, **SPORTS**, **SALES PERSON**, **Sales Region**, **Target**, **SALES**, **SALES YEAR**, **SALES MONTH** and **SALES QTR** are contained.

Firstly, we need to **import the data**. Since the data is already processed, we will **create a dynamic dashboard** to visualize the overall result.

In a nutshell, the project emphasizes practical data manipulation and visualization skills within the context of educational assessment.

## Getting Started <a name="import"></a>

1. Download the Dataset2.txt file.

2. To import the Dataset2.txt file on Google Sheets, choose 'File' and click 'Import'.
   
   <div align="center">
   <img src="import.png" alt="import" width="350">
   </div><br>
   
3. Choose the file and click 'Import data'.

4. Figure shows the data that has been entered into Google Sheets. This dataset contains ten columns: **CUSTOMER**, **PRODUCTS**, **SPORTS**, **SALES PERSON**, **Sales Region**, **Target**, **SALES**, **SALES YEAR**, **SALES MONTH** and **SALES QTR**.

## Creating a Dynamic Dashboard <a name = "dashboard"></a>
   <div align="center">
   <img src="dashboard.png" alt="import">
   </div><br>

5. Create Pivot table
   
   Click “Insert” button then choose “Pivot Table” as shown below
   <div align="center">
   <img src="createPivot.png" alt="import" width="350">
   </div><br>

   Select all the data from the dataset for data range 
    <div align="center">
   <img src="createPivot2.png" alt="import" width="350">
   </div><br>

   Then choose whether “Existing sheet” to apply at same page, for “New sheet” it will create and apply at the new sheet. Lastly, click “Create” button to create pivot table
   <div align="center">
   <img src="createPivot4.png" alt="import" width="350">
   </div><br>

   Here is the examples of pivot table that already created 
   <div align="center">
   <img src="createPivot6.png" alt="import" width="350">
   </div><br>

   
   SALES REGION
   
   For sales region, drag “Sales Region” to “Rows” and “Filters”, then drag “SALES” to the values
    <div align="center">
   <img src="createPivot7.png" alt="import" width="350">
   </div><br>

   Here is the result of SALES REGION
   
    <div align="center">
   <img src="createPivot8.png" alt="import" width="350">
   </div><br>

   SALES YEAR

   For Sales year, drag “SALES YEAR” to “Rows”, drag “SALES” to Values and set it as  “SUM”, and lastly drag “SALES YEAR” to “Filters”.
    <div align="center">
   <img src="salesYear2.png" alt="import" width="350">
   </div><br>

   Here is the result of SALES YEAR
   <div align="center">
   <img src="salesYear3.png" alt="import" width="350">
   </div><br>

   SALES PERSON

   For Customer, drag “CUSTOMER”,  to “Rows”, then drag “PRODUCTS” to the “Columns”, drag “PRODUCTS” to value and set the value as “COUNTA”  and lastly drag “SALES PERSON” to “Filters”
    <div align="center">
   <img src="salesPerson2.png" alt="import" width="350">
   </div><br>

   Here is the result for SALES PERSON
   <div align="center">
   <img src="salesPerson3.png" alt="import" width="350">
   </div><br>

   CUSTOMER
   
   For Customer, drag “CUSTOMER”  to “Rows”, then drag “PRODUCTS” to the values and lastly drag “CUSTOMER” to “Filters”
   <div align="center">
   <img src="customer2.png" alt="import" width="350">
   </div><br>

    Here is the result for CUSTOMER
   <div align="center">
   <img src="customer3.png" alt="import" width="350">
   </div><br>
   
   

   PRODUCTS
   
   For monthly sales, drag “SALES PERSON”  to “Rows”, then drag “PRODUCT” to the “Columns”, drag “PRODUCT” to values and set it as “COUNTA” , and lastly drag “SALES PERSON” and “PRODUCTS” to “Filters”
    <div align="center">
   <img src="product2.png" alt="import" width="350">
   </div><br>

   
   Here is the result for PRODUCTS 
   <div align="center">
   <img src="product3.png" alt="import" width="350">
   </div><br>


   SALES TREND

   For sales trend, drag “SALES YEAR”, “MONTH NUMBER” and “SALES MONTH”  to “Rows”, then drag “SALES” to the values and lastly drag “SALES YEAR” to “Filters”
   <div align="center">
   <img src="salesTrend2.png" alt="import" width="350">
   </div><br>

   Here is the result for SALES TREND 
   <div align="center">
   <img src="salesTrend3.png" alt="import" width="350">
   </div><br>
    

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


