# drop = drop all relevant indexes, only left 0 1 2 3..
# inplace = changes will be made in the respective ds / df
# ignore_index = true means the index will be reset 0 1 2 3 instead on 0 1 2 0 1

import pandas as pd 

# print simple data series 
print("Data series: ")
ds1 = pd.Series([2, 4, 6, 8, 10])
print(ds1)
print("")
print("---------------------")


print("------------type----------")
# type() gives the dtype of ds itself 
print("type()")
print(type(ds1))
print("")

# .dtypes gives the dtype of values 
print(".dtypes")
print(ds1.dtypes)
print("")
print("---------------------")

# math operation 
print("---------operation--------")
ds2 = pd.Series([1, 3, 5, 7, 9])
print("Add:")
ds = ds1 + ds2
print(ds)
print("Sub:")
ds = ds1 - ds2
print(ds)
print("Mul:")
ds = ds1 * ds2
print(ds)
print("Div:")
ds = ds1 / ds2
print(ds)
print("")
print("---------------------")

# sorting 
print("-----------sort-----------")
s = pd.Series(['3', '7', '2', 'python', '1'])
print(s)
s.sort_values(inplace=True)
print(s)
print("")
print("---------------------")

# add data with concat 
print("-----------concatenation----------")
s1 = pd.Series(['3', '7', '2', 'python', '1'])
s2 = pd.Series([5, 'c'])
s = pd.concat([s1, s2], ignore_index=True) 
# cant use drop cos default index is provided, just that the indexes for both ds will remain the same if not ignored
print(s1)
print(s2)
print(s)
print("")
print("---------------------")


# reindex
print("--------reindex--------")
s1 = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
print(s1)
s1 = s1.reindex(index=['B', 'A', 'C', 'E', 'D'])
print(s1)
print("")
print("---------------------")

# get location 
print("--------get_loc---------")
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s2 = pd.Series([1, 3, 5, 7, 10])
res = [pd.Index(s1).get_loc(i) for i in s2]
# get the location of indexes from s1 which values are also in s2
# but put it in a list 
# can also use isin 
res2 = s1[s1.isin(s2)]
list = res2.index.tolist()
print(res)
print(res2)
print(list)

# map 
# for each word, choose the letter according to index and map to upper 
print("--------map--------")
series1 = pd.Series(['php', 'python', 'java', 'c#'])
series2 = series1.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print(series2)
series2 = series1.map(lambda x : len(x))
print(series2)
print("")
print("---------------------")

# diff 
# diff between each value then put it into a list
print("---------diff-----------")
s1 = pd.Series([2, 3, 5, 6, 1, 9])
print(s1)
print(s1.diff().tolist())
print(s1.diff().diff().tolist())
print(s1.diff().diff().diff().tolist())
print("")
print("---------------------")

# return the index of min / max with idxmin / idxmax
print("Return index of min and max")
nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print(nums)
print(nums.idxmax())
print(nums.idxmin())
print("")
print("---------------------")

