import pandas as pd 
import numpy as np

# mean & standard deviation
print("---------mean & sd----------")
s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print(s)
mean = s.mean();
sd = s.std()
print(mean)
print(sd)
print("")
print("---------------------")

# percentile 
# RandomState exposes a number of methods for generating random numbers drawn from a variety of probability distributions. 
# each method takes a keyword argument size that defaults to None. If size is None, then a single value is generated and returned. If size is an integer, 
# then a 1-D array filled with generated values is returned. If size is a tuple, then an array with that shape is filled and returned.
# NumPy random.normal() function in Python is used to create an array of specified shape and fills it with random values from a normal (Gaussian) distribution. 
print("---------percentile---------")
numstate = np.random.RandomState(100)
print(numstate)
ds = pd.Series(numstate.normal(10, 4, 20))
print(ds)
res = np.percentile(ds, q=[0, 25, 50, 75, 100])
print(res)
print("")
print("---------------------")

# frequency
# randomrandint generates values of random from 1-5 for 15 values 
print("-------frequency--------")
ds = pd.Series(np.random.randint(1, 5, 15))
print(ds)
print("Freq")
print(ds.value_counts())
# [:1] most freq
# [:2] until 2 most freq and so on 
# change those values in ds thats not in most freq to 'other'
ds[~ds.isin(ds.value_counts().index[:1])] = 'other'
print(ds)
print("")
print("---------------------")