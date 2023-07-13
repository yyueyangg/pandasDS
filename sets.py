import pandas as pd 
import numpy as np 

# find a subset 
print("--------subset-------")
s1 = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(s1)
n = 7
s2 = s1[s1<n]
print(s2)
print("")
print("---------------------")

# isin
print("-----------isin----------")
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 4, 6, 8, 10])

# check if 3 is in s1, true or false 
res1 = s1.isin([3])
print(res1)

# check if 5 is in s1, if have print the value and the index 
res2 = s1[s1.isin([5])]
print(res2)

# check those values in s1 thats in s2
res3 = s1[s1.isin(s2)]
print(res3)

# check those values in s1 thats not in s2
res4 = s1[~s1.isin(s2)]
print(res4)

# check those values in s2 thats in s1 
res5 = s2[s2.isin(s1)]
print(res5)

# check those values in s2 thats not in s1
res6 = s2[~s2.isin(s1)]
print(res6)

print("")
print("---------------------")

print("-------union & interesect--------")
# union = u     intersect = n
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 4, 6, 8, 10])
union = pd.Series(np.union1d(s1, s2))
print(union)
intersect = pd.Series(np.intersect1d(s1, s2))
print(intersect)
# check those values in union but not in intersect 
res = union[~union.isin(intersect)]
print(res)
print("")
print("---------------------")