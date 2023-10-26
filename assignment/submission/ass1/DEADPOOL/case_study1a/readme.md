<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: DEADPOOL
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | ------------- |
| UMAR HAZIQ BIN MUHAMAD NORHISHAM            | A21EC0235     |  DATA PREPROCESSING DASHBOARD ASM1  |
| SAM CHIA YUN              | A21EC0127     | DATA TRANSFORMATION     |
| MUHAMMAD IZZUDDIN BIN SHABRIN             | A21EC0083     |   VISUALIZATION   |
| KEE SHIN PEARL             | A21EC0190     | DOCUMENTATION     |

## Dataset Information <a name = "dataset_info"></a>
This dataset describes exam outcomes, allowing us to determine if students passed or failed. There are five factors that go into determining a student's grade: co-curriculum, athletics, academics, tests 1 and 2

**Deadpool Google Sheet**: https://docs.google.com/spreadsheets/d/1-a6XEi_X0BPA2ugBbEKP3aqwfWSL5TKOPjdZvjvMh68/edit#gid=1538304567

## Data Import  <a name = "importing data"></a>
1. Download and import dataset1 to google sheet.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/dataset%20pic1.png" width=300>
</p>

<div align="center">
  
Figure 1: Import Dataset to Google Sheet
</div>

## Data Processing <a name = "processing"></a>


1. Formula (Column Number/61)*3.33 was used in order to calculate the value for P1. P1 represents the score for academic.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic4.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 2: The (Column Number/61)*3.33 was used in order to obtain the value for column P1
</div>
<br>

2. Formula (Column Number/10)*3.33 was used in order to calculate the value for P2. P2 represents Sport's score.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic5.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 3: The (Column Number/10)*3.33 was used in order to obtain the value for column P2
</div>
<br>

3. Formula (Column Number/15)*3.33 was used in order to calculate the value for P3. P3 represents Co-Curriculum score.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic6.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 4: The (Column Number/15)*3.33 was used in order to obtain the value for column P3
</div>
<br>

4. Formula (Column Number/10)*3.33 was used in order to calculate the value for P4. P4 represents Test 1 mark.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic7.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 5: The (Column Number/10)*3.33 was used in order to obtain the value for column P4
</div>
<br>

5. Formula (Column Number/10)*3.33 was used in order to calculate the value for P5. P5 represents Test 2 mark.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic8.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 6: The (Column Number/10)*3.33 was used in order to obtain the value for column P5
</div>
<br>

6. Every new column has be rounded off by selecting 'Number' from the Format ribbon."
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic9.jpg" width=500>
</p>
<div align="center">  
Figure 7: Rounding off to two decimal places
</div>
<br>

7. Next, determine which three numbers in columns P1 through P5 are the highest. To fill the value of the columns to the last row, use Ctrl+C, Ctrl+space, and Ctrl+V for each column. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic10.jpg" width=400>
</p>
<div align="center">  
Figure 8: For the highest values for column P1, use the formula as shown. 
</div>
<be>

8. Top 3 values from column P1-P5 are selected.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic11.jpg" width=400>
</p>
<div align="center">  
Figure 9: For the highest values for column P1, use the formula as shown. 
</div>
<be>

9. Calculate the total for the three highest values by using the formula SUM(L2:N2).
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic12.jpg" width=400>
</p>
<div align="center">  
Figure 10: Formula to calculate total marks. 
</div>
<be>





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


