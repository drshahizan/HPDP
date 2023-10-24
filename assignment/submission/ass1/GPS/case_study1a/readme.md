<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: GPS (GroupPalingSolid)
### Group Members

| Name                                     | Matrix Number | Photo |
| :---------------------------------------- | :-------------: | ------------- |
| MUHAMMAD FARHAN BIN IBRAHIM | A21EC0072   |      |
| FONG KHAH KHEH              | A21EC0026   |      |	
| LING WAN YIN                | A21EC0047   |      |	
| SARAH WARDINA BINTI RAFIDIN | A21EC0128   |      |

## Table of Contents
+ [Dataset Information](#dataset_info)
+ [Data Import and Data Preprocessing](#preprocessing)
+ [Data Processing](#processing)
+ [Dashboard](#dashboard)

## Dataset Information <a name = "dataset_info"></a>
This dataset contains the attributes of Id_No, Academic,	Sports,	Co-Curriculum,	Test_1 and	Test_2. 

**Source**: https://docs.google.com/spreadsheets/d/1uSaVrYlYKFgK8fy_vs9hr13n1iBJq14A0JnEcstmDrI/edit#gid=1756902967 

## Data Import and Data Preprocessing <a name = "preprocessing"></a>
1. Press "File" > "Import" to upload the “Dataset1.txt” that has been downloaded earlier by clicking “Browse” to find the directory of the file.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/96f95fff-a9e4-4864-a031-bf3dc30c80ad">
</p>

<div align="center">
  
Figure 1: "File" > "Import" 
</div>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/browse.png" width=500>
</p>

<div align="center">
  
Figure 2: Click "Browse" unfder the "Upload" bar
</div>

2. Select the "Dataset1.txt" and then press "OK".

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/file%20selection.png" width=500>
</p>

<div align="center">
  
Figure 3: File selection

</div>

3. Wait until it loads finish. It may takes a few seconds to load the dataset file into the Google Sheet. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/waiting.png" width=400>
</p>

<div align="center">
  
Figure 4: Loading

</div>

4. Make sure the selected file to be loaded into Google Sheet is correct. Then, check the following details and press "Import Data".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/details.png" width=400>
</p>

<div align="center">
  
Figure 5: Importing data

</div> 

5. To ensure each record has two decimal places, click every column letter and select "123" under the toolbar. Click "Numbers".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/roundoff.png" width=500>
</p>

<div align="center">
  
Figure 6: Click "Numbers"

</div>

## Data Processing <a name = "processing"></a>
1. To get the value for the new column name "P1", "P2", "P3", "P4" and "P5", the insertion of the formulas are as follows.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P1.png" width=300>
</p>

<div align="center">  
Figure 7: Column P1 
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P2.png" width=300>
</p>
<div align="center">  
Figure 8: Column P2 
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P3.png" width=300>
</p>
<div align="center">  
Figure 9: Column P3 
</div>   
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/P4.png" width=300>
</p>
<div align="center">  
Figure 10: Column P4 
</div>
<br>

2. Double-click the **"+"** shape in the bottom right corner of the data in each column to retrieve data until the last row in each column.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/+.png" width=500>
</p>
<div align="center">  
Figure 11: Data retrieval until last row
</div>
<br>
3. Click every column letter and then select "123" > "Numbers".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/two.png" width=500>
</p>
<div align="center">  
Figure 12: Rounding off to two decimal places
</div>
<br>
4. The highest value in column L (B1), the second highest value in column M (B2), and the third highest value in column N (B3) are retrieved using the formulas as shown below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/B1.png" width=400>
</p>
<div align="center">  
Figure 13: Formula for column B1 
</div>
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/B2.png" width=400>
</p>
<div align="center">  
Figure 14: Formula for column B2
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/B3.png" width=400>
</p>
<div align="center">  
Figure 15: Formula for column B3 
</div>

5. Repeat step 2 & 3.

6. The formula below calculates the percentage value for the data in column O (TM).
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/TM.png" width=400>
</p>
<div align="center">  
Figure 16: Formula for column TM 
</div>

7. Repeat step 2 & 3.
   
8. Use the value retrieved from the column TM to get the marks percentage by inserting formula as shown.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/percent.png" width=400>
</p>
<div align="center">  
Figure 16: Formula for column Percent
</div>
<br>

10. Repeat step 2 & 3.
    
11. To assign grades according to the respective marks, the usage of the formula is as below
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/grade.png" width=1000>
</p>
<div align="center">  
Figure 16: Formula for column Grade 
</div>

12. Repeat step 2 to get the remaining values.

13. To determine whether each Id_no has passed the examination, the following formula is used.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/status.png" width=400>
</p>
<div align="center">  
Figure 16: Formula to determine the status 
</div>
<br>
14. Repeat step 2 to get the remaining values.
15. Hold the Shift key and click a few rows which then filling in all the row number that need to be highlighted under the name box and then choose the red colour as the font colour.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/red.png" width=400>
</p>
<div align="center">  
Figure 17: Red colour font  
</div>
<br>
16. Click "Formatting">"Conditional Formatting" and select the conditional format rules that colour the cells with value greater or equal to than 65 to denote the passing percent.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/conditional.png" width=200>
</p>
<div align="center"> Figure 18: "Formatting">"Conditional Formatting"   
</div> 
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/green.png" width=400>
</p>
<div align="center"> Figure 19: Green colour filled cells with value greater or equal to 65 
</div> 
<br>
17. Click the column letter R (Status) and then right click to create a filter to filter rows with "Pass" only.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/createafilter.png" width=100 length=100>
</p>
<div align="center"> Figure 20: Create a filter
</div>  
<br><br>
18. Filter the rows with status "Pass" only
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pass.png" width=200 length=150>
</p>
<div align="center"> Figure 21: Filtering requirement
</div>  
<br>

20. Colour all the column with the status of "Pass" with light red by holding the shift key to select until the last rows.
    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/highlight1.png" width=500>
</p>
<div align="center"> Figure 22a: Colour the whole records with rows of status "Pass"
</div>  
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/highlight2.png" width=500>
</p>
<div align="center"> Figure 22b: Colour the whole records with rows of status "Pass"
</div>  
<br>

21. After that, remove the filter.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/removefilter.png" width=100>
</p>
<div align="center"> Figure 23: Remove filter
</div>  
<br>      

## Dashboard <a name = "dashboard"></a>
1. Select all the columns and press "Insert">"Pivot Table". Check "New sheet" to create the dashboard in another sheet and press "Create"
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivot.png" width=500>
</p>
<div align="center"> Figure 24: "Insert">"Pivot Table"
</div>  
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivottable.png" width=200>
</p>
<div align="center"> Figure 25: Creating "Pivot Table" requirement
</div>  
<br>

2. Rename the newly created sheet as "Dashboard" by right clicking the worksheet and click "Rename".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/rename.png" width=200>
</p>
<div align="center"> Figure 26: Rename the sheet as "Dashboard"
</div>  
<br> 

3. Drag the Percent to be placed under the Values and select summarization by "MIN" and "Show as" remain "DEFAULT".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivoteditor.png" width=200>
</p>
<div align="center">Figure 27: Placing of Percent under the Vales in the Pivot Table Editor
</div>  
<br>     

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/min.png" width=200>
</p>
<div align="center">Figure 28: MIN Percent
</div>  
<br> 

4. Select "Insert">"Pivot Table" but this time, check "Existing sheet" which is "Dashboard".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/pivot2.png" width=200>
</p>
<div align="center"> Figure 29: Rename the sheet as "Dashboard"
</div>  
<br> 

5. Repeat step 3 but select summarization by "MAX" instead.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/max.png" width=200>
</p>
<div align="center"> Figure 30: MAX Percent
</div>  
<br> 

7. Repeat step 4 & 5 to get another pivot table of "AVERAGE"
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/avg.png" width=200>
</p>
<div align="center">Figure 31: AVERAGE Percent
</div>  
<br>   

8. Repeat step 4. Drag "Grade" to the "Rows" and "Values" box. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/GPS/case_study1a/table.png" width=500>
</p>
<div align="center">Figure 32: COUNT of Grade
</div>  
<br> 

9. Repeat step 4.
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


