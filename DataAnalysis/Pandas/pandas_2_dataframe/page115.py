# pandas选择
import numpy as np
import pandas as pd

# 创建DataFrame
t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
# print(t)

# 通过标签索引一个值->loc
print("通过标签索引一个值")
print(t)
print(t.loc["a","Z"])
print("*"*60)

# 通过标签索引一行->loc
print("通过标签索引一行")
print(t)
print(t.loc["a"])
print("*"*60)

# 通过标签索引一列->loc
print("通过标签索引一列")
print(t)
print(t.loc[:,"Y"])
print("*"*60)

# 通过标签索引多行->loc
print("通过标签索引多行")
print(t)
print(t.loc[["a","c"]])
print("*"*60)

# 通过标签索引多列->loc
print("通过标签索引多列")
print(t)
print(t.loc[:,["W","Z"]])
print("*"*60)

# 通过标签索引多行多列->loc
print("通过标签索引多行多列")
print(t)
print(t.loc[["a","b"],["W","Z"]])
print("*"*60)

# 通过位置索引一行
print("通过位置索引一行")
print(t)
print(t.iloc[1,:])
print("*"*60)

# 通过位置索引一列
print("通过位置索引一列")
print(t)
print(t.iloc[:,2])
print("*"*60)

# 通过位置索引多列
print("通过位置索引多列")
print(t)
print(t.iloc[:,[2,3]])
print("*"*60)

# 通过位置索引多行多列
print("通过位置索引多行多列")
print(t)
print(t.iloc[[0,2],[2,3]])
print("*"*60)