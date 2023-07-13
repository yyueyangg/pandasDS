import pandas as pd
print("Check for inequlity")
df_data = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86], 'Y':[84,94,89,86,86],'Z':[86,97,96,72,83]});
sr_data = pd.Series([68, 75, 86, 80, None]) 
print("Original DataFrame:")
print(df_data)
print("\nOriginal Series:")
print(sr_data)
print("Check for inequality")
print(df_data.ne((sr_data), axis=0))
# print(sr_data.ne(df_data, axis=0))
# cant use something big to check for something small 

print("---------Compare-------")
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
print("Equals:")
print(ds1==ds2)
print("Greater than:")
print(ds1>ds2)
print("Lesser than:")
print(ds1<ds2)
print("")
print("---------------------")