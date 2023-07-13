import pandas as pd 

s1 = pd.Series(list('abcdefghij'))
s2 = pd.Series(range(10))
# vertical stack using concat 
print("s5")
s5 = pd.concat([s1, s2], axis=0)
print(s5)

# horizontal stack using concat 
print("s6")
s6 = pd.concat([s1, s2], axis=1)
print(s6)