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
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/1.png">
</p>

<div align="center">
  
Figure 1: To import Dataset
</div>

2. Select on the 'Upload' and click on 'Browse.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/2.png" width=400>
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

1. The following formulas are inserted to obtain the value for the new column names 'P1', 'P2', 'P3', 'P4', and 'P5'.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/6.png" width=300>
</p>

<div align="center">  
Figure 7: By adding the formula shown in the image above, you may get a new value for all the data in the Academic column to the "Test_2" column, which is named P1 under the G column. After that, click on column G2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/7.png" width=300>
</p>
<div align="center">  
Figure 8: As for the column ‘Sports’, which is named P2 under the H column, with the formula shown in the image below. After that, click on column H2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/8.png" width=300>
</p>
<div align="center">  
Figure 9: As for the column ‘Co-curriculum’, which is named P3 under the I column, with the formula shown in the image below. After that, click on column I2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
</div>   
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/9.png" width=300>
</p>
<div align="center">  
Figure 10: As for the column ‘Test_1’, which is named P4 under the J column, with the formula shown in the image below. After that, click on column J2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
</div>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/10.png" width=300>
</p>
<div align="center">  
Figure 11: As for the column ‘Sports’, which is named P5 under the H column, with the formula shown in the image below. After that, click on column H2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
</div>
<br>

<be>

3. Round off every new column by clicking on the Format ribbon, then choose 'Number'".
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submissionass1/ganthegang/case_study1a/11.png" width=500>
</p>
<div align="center">  
Figure 12: Rounding off to two decimal places
</div>
<br>

4. Next, get the top three highest values from the column P1 to P5 column. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/12.png" width=400>
</p>
<div align="center">  
Figure 13: For the highest values for column H1, use the formula as shown. After that, click on column L1, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
</div>
<br>
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/13.png" width=400>
</p>
<div align="center">  
Figure 14: For the second-highest value for H2, use the formula above. After that, click on column M2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the 
</div>
<br>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/14.png" width=400>
</p>
<div align="center">  
For the second-highest value for H3, use the formula above. After that, click on column N2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
</div>

5. To get the total values for the top three highest values, use the formula as shown below. Click on column O2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
   <p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/15.png" width=400>
</p>
<div align="center">  
Figure 16: Calculate Total Value For The Top Three Highest Value
 
</div> 

6. To calculate the percentage, use the formula shown below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/16.png" width=400>
</p>
<div align="center">  
Figure 16: To Calculate the percentage
</div>

7. The formula is used as follows to determine grades based on the respective marks.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/17.png" width=400>
</p>
<div align="center">  
Figure 16: Formula To determine grades.
</div>
<br>

8. To determine whether each ID passes or fails, we need to use the formula below. After that, click on column P2, press Ctrl+C and press Ctrl+space, then Ctrl+V to fill the value of the columns to the last row.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/18.png" width=400>
</p>
<div align="center">  
Figure 16: Formula To Determine Status
</div>
<br>

 
9. For each ID, if the status is Pass, the column P will be filled with green, while Fail will be filled with red. Click on the ribbon Format, choose ‘Conditional Formatting’ and click on ‘New Rule’.  
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/ganthegang/case_study1a/19.png" width=400>
</p>
<div align="center">  
Figure 16: Formula for column Percent
</div>
<br>


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


