import pandas as pd 
import numpy as np
from datetime import datetime

print("--------Conversion---------")
ds1 = pd.Series([2, 4, 6, 8, 10])
# convert ds to list 
print("Convert ds to list")
listds = ds1.tolist()
print(listds)
print(type(listds))
print("")

# convert list to ds
print("Convert list to ds")
ds = pd.Series(list('012345'))
print(ds)
print("")

# convert arrays to ds 
print("Convert array to ds")
arr = np.array([1, 2, 3, 4, 5])
ds3 = pd.Series(arr)
print(ds3)
print("")

# convert ds to arrays
print("Convert ds to array")
s1 = pd.Series(['100', '200', 'python', '325.5', '400'])
arr = s1.values
print(arr)
print(type(arr))
print("")

# convert ds to numerical values only 
print("Convert ds to numerical values")
s1 = pd.Series(['100', '200', 'python', '325.5', '400'])
print(s1)
s2 = pd.to_numeric(s1, errors='ignore')
print(s2)
s3 = pd.to_numeric(s1, errors='coerce')
print(s3)
# s4 = pd.to_numeric(s1, errors='raise')
# this will raise an error 
print("")

# convert dict to ds 
print("Convert dict to ds")
d1 = {'a':100, 'b':200, 'c':300, 'd':400}
ds = pd.Series(d1)
print(ds)
print("")

# convert ds to df using to_frame 
print("Convert ds to df")
char_list = 'ABCDE'
num_array = range(5)
series = pd.Series(dict(zip(num_array, char_list)))
print(series)
df = series.to_frame(name='new df')
print(df)
df.reset_index(inplace=True)
print(df)
print("")

# convert series of list to series 
print("Convert series of list to series")
s = pd.Series([['red', 'green', 'blue'], 
              ['purple', 'yellow'], 
              ['white']])
print(s)
s1 = s.apply(pd.Series).stack().reset_index(drop=False)
print(s1)
s2 = s.apply(pd.Series).stack().reset_index(drop=True)
print(s2)
print("")


# convert ds to datetime 
print("Convert ds to datetime")
# 2 rules for converting series to the same date 
# 1. cant have year in the middle if the month is not in words 
# 2. can only choose 1 format to convert to datetime together if the format is in numbers 
ds = pd.Series(['2 jan 2015', 'jan 2 2015', '2015 jan 2', '2015 2 jan', 'jan 2 2015', 'jan 2015 2'])
ds2 = pd.Series('10-02-2016')
ds3 = pd.Series('20180703')
ds4 = pd.Series('2014/05/06')
ds5 = pd.Series('2019-04-06T11:20')
print(pd.to_datetime(ds))
print(pd.to_datetime(ds2))
print(pd.to_datetime(ds3))
print(pd.to_datetime(ds4))
print(pd.to_datetime(ds5))
print("")

# convert datetime to series 
print("Convert datetime to series")
dt = pd.to_datetime(ds)
ds2 = pd.Series(dt)
print(ds2)
print("")

print("Convert string to ds")
str1 = "abc def abcdef ab c i"
print(str1)
series = pd.Series(list(str1))
print(series)
print("")

# convert ds to string 
# convert to list, then series, then join
print("Convert ds to string")
print(series)
res = ''.join(series)
print(res)
print("")

# count the freq of each element
# drop the least freq element and replace the space with this element 
freq = series.value_counts()
print(freq)
drop = freq.dropna().index[-1]
print(drop)
series2 = series.replace(' ', drop)
print(series2)
res2 = ''.join(series2)
print(res2)
print("")


# convert ds to df 
print("Convert ds to df")
sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])
print("Original Series:")
print(sr1)
print(sr2)
# 1. 
df1 = pd.DataFrame(sr1, sr2).reset_index().rename(columns={0:'lang'})
print(df1)

#2. 
df2 = pd.DataFrame({'index':sr2, 'lang':sr1})
print(df2)
print("")