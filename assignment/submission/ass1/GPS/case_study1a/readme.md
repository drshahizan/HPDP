<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: GPS (GroupPalingSolid)
### Group Members

| Name                                     | Matrix Number |
| :---------------------------------------- | :-------------: |
| MUHAMMAD FARHAN BIN IBRAHIM | A21EC0072   | 
| FONG KHAH KHEH              | A21EC0026   |  	
| LING WAN YIN                | A21EC0047   |  	
| SARAH WARDINA BINTI RAFIDIN | A21EC0128   | 

## Table of Contents
+ [Dataset Information](#dataset_info)
+ [Data Import and Data Preprocessing](#preprocessing)
+ [Data Processing](#processing)
+ [Dashboard](#dashboard)
+ [Contributions](#contribution)

## Dataset Information <a name = "dataset_info"></a>
This dataset contains the attributes of Id_No, Academic, Sports, Co-Curriculum,	Test_1 and	Test_2. 

**Source**: https://docs.google.com/spreadsheets/d/1uSaVrYlYKFgK8fy_vs9hr13n1iBJq14A0JnEcstmDrI/edit#gid=1756902967 

## Data Import and Data Preprocessing <a name = "preprocessing"></a>
1. Press **"File" > "Import"** to upload the **"Dataset1.txt"** that has been downloaded earlier by clicking **"Browse"** to find the directory of the file.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/96f95fff-a9e4-4864-a031-bf3dc30c80ad"width=300>
</p>

<div align="center">
  
_Figure 1: **"File" > "Import"**_ </div>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/browse.png" width=500>
</p>

<div align="center">
  
_Figure 2: Click **"Browse"** under the **"Upload"** pane_

</div>

2. Select the **"Dataset1.txt"** and then click **"Open"**.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/file%20selection.png" width=500>
</p>

<div align="center">
  
_Figure 3: File selection_
</div>

3. Wait until it loads finish. It may takes a few seconds to load the dataset file into the Google Sheets. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/waiting.png" width=400>
</p>

<div align="center">
  
_Figure 4: Loading_
</div>

4. Make sure the selected file to be loaded into Google Sheets is correct. Then, check the following details and click **"Import data"**.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/details.png" width=400>
</p>

<div align="center">
  
_Figure 5: Importing data_
</div> 

5. To ensure each record has two decimal places, click every column letter and select **"123"** under the toolbar. Click **"Numbers"**.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/roundoff.png" width=500>
</p>

<div align="center">
  
_Figure 6: Click **"Numbers"**_

</div>

## Data Processing <a name = "processing"></a>
1. To get the value for the new column named **P1**, **P2**, **P3**, **P4** and **P5**, the insertion of the formulas are as follows.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P1.png" width=300>
</p>
<div align="center">
    
_Figure 7: Column P1_
    
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P2.png" width=300>
</p>
<div align="center">  
    
_Figure 8: Column P2_ 

</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P3.png" width=300>
</p>
<div align="center">  
    
_Figure 9: Column P3_

</div>   
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P4.png" width=300>
</p>
<div align="center">  
    
_Figure 10: Column P4_
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P5.png" width=300>
</p>
<div align="center">  
    
_Figure 11: Column P5_
</div>
<br>

2. Double-click the **"+"** shape in the bottom right corner of the data in each column to retrieve data until the last row in each column.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/+.png" width=500>
</p>
<div align="center">  
    
_Figure 12: Data retrieval until last row_
</div>
<br>

3. Click every column letter and then select **"123" > "Numbers"** to round off to two decimal places.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/two.png" width=500>
</p>
<div align="center"> 
    
_Figure 13: Rounding off to two decimal places_
</div>
<br>

4. The highest value in column L (B1), the second highest value in column M (B2), and the third highest value in column N (B3) are retrieved using the formulas as shown below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/B1.png" width=300>
</p>
<div align="center">  
    
_Figure 14: Formula for column B1_
</div>
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/B2.png" width=300>
</p>
<div align="center">  
    
_Figure 15: Formula for column B2_
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/B3.png" width=300>
</p>
<div align="center"> 
    
_Figure 16: Formula for column B3_ 
</div>

5. Repeat step 2 & 3 to get all the values in two decimal places.

6. The formula below calculates the percentage value for the data in column O (TM).
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/TM.png" width=300>
</p>
<div align="center">  
    
_Figure 17: Formula for column TM_
    
</div>

7. Repeat step 2 & 3 to get all the values in two decimal places.
   
8. Use the value retrieved from the column TM to get values in the column P (Percent) by inserting the following formulas.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/percent.png" width=300>
</p>
<div align="center">  
    
_Figure 18: Formula for column Percent_
</div>
<br>

10. Repeat step 2 & 3 to get all the values in two decimal places.
    
11. To assign grades according to the respective marks, the usage of the formula is as below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/grade.png" width=1000>
</p>
<div align="center">  
    
_Figure 19: Formula for column Grade_
</div>

12. Repeat step 2 to get the remaining values.

13. To determine whether each Id_no has passed the examination, the following formula is used.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/status.png" width=400>
</p>
<div align="center">  
    
_Figure 20: Formula to determine the status **"Pass"** or **"Fail"**_ 
</div>
<br>

14. Repeat step 2 to get the remaining values.

15. Hold the _Shift_ key and click a few rows which then filling in all the row number that need to be highlighted under the name box and then choose the _**red**_ colour as the font colour.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/red.png" width=650>
</p>
<div align="center">  
    
_Figure 21: Selecting **red** colour font_

</div>
<br>

16. Click **"Formatting" > "Conditional Formatting"** and select the conditional format rules that colour the cells with value **greater than or equal to 65** to denote the passing status. Click **"Done"** to enable the filling of the cells with the defined conditional format rules.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/conditional.png" width=200>
</p>
<div align="center"> 
    
_Figure 22: "**Formatting">"Conditional Formatting**"_ 
    
</div> 
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/green.png" width=400>
</p>
<div align="center">
    
_Figure 23: **Green** colour filled cells with value **greater than or equal to 65**_ 
</div> 
<br>

17. Click the column letter R (Status) and then right click to create a filter to filter rows with status of **"Pass"** only.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/createafilter.png" width=100 length=100>
</p>
<div align="center">
    
_Figure 20: Create a filter_
</div>  
<br><br>

18. Filter the rows with status **"Pass"** only
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pass.png" width=200 length=150>
</p>
<div align="center"> 
    
_Figure 24: Filtering requirement_
</div>  
<br>

20. Colour all the cells with the status of **"Pass"** with **_light red_** by holding the _Shift_ key to select the first cells until the last cells.
    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/highlight1.png" width=500>
</p>
<div align="center"> 

_Figure 25a: Selecting the cells with records of status **"Pass"** to fill with **light red**_
</div>  
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/highlight2.png" width=500>
</p>
<div align="center"> 

_Figure 25b: Selecting the remaining cells with records of status **"Pass"** to fill with **light red**_
</div>  
<br>

21. After that, right clicking the column to remove the filter. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/removefilter.png" width=100>
</p>
<div align="center"> 

_Figure 26: Select **"Remove filter"**_
</div>  
<br>      

22. The dataset will be as the following figure.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/dataset.png" width=800>
</p>
<div align="center"> 

_Figure 27: Dataset1_
</div>  
<br>   

## Dashboard <a name = "dashboard"></a>
1. Select all the columns and press **"Insert" > "Pivot Table"**. Check **"New sheet"** to create the dashboard in another sheet and click **"Create"**.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pppivot.png" width=350>
</p>
<div align="center"> 

_Figure 28: **"Insert" > "Pivot Table"**_
</div>  
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivottable.png" width=300>
</p>
<div align="center"> 
    
_Figure 29: Creating **"Pivot Table"** requirement_
</div>  
<br>

2. Rename the newly created sheet as **"Dashboard"** by right clicking the worksheet and click **"Rename"**.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/rename.png" width=300>
</p>
<div align="center"> 
    
_Figure 30: Rename the sheet as **"Dashboard"**_
</div>  
<br> 

3. Drag the **"Percent"** to be placed under the **"Values"** and select summarization by **"MIN"** and **"Show as"** remain **"Default"**.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivoteditor.png" width=200>
</p>
<div align="center">

_Figure 31: Placing of **"Percent"** under the **"Values"** in the **"Pivot table editor"** pane_
</div>  
<br>     

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/min.png" width=200>
</p>
<div align="center">
    
_Figure 32: Select summarization by **"MIN"** Percent_
</div>  
<br> 

4. Select **"Insert">"Pivot Table"** but this time, check **"Existing sheet"** which is **"Dashboard"**.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivot2.png" width=200>
</p>
<div align="center"> 
    
_Figure 33: Check **"Existing sheet"** in the **"Create pivot table"**_
</div>  
<br> 

5. Click **"Edit"** located on the end of left side of the table. Repeat step 3 but select summarization by **"MAX"** instead.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/edit.png" width=150>
</p>
<div align="center">
    
_Figure 34: Click **"Edit"**_
</div>  
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/max.png" width=200>
</p>
<div align="center"> 
    
_Figure 35: Pivot table setup representing **MAX** Percent_
</div>  
<br> 

7. Repeat step 4 & 5 to get another pivot table of **"AVERAGE"**
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/avg.png" width=200>
</p>
<div align="center">
    
_Figure 36: Pivot table setup representing **AVERAGE** Percent_
</div>  
<br>   

8. Click **"Edit"** located on the end of left side of the table. Repeat step 4. Drag **"Grade"** to the **"Rows"** and **"Values"** box to get a summarized table categorized by grade. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/table.png" width=200>
</p>
<div align="center">
    
_Figure 37: Pivot table setup representing **COUNT of Grade**_
</div>  
<br> 

9. Click **"Edit"** located on the end of left side of the table. Repeat step 4. Drag **"Status"** to the **"Rows"** and **"Values"** box to get a summarized table categorized by status. 
 
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/statustable.png" width=200>
</p>
<div align="center">
    
_Figure 38: Pivot table setup representing **COUNT of Status**_
</div>  
<br> 

10. The created pivot tables will be as follows.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivot.png" width=250>
</p>
<div align="center">
    
_Figure 39: Pivot Tables_
</div>  
<br>     

11. To create a scorecard, select **"Insert" > "Chart"**. Then, under **"Setup"** in the **"Chart Editor"**, select **"Scorecard chart"** located under **"Other"** category.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/scorecard.png" width=500>
</p>
<div align="center">
    
_Figure 40: Selection of **"Scorecard chart"**_
</div>  
<br>  

12. Select appropriate data range in the **"Dashboard"** that is the data range of the created pivot table and select **"OK"**.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/datarange.png" width=200>
</p>
<div align="center">
    
_Figure 41: Data range_
</div>  
<br> 

13. Perform customization for the scorecard like putting the title for the scorecard, selecting the font size and colour.
    
14. Repeat step 11-13 to create scorecard representing **"Max percent scorecard"**.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/maxscore.png" width=200>
</p>
<div align="center">

_Figure 42: Max percent scorecard setup_
</div>  
<br>    

15. Repeat step 11-13 to create scorecard representing **"Avg percent scorecard"**.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/avgscore.png" width=200>
</p>
<div align="center">
    
_Figure 43: Avg percent scorecard setup_
</div>  
<br>  

16. Repeat step 11 but instead of selecting the scorecard, select **"Column chart"** under **"Column"** category. Repeat step 12 get the data range.
  <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/column_chart.png" width=200>
</p>
<div align="center">
    
_Figure 44: Selection of **"Column chart"**_ 
</div>  
<br>

 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/columnchart.png" width=200>
</p>
<div align="center">
    
_Figure 45: Column chart setup_
</div>  
<br>

17. Perform customization for the column chart.

18. Repeat step 11 but instead of selecting the scorecard, select **"Table chart"** under **"Other"** category. Repeat step 12 get the data range.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/table_chart.png" width=200>
</p>
<div align="center">
    
_Figure 46: Selection of **"Table chart"**_
</div>  
<br>

 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/tablechart.png" width=200>
</p>
<div align="center">
    
_Figure 47: Table chart setup_
</div>  
<br>

19. Repeat step 11 but instead of selecting the scorecard, select **"Doughnut chart"** under **"Other"** category. Repeat step 12 get the data range.
  <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/doughnut_chart.png" width=200>
</p>
<div align="center">
    
_Figure 48: Selection of **"Doughnut chart"**_
</div>  
<br>

 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/doughnut.png" width=200>
</p>
<div align="center">
    
_Figure 49: Doughnut chart setup_
</div>  
<br>

20. Repeat step 11-13 to create total record scorecard, pass rate scorecard and fail rate scorecard.
<p align="center">
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/totalrecord.png" width="200">
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/maxpass.png" width="200">
    
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/minpass.png" width="200">
</p>
<div align="center">
    
_Figure 50: Total record scorecard, Pass rate scorecard and Fail rate scorecard setup_
</div>  
<br>

21. We create another scorecard chart to show the actual number of records.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/scorerecorde2.png" width=200>
</p>
<div align="center">
    
_Figure 51: Scorecards with the actual record for Pass and Fail Scorecards_
</div>  
<br>

22. Perform setup and customization for the Scorecard chart.
     <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/scorerecord.png" width=200>
</p>
<div align="center">
    
_Figure 52: Setup of the Scorecard_
</div>  
<br>

 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/scorecust.png" width=200>
</p>
<div align="center">
    
_Figure 53: Customization of the Scorecard_
</div>  
<br>

23. The dashboard as is in the image below is created.
 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/dashboard.png" width=800>
</p>
<div align="center">
    
_Figure 51: Dashboard_
</div>  
<br>

## Contribution 🛠️ <a name = "contribution"></a>
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


