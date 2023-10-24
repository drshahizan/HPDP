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

Source code : (https://docs.google.com/spreadsheets/d/1QnBDqq86TcZbKna6d90OCFNhZcOz8nY8N5COSs3UppM/edit#gid=158907566)

---

## 1. Import dataset into Google Sheet


<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/96f95fff-a9e4-4864-a031-bf3dc30c80ad">
</p>

<div align="center">
  
_Figure 1: Import the data_

</div>


- After opening Google Sheet, click on **File** and choose **Import**.


![Screenshot (979)](https://github.com/drshahizan/HPDP/assets/89633522/ab5caf43-26f0-4553-a10e-e53e97b2f043)

<div align="center">
  
_Figure 2: Choose your data_

</div>

- Choose** Browse **and choose 'Dataset1.txt' as our dataset.

  
![Screenshot (980)](https://github.com/drshahizan/HPDP/assets/89633522/d98a6b2b-0750-4eff-bc2b-75d20c3ccd3d)

<div align="center">
  
_Figure 3: Import data_

</div>

- Choose '**Replace in current sheet**' as Import location and '**Detect automatically**' as separator type. Check on the checkboard. Then, click Import Data.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/8cc5a7e5-f0f7-44e6-8911-d34385360f96">
</p>

<div align="center">
  
_Figure 4: Database imported successfully_

</div>

- The database has imported successfully.
  
----

## 2. Perform data processing
#### i. Convert the Academic, Sports, Co-Curriculum, Test 1 and Test 2 data values to two decimal places.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/2ae18c09-70d7-4de1-975e-141a90cbd05f">
</p>

<div align="center">
  
_Figure 5_

</div>

- Click **Ctrl+ Shift** and click on Academics table, Sports, Co-Curriculum, Test 1 and Test 2. Then, click on **increase decimal place** button on the ribbon one time.

-----

#### ii.	Please provide a new value for columns B (Academic) through F (Test 2), with the new maximum value of 3.33 for each column. Please update the values in columns G (P1) to K (PS) (refer to Table 2 and Figure 2). Values are displayed to two decimal places.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/6de5b0fb-cd84-40e8-a426-26ef9bb014e1">
</p>

<div align="center">
  
_Figure 6 : Add column P1 in on the sheet_

</div>

- **Add** column P1, P2, P3, P4 and P5
- For **column P1**, use formula =*(B2/61)*3.33*. B2 is row number while 61 is the full mark for Academic column. 3.33 is the maximum value for each column.
- **Continue** to calculate the value of P2 until P5 by using
  -  P2 = *(C2/61)*3.33*
  -  P3 = *(D2/10)*3.33*
  -  P4 = *(E2/15)*3.33*
  -  P5 = *(F2/15)*3.33*
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/b37b0731-9fc3-402c-816f-8ab3adb82158">
</p>

<div align="center">
  
_Figure 7: The output of the data_

</div>

----

#### iii. Determine the top three values based on the values in columns G to K. Fill in the highest value in column L (B1), the second highest value in column M (B2), and the third highest value in column N (B3)

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/69a28f08-53d2-4773-812a-66d4b58ea695">
</p>

<div align="center">
  
_Figure 8_

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


<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/190c0f40-3524-4b60-8e9a-ca9841b97f5d">
</p>

<div align="center">
  
_Figure 9 : Output of TM_

</div>


- **Add** column **TM**.
- For **column TM**, use formula *=SUM(L2,M2,N2)1)*
- The reason behind this formula is to find the total of COLUMN  L2, M2 and N2.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

------

#### V. Please calculate the percentage value for data in the column O. In column P, enter percentage value (Percent). Check that the percentage value is within two decimal places.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/c6152175-33ab-4475-806d-6115dd9a4a20">
</p>

<div align="center">
  
_Figure 10 : Output of Percentage_

</div>

- **Add** column **Percentage**.
- For **column Percentage**, use formula *=ROUND(O2*10, 2)*
- The reason behind this formula is to find the percentage of of column TM within two decimal places.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

  -------

 #### vi. Based on Table 3, assist a grade, Column Q is for grade, and column R is for status.

<p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/89633522/f08923f8-c81f-40e4-bfc6-2a8d49176fc1" width="200">
</p>

 <div align="center">
  
_Table 3_

</div>

 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/76216ecc-40f8-4757-b831-ccd0d9387ff1">
</p>

<div align="center">
  
_Figure 10: Output of Grade_

</div>

- **Add** column **Grade**.
- For **column Grade**, use formula *=IF(P2 >= 90, "A+", IF(P2 >= 80, "A", IF(P2 >= 75, "A-", IF(P2 >= 70, "B+", IF(P2 >= 65, "B", IF(P2 >= 60, "B-", IF(P2 >= 55, "C+", IF(P2 >= 50, "C", IF(P2 >= 45, "C-", IF(P2 >= 40, "D+", IF(P2 >= 35, "D", IF(P2 >= 30, "D-", "E"))))))))))))*
- The reason behind this formula is to find the grade based on the mark given.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/e0a94d7c-0144-4102-8620-662178ba21ff">
</p>

<div align="center">
  
_Figure 11: Output of status_

</div>

- **Add** column **Status**.
- For **column Status**, use formula *=IF(OR(Q2="B", Q2="B+", Q2="A", Q2="A-", Q2="A+"), "Pass", "Fail")*
- The reason behind this formula is to find the statsu based on the mark and grades given.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.


------

 #### vii. If the status is Pass, please colour column P with Green, You should colour the Pass line with light red.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/4e6d702f-5d90-4bff-ba16-bed7bb3ee6b2">
</p>

<div align="center">
  
_Figure 12: Green colour with Pass status and Light Red for pass line_

</div>

- **Choose** *Fill color* on the ribon.
- **Select** respective line to fill in the colour.
-  Fill in *green colour* for *column P with status Pass*.
-  Fill in *light red* for *Pass line*

----

## Output of the data

![Screenshot (999)](https://github.com/drshahizan/HPDP/assets/89633522/33d3ef01-ccd6-4dca-9d19-3ca09cf7366e)

<div align="center">
  
_Figure 13 : Final ouput of the sheet_

</div>


![Screenshot (1000)](https://github.com/drshahizan/HPDP/assets/89633522/536afc26-de8a-4fdb-9f42-36733e62b7b8)

<div align="center">
  
_Figure 14 : Final ouput of the sheet_

</div>

# 3. Create Dashboard in Google Sheet.






 
