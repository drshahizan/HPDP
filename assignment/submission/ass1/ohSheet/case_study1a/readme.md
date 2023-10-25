<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: ohSheet
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | ------------- |
| MIKHAIL BIN YASSIN                       |  A21EC0053       |      Pre-processing |
| FAUZAN AQIL BIN AZMAN                    |    A21EC0174     |    Data Transformation           |
| YASMEEN NATASHA BINTI HAFIZ SHAHREL      |     A21EC0147    |     Visualisation|   
| MUHAMMAD ADAM FAHMI BIN MOHD TAUFIQ      |      A21EC0061   |       Documentation         |     

## Table of Contents
+ [About](#about)
+ [Importing and Preprocessing Data](#preprocess)
+ [Obtaining Grade and Status](#grade_status)
+ [Creating a Dashboard](#dashboard)
+ [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>
The main goal of this project is to utilize Google Sheets to process and present data, with a specific focus on a case study related to examination results. The project involves tasks such as calculating statistics, creating charts, and generating meaningful insights from the examination results. Overall, the project emphasizes practical data manipulation and visualization skills within the context of educational assessment.

## Importing and Preprocessing Data <a name = "preprocess"></a>
1. Download the Dataset1.txt file.
   
2. To import the Dataset1.txt file on Google Sheets, choose 'File' and click 'Import'.

3. Choose the file and click 'Import data'.
   
4. Figure shows the data that has been entered into Google Sheets. This dataset contains five columns: Id_No, Academic, Sports, Co-Curriculum, Test_1, and Test_2.
   
5. To convert the Academic, Sports, Co-Curriculum, Test_1, and Test_2 data values to two decimal places, select column B through column F.

6. Choose 'Format' and click 'Number'.
   
7. Select 'Custom number format' and apply the two decimal values.
   
8. Create new columns to create new values of column B (Academic) to column F (Test_2) to standardize the maximum value to 3.33 for each column. The new columns should be name as below:

   Academic: P1 (Column G) <br>
   Sports: P2 (Column H) <br>
   Co-Curriculum: P3 (Column I) <br>
   Test_1: P4 (Column J) <br>
   Test_2: P5 (Column K) 

   To calculate the new values, divide the score of each category by its full mark. The formula for each column is:
   
   Column P1: '=(B2/61)*3.33' <br>
   Column P2: '=(C2/10)*3.33' <br>
   Column P3: '=(D2/15)*3.33' <br>
   Column P4: '=(E2/10)*3.33' <br>
   Column P5: '=(F2/10)*3.33' 
   
   For each column, click enter after filling out the formula to autofill the entire column. 

9. Create three new columns named B1 (Column L), B2 (Column M), and B3 (Column N) to determine the top three values based on the values on columns G to K. The new columns represent information as below:

   Column L (B1): The highest value <br>
   Column M (B2): The second highest value <br>
   Column N (B3): The third highest value

   The formula to get the values for each column is:

   Column B1: '=LARGE($G2:$K2,1)' <br>
   Column B2: '=LARGE($G2:$K2,2)' <br>
   Column B3: '=LARGE($G2:$K2,3)'

   For each column, click enter after filling out the formula to autofill the entire column.

10. Create a new column named TM (Column O) to calculate the total points by combining the data from columns L to N. The formula to calculate the total mark value is:

    '=SUM(L2:N2)'
    
    Click enter after filling out the formula to autofill the entire column.

11. Create a new column named Percent (Column P) to calculate the percentage value for the data in Column O (TM). The formula to calculate the percentage is:

    '=(O2/9.99)*100'

    Click enter after filling out the formula to autofill the entire column.

    The percentage value must be in two decimal places.

## Obtaining Grade and Status <a name = "grade_status"></a>
1. Create two new columns, Column Q for Grade and column R for Status.

   The grade and status must be obtained based on the following table.

2. The formula to determine the grade is:

   ='VLOOKUP(P2,$U3:$W16,2)'

   Click enter after filling out the formula to autofill the entire column.

3. The formula to determine the status is:

   '=VLOOKUP(P2,$Y$4:$Z$16,2)'

   Click enter after filling out the formula to autofill the entire column.

   Colour column P with green for Pass and light red for the Pass line.

4. Figure shows the final result of Dataset1 sheet before creating a dashboard.

## Creating a Dashboard <a name = "dashboard"></a>


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


