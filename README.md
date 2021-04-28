# Streamlit-web-app-covid-19-affect
import numpy as np
import pandas as pd
Albania = pd.read_stata("C:\\Users\\HP\\Desktop\\Albania_removed_missing_values.dta")
Albania.shape
(347, 86)
Albania.columns
Index(['index', 'idstd', 'id', 'a1', 'countryx', 'a1a', 'mode', 'a0',
       'COVa20d', 'COVa20m', 'COVa20y', 'COVa20m_1', 'COVb0', 'COVb1a',
       'COVb1b', 'COVb2a', 'COVb2b', 'COVb2c', 'COVb3a', 'COVb3b', 'COVb3c',
       'COVb4', 'COVc3', 'COVc1', 'COVc2a', 'COVc2b', 'COVc2c', 'COVc4a',
       'COVc4b', 'COVc4c', 'COVc5', 'COVc6', 'COVd0a', 'COVd0b', 'COVd1',
       'COVd2', 'COVd3b', 'COVd4', 'COVd5', 'COVd6', 'COVd7', 'COVd8', 'COVd9',
       'COVe1a', 'COVe1b', 'COVe1c', 'COVe2', 'COVe3a', 'COVe3b', 'COVe3c',
       'COVe4', 'COVe5', 'COVf1', 'COVf2a', 'COVf2b', 'COVf2c', 'COVf2d',
       'COVf2e', 'COVf2f', 'COVf2fx', 'COVg1', 'COVg2', 'COVg3', 'COVg4',
       'COVh1ay', 'COVh1am', 'COVh2a', 'COVh2b', 'COVh2c', 'COVh2d', 'COVh2e',
       'COVh2f', 'COVh3', 'a21x', 'a22', 'a22online', 'a23', 'a24', 'a25',
       'a26', 'eligibilitycode', 'statuscode', 'strata', 'wmedian_ES',
       'wmedian_COVID', 'wweak_COVID'],
      dtype='object')
Albania.drop(['index','idstd', 'id', 'a1', 'countryx', 'a1a', 'mode',
              'COVa20d', 'COVa20m', 'COVa20y', 'COVa20m_1', 
              'COVb2b', 'COVb2c', 'COVb3a', 'COVc1', 'COVc5', 'COVc6', 'COVd0a', 'COVd0b', 'COVd1',
              'COVd2', 'COVd4', 'COVd5', 'COVd6', 'COVd7', 'COVd8', 'COVd9',
              'COVe3a', 'COVe3b', 'COVe3c','COVe4', 'COVe5', 'COVf2b','COVf2d',
              'COVf2e', 'COVf2f', 'COVf2fx', 'COVg1', 'COVg2', 'COVg3', 'COVg4',
              'COVh1ay', 'COVh1am', 'COVh2a', 'COVh2b', 'COVh2c', 'COVh2d', 'COVh2e',
              'COVh2f', 'COVh3', 'a21x', 'a22', 'a22online', 'a23', 'a24', 'a25',
              'a26', 'eligibilitycode', 'statuscode', 'strata', 'wmedian_ES',
              'wmedian_COVID', 'wweak_COVID'],axis=1,inplace=True)
Albania.shape
(347, 23)
Albania.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 347 entries, 0 to 346
Data columns (total 23 columns):
 #   Column  Non-Null Count  Dtype   
---  ------  --------------  -----   
 0   a0      347 non-null    category
 1   COVb0   347 non-null    category
 2   COVb1a  300 non-null    category
 3   COVb1b  222 non-null    category
 4   COVb2a  344 non-null    category
 5   COVb3b  344 non-null    category
 6   COVb3c  344 non-null    category
 7   COVb4   344 non-null    category
 8   COVc3   344 non-null    category
 9   COVc2a  344 non-null    category
 10  COVc2b  344 non-null    category
 11  COVc2c  344 non-null    category
 12  COVc4a  344 non-null    category
 13  COVc4b  344 non-null    category
 14  COVc4c  344 non-null    category
 15  COVd3b  344 non-null    category
 16  COVe1a  344 non-null    category
 17  COVe1b  344 non-null    category
 18  COVe1c  344 non-null    category
 19  COVe2   241 non-null    category
 20  COVf1   344 non-null    category
 21  COVf2a  144 non-null    category
 22  COVf2c  144 non-null    category
dtypes: category(23)
memory usage: 15.6 KB
Albania.drop(['COVb1b','COVe2','COVf2a','COVf2c'],axis = 1,inplace = True)
Albania.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 347 entries, 0 to 346
Data columns (total 19 columns):
 #   Column  Non-Null Count  Dtype   
---  ------  --------------  -----   
 0   a0      347 non-null    category
 1   COVb0   347 non-null    category
 2   COVb1a  300 non-null    category
 3   COVb2a  344 non-null    category
 4   COVb3b  344 non-null    category
 5   COVb3c  344 non-null    category
 6   COVb4   344 non-null    category
 7   COVc3   344 non-null    category
 8   COVc2a  344 non-null    category
 9   COVc2b  344 non-null    category
 10  COVc2c  344 non-null    category
 11  COVc4a  344 non-null    category
 12  COVc4b  344 non-null    category
 13  COVc4c  344 non-null    category
 14  COVd3b  344 non-null    category
 15  COVe1a  344 non-null    category
 16  COVe1b  344 non-null    category
 17  COVe1c  344 non-null    category
 18  COVf1   344 non-null    category
dtypes: category(19)
memory usage: 12.9 KB
Albania.dropna(subset=["a0"],how="any",inplace = True)
Albania.isnull().sum()
a0         0
COVb0      0
COVb1a    47
COVb2a     3
COVb3b     3
COVb3c     3
COVb4      3
COVc3      3
COVc2a     3
COVc2b     3
COVc2c     3
COVc4a     3
COVc4b     3
COVc4c     3
COVd3b     3
COVe1a     3
COVe1b     3
COVe1c     3
COVf1      3
dtype: int64
Albania.dropna(subset=['COVb1a', 'COVb2a', 'COVb3b', 'COVb3c', 'COVb4', 'COVc3',
       'COVc2a', 'COVc2b', 'COVc2c', 'COVc4a', 'COVc4b', 'COVc4c', 'COVd3b',
       'COVe1a', 'COVe1b', 'COVe1c', 'COVf1'],how="all",inplace = True)
Albania.isnull().sum()
a0         0
COVb0      0
COVb1a    44
COVb2a     0
COVb3b     0
COVb3c     0
COVb4      0
COVc3      0
COVc2a     0
COVc2b     0
COVc2c     0
COVc4a     0
COVc4b     0
COVc4c     0
COVd3b     0
COVe1a     0
COVe1b     0
COVe1c     0
COVf1      0
dtype: int64
Albania.to_stata("Albania_Final_Data.dta")
Albania.shape
(344, 19)
Albania.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 344 entries, 0 to 345
Data columns (total 19 columns):
 #   Column  Non-Null Count  Dtype   
