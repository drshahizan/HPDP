<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: GanTheGang

### Group Members

| Name                                     | Matrix Number | Photo |
| :---------------------------------------- | :-------------: | ------------- |
| ALIEYA ZAWANIE BINTI A ZAINI | A21EC0156   |      |
| YEW RUI XIANG               | A21EC0149   |      |	
| WAN AMIRUL HAFIQ BIN WAN HUZAINI      | A21EC0141   |      |	
| ABDUL MUHAIMIN BIN ABDUL RAZAK | A21EC0002   |      |

## Table of Contents
+ [Dataset Information](#dataset_info)
+ [Data Import and Data Preprocessing](#preprocessing)
+ [Data Processing](#processing)
+ [Dashboard](#dashboard)
  
## Dataset Information <a name = "dataset_info"></a>
This dataset is called dataset1.txt. This dataset has five columns that contain information about Id_No, Academic, Sports, Co-Curriculum, Test_1 and Test_2. Table 1 shows the full marks for the data

**Source**: https://docs.google.com/spreadsheets/d/1uIP38OoPoM2d_JJCayWT4M7lAA1ZmoMy_7NHFh4sX0g/edit#gid=54841748

## Data Import and Data Preprocessing <a name = "preprocessing"></a>
1. In the ribbon 'File', click on "Import" to upload the “Dataset1.txt”.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/1.png" width=300>
</p>

<div align="center">
  
Figure 1: To import Dataset
</div>

2. Select on the 'Upload' and click on 'Browse.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/2.png" width=300>
</p>

<div align="center">
  
Figure 2: Browse To Import The Dataset

</div>


3. Select the 'Dataset1.txt' and then press 'OK'.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/3.png" width=400>
</p>

<div align="center">
  
Figure 3: Select The Dataset

</div>

4. After the file has been loaded into Google Sheets, click on 'Import Data'. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/4.png" width=400>
</p>

<div align="center">
  
Figure 4: Import Dataset

</div>

5. Press To select all the data in the Academic column at once and move it to the Test_2 column, use Ctrl + Shift  and select Academic, Sports, Co-Curriculum, Test 1 and Test 2.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/5.png" width=300>
</p>

<div align="center">
  
Figure 5: Selecting The Data

</div>

## Data Processing <a name = "processing"></a>

1. The following formulas are inserted to obtain the value for the new column names 'P1', 'P2', 'P3', 'P4', and 'P5'. For every column, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/6.png" width=300>
</p>

<div align="center">  
Figure 7: By adding the formula shown in the image above, you may get a new value for all the data in the Academic column to the "Test_2" column, which is named P1 under the G column.
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/7.png" width=300>
</p>
<div align="center">  
Figure 8: As for the column ‘Sports’, which is named P2 under the H column, with the formula shown in the image above.
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/8.png" width=300>
</p>
<div align="center">  
Figure 9: As for the column ‘Co-curriculum’, which is named P3 under the I column, with the formula shown in the image above.
</div>   
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/9.png" width=300>
</p>
<div align="center">  
Figure 10: As for the column ‘Test_1’, which is named P4 under the J column, with the formula shown in the image above.
</div>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/10.png" width=300>
</p>
<div align="center">  
Figure 11: As for the column ‘Sports’, which is named P5 under the H column, with the formula shown in the image above. 
</div>
<br>


3. Round off every new column by clicking on the Format ribbon, then choose 'Number'".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/11.png" width=500>
</p>
<div align="center">  
Figure 12: Rounding off to two decimal places
</div>
<br>

4. Next, get the top three highest values from the column P1 to P5 column. For each column, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/12.png" width=400>
</p>
<div align="center">  
Figure 13: For the highest values for column H1, use the formula as shown. 
</div>
<be>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/13.png" width=400>
</p>
<div align="center">  
Figure 14: For the second-highest value for H2, use the formula above. 
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/14.png" width=400>
</p>
<div align="center">  
Figure 15: For the third-highest value for H3, use the formula above.
</div>
<br>

5. To get the total values for the top three highest values, use the formula as shown below. Click on column O2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/15.png" width=400>
</p>
<div align="center">  
Figure 16: Calculate Total Value For The Top Three Highest Value
</div>
<br>

6. To calculate the percentage, use the formula shown below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/16.png" width=400>
</p>
<div align="center">  
Figure 17: To Calculate the percentage
</div>
<br>

7. The formula is used as follows to determine grades based on the respective marks.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/17.png" width=400>
</p>
<div align="center">  
Figure 18: Formula To determine grades.
</div>
<br>

8. To determine whether each ID passes or fails, we need to use the formula below. After that, click on column P2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/18.png" width=400>
</p>
<div align="center">  
Figure 19: Formula To Determine Status
</div>
<br>

 
9. If the status is Pass for each ID, column P will be filled with green data, and if the status is Fail, it will be filled with red data. Hold down the shift key as you click on H1, H2, and H3, fill in all the row numbers that need to be highlighted beneath the name box, and then select the red font colour. 
<p align="center">
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/22.png" width=300>
</p>
<div align="center">  
Figure 20: The Red Font
</div>
<be>

15. Click on 'Format', choose 'Conditional Formatting' and follow the steps below.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/20.png" width=250>
</p>
<div align="center">  
Figure 20:  Percentage greater than 65 will be coloured in Green
  
</div>
<br>

16. Select column 'Status, and press right-click to create a filter to filter "Pass" only.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission//ass1/ganthegang/case_study1a/23.png" width=200>
</p>
<div align="center"> 
Figure 21: Pass Filtering
    
</div> 
<br>

17. By pressing and holding the "Shift" key while selecting all the rows, colour all the columns with the status "Pass" with a light red.
    <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/26.png" width=500>
</p>
<div align="center"> 
Figure 22: Colour the whole record with rows of status 'Pass' with the light red font.
</div>  
<br>
<p align="center">
  
18. Remove the filter.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/25.png" width=200>
</p>
<div align="center"> 
Figure 23: Removing the filter
</div>  
<br>      

## Dashboard <a name = "dashboard"></a>
1. Select all the columns and press **"Insert">"Pivot Table"**. Check **"New sheet"** to create the dashboard in another sheet and press **"Create"**


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


