<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: HANY
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | :-------------: |
| ALYA BALQISS BINTI AZAHAR             |A21EC0158      | DOCUMENTATION     |
| MUHAMMAD HARITH HAKIM BIN OTHMAN              | A21EC0205     | ANALYSIS     |
|NADIA SYAFIQAH BINTI ZULKIPLI|A21EC0098      | PREPROCESSING     |
| LIEW YVONNE              |A21EC0045      | VISUALISATION     |

## Table of Contents
1. [Introduction](#introduction)
2. [Data Importation](#data-importation)
   - 2.1. [Importing a Dataset into Google Sheets](#importing-a-dataset-into-google-sheets)
3. [Data Processing](#data-preprocessing)
   - 3.1. [Decimal Places Adjustment](#decimal-places-adjustment)
   - 3.2. [Transformation of Value](#transformation-of-value)
   - 3.3. [Determine the Top Three Values](#determine-the-top-three-values)
   - 3.4. [Total Points Calculation](#total-points-calculation)
   - 3.5. [Percentage Value Calculation](#percentage-value-calculation)
   - 3.6. [Grade Assignment](#grade-assignment)
   - 3.7. [Differentiate Status Based on Color](#differentiate-status-based-on-color)
4. [Data Visualisation](#data-visualisation)
   - 4.1. [Creating Dashboard](#creating-dashboard)
5. [Contribution](#contribution)





## 1. Introduction 
**CASE STUDY 1: Examination Results** involves working with a dataset named dataset1.txt, which contains valuable information about students' examination results. The objective of this case study is to use the dataset to carry out a series of data processing tasks. These steps are necessary to enhance the analysis and visualization of examination results using Google Sheets' features. This case study provides an opportunity to explore and analyze student examination results, from data processing to visualization, ultimately assisting in making informed decisions and improvements in academic performance evaluation.

## 2. Data Importation 
### 2.1 Importing a Dataset into Google Sheets 

Before you can create a dashboard or begin analyzing your data, you must first import your dataset into Google Sheets, as shown in Figure 1 and Figure 2. 
  1. Navigate to the **File** menu, and then choose for the **Import** option.
  2. Explore your directory to locate by clicking **Browse**.
  3. Choose for the file named **Dataset1.txt**.
  4. Click on **Open** to bring the data into Google Sheets.
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/166e8597-288a-47e4-8ca9-54a2f43ab6a7" style="width: 500px; height: 200px;">  
    
**Figure 1: Importing dataset.**   
  <br><br>
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/be3f5ddb-1eca-4457-9ac4-500c9608432c" style="width: 700px; height: 350px;">  
**Figure 2: Inserting file.**   
</div>

  5. Choose **Import Data** and ensure that the **Import location** is set to "Create a new spreadsheet".
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/7bc4178d-c5ff-4ab0-9978-4432d0b85dd2" style="width: 400px; height: 250px;">
    
**Figure 3: Creating new spreadsheet by importing the data.**  
</div>

  6. The Dataset1 spreadsheet will be displayed as shown in Figure 4.
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/20ee4e61-358a-4252-b89b-a7a0e08545ed" style="width: 600px; height: 450px;">

**Figure 4: Imported Dataset1 spreadsheet into Google Sheet.**  
</div>

## 3. Data Processing

### 3.1 Decimal Places Adjustment
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/b164435f-fc04-43cc-bd0b-d808210dda6f">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/60cba0d6-cbce-45fb-beb2-789d92819a64" style="width: 400px; height: 350px;">
      
### 3.2. Transformation of Value
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/48eda989-2b75-49cd-bd9b-cc7bcb50323d" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/f89b3483-e386-4e57-a103-8498065c9ce6" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/53bd2a16-914d-4bd6-9f9b-4f2ec16bf9aa" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/965a0e15-634a-401e-b214-57e95d32bfbd" style="width: 400px; height: 350px;">

### 3.3. Determine the Top Three Values
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/a04b939b-2e90-4f16-9122-46b637491ca5" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/d73e6421-d145-4e5b-840b-19a6574f92a6" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/91afc21c-d2e8-49a9-8f5a-507c1fff9493" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/56527951-b23e-46a5-9bd6-60a7b6a2ddf7" style="width: 250px; height: 350px;">
   

### 3.4. Total Points Calculation

### 3.5. Percentage Value Calculation

### 3.6. Grade Assignment

### 3.7. Differentiate Status Based on Color






     







## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