---  ------  --------------  -----   
 0   a0      344 non-null    category
 1   COVb0   344 non-null    category
 2   COVb1a  300 non-null    category
 3   COVb2a  344 non-null    category
 4   COVb3b  344 non-null    category
 5   COVb3c  344 non-null    category
 6   COVb4   344 non-null    category
 7   COVc3   344 non-null    category
 8   COVc2a  344 non-null    category
 9   COVc2b  344 non-null    category
 10  COVc2c  344 non-null    category
 11  COVc4a  344 non-null    category
 12  COVc4b  344 non-null    category
 13  COVc4c  344 non-null    category
 14  COVd3b  344 non-null    category
 15  COVe1a  344 non-null    category
 16  COVe1b  344 non-null    category
 17  COVe1c  344 non-null    category
 18  COVf1   344 non-null    category
dtypes: category(19)
memory usage: 12.8 KB
Albania["a0"].value_counts()
Other services     141
Manufacturing      131
Retail services     72
Name: a0, dtype: int64
Albania["COVb0"].value_counts(dropna=False)
Open                  300
Temporarily closed     44
Permanently closed      0
Name: COVb0, dtype: int64
Albania[Albania["COVb0"] == 'Permanently closed']
a0	COVb0	COVb1a	COVb2a	COVb3b	COVb3c	COVb4	COVc3	COVc2a	COVc2b	COVc2c	COVc4a	COVc4b	COVc4c	COVd3b	COVe1a	COVe1b	COVe1c	COVf1
Albania["COVb1a"].value_counts(dropna=False)
Yes    178
No     122
NaN     44
Name: COVb1a, dtype: int64
Albania["COVb2a"].value_counts(dropna=False)
Decrease                    286
Remain the same              34
Increase                     23
Don't know (spontaneous)      1
Name: COVb2a, dtype: int64
Albania["COVb2a"].unique()
[Decrease, Remain the same, Increase, Don't know (spontaneous)]
Categories (4, object): [Don't know (spontaneous) < Increase < Remain the same < Decrease]
Albania[Albania["COVb2a"]== "Don't know (spontaneous)"]
a0	COVb0	COVb1a	COVb2a	COVb3b	COVb3c	COVb4	COVc3	COVc2a	COVc2b	COVc2c	COVc4a	COVc4b	COVc4c	COVd3b	COVe1a	COVe1b	COVe1c	COVf1
216	Manufacturing	Temporarily closed	NaN	Don't know (spontaneous)	Don't know (spontaneous)	Don't know (spontaneous)	Does not apply	No	Don't know (spontaneous)	Decrease	Decrease	No	No	No	Decrease	Decrease	Decrease	Decrease	No
Albania["COVb2a"] = Albania["COVb2a"].map({"Don't know (spontaneous)":np.NaN , "Decrease":"Decrease", "Remain the same":"Remain the same", "Increase":"Increase"})
Albania["COVb2a"].value_counts(dropna=False)
Decrease           286
Remain the same     34
Increase            23
NaN                  1
Name: COVb2a, dtype: int64
Albania["COVb3b"].value_counts(dropna=False)
0.0                         326
Don't know (spontaneous)      4
30.0                          3
100.0                         2
50.0                          2
15.0                          2
10.0                          2
90.0                          1
20.0                          1
5.0                           1
Name: COVb3b, dtype: int64
Albania["COVb3b"].value_counts()
0.0                         326
Don't know (spontaneous)      4
30.0                          3
100.0                         2
50.0                          2
15.0                          2
10.0                          2
90.0                          1
20.0                          1
5.0                           1
Name: COVb3b, dtype: int64
Albania.to_stata("Albu.dta")
Albania = Albania.replace("Don't know (spontaneous)",np.NaN)
Albania["COVb3b"].value_counts(dropna=False)
0.0      326
NaN        4
30.0       3
100.0      2
50.0       2
15.0       2
10.0       2
90.0       1
20.0       1
5.0        1
Name: COVb3b, dtype: int64
 
Albania["COVb3b"].value_counts(dropna=False)
0.0      326
NaN        4
30.0       3
100.0      2
50.0       2
15.0       2
10.0       2
90.0       1
20.0       1
5.0        1
Name: COVb3b, dtype: int64
Albania["COVb3c"].value_counts(dropna=False)
0.0      258
100.0     47
50.0      11
20.0       5
NaN        4
90.0       3
10.0       3
97.0       2
30.0       2
5.0        2
85.0       1
80.0       1
70.0       1
60.0       1
45.0       1
25.0       1
15.0       1
Name: COVb3c, dtype: int64
Albania["COVb4"].value_counts(dropna=False)
Does not apply     204
Decrease            75
Increase            45
Remain the same     20
Name: COVb4, dtype: int64
Albania["COVc3"].value_counts(dropna=False)
Yes    249
No      91
NaN      4
Name: COVc3, dtype: int64
Albania["COVc2a"].value_counts()
Decrease           168
Remain the same    164
Increase            10
Name: COVc2a, dtype: int64
Albania["COVc2b"].value_counts()
Decrease           235
Remain the same     74
Increase            33
Name: COVc2b, dtype: int64
Albania["COVc2c"].value_counts()
Decrease           218
Remain the same     88
Increase            30
Name: COVc2c, dtype: int64
Albania["COVc3"].value_counts()
Yes    249
No      91
Name: COVc3, dtype: int64
Albania["COVc2a"].value_counts()
Decrease           168
Remain the same    164
Increase            10
Name: COVc2a, dtype: int64
Albania["COVc2b"].value_counts()
Decrease           235
Remain the same     74
Increase            33
Name: COVc2b, dtype: int64
Albania["COVc2c"].value_counts()
Decrease           218
Remain the same     88
Increase            30
Name: COVc2c, dtype: int64
Albania["COVc4a"].value_counts()
No     279
Yes     55
Name: COVc4a, dtype: int64
Albania["COVc4b"].value_counts()
No     245
Yes     90
Name: COVc4b, dtype: int64
Albania["COVc4c"].value_counts()
No     292
Yes     44
Name: COVc4c, dtype: int64
Albania["COVd3b"].value_counts() 
Decrease           179
Remain the same    100
Increase             4
Name: COVd3b, dtype: int64
Albania["COVe1a"].value_counts() 
Decrease           241
Remain the same     52
Increase            47
Name: COVe1a, dtype: int64
Albania["COVe1b"].value_counts() 
Remain the same    116
Decrease           111
Increase            75
Name: COVe1b, dtype: int64
Albania["COVe1c"].value_counts() 
Remain the same    133
Decrease           102
Increase            70
Name: COVe1c, dtype: int64
Albania["COVf1"].value_counts() 
No                                                     196
Yes                                                    133
No, but expect to receive them in the next 3 months     11
Name: COVf1, dtype: int64
Albania.isnull().sum()
a0         0
COVb0      0
COVb1a    44
COVb2a     1
COVb3b     4
COVb3c     4
COVb4      0
COVc3      4
COVc2a     2
COVc2b     2
COVc2c     8
COVc4a    10
COVc4b     9
COVc4c     8
COVd3b    61
COVe1a     4
COVe1b    42
COVe1c    39
COVf1      4
dtype: int64
Albania.columns
Index(['a0', 'COVb0', 'COVb1a', 'COVb2a', 'COVb3b', 'COVb3c', 'COVb4', 'COVc3',
       'COVc2a', 'COVc2b', 'COVc2c', 'COVc4a', 'COVc4b', 'COVc4c', 'COVd3b',
       'COVe1a', 'COVe1b', 'COVe1c', 'COVf1'],
      dtype='object')
data = pd.DataFrame(Albania)
data
a0	COVb0	COVb1a	COVb2a	COVb3b	COVb3c	COVb4	COVc3	COVc2a	COVc2b	COVc2c	COVc4a	COVc4b	COVc4c	COVd3b	COVe1a	COVe1b	COVe1c	COVf1
0	Manufacturing	Open	No	Decrease	0.0	0.0	Does not apply	No	Decrease	Decrease	Decrease	No	Yes	No	Remain the same	Decrease	Remain the same	Increase	No
1	Retail services	Open	No	Remain the same	0.0	0.0	Does not apply	Yes	Decrease	Decrease	Decrease	Yes	No	No	Decrease	Decrease	Increase	Remain the same	No
2	Retail services	Open	Yes	Decrease	0.0	0.0	Does not apply	Yes	Decrease	Decrease	Remain the same	Yes	Yes	Yes	Decrease	Decrease	Remain the same	Remain the same	No
3	Manufacturing	Temporarily closed	NaN	Decrease	0.0	0.0	Does not apply	No	Decrease	Decrease	Decrease	No	No	No	Remain the same	Decrease	Remain the same	Remain the same	No
4	Manufacturing	Open	Yes	Decrease	0.0	0.0	Does not apply	Yes	Decrease	Decrease	Decrease	Yes	Yes	No	Remain the same	Decrease	Remain the same	Remain the same	No
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
341	Manufacturing	Open	Yes	Decrease	0.0	0.0	Decrease	NaN	Remain the same	Decrease	Decrease	No	No	No	NaN	Increase	Increase	Remain the same	Yes
342	Retail services	Open	Yes	Decrease	0.0	0.0	Decrease	Yes	Remain the same	Decrease	Decrease	Yes	No	Yes	Decrease	Increase	Increase	Increase	No
343	Retail services	Open	Yes	Decrease	0.0	100.0	Increase	No	Decrease	Remain the same	Decrease	No	No	No	Decrease	Decrease	Increase	Remain the same	Yes
344	Retail services	Open	No	Increase	0.0	0.0	Does not apply	Yes	Remain the same	Increase	Increase	No	No	No	Decrease	Increase	Remain the same	Remain the same	No
345	Manufacturing	Open	Yes	Decrease	0.0	0.0	Does not apply	No	Decrease	Decrease	Decrease	Yes	No	No	Remain the same	Decrease	Increase	Remain the same	Yes
344 rows × 19 columns

data.drop(['COVb1a','COVb4','COVc4b','COVd3b','COVe1b', 'COVe1c'],axis = 1, inplace = True)
data.columns
Index(['a0', 'COVb0', 'COVb2a', 'COVb3b', 'COVb3c', 'COVc3', 'COVc2a',
       'COVc2b', 'COVc2c', 'COVc4a', 'COVc4c', 'COVe1a', 'COVf1'],
      dtype='object')
LAST SELECTED VARIABLES FOR MODEL BULLDING
data.isnull().sum()
a0         0
COVb0      0
COVb2a     1
COVb3b     4
COVb3c     4
COVc3      4
COVc2a     2
COVc2b     2
COVc2c     8
COVc4a    10
COVc4c     8
COVe1a     4
COVf1      4
dtype: int64
Treating Missing Values
data.dropna(subset= ['COVc4a', 'COVc4c'],how = "all",inplace = True)
data.isnull().sum()
a0        0
COVb0     0
COVb2a    1
COVb3b    4
COVb3c    4
COVc3     3
COVc2a    2
COVc2b    1
COVc2c    5
COVc4a    2
COVc4c    0
COVe1a    4
COVf1     4
dtype: int64
data.shape
(336, 13)
Albania_without_null = data.dropna(how = "any")
Albania_without_null.to_stata("Albania_without_null.dta")
data = pd.DataFrame(Albania_without_null)
data
a0	COVb0	COVb2a	COVb3b	COVb3c	COVc3	COVc2a	COVc2b	COVc2c	COVc4a	COVc4c	COVe1a	COVf1
0	Manufacturing	Open	Decrease	0.0	0.0	No	Decrease	Decrease	Decrease	No	No	Decrease	No
1	Retail services	Open	Remain the same	0.0	0.0	Yes	Decrease	Decrease	Decrease	Yes	No	Decrease	No
2	Retail services	Open	Decrease	0.0	0.0	Yes	Decrease	Decrease	Remain the same	Yes	Yes	Decrease	No
3	Manufacturing	Temporarily closed	Decrease	0.0	0.0	No	Decrease	Decrease	Decrease	No	No	Decrease	No
4	Manufacturing	Open	Decrease	0.0	0.0	Yes	Decrease	Decrease	Decrease	Yes	No	Decrease	No
...	...	...	...	...	...	...	...	...	...	...	...	...	...
340	Other services	Temporarily closed	Decrease	20.0	0.0	Yes	Decrease	Decrease	Decrease	No	No	Decrease	No
342	Retail services	Open	Decrease	0.0	0.0	Yes	Remain the same	Decrease	Decrease	Yes	Yes	Increase	No
343	Retail services	Open	Decrease	0.0	100.0	No	Decrease	Remain the same	Decrease	No	No	Decrease	Yes
344	Retail services	Open	Increase	0.0	0.0	Yes	Remain the same	Increase	Increase	No	No	Increase	No
345	Manufacturing	Open	Decrease	0.0	0.0	No	Decrease	Decrease	Decrease	Yes	No	Decrease	Yes
316 rows × 13 columns

data.isnull().sum()
a0        0
COVb0     0
COVb2a    0
COVb3b    0
COVb3c    0
COVc3     0
COVc2a    0
COVc2b    0
COVc2c    0
COVc4a    0
COVc4c    0
COVe1a    0
COVf1     0
dtype: int64
Countplot for understanding the missing values classification
import seaborn as sns
import matplotlib.pylab as plt
data.columns = ['Idustry_Type', 'Current_Situation', 'Sales_Performance', 'Indirect_Exports', 'Direct_Export', 
                'Production_Conversion', 'Hours_Worked_Per_Week',
                'Demand_For_Product', 'Supply_Of_Raw_Materials', 'Online_Business',
                'Remote_Work_Arrangements', 'Financial_Performance', 'Received_Any_Establishment']
plt.figure(figsize = (8,6))
plt.title("Relation between Industry type and Sales performance")
sns.countplot('Idustry_Type',hue = "Sales_Performance",data =data,palette = 'Set2')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce286a00>

plt.figure(figsize = (8,6))
plt.title("Indirect Exports and Sales performance")
sns.countplot('Indirect_Exports',hue = "Sales_Performance",data =data,palette = 'rocket')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce367c10>

plt.figure(figsize = (8,6))
plt.title("Current_Situation and Sales performance")
sns.countplot('Current_Situation',hue = "Sales_Performance",data =data,palette = 'hls')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce43dcd0>

data.columns
Index(['Idustry_Type', 'Current_Situation', 'Sales_Performance',
       'Indirect_Exports', 'Direct_Export', 'Production_Conversion',
       'Hours_Worked_Per_Week', 'Demand_For_Product',
       'Supply_Of_Raw_Materials', 'Online_Business',
       'Remote_Work_Arrangements', 'Financial_Performance',
       'Received_Any_Establishment'],
      dtype='object')
plt.figure(figsize = (8,6))
plt.title("Direct_Export and Sales performance")
sns.countplot('Direct_Export',hue = "Sales_Performance",data =data,palette = 'rainbow')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce498a90>

plt.figure(figsize = (8,6))
plt.title("Production_Conversion and Sales performance")
sns.countplot('Production_Conversion',data =data,palette = 'Set2')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce4a4a30>

plt.figure(figsize = (8,6))
plt.title("Production_Conversion and Sales performance")
sns.countplot('Production_Conversion',hue = "Sales_Performance",data =data,palette = 'Set2')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce5d48b0>

plt.figure(figsize = (8,6))
plt.title("Hours_Worked_Per_Week and Sales performance")
sns.countplot('Hours_Worked_Per_Week',hue = "Sales_Performance",data =data,palette = 'hls')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce637ac0>

plt.figure(figsize = (8,6))
plt.title("Demand_For_Product and Sales performance")
sns.countplot('Demand_For_Product',data =data,palette = 'winter')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce6ba820>

plt.figure(figsize = (8,6))
plt.title("Demand_For_Product and Sales performance")
sns.countplot('Demand_For_Product',hue = "Sales_Performance",data =data,palette = 'winter')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce3021c0>

plt.figure(figsize = (8,6))
plt.title("Supply_Of_Raw_Materials and Sales performance")
sns.countplot('Supply_Of_Raw_Materials',hue = "Sales_Performance",data =data,palette = 'rocket')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce6b6250>

plt.figure(figsize = (8,6))
plt.title("Online_Business and Sales performance")
sns.countplot('Online_Business',hue = "Sales_Performance",data =data,palette = 'hls')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce707f70>

plt.figure(figsize = (8,6))
plt.title("Remote_Work_Arrangements and Sales performance")
sns.countplot('Remote_Work_Arrangements',hue = "Sales_Performance",data =data,palette = 'rainbow')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdce80cbe0>

plt.figure(figsize = (8,6))
plt.title("Financial_Performance and Sales performance")
sns.countplot('Financial_Performance',hue = "Sales_Performance",data =data,palette = 'rainbow')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdcf836c10>

plt.figure(figsize = (8,6))
plt.title("Received_Any_Establishment and Sales performance")
sns.countplot('Received_Any_Establishment',hue = "Sales_Performance",data =data,palette = 'rainbow')
<matplotlib.axes._subplots.AxesSubplot at 0x1bdcf8906d0>

data.isnull().sum()
Idustry_Type                  0
Current_Situation             0
Sales_Performance             0
Indirect_Exports              0
Direct_Export                 0
Production_Conversion         0
Hours_Worked_Per_Week         0
Demand_For_Product            0
Supply_Of_Raw_Materials       0
Online_Business               0
Remote_Work_Arrangements      0
Financial_Performance         0
Received_Any_Establishment    0
dtype: int64
data = data.reindex(['Sales_Performance','Indirect_Exports', 'Direct_Export','Idustry_Type',
                     'Current_Situation','Hours_Worked_Per_Week', 'Demand_For_Product',
                     'Supply_Of_Raw_Materials','Financial_Performance', 'Online_Business',
                     'Production_Conversion',
                     'Received_Any_Establishment','Remote_Work_Arrangements'],axis = 1)
data.columns
Index(['Sales_Performance', 'Indirect_Exports', 'Direct_Export',
       'Idustry_Type', 'Current_Situation', 'Hours_Worked_Per_Week',
       'Demand_For_Product', 'Supply_Of_Raw_Materials',
       'Financial_Performance', 'Online_Business', 'Production_Conversion',
       'Received_Any_Establishment', 'Remote_Work_Arrangements'],
      dtype='object')
data.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 316 entries, 0 to 345
Data columns (total 13 columns):
 #   Column                      Non-Null Count  Dtype   
---  ------                      --------------  -----   
 0   Sales_Performance           316 non-null    object  
 1   Indirect_Exports            316 non-null    category
 2   Direct_Export               316 non-null    category
 3   Idustry_Type                316 non-null    category
 4   Current_Situation           316 non-null    category
 5   Hours_Worked_Per_Week       316 non-null    category
 6   Demand_For_Product          316 non-null    category
 7   Supply_Of_Raw_Materials     316 non-null    category
 8   Financial_Performance       316 non-null    category
 9   Online_Business             316 non-null    category
 10  Production_Conversion       316 non-null    category
 11  Received_Any_Establishment  316 non-null    category
 12  Remote_Work_Arrangements    316 non-null    category
dtypes: category(12), object(1)
memory usage: 20.8+ KB
Converting percentages in to intervel categories
1. Indirect_Exports ,2. Direct_Export
0 - 25 range --> very_low
26- 50 --> low
51 - 75 --> medium
76 - 100 --> high
data.Indirect_Exports.unique()
[0.0, 10.0, 30.0, 50.0, 15.0, 100.0, 90.0, 5.0, 20.0]
Categories (9, object): [0.0 < 5.0 < 10.0 < 15.0 ... 30.0 < 50.0 < 90.0 < 100.0]
data.Indirect_Exports.value_counts()
0.0      302
30.0       3
100.0      2
50.0       2
15.0       2
10.0       2
90.0       1
20.0       1
5.0        1
Name: Indirect_Exports, dtype: int64
data.Direct_Export.value_counts()
0.0      242
100.0     44
50.0       9
20.0       5
97.0       2
90.0       2
30.0       2
5.0        2
85.0       1
80.0       1
70.0       1
60.0       1
45.0       1
25.0       1
15.0       1
10.0       1
Name: Direct_Export, dtype: int64
data.head(4)
Sales_Performance	Indirect_Exports	Direct_Export	Idustry_Type	Current_Situation	Hours_Worked_Per_Week	Demand_For_Product	Supply_Of_Raw_Materials	Financial_Performance	Online_Business	Production_Conversion	Received_Any_Establishment	Remote_Work_Arrangements
0	Decrease	0.0	0.0	Manufacturing	Open	Decrease	Decrease	Decrease	Decrease	No	No	No	No
1	Remain the same	0.0	0.0	Retail services	Open	Decrease	Decrease	Decrease	Decrease	Yes	Yes	No	No
2	Decrease	0.0	0.0	Retail services	Open	Decrease	Decrease	Remain the same	Decrease	Yes	Yes	No	Yes
3	Decrease	0.0	0.0	Manufacturing	Temporarily closed	Decrease	Decrease	Decrease	Decrease	No	No	No	No
data_dummy_of_DI = data.iloc[:,1:3]
data_dummy_of_DI.head(5)
Indirect_Exports	Direct_Export
0	0.0	0.0
1	0.0	0.0
2	0.0	0.0
3	0.0	0.0
4	0.0	0.0
numerical value of direct and indirect tax both in a single data frame
data_dummy_of_DI["Indirect_Exports"]=data_dummy_of_DI["Indirect_Exports"].astype(float)
data_dummy_of_DI["Direct_Export"]=data_dummy_of_DI["Direct_Export"].astype(float)
data_dummy_of_DI.head(4)
Indirect_Exports	Direct_Export
0	0.0	0.0
1	0.0	0.0
2	0.0	0.0
3	0.0	0.0
data = pd.concat([data,data_dummy_of_DI],axis = 1,ignore_index= False)
# deinition for dummy variable creation
def dummy_indirect(i):
    if i == 0.0:
        return "very_low"
    if i == 30.0:
        return "low"
    if i ==100.0:
        return "high"
    if i == 50.0:
        return "medium"
    if i == 15.0:
        return "very_low"
    if i == 10.0:
        return "very_low"  
    if i == 90.0:
        return "high" 
    if i == 20.0:
        return "very_low"     
    else:
        return "very_low"
    
data['Indirect_Export'] = data['Indirect_Exports'].apply(dummy_indirect)
data['Indirect_Export'].head(3)
0    very_low
1    very_low
2    very_low
Name: Indirect_Export, dtype: object
data['Indirect_Export'].value_counts()
very_low    308
high          3
low           3
medium        2
Name: Indirect_Export, dtype: int64
del data["Indirect_Exports"]
data.columns
Index(['Sales_Performance', 'Idustry_Type', 'Current_Situation',
       'Hours_Worked_Per_Week', 'Demand_For_Product',
       'Supply_Of_Raw_Materials', 'Financial_Performance', 'Online_Business',
       'Production_Conversion', 'Received_Any_Establishment',
       'Remote_Work_Arrangements', 'Direct_Export', 'Indirect_Export'],
      dtype='object')
# deinition for dummy variable creation
def dummy_direct(i):
    if i == 0.0:
        return "very_low"
    if i == 30.0:
        return "low"
    if i ==100.0:
        return "high"
    if i == 50.0:
        return "medium"
    if i == 15.0:
        return "very_low"
    if i == 10.0:
        return "very_low"  
    if i == 90.0:
        return "high" 
    if i == 20.0:
        return "very_low"
    if i == 97.0:
        return "high"
    if i == 85.0:
        return "high"
    if i == 80.0:
        return "high"
    if i == 70.0:
        return "medium"
    if i == 60.0:
        return "medium"
    if i == 45.0:
        return "low"
    if i == 25.0:
        return "very_low"
    else:
        return "very_low"
data.Direct_Export.unique().shape
(16,)
data['Direct_Export'] = data['Direct_Export'].apply(dummy_direct)
data.Direct_Export.value_counts()
very_low    252
high         50
medium       11
low           3
Name: Direct_Export, dtype: int64
data.columns
Index(['Sales_Performance', 'Idustry_Type', 'Current_Situation',
       'Hours_Worked_Per_Week', 'Demand_For_Product',
       'Supply_Of_Raw_Materials', 'Financial_Performance', 'Online_Business',
       'Production_Conversion', 'Received_Any_Establishment',
       'Remote_Work_Arrangements', 'Direct_Export', 'Indirect_Export'],
      dtype='object')
data = data.reindex(['Sales_Performance', 'Idustry_Type', 'Current_Situation', 'Direct_Export', 'Indirect_Export',
                    'Hours_Worked_Per_Week', 'Demand_For_Product',
                    'Supply_Of_Raw_Materials', 'Financial_Performance', 'Online_Business',
                    'Production_Conversion', 'Received_Any_Establishment','Remote_Work_Arrangements'],axis=1)
data.columns
Index(['Sales_Performance', 'Idustry_Type', 'Current_Situation',
       'Direct_Export', 'Indirect_Export', 'Hours_Worked_Per_Week',
       'Demand_For_Product', 'Supply_Of_Raw_Materials',
       'Financial_Performance', 'Online_Business', 'Production_Conversion',
       'Received_Any_Establishment', 'Remote_Work_Arrangements'],
      dtype='object')
data.head(4)
Sales_Performance	Idustry_Type	Current_Situation	Direct_Export	Indirect_Export	Hours_Worked_Per_Week	Demand_For_Product	Supply_Of_Raw_Materials	Financial_Performance	Online_Business	Production_Conversion	Received_Any_Establishment	Remote_Work_Arrangements
0	Decrease	Manufacturing	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	No	No	No	No
1	Remain the same	Retail services	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	Yes	Yes	No	No
2	Decrease	Retail services	Open	very_low	very_low	Decrease	Decrease	Remain the same	Decrease	Yes	Yes	No	Yes
3	Decrease	Manufacturing	Temporarily closed	very_low	very_low	Decrease	Decrease	Decrease	Decrease	No	No	No	No
data["Sales_Performance"] = data["Sales_Performance"].map({'Decrease':0,'Remain the same':1,'Increase':2})
data["Sales_Performance"] = data["Sales_Performance"].astype(int)
data.head(4)
Sales_Performance	Idustry_Type	Current_Situation	Direct_Export	Indirect_Export	Hours_Worked_Per_Week	Demand_For_Product	Supply_Of_Raw_Materials	Financial_Performance	Online_Business	Production_Conversion	Received_Any_Establishment	Remote_Work_Arrangements
0	0	Manufacturing	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	No	No	No	No
1	1	Retail services	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	Yes	Yes	No	No
2	0	Retail services	Open	very_low	very_low	Decrease	Decrease	Remain the same	Decrease	Yes	Yes	No	Yes
3	0	Manufacturing	Temporarily closed	very_low	very_low	Decrease	Decrease	Decrease	Decrease	No	No	No	No
data.to_stata('Actual_data_of_Angolia.dta')
import pandas as pd
import numpy as np
data = pd.read_stata("C:\\Users\\Lenovo\\Desktop\\webapp\\Baijuu\\Actual_data_of_Angolia.dta")
del data['index']
data.head(5)
Sales_Performance	Idustry_Type	Current_Situation	Direct_Export	Indirect_Export	Hours_Worked_Per_Week	Demand_For_Product	Supply_Of_Raw_Materials	Financial_Performance	Online_Business	Production_Conversion	Received_Any_Establishment	Remote_Work_Arrangements
0	0	Manufacturing	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	No	No	No	No
1	1	Retail services	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	Yes	Yes	No	No
2	0	Retail services	Open	very_low	very_low	Decrease	Decrease	Remain the same	Decrease	Yes	Yes	No	Yes
3	0	Manufacturing	Temporarily closed	very_low	very_low	Decrease	Decrease	Decrease	Decrease	No	No	No	No
4	0	Manufacturing	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	Yes	Yes	No	No
data.Sales_Performance.value_counts()
0    262
1     34
2     20
Name: Sales_Performance, dtype: int64
# Considering the 1 and 2 as 1, because, 0 means covid Affected the company and the sales decreases. 1 means that covid not affected the company. sales is constand or increaase.
def change(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return 1
data["Sales_Performance"] = data["Sales_Performance"].apply(change)
data.Sales_Performance.value_counts()
0    262
1     54
Name: Sales_Performance, dtype: int64
data.head(3)
Sales_Performance	Idustry_Type	Current_Situation	Direct_Export	Indirect_Export	Hours_Worked_Per_Week	Demand_For_Product	Supply_Of_Raw_Materials	Financial_Performance	Online_Business	Production_Conversion	Received_Any_Establishment	Remote_Work_Arrangements
0	0	Manufacturing	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	No	No	No	No
1	1	Retail services	Open	very_low	very_low	Decrease	Decrease	Decrease	Decrease	Yes	Yes	No	No
2	0	Retail services	Open	very_low	very_low	Decrease	Decrease	Remain the same	Decrease	Yes	Yes	No	Yes
# Industry type
data['Idustry_Type'].value_counts()
Other services     130
Manufacturing      119
Retail services     67
Name: Idustry_Type, dtype: int64
data['Idustry_Type'] =data['Idustry_Type'].map({'Other services':'Other','Manufacturing':'Manufacturing','Retail services':'Retail'})
data['Idustry_Type'].value_counts()
Other            130
Manufacturing    119
Retail            67
Name: Idustry_Type, dtype: int64
# Current Situation 
data["Current_Situation"].value_counts()
Open                  279
Temporarily closed     37
Name: Current_Situation, dtype: int64
data.shape
(316, 13)
data["Current_Situation"] = data["Current_Situation"].map({'Open':'Open','Temporarily closed':'Temporarily_Closed'})
data["Current_Situation"].value_counts()
Open                  279
Temporarily_Closed     37
Name: Current_Situation, dtype: int64
data['Direct_Export'].value_counts()
very_low    252
high         50
medium       11
low           3
Name: Direct_Export, dtype: int64
data['Direct_Export'] = data['Direct_Export'].map({'very_low':'Very_Low','high':'High','medium':'Medium','low':'Low'})
data['Direct_Export'].value_counts()
Very_Low    252
High         50
Medium       11
Low           3
Name: Direct_Export, dtype: int64
data.columns
Index(['Sales_Performance', 'Idustry_Type', 'Current_Situation',
       'Direct_Export', 'Indirect_Export', 'Hours_Worked_Per_Week',
       'Demand_For_Product', 'Supply_Of_Raw_Materials',
       'Financial_Performance', 'Online_Business', 'Production_Conversion',
       'Received_Any_Establishment', 'Remote_Work_Arrangements'],
      dtype='object')
data['Indirect_Export'].value_counts()
very_low    308
high          3
low           3
medium        2
Name: Indirect_Export, dtype: int64
data['Indirect_Export'] = data['Indirect_Export'].map({'very_low':'Very_Low','high':'High','medium':'Medium','low':'Low'})
data['Indirect_Export'].value_counts()
Very_Low    308
Low           3
High          3
Medium        2
Name: Indirect_Export, dtype: int64
data['Hours_Worked_Per_Week'].value_counts()
Decrease           159
Remain the same    147
Increase            10
Name: Hours_Worked_Per_Week, dtype: int64
data['Hours_Worked_Per_Week'] = data['Hours_Worked_Per_Week'].map({'Decrease':'Decrease','Remain the same':'Remain_the_Same','Increase':'Increase'})
data['Hours_Worked_Per_Week'].value_counts()
Decrease           159
Remain_the_Same    147
Increase            10
Name: Hours_Worked_Per_Week, dtype: int64
data.columns
Index(['Sales_Performance', 'Idustry_Type', 'Current_Situation',
       'Direct_Export', 'Indirect_Export', 'Hours_Worked_Per_Week',
       'Demand_For_Product', 'Supply_Of_Raw_Materials',
       'Financial_Performance', 'Online_Business', 'Production_Conversion',
       'Received_Any_Establishment', 'Remote_Work_Arrangements'],
      dtype='object')
data["Demand_For_Product"].value_counts()
Decrease           218
Remain_the_Same     70
Increase            28
Name: Demand_For_Product, dtype: int64
data["Demand_For_Product"] = data["Demand_For_Product"].map({'Decrease':'Decrease','Remain the same':'Remain_the_Same','Increase':'Increase'})
data["Supply_Of_Raw_Materials"].value_counts()
Decrease           207
Remain the same     80
Increase            29
Name: Supply_Of_Raw_Materials, dtype: int64
data["Supply_Of_Raw_Materials"] = data["Supply_Of_Raw_Materials"].map({'Decrease':'Decrease','Remain the same':'Remain_the_Same','Increase':'Increase'})
data["Supply_Of_Raw_Materials"].value_counts()
Decrease           207
Remain_the_Same     80
Increase            29
Name: Supply_Of_Raw_Materials, dtype: int64
data["Financial_Performance"].value_counts()
Decrease           231
Remain_the_Same     45
Increase            40
Name: Financial_Performance, dtype: int64
data["Financial_Performance"] = data["Financial_Performance"].map({'Decrease':'Decrease','Remain the same':'Remain_the_Same','Increase':'Increase'})
data["Online_Business"].value_counts()
No     266
Yes     50
Name: Online_Business, dtype: int64
Angolia_Cleaned = pd.DataFrame(data.iloc[:,:10])
Angolia_Cleaned.head(4)
Sales_Performance	Idustry_Type	Current_Situation	Direct_Export	Indirect_Export	Hours_Worked_Per_Week	Demand_For_Product	Supply_Of_Raw_Materials	Financial_Performance	Online_Business
0	0	Manufacturing	Open	Very_Low	Very_Low	Decrease	Decrease	Decrease	Decrease	No
1	1	Retail	Open	Very_Low	Very_Low	Decrease	Decrease	Decrease	Decrease	Yes
2	0	Retail	Open	Very_Low	Very_Low	Decrease	Decrease	Remain_the_Same	Decrease	Yes
3	0	Manufacturing	Temporarily_Closed	Very_Low	Very_Low	Decrease	Decrease	Decrease	Decrease	No
data['Sales_Performance'].value_counts()
0    262
1     54
Name: Sales_Performance, dtype: int64
# change the Sales_Performance variable as a real format
def change(num):
    if num == 0:
        return 'Affeced'
    else:
        return 'Not_Affected'

data["Sales_Performance"] = data["Sales_Performance"].apply(change)
data['Sales_Performance'].value_counts()
Affeced         262
Not_Affected     54
Name: Sales_Performance, dtype: int64
Angolia_Cleaned_Data = pd.DataFrame(data.iloc[:,:10])
Angolia_Cleaned_Data.to_csv("Angolia_Cleaned_Data.csv",encoding="utf-8")
Angolia_Cleaned.head(3)
Sales_Performance	Idustry_Type	Current_Situation	Direct_Export	Indirect_Export	Hours_Worked_Per_Week	Demand_For_Product	Supply_Of_Raw_Materials	Financial_Performance	Online_Business
0	0	Manufacturing	Open	Very_Low	Very_Low	Decrease	Decrease	Decrease	Decrease	No
1	1	Retail	Open	Very_Low	Very_Low	Decrease	Decrease	Decrease	Decrease	Yes
2	0	Retail	Open	Very_Low	Very_Low	Decrease	Decrease	Remain_the_Same	Decrease	Yes
data = Angolia_Cleaned.copy()
data.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 316 entries, 0 to 315
Data columns (total 10 columns):
 #   Column                   Non-Null Count  Dtype   
---  ------                   --------------  -----   
 0   Sales_Performance        316 non-null    int64   
 1   Idustry_Type             316 non-null    category
 2   Current_Situation        316 non-null    category
 3   Direct_Export            316 non-null    object  
 4   Indirect_Export          316 non-null    object  
 5   Hours_Worked_Per_Week    316 non-null    category
 6   Demand_For_Product       316 non-null    category
 7   Supply_Of_Raw_Materials  316 non-null    category
 8   Financial_Performance    316 non-null    category
 9   Online_Business          316 non-null    category
dtypes: category(7), int64(1), object(2)
memory usage: 22.7+ KB
dummy = pd.DataFrame(data.iloc[:,1:])
y = pd.DataFrame(data.iloc[:,:1])
data.to_csv('Angolia_Cleaned_Data_with_y.csv',encoding='utf-8')
dummy = pd.get_dummies(dummy,drop_first=True)
dummy.head(3)
Idustry_Type_Retail	Idustry_Type_Other	Current_Situation_Open	Direct_Export_Low	Direct_Export_Medium	Direct_Export_Very_Low	Indirect_Export_Low	Indirect_Export_Medium	Indirect_Export_Very_Low	Hours_Worked_Per_Week_Remain_the_Same	Hours_Worked_Per_Week_Decrease	Demand_For_Product_Remain_the_Same	Demand_For_Product_Decrease	Supply_Of_Raw_Materials_Remain_the_Same	Supply_Of_Raw_Materials_Decrease	Financial_Performance_Remain_the_Same	Financial_Performance_Decrease	Online_Business_No
0	0	0	1	0	0	1	0	0	1	0	1	0	1	0	1	0	1	1
1	1	0	1	0	0	1	0	0	1	0	1	0	1	0	1	0	1	0
2	1	0	1	0	0	1	0	0	1	0	1	0	1	1	0	0	1	0
dummy.shape
(316, 18)
data = pd.concat([y,dummy],axis=1)
data.head(4)
Sales_Performance	Idustry_Type_Retail	Idustry_Type_Other	Current_Situation_Open	Direct_Export_Low	Direct_Export_Medium	Direct_Export_Very_Low	Indirect_Export_Low	Indirect_Export_Medium	Indirect_Export_Very_Low	Hours_Worked_Per_Week_Remain_the_Same	Hours_Worked_Per_Week_Decrease	Demand_For_Product_Remain_the_Same	Demand_For_Product_Decrease	Supply_Of_Raw_Materials_Remain_the_Same	Supply_Of_Raw_Materials_Decrease	Financial_Performance_Remain_the_Same	Financial_Performance_Decrease	Online_Business_No
0	0	0	0	1	0	0	1	0	0	1	0	1	0	1	0	1	0	1	1
1	1	1	0	1	0	0	1	0	0	1	0	1	0	1	0	1	0	1	0
2	0	1	0	1	0	0	1	0	0	1	0	1	0	1	1	0	0	1	0
3	0	0	0	0	0	0	1	0	0	1	0	1	0	1	0	1	0	1	1
data = data.astype(int)
data.sample(5)
Sales_Performance	Idustry_Type_Retail	Idustry_Type_Other	Current_Situation_Open	Direct_Export_Low	Direct_Export_Medium	Direct_Export_Very_Low	Indirect_Export_Low	Indirect_Export_Medium	Indirect_Export_Very_Low	Hours_Worked_Per_Week_Remain_the_Same	Hours_Worked_Per_Week_Decrease	Demand_For_Product_Remain_the_Same	Demand_For_Product_Decrease	Supply_Of_Raw_Materials_Remain_the_Same	Supply_Of_Raw_Materials_Decrease	Financial_Performance_Remain_the_Same	Financial_Performance_Decrease	Online_Business_No
0	0	0	0	1	0	0	1	0	0	1	0	1	0	1	0	1	0	1	1
44	0	0	0	1	0	0	1	0	0	1	1	0	1	0	1	0	0	1	1
153	0	0	0	1	0	0	1	0	0	1	1	0	0	1	0	1	0	1	1
78	0	1	0	1	0	0	1	0	0	1	0	1	0	1	0	1	0	0	1
101	0	0	1	1	0	0	1	0	0	1	1	0	1	0	1	0	0	1	1
Logistic Regression in whole data for identifying the importance of dummy features
import statsmodels.formula.api as sm
logit_model=sm.logit('Sales_Performance~Idustry_Type_Retail+Idustry_Type_Other+Current_Situation_Open+Direct_Export_Low+Direct_Export_Medium+Direct_Export_Very_Low+Indirect_Export_Low+Indirect_Export_Medium+Indirect_Export_Very_Low+Hours_Worked_Per_Week_Remain_the_Same+Hours_Worked_Per_Week_Decrease+Demand_For_Product_Remain_the_Same+Demand_For_Product_Decrease+Supply_Of_Raw_Materials_Remain_the_Same+Supply_Of_Raw_Materials_Decrease+Financial_Performance_Remain_the_Same+Financial_Performance_Decrease+Online_Business_No',data = data).fit()
C:\Users\Lenovo\Anaconda3\lib\site-packages\statsmodels\tools\_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
  import pandas.util.testing as tm
Warning: Maximum number of iterations has been exceeded.
         Current function value: 0.213963
         Iterations: 35
C:\Users\Lenovo\Anaconda3\lib\site-packages\statsmodels\base\model.py:512: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  "Check mle_retvals", ConvergenceWarning)
logit_model.summary()
Logit Regression Results
Dep. Variable:	Sales_Performance	No. Observations:	316
Model:	Logit	Df Residuals:	297
Method:	MLE	Df Model:	18
Date:	Sun, 16 Aug 2020	Pseudo R-squ.:	0.5321
Time:	22:46:13	Log-Likelihood:	-67.612
converged:	False	LL-Null:	-144.50
Covariance Type:	nonrobust	LLR p-value:	1.365e-23
coef	std err	z	P>|z|	[0.025	0.975]
Intercept	3.5417	2.928	1.210	0.226	-2.197	9.280
Idustry_Type_Retail	-0.2157	0.676	-0.319	0.750	-1.540	1.109
Idustry_Type_Other	-0.6806	0.614	-1.109	0.268	-1.884	0.523
Current_Situation_Open	0.5496	1.080	0.509	0.611	-1.568	2.667
Direct_Export_Low	-17.8352	3.08e+04	-0.001	1.000	-6.04e+04	6.04e+04
Direct_Export_Medium	-0.6477	1.318	-0.491	0.623	-3.231	1.936
Direct_Export_Very_Low	0.6700	0.755	0.887	0.375	-0.810	2.150
Indirect_Export_Low	-0.9683	3.856	-0.251	0.802	-8.527	6.590
Indirect_Export_Medium	-10.8822	90.665	-0.120	0.904	-188.583	166.819
Indirect_Export_Very_Low	0.7363	1.609	0.458	0.647	-2.417	3.890
Hours_Worked_Per_Week_Remain_the_Same	-3.0081	2.045	-1.471	0.141	-7.016	1.000
Hours_Worked_Per_Week_Decrease	-2.3418	2.062	-1.136	0.256	-6.383	1.700
Demand_For_Product_Remain_the_Same	-1.4109	0.764	-1.846	0.065	-2.909	0.087
Demand_For_Product_Decrease	-3.7782	0.886	-4.263	0.000	-5.515	-2.041
Supply_Of_Raw_Materials_Remain_the_Same	-0.0338	0.764	-0.044	0.965	-1.532	1.464
Supply_Of_Raw_Materials_Decrease	-1.2690	0.876	-1.449	0.147	-2.986	0.448
Financial_Performance_Remain_the_Same	1.4088	0.736	1.913	0.056	-0.034	2.852
Financial_Performance_Decrease	-1.5771	0.633	-2.493	0.013	-2.817	-0.337
Online_Business_No	-0.5804	0.618	-0.939	0.348	-1.792	0.631
Train and Test split : Train for training the model , Test for validation check
y = data.iloc[:,:1]
X = data.iloc[:,1:]

from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test = train_test_split(X,y,test_size = 0.2)

print("train_shape :" ,X_train.shape[0])
print("test_shape: " ,X_test.shape[0])
train_shape : 252
test_shape:  64
Checking the dependent variable in train data is balanced or not
import matplotlib.pylab as plt
import seaborn as sns
plt.figure(figsize=(8,6))
plt.title("Sales_Affected = 0, Sales_Not_Affected = 1")
sns.countplot(y_train["Sales_Performance"])
<matplotlib.axes._subplots.AxesSubplot at 0x189507e6248>

Imbalanced dependent variable to balanced format through over sampling technique(SMOTE)
from imblearn.over_sampling import SMOTE # For treating Imbalance of the output variable in train data.
smote = SMOTE()
X_train_smote,y_train_smote = smote.fit_sample(X_train,y_train)
import matplotlib.pylab as plt
plt.figure(figsize=(6,4))
plt.title("Sales_Affected = 0, Sales_Not_Affected = 1")
sns.countplot(y_train_smote["Sales_Performance"])
<matplotlib.axes._subplots.AxesSubplot at 0x189531fd688>

Model 1 Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train_smote,y_train_smote)

y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
C:\Users\Lenovo\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
Confusion Matrix of Train data:
[[194  16]
 [ 15 195]]
Train Accuracy Score is : 92.61904761904762
 
 
Confusion Matrix of Test data:
[[51  1]
 [ 5  7]]
Test Accuracy Score is : 90.625
model 2: Logistic regression : except these following variables
'Production_Conversion_No',
'Received_Any_Establishment_No_but_expect_to_receive',
'Received_Any_Establishment_No', 'Remote_Work_Arrangements_No'
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train_smote,y_train_smote)

