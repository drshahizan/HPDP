<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: KHUCHIN

## Table of Contents
- [Introduction](#ntroduction)
- [Data preprocessing](#data-preprocessing)
  - [Import dataset to Google Sheets](#import-dataset-to-Google-Sheets)
  - [Remove redundant data](#import-dataset-to-Google-Sheets)
  - [Changing decimal places](#changing-decimal-places)
  - [Creating Column](#creating-column)
  - [Three Highest Value](#three-highest-value)
  - [Total Marks](#total-marks)
  - [Calculating Percentage](#calculating-percentage)
  - [Creating Grade and Status (Pass or Fail)](#creating-grade-and-status-pass-or-fail)
  - [Total Marks](#total-marks)
  - [Highlighting Pass students](#highlighting-pass-students)
- [Dashboard creation](#dashboard-creation)
  - [Scorecard Chart](#scorecard-chart)
  - [Calculation of Minimum, Maximum, and Average](#calculation-of-minimum-maximum-and-average)
  - [Grading chart](#grading-chart)
  - [Creating Total Record, Pass and Fail](#creating-total-record-pass-and-fail)
  - [Pie Chart for Pass and Fail](#pie-chart-for-pass-and-fail)
  - [Dashboard Creation](#dashboard-creation)
- [Analysis of the dataset](#analysis-of-the-dataset)


## Introduction

Google Sheets is a spreadsheet tool that is part of Google's free, web-based Google Docs Editors suite. Google Sheets is accessible as a web app, a mobile app for Android and iOS, and a desktop app for Google's ChromeOS. The software supports Microsoft Excel file formats. Many people, organizations, and corporations use Google Sheets as it provides many variety of features that Google Sheets has capabilities to make many kinds of data management and analytical jobs. Users can use the application to create and edit files online while interacting with other users in real-time. Edits are documented by the user who made them, as well as a revision history. 

One dataset has been chosen for data analysis based on the case study that was given which is the Examination Result dataset. The dataset contains six columns which are Id_no, Academic, Sports, Co-Curriculum, Test_1, and Test_2. By doing this case study, we will show how to make data analysis based on the dataset that has been given based on the case study to turn it from raw data to valuable data.

## Data preprocessing

### Import dataset to Google Sheets
1. Import the dataset (Dataset1.txt) to Google Sheets (https://docs.google.com/spreadsheets/d/1q5UVmeU4xmzsocV9yqeHlnukuoOLkBJZTEqH96sb3oc/edit?usp=sharing) by clicking File on the upper left corner tab and select Import.
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/DP1.png" alt="Image description">
</div>

### Remove redundant data
2. Remove redundant data in the Google Sheet by selecting the redundant data and use the keyboard shortcut ctrl+shift+del

### Changing decimal places
3. Since we want our dataset to be two decimal places, we will use the decrease decimal places tab on the upper Google Sheet tab.
4. Click the  decrease decimal places tab until we get two decimal places
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/DP2.png" alt="Image description">
</div>


### Creating Column
5. Creating a new column P1 to P5 based on the guide below:
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/118237589/930d3b47-d949-4e3e-b009-d7a1d859e3de" alt="Image description">
</div>

6. The new column (P1-P5) must be calculated for each column based on the marks for each categories (refer table below). For example column P1 is taken from column B. All the marks received by students must be divided by the max mark (from the table below) and multiply by 3.33:
<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/ea1f8809-23da-4b1b-83fa-60c3ec258483">
</div>

7. The calculation for each categories are shown below:
   
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/118237589/ebb52714-55fa-43e2-9a14-4947664b7021" alt="Image 1">
  <img src="https://github.com/drshahizan/HPDP/assets/118237589/4f6e014c-52ff-4571-b71a-fc0cb91888fc" alt="Image 2">
  <img src="https://github.com/drshahizan/HPDP/assets/118237589/09d18afe-cb57-499d-b7d9-02df23d9b94c" alt="Image 3">
  <img src="https://github.com/drshahizan/HPDP/assets/118237589/38a1450e-cf9f-4225-b19e-9d6e4f8df2dd" alt="Image 4">
  <img src="https://github.com/drshahizan/HPDP/assets/118237589/31da351c-0dd5-4f82-b709-0c5627be809a" alt="Image 5">
</div>


8. The rest in the column are calculated by double-clicking on the bottom right of the cell. Refer to the picture below:

<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/118237589/ed360a0c-6810-46e1-8f6e-ae001d2b657a" alt="Image description">
</div>

### Three Highest Value

9. Get the top three highest value from the row by using simple formula as shown in the pictures below:

<div align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/118237589/0911bd5e-4a5c-4804-82bb-017498677259" alt="Image 1">
    <img src="https://github.com/drshahizan/HPDP/assets/118237589/b37210a4-d4de-426e-8326-7f65ee782056" alt="Image 2">
    <img src="https://github.com/drshahizan/HPDP/assets/118237589/769ed382-82f9-41d1-acb3-2e6c230da1f0" alt="Image 3">
  </div>

10. The rest are calculated the same way as in Step 8.

### Total Marks
11. Total marks are calculated by finding the sum value of top three highest mark from before:

<div align="center">
<img src="https://github.com/drshahizan/HPDP/assets/118237589/4f5b6c79-e1ca-4b11-8baf-5b2c7a9f2e18">
</div>

12. The rest are calculated the same way as in Step 8.

### Calculating Percentage

13. Percentage of the marks are calculated to determine the grade of students. Percentage is calculated as below:
    

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/4383a63c-8d12-46be-8b06-5b66a6d9c138">
</div>

14. As always the rest are calculated the same way as in Step 8.

### Creating Grade and Status (Pass or Fail)

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/6d68f4f9-3f51-4433-9b1e-fff413da5bc6">
</div>



15. First create a range of the score for each grade in ascending order.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/95f820d7-d24e-4a43-8a0e-dc8667f70760">
</div>

16. Then link the previous range of score using th VLOOKUP formula to automatically set the grade for each percentage.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/e13162bb-0c74-4807-92af-a298945a8288">
</div>

17. Do the same for status Pass or Fail follow step 15.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/de80c17d-b232-4c9e-9c6d-868182a93f68">
</div>

18. Follow step 16.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/905b9b10-18e9-4da0-88ab-d5b83426fa3d">
</div>

### Highlighting Pass students

19. To highlight passing students (red for the row and green for the cell) we need to use conditional formatting.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/6eef88f0-68a0-4921-a2c3-49cdfae7ef2c">
</div>


## Dashboard creation

### Scorecard Chart

1. To make a Scorecard Chart, click the Insert Chart tab on the upper Google Sheet tab.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/DC2.png">
</div>

2. After that select chart type on the right and go to others section and select Scorecard chart

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/DC3.png">
</div>

### Calculation of Minimum, Maximum, and Average

3. To calculate Minimum (Min), Maximum (Max), and Average we will use formulas that have been provided by the Google Sheet to ease our calculation. For the Min, we will use =MIN(Dataset1!P2:P111520), for the Max we will use  =MAX(Dataset1!P2:P111520) and for average we will use =AVERAGE(Dataset1!P2:P111520). The result will be shown below

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/DC1.png">
</div>

### Grading chart

4. To make a grading chart, we need to make a new table and make it in descending order based on grades from A+ to E. We will use the formula for each grade to make a calculation of how many students get for each grade. The formula are:

- A+ → =COUNTIF(Dataset1!Q2:Q111520,"A+")
- A → =COUNTIF(Dataset1!Q2:Q111520,"A")
- A- → =COUNTIF(Dataset1!Q2:Q111520,"A-")
- B+ → =COUNTIF(Dataset1!Q2:Q111520,"B+")
- B → =COUNTIF(Dataset1!Q2:Q111520,"B")
- B- → =COUNTIF(Dataset1!Q2:Q111520,"B-")
- C+ → =COUNTIF(Dataset1!Q2:Q111520,"C+")
- C → =COUNTIF(Dataset1!Q2:Q111520,"C")
- C- → =COUNTIF(Dataset1!Q2:Q111520,"C-")
- D+ → =COUNTIF(Dataset1!Q2:Q111520,"D+")
- D → =COUNTIF(Dataset1!Q2:Q111520,"D")
- D- → =COUNTIF(Dataset1!Q2:Q111520,"D-")
- E → =COUNTIF(Dataset1!Q2:Q111520,"E")

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/DC4.png">
</div>

5. To make a grading chart, click To make a Scorecard Chart, click the Insert Chart tab on the upper Google Sheet tab. Select chart type, go to column section and select column chart.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/DC5.png">
</div>

### Creating Total Record, Pass and Fail

6. Calculating total record of student is really easy. All you need is selecting all dataset as well as formula "COUNT".

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/addaaf97-1c14-4786-baa4-8ad40b1fff7d">
</div>

7. For its scorecard chart just follow the step 5. It's literally the same.
  
8. For passing and fail, remember that before this we already set the passing grade, which one is pass and which one is fail. You need to the "Status" column and just use this formula "=COUNTIF(Dataset1!R2:R111520, "PASS")" where 'R' is referring to Status column. Now change the "PASS" to "FAIL" to count the FAIL students.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/046646ba-ca10-4b96-8262-137f78417a9d">
</div>
   
9. For the percentage just divide the passing students with the total of students.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/bf7b691c-bd63-4398-b31d-834533b7df47">
</div>

10. Lastly you will get it looks like this.
<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/5100f4b5-1c34-42bd-aa6a-cbde3abb0262">
</div>

### Pie Chart for Pass and Fail

11. To create a pie chart to represent “Pass” and “Fail”, we take the total record for both “Pass” and “Fail” that has been calculated and choose ‘pie chart’ from chart section.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/2ecf3c3b-1f6a-4c97-9475-22d8328660ba">
</div>


### Dashboard Creation
12. The overall dashboard that we already done will look like this.

<div align="center">   
<img src ="https://github.com/drshahizan/HPDP/assets/118237589/4c4fd56a-84b0-4a8c-b81f-4fb1d40f5e3c">
</div>




## Analysis of the dataset

<div id="Google_Sheet_Dashboard" align="center">
<img src="https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/KHUCHIN/case_study1a/Google_Sheet_Dashboard.png" width="800"/>
</div>

Based on the dataset, which has a total of 112K records, we may conduct an analysis in which the lowest overall percent that a student receives is 14.82 and the maximum is 98.57, with an 83.75 gap between the two. The overall percentage for students is 69.36. In terms of grading, we may look at the distribution of grades based on the top three highest grades in the dataset, which have high percentages, while the top three lowest grades stand out:

Top Three Highest Grades:
1. A → 23,214 Students
2. B+ → 13,851 Students
3. B → 13,515

Top Three Lowest Grades:
1. E → 712
2. D- → 1,029 
3. D → 1,681

The percentage of students who pass is 63.30% or 70,594 students, and the percentage of students who fail is 36.70%, or 40,925 students. Approximately half of the students passed the examination, while the remaining students did not meet the required standard to pass the examination. We can conclude that half of the students who take the examination have passed the exam and most of them get A grade.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


