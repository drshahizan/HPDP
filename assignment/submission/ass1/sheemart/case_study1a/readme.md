<div align="center">

# Assignment 1: Data Analysis using Google Sheets
## Dataset 1 Report

</div>


---

### 🍀Group Name: sheemart
### 🌼Group Members

| Name                                     | Matrix Number | Photo |
| :---------------------------------------- | :-------------: | ------------|
| MUHAMMAD AMIR JAMIL BIN JAMLUS | A21EC0202 |              |
| MUHAMMAD NAQUIB BIN ZAKARIA | A20BE0161 |              |
| MUHAMMAD HAZIM BIN SALMAN | A21EC0078 |              |
| NURUNNAJWA BINTI ZULKIFLI | A21EC0121 |                  |

------
## 🌟Table of content

------

## Dataset Information

We work with a dataset called dataset1.txt. This dataset has five column that contain information about Id_no, Academic, Sports, Co-curiculum, Test_1 and Test_2.

---

## 1. Import dataset into Google Sheet

![Screenshot (978)](https://github.com/drshahizan/HPDP/assets/89633522/904d2f0a-9d3e-4670-8a20-74eff83f6af3)
<div align="center">
  
_Figure 1_

</div>


- After opening Google Sheet, click on **File** and choose **Import**.


![Screenshot (979)](https://github.com/drshahizan/HPDP/assets/89633522/b9da0112-a0ad-418d-a16c-2a9295e1569b)
<div align="center">
  
_Figure 2_

</div>

- Choose** Browse **and choose 'Dataset1.txt' as our dataset.

  
![Screenshot (980)](https://github.com/drshahizan/HPDP/assets/89633522/d0b48741-7eb7-48f8-bfcc-ebd7c5d60f28)
<div align="center">
  
_Figure 3_

</div>

- Choose '**Replace in current sheet**' as Import location and '**Detect automatically**' as separator type. Check on the checkboard. Then, click Import Data.

![Screenshot (981)](https://github.com/drshahizan/HPDP/assets/89633522/8e000844-ef78-4fa8-9e54-28d732bc53b8)
<div align="center">
  
_Figure 4_

</div>

- The database has imported successfully.
  
----

## 2. Perform data processing
#### i. Convert the Academic, Sports, Co-Curriculum, Test 1 and Test 2 data values to two decimal places.


![Screenshot (982)](https://github.com/drshahizan/HPDP/assets/89633522/5635183f-4dba-429d-90e4-f607bdcb4993)
<div align="center">
  
_Figure 5_

</div>

- Click **Ctrl+ Shift** and click on Academics table, Sports, Co-Curriculum, Test 1 and Test 2. Then, click on **increase decimal place** button on the ribon one time.

-----

#### ii.	Please provide a new value for columns B (Academic) through F (Test 2), with the new maximum value of 3.33 for each column. Please update the values in columns G (P1) to K (PS) (refer to Table 2 and Figure 2). Values are displayed to two decimal places.


![Screenshot (990)](https://github.com/drshahizan/HPDP/assets/89633522/12207198-cad7-42df-a7c6-686799208c3f)

<div align="center">
  
_Figure 6_

</div>

- **Add** column P1, P2, P3, P4 and P5
- For **column P1**, use formula =*(B2/61)*3.33*. B2 is row number while 61 is the full mark for Academic column. 3.33 is the maximum value for each column.
- **Continue** to calculate the value of P2 until P5 by using
  -  P2 = (C2/61)*3.33
  -  P3 = (D2/10)*3.33
  -  P4 = (E2/15)*3.33
  -  P5 = (F2/15)*3.33
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

----

#### iii. Determine the top three values based on the values in columns G to K. Fill in the highest value in column L (B1), the second highest value in column M (B2), and the third highest value in column N (B3)

  
![Screenshot (991)](https://github.com/drshahizan/HPDP/assets/89633522/3f5306b5-44ce-469a-85a0-bb60c787a227)

<div align="center">
  
_Figure 7_

</div>

- **Add** column B1, B2 AND B3.
- For **column B1**, use formula *=LARGE(UNIQUE(G2:K2),1)*
- The reason behind this formula is to find the first highest mark of P1 until P5 in column L (B1).
- **Continue** to calculate the value of B2 until B3 by using
  - B2 = LARGE(UNIQUE(G2:K2),2)
  - B3 = LARGE(UNIQUE(G2:K2),3)
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

------

#### iv. Compute total points by combining the data from column L to N. The total mark value is entered in column O (TM).

![Screenshot (992)](https://github.com/drshahizan/HPDP/assets/89633522/f0070eda-9c0d-4cc4-9ebd-113cae3ce38a)

<div align="center">
  
_Figure 8_

</div>


- **Add** column **TM**.
- For **column TM**, use formula *=SUM(L2,M2,N2)1)*
- The reason behind this formula is to find the total of COLUMN  L2, M2 and N2.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

------

#### V. Please calculate the percentage value for data in the column O. In column P, enter percentage value (Percent). Check that the percentage value is within two decimal places.

![Screenshot (994)](https://github.com/drshahizan/HPDP/assets/89633522/f76ccea7-bea6-44cd-ac5f-a9bfdffe7dee)


<div align="center">
  
_Figure 9_

</div>

- **Add** column **Percentage**.
- For **column Percentage**, use formula *=ROUND(O2*10, 2)*
- The reason behind this formula is to find the percentage of of column TM within two decimal places.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

  -------

 #### vi. Based on Table 3, assist a grade, Column Q is for grade, and column R is for status.

 ![Screenshot (996)](https://github.com/drshahizan/HPDP/assets/89633522/f08923f8-c81f-40e4-bfc6-2a8d49176fc1)

 <div align="center">
  
_Table 3_

</div>


![Screenshot (995)](https://github.com/drshahizan/HPDP/assets/89633522/da04d28a-7b5f-4298-8740-81d5efb3fa82)

<div align="center">
  
_Figure 10_

</div>

- **Add** column **Grade**.
- For **column Grade**, use formula *=IF(P2 >= 90, "A+", IF(P2 >= 80, "A", IF(P2 >= 75, "A-", IF(P2 >= 70, "B+", IF(P2 >= 65, "B", IF(P2 >= 60, "B-", IF(P2 >= 55, "C+", IF(P2 >= 50, "C", IF(P2 >= 45, "C-", IF(P2 >= 40, "D+", IF(P2 >= 35, "D", IF(P2 >= 30, "D-", "E"))))))))))))*
- The reason behind this formula is to find the grade based on the mark given.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

![Screenshot (997)](https://github.com/drshahizan/HPDP/assets/89633522/9d24b756-fd72-4f14-b99f-6e0bc1e9b783)


<div align="center">
  
_Figure 10_

</div>

  
- **Add** column **Status**.
- For **column Status**, use formula *=IF(OR(Q2="B", Q2="B+", Q2="A", Q2="A-", Q2="A+"), "Pass", "Fail")*
- The reason behind this formula is to find the statsu based on the mark and grades given.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.


------

 #### vii. If the status is Pass, please colour column P with Green, You should colour the Pass line with light red.

 ![Screenshot (998)](https://github.com/drshahizan/HPDP/assets/89633522/4f9163de-3b0d-4478-b97a-5ac97d0476b7)

<div align="center">
  
_Figure 11_

</div>

- **Choose** *Fill color* on the ribon.
- **Selec**t respective line to fill in the colour.
-  Fill in *green colour* for *column P with status Pass*.
-  Fill in *light red* for *Pass line*

----

# 3. Create Dashboard in Google Sheet.


 