y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
Confusion Matrix of Train data:
[[194  16]
 [ 15 195]]
Train Accuracy Score is : 92.61904761904762
 
 
Confusion Matrix of Test data:
[[51  1]
 [ 5  7]]
Test Accuracy Score is : 90.625
C:\Users\Lenovo\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
Result of logistic regression
response = ['1','0','0','1','1','0','0','0','1','0','1','0','1','0','1','0','1','1']
response = pd.DataFrame(response)
response = response.T
response = response.astype(int)
pred = classifier.predict(response) 
pred[0]
0
model 3: K Nearest Neighbours (KNN) ,k=2
# K NEAREST NEIGHBOUR (KNN)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=4)
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
Confusion Matrix of Train data:
[[203   7]
 [ 13 197]]
Train Accuracy Score is : 95.23809523809523
 
 
Confusion Matrix of Test data:
[[52  0]
 [ 7  5]]
Test Accuracy Score is : 89.0625
C:\Users\Lenovo\Anaconda3\lib\site-packages\ipykernel_launcher.py:4: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  after removing the cwd from sys.path.
Support Vector Machine Classifier model with Linear Kernel
from sklearn.svm import SVC
classifier = SVC(kernel = "linear")
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
Confusion Matrix of Train data:
[[200  10]
 [ 15 195]]
