<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

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

## Data Preprocessing <a name = "dataset_preprocessing"></a>
1. Select the range of cells that contain data need to be convert to 2 decimal places and click on the **"Format"**, and select **"Number"**.
<p align="center"><img align="center" alt="Coding" width="400" src="rounddecimal.png"></p> 
<p align="center"> <em> Figure 2: Convert the data to 2 decimal places </em> </p> 

2. The data values was displayed in two decimal places.
<p align="center"><img align="center" alt="Table" width="400" src="rounddecimaldone.png"></p>
<p align="center"> <em> Figure 3: The data converted to 2 decimal places </em> </p> 


## Data Processing <a name = "processing"></a>


1. Formula (Column Number/61)*3.33 was used in order to calculate the value for P1. P1 represents the score for academic.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic4.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 4: The (Column Number/61)*3.33 was used in order to obtain the value for column P1
</div>
<br>

2. Formula (Column Number/10)*3.33 was used in order to calculate the value for P2. P2 represents Sport's score.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic5.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 5: The (Column Number/10)*3.33 was used in order to obtain the value for column P2
</div>
<br>

3. Formula (Column Number/15)*3.33 was used in order to calculate the value for P3. P3 represents Co-Curriculum score.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic6.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 6: The (Column Number/15)*3.33 was used in order to obtain the value for column P3
</div>
<br>

4. Formula (Column Number/10)*3.33 was used in order to calculate the value for P4. P4 represents Test 1 mark.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic7.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 7: The (Column Number/10)*3.33 was used in order to obtain the value for column P4
</div>
<br>

5. Formula (Column Number/10)*3.33 was used in order to calculate the value for P5. P5 represents Test 2 mark.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic8.jpg" width=300 length=300 >
</p>

<div align="center">  
Figure 8: The (Column Number/10)*3.33 was used in order to obtain the value for column P5
</div>
<br>

6. Every new column has be rounded off by selecting 'Number' from the Format ribbon."
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic9.jpg" width=500>
</p>
<div align="center">  
Figure 9: Rounding off to two decimal places
</div>
<br>

7. Next, determine which three numbers in columns P1 through P5 are the highest. To fill the value of the columns to the last row, use Ctrl+C, Ctrl+space, and Ctrl+V for each column. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic10.jpg" width=400>
</p>
<div align="center">  
Figure 10: For the highest values for column P1, use the formula as shown. 
</div>
<br>

8. Top 3 values from column P1-P5 are selected.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic11.jpg" width=400>
</p>
<div align="center">  
Figure 11: For the highest values for column P1, use the formula as shown. 
</div>
<br>

9. Calculate the total for the three highest values by using the formula SUM(L2:N2).
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic12.jpg" width=400>
</p>
<div align="center">  
Figure 12: Formula to calculate total marks. 
</div>
<br>

10. Change the total marks to percentage by using (O2/10*100) formula.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic13.jpg" width=400>
</p>
<div align="center">  
Figure 13: Formula to calculate total marks. 
</div>
<br>

11. Determine the grade for the students by using the formula shown below.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic14.jpg" width=400>
</p>
<div align="center">  
Figure 14: Formula to determine students' grade. 
</div>
<br>

12. Determine either the students passed or failed the examination. The red rows indicate the students have successfully passed the exam meanwhile the not coloured rows indicate the students failed.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic15.jpg" width=400>
</p>
<div align="center">  
Figure 15: Formula to determine the students passed or failed. 
</div>
<br>

## Dashboard <a name = "processing"></a>

1. Determine the min for student's examination result
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic17.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic18.jpg" width=400>
</p>
<div align="center">  
Figure 16: Min mark for student's examination results. 
</div>
<br>

2. Determine the max for student's examination result
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic19.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic20.jpg" width=400>
</p>
<div align="center">  
Figure 17: Max mark for student's examination results. 
</div>
<br>

3. Determine the average for student's examination result
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic21.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic22.jpg" width=400>
</p>
<div align="center">  
Figure 18: Average mark for student's examination results. 
</div>
<br>

4. Create a column chart to analyse the number of students getting grade A+ to E. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic23.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic24.jpg" width=400>
</p>
<div align="center">  
Figure 19: Chart for students' grades. 
</div>
<br>

5. Calculate the number of students for each grade by using formula shown below. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic25.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic26.jpg" width=400>
</p>
<div align="center">  
Figure 20: Students' grade Table. 
</div>
<br>

6. Create a doughnut table to illustrate number of students who passed and failed. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic27.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic28.jpg" width=400>
</p>
<div align="center">  
Figure 21: Students' grade doughnut chart. 
</div>
<br>

7. Create a scorecard chart to calculate total amount of students/records. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic29.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic30.jpg" width=400>
</p>
<div align="center">  
Figure 22: Scorecard chart shows number of records/students. 
</div>
<br>

8. Create a scorecard chart to calculate total amount of students who passed the exam. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic31.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic32.jpg" width=400>
</p>
<div align="center">  
Figure 23: Scorecard chart shows number of students passed. 
</div>
<br>

9. Create a scorecard chart to calculate total amount of students who failed the exam. 
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic33.jpg" width=400>
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic34.jpg" width=400>
</p>
<div align="center">  
Figure 24: Scorecard chart shows number of students failed. 
</div>
<br>




10. finalise dashboard for examination results.
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1a/datasetpic16.jpg" width=400>
</p>
<div align="center">  
Figure 25: Examiniation result dashboard. 
</div>
<br>






## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


