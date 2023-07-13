# more numpy functions on pandas 
import pandas as pd
import numpy as np

# where
# use random randint to generate integers from 1 to 9 of size 9
# then use where to print out the index of the series value that mod 5 = 0
print("--------where1.0-------")
ds = pd.Series(np.random.randint(1, 10, 9))
print(ds)
res = np.where(ds % 5 == 0)
print(res)
print("")
print("---------------------------")

print("--------where2.0-----------")
# 1   8   7   5   6   5   3   4   7   1
# +7  -1  -2  +1  -1  -2  +1  +3  -6
# 1   -1  -1  1   -1  -1  1   1   -1
# -2  0   +2  -2  0   +2  0   -2

# np.diff find diff between numbers 
# np.sign finds the sign 
# then diff again 
# now apply np.where 
num = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print(num)
temp = np.diff(np.sign(np.diff(num)))
res = np.where(temp==-2)
print(res)
print("")
print("---------------------------")


# take 
# take the value of the index specified 
print("---------take----------")
ds = pd.Series(list('2390238923902390239023'))
print(ds)
pos = [0, 2, 6, 11, 21]
res = ds.take(pos)
res2 = ds.take([5])
print(res)
print(res2)
print("")
print("---------------------------")