Train Accuracy Score is : 94.04761904761905
 
 
Confusion Matrix of Test data:
[[51  1]
 [ 6  6]]
Test Accuracy Score is : 89.0625
C:\Users\Lenovo\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
Support Vector Machine Classifier model with Non Linear Kernel
from sklearn.svm import SVC
classifier = SVC(kernel = "poly")
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
Confusion Matrix of Train data:
[[204   6]
 [  8 202]]
Train Accuracy Score is : 96.66666666666667
 
 
Confusion Matrix of Test data:
[[51  1]
 [ 5  7]]
Test Accuracy Score is : 90.625
C:\Users\Lenovo\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
Confusion Matrix of Train data:
[[140  70]
 [  1 209]]
Train Accuracy Score is : 83.0952380952381
 
 
Confusion Matrix of Test data:
[[31 21]
 [ 3  9]]
Test Accuracy Score is : 62.5
C:\Users\Lenovo\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
Decision Tree classifier
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy',random_state = 0)
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
Confusion Matrix of Train data:
[[206   4]
 [  6 204]]
Train Accuracy Score is : 97.61904761904762
 
 
Confusion Matrix of Test data:
[[48  4]
 [ 4  8]]
Test Accuracy Score is : 87.5
Random Forest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 80,criterion = 'entropy',random_state = 0)
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
C:\Users\Lenovo\Anaconda3\lib\site-packages\ipykernel_launcher.py:3: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  This is separate from the ipykernel package so we can avoid doing imports until
Confusion Matrix of Train data:
[[206   4]
 [  6 204]]
