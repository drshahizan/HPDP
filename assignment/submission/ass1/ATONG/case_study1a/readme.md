<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: ATONG (ATG)

## Table of Contents
- [Data Preprocessing](#data-preprocessing)
  - [Importing Dataset](#importing-dataset)
  - [Removing Unused Rows](#removing-unused-rows)
  - [Changing Decimal Places](#changing-decimal-places)
  - [Creating New Column (P1 to P5)](#creating-new-column-p1-to-p5)
  - [Three Highest Value](#three-highest-value)
  - [Calculating Total Marks (TM)](#calculating-total-marks-tm)
  - [Calculating Percentage](#calculating-percentage)
  - [Creating Pass and Status](#creating-pass-and-status)
  - [Highlighting Pass Students](#highlighting-pass-students)

- [Dashboard Creation](#dashboard-creation)
  - [Scorecard Chart](#scorecard-chart)
  - [Calculating Min, Max, Average](#calculating-min-max-average)
  - [Grading Chart](#grading-chart)
  - [Creating Total Record, Pass and Fail](#creating-total-record-pass-and-fail)
  - [Pie Chart (Fail and Pass)](#pie-chart-fail-and-pass)
  - [Dashboard](#dashboard)

## Data Preprocessing

### Importing Dataset

1. We import the dataset (Dataset1.txt) to Google Sheet (https://docs.google.com/spreadsheets/) where we click the import button from file.


<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/77014f96-9705-45a8-8987-58a23f55ee10" width="400"></div>

### Removing unused rows

2. We remove unused rows because the data only has 111520 rows by using ctrl+shift+del and selecting all the unused rows.

### Changing Decimal places

3. To change the data to two decimal places, first of all we have to select the columns that we want to change the format of the data. Then, go to the “Format” tab and select “Number” and go to “Custom number format”.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/641f00a4-11d0-4240-a499-74e8697c45b2" width="400"></div>


4. In the “Custom number format tab”, select the one as shown in the image below:

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/035afcfc-441b-4d87-9936-4f0b0dbf0b61" width="400"></div>


### Creating new column (P1 to P5)

5. Creating a new column P1 to P5 based on the guide table below:-

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/618c0ad5-4cbe-4479-a695-822018d839e2" width="400"></div>


6. The new column (P1-P5) must be calculated following the existing column; for example, to create column P1, we take the value from column B and calculate it as the question wants the maximum marks to be 3.33%. Below is the full marks for each column:-

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/12fae10a-5b46-4c7b-b652-23d93df76536" width="400"></div>


7. Then, we use the formula as in the picture below to calculate each new column (p1-p5):-

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/09239587-58f9-4f76-a82f-c89870c8cdc1" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/8b34b6f1-5d9f-447a-b939-d4cea5199871" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/c55cdb1f-9c02-4fb6-8658-5a37bcd0fa14" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/a2fecdfd-9444-4b66-b256-926e90a85f34" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/78fd2d78-7deb-48c1-9b2b-45b3c2b33ff2" width="400"></div>


8. Use “Ctrl” + “Shift” + “↓” to select all the rows for the column and click “Ctrl” + “D” to duplicate the formulas for all rows.

### Three Highest Value

9. Get the top three highest values from column “P1”p to column “P5” by inserting the formula as in the image below:

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/c323df25-046d-4bac-8547-5a46e796401e" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/e80480e2-36d0-414b-bb49-ed59a92f888c" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/d57b6632-ec18-4799-985c-d1b0a06ea409" width="400"></div>


10. Use “Ctrl” + “Shift” + “↓” to select all the rows for the column and click “Ctrl” + “D” to duplicate the formulas for all rows.

### Calculating Total Marks (TM)

11. Get the total points from column “B1” to column “B3” by inserting the formula as in the image below:

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/34496ad4-48c0-4430-8914-8e72c3862f8a" width="400"></div>


12. Use “Ctrl” + “Shift” + “↓” to select all the rows for the column and click “Ctrl” + “D” to duplicate the formulas for all rows.

### Calculating Percentage

13. Get the percentage value of the “TM” column by inserting the formula as in the image below:

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/83f9dde1-e688-4f58-afd3-1faf7e9a7aef" width="400"></div>


14. Use “Ctrl” + “Shift” + “↓” to select all the rows for the column and click “Ctrl” + “D” to duplicate the formulas for all rows. After that, select the column and go the the “Format” tab, go to  “Custom Number Format” and select “@” as shown in an image below:

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/1280c34d-79da-4636-912a-39b8076a26ca" width="200"></div>


### Creating Pass and Status 

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/d4b23a24-9857-4a4d-82e4-954a7d68d5b3" width="200"></div>


15. To create a Grade and Pass column, we refer to the table given. We use the IFS formula that has been linked inside the percent to grade in the pictures below to create a Grade column

> [!IMPORTANT]
> =IFS(P2 >= 90, "A+", P2 >= 80, "A", P2 >= 75, "A-", P2 >= 70, "B+",P2 >= 65, "B", P2 >= 60, "B-", P2 >= 55, "C+", P2 >= 50, "C", P2 >= 45, "C-", P2 >= 40, "D+", P2 >= 35, "D", P2 >= 30, "D-", P2 >= 0, "E" )

16. For the Pass column, the value inside is either “Pass” or “Fail”. We use the formula that checks the Percent column to see whether the value is <65, then the value for column Pass is “Fail”, otherwise.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/e87ade9a-2531-4aea-a002-b04e8670c392" width="400"></div>


### Highlighting Pass Students

17. Go to the “Conditional Formatting” tab, then go to “Conditional format rules”tab and do as shown in the image below:
    
<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/30c23370-cf04-4878-a9a1-1c95376602bf" width="200"></div>


## Dashboard Creation

### Scorecard Chart

1. To create a dashboard, we use a scorecard chart from ‘Chart’ inside the ‘Insert’ tab. First, we select the data we want to be inside the chart then click the selected chart. Repeat the steps to create for Total Record, Number Pass, Percentage Pass, Number Fail, Percentage Fail, Min, Max, and Average.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/4cb65a44-7460-4f28-96d3-b8e9b7158a85" width="400"></div>


### Calculating Min, Max, Average

2. To count the Max, Min and Average, we use formulas for each of them. The formula for Max is =MAX(Dataset1!P2:P). To calculate Min, the formula is =MIN(Dataset1!P2:P) and lastly, for Average, the formula is =AVERAGE(Dataset1!P2:P).

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/ba70b3e0-2f0a-42fe-aabf-67b52772f930" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/40543aa9-78bb-48a6-adb2-f351df42444e" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/800e2c6a-e0af-4910-ada6-7a7880a63908" width="400"></div>

3. So, these are the charts that we managed to create.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/e5bd7cee-3be9-42d0-8405-9bfe15028f61" width="200"></div>


# Grading Chart

4. To display the grading chart, first we have to sort the grade in descending order, which is from A+, A, A-, B+ and so on until E. Then, use the formula to get the total number for each grade.

=COUNTIF(Dataset1!Q:Q, "A+")
=COUNTIF(Dataset1!Q:Q, "A")
=COUNTIF(Dataset1!Q:Q, "A-")
=COUNTIF(Dataset1!Q:Q, "B+")
=COUNTIF(Dataset1!Q:Q, "B")
=COUNTIF(Dataset1!Q:Q, "B-")
=COUNTIF(Dataset1!Q:Q, "C+")
=COUNTIF(Dataset1!Q:Q, "C")
=COUNTIF(Dataset1!Q:Q, "C-")
=COUNTIF(Dataset1!Q:Q, "D+")
=COUNTIF(Dataset1!Q:Q, "D")
=COUNTIF(Dataset1!Q:Q, "D-")
=COUNTIF(Dataset1!Q:Q, "E") 

5. To calculate the grand total of every grade, we use formula as shown in the image below:

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/f1098f3f-f44c-4aa1-a3ff-d2b5a4c42ab5" width="200"></div>


6. From that table, we can create a bar chart by selecting the column “Grade” and “Data” and then we go to the “Insert” tab and select “Chart” and then choose the “Column Chart”.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/7972cb3b-4d9b-49c8-8e09-fcf55226911d" width="400"></div>


### Creating Total Record, Pass and Fail

7. To calculate the total record, we use the formula “=COUNTA(Dataset1!A2:A)” where this data is put into another sheet for visualization purposes.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/774da157-99f2-404a-9ae2-60e66fa8ee5a" width="400"></div>


8. To calculate the number of “Pass” and “Fail” records, with their percentage. We calculate using the formula =COUNTIF(Dataset1!R:R, "Pass") (change to “Fail” for Fail record). The ‘R’ is the column for the Status Column. Next, we use the formula =(COUNTIF(Dataset1!R:R, "Pass") / COUNTA(Dataset1!R:R)) * 100 (change to “Fail” for Fail record) to find the percentage of their record.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/3980254b-8b8a-446c-9168-df1159e85202" width="400"></div>

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/e7fea2aa-0bd1-4dc3-9e1d-4236015ba086" width="100"></div>


9. Thus creating:-

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/9b0e024c-1ed0-4d59-b116-ffcb5d40c5cf" width="200"></div>


### Pie Chart (Fail and Pass)

10. To create a pie chart to represent “Pass” and “Fail”, we take the total record for both “Pass” and “Fail” that has been calculated and choose ‘pie chart’ from chart section.

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/d3041cb2-689f-4554-a16a-2029a4c8ea7c" width="600"></div>


### Dashboard 

11. So, this is the dashboard the we managed to create:

<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/104277576/778212f9-d096-4009-8656-25bae6e3b6ac" width="800"></div>




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



