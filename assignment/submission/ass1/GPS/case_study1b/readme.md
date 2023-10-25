<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: GPS (GroupPalingSolid)

## Dataset information
This dataset is called Dataset2.txt. This dataset has nine columns which are CUSTOMER, PRODUCTS, SALES PERSON, Sales Region, Target, SALES, SALES YEAR, SALES MONTH	and SALES QTR.

**Source**: https://docs.google.com/spreadsheets/d/1vUogP0glv5RVHAp1kRcJCLvHPztVrFxzTwvV4YZCsiE/edit?usp=sharing 

### Importing data :
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
### Monthly sales chart
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

4. The output is shown in the image below: 
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

7. For the Sales Monthly Chart, the output of the chart is shown below:
<p align="center">
  <img src="images/11.png" alt="Image Description">
</p>

### Sales region

### Customer

### Salesperson

### Sales Trend

## Slicer


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