Train Accuracy Score is : 97.61904761904762
 
 
Confusion Matrix of Test data:
[[51  1]
 [ 5  7]]
Test Accuracy Score is : 90.625
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
C:\Users\Lenovo\Anaconda3\lib\site-packages\sklearn\utils\validation.py:73: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  return f(**kwargs)
Confusion Matrix of Train data:
[[204   6]
 [  5 205]]
Train Accuracy Score is : 97.38095238095238
 
 
Confusion Matrix of Test data:
[[49  3]
 [ 5  7]]
Test Accuracy Score is : 87.5
Random Forest with parameter tuning
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(min_impurity_decrease=0.0001,n_estimators = 100,criterion = 'entropy',random_state = 0,min_samples_leaf=2,ccp_alpha=0.001)
classifier.fit(X_train_smote,y_train_smote)
y_pred = classifier.predict(X_train_smote)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Train data:")
print(confusion_matrix(y_train_smote,y_pred))
print("Train Accuracy Score is :",accuracy_score(y_train_smote,y_pred)*100)
print(" ")
print(" ")
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print("Confusion Matrix of Test data:")
print(confusion_matrix(y_test,y_pred))
print("Test Accuracy Score is :",accuracy_score(y_test,y_pred)*100)
C:\Users\Lenovo\Anaconda3\lib\site-packages\ipykernel_launcher.py:3: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  This is separate from the ipykernel package so we can avoid doing imports until
Confusion Matrix of Train data:
[[204   6]
 [  8 202]]
Train Accuracy Score is : 96.66666666666667
 
 
Confusion Matrix of Test data:
[[52  0]
 [ 4  8]]
Test Accuracy Score is : 93.75
#Selecting Random Forest
import pickle
pickle.dump(classifier,open('model.pkl','wb'))
X_train_smote.to_csv('X_train_smote.csv',encoding = 'utf-8')
y_train_smote.to_csv('y_train_smote.csv',encoding = 'utf-8')
X_test.to_csv('X_test.csv',encoding = 'utf-8')
y_test.to_csv('y_test.csv',encoding = 'utf-8')
X_train.to_csv('X_train.csv',encoding = 'utf-8')
y_train.to_csv('y_train.csv',encoding = 'utf-8')
