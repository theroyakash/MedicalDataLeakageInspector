# Medical Data Leakage Inspector
Inspects Leakage in various training, validation dataframe to see if patient overlap had occured or not.

```
Test Case 1
This is df1    patient_id
0           0
1           1
2           2
-------------------------------------
This is df2    patient_id
0           2
1           3
2           4
leakage output: True
-------------------------------------
-------------------------------------
-------------------------------------
-------------------------------------
Test Case 2
This is df1    patient_id
0           0
1           1
2           2
-------------------------------------
This is df2    patient_id
0           3
1           4
2           5
leakage output: False
-------------------------------------
```
