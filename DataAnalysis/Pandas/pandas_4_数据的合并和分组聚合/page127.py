# 数据合并
# 导入
import numpy as np
import pandas as pd

# 定义df1
dict1 = {'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],'feature2':['low','medium','medium','high','low','high']}
df1 = pd.DataFrame(dict1)
# print(df1)

# 定义df2
dict2 = {'alpha':['A','A','B','F'],'pazham':['apple','orange','pine','pear'],'kilo':['high','low','high','mum'],'price':[5,6,5,7]}
df2 = pd.DataFrame(dict2)
# print(df2)

# 基于共同列的内连接
print("基于共同列的内连接")
df3 = pd.merge(df1,df2,how="inner",on='alpha')
print(df1)
print(df2)
print(df3)
print("*"*60)

# 基于共同列的外连接
print("基于共同列的外连接")
df4 = pd.merge(df1,df2,how="outer",on="alpha")
print(df1)
print(df2)
print(df4)
print("*"*60)

# 左连接
print("左连接")
df5 = pd.merge(df1,df2,how="left",on="alpha")
print(df1)
print(df2)
print(df5)
print("*"*60)

# 右连接
print("右连接")
df6 = pd.merge(df1,df2,how="right",on="alpha")
print(df1)
print(df2)
print(df6)
print("*"*60)