# 缺失数据的处理
# 导入
import pandas as pd
import numpy as np

# 创建含nan的DataFrame数组
t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
t.loc["b",["W","X"]] = np.nan
t.loc["c",:] = np.nan
print(t)

# 判断数据是否含有nan->nan为ture
print("判断数据是否含有nan->nan为ture")
print(t)
print(pd.isnull(t))
print("*"*60)

# 判断数据是否含有nan->nan为false
print("判断数据是否含有nan->nan为false")
print(t)
print(pd.notnull(t))
print("*"*60)

# 判断某列数据是否含有nan->nan为false
print("判断某列数据是否含有nan->nan为false")
print(t)
print(pd.notnull(t["W"]))
print("*"*60)

# 选取DataFrame数据中某列数据非nan的行
print("# 选取DataFrame数据中某列数据非nan的行")
print(t)
print(t[pd.notnull(t["W"])])
print("*"*60)

# 删除nan所在的行->只要含有nan（默认值）
print("删除nan所在的行->只要含有nan（默认值）")
print(t)
print(t.dropna(axis=0))
print(t.dropna(axis=0,how="any"))
print("*"*60)

# 删除nan所在的行->全部都是nan
print("删除nan所在的行->全部都是nan")
print(t)
print(t.dropna(axis=0,how="all"))
print("*"*60)

# 删除nan所在的行->全部都是nan->并且立刻重写
t1 = t.copy()
print("删除nan所在的行->任意都是nan->并且立刻重写")
print(t1)
print(t1.dropna(axis=0,how="all",inplace=True))
print(t1)
print("*"*60)

# 替换数据中的nan值
print("替换数据中的nan值")
print(t)
print(t.fillna(100))
print(t)
print("*"*60)

# 用均值替换数据中某列的nan值->不会改变原数据的值->忽略nan计算其他数值的均值
print("用均值替换数据中某列的nan值")
print(t)
print(t["Y"].fillna(t["Y"].mean()))
print(t)
print("*"*60)

# 用均值替换数据中的nan值
print("用均值替换数据中的nan值")
print(t)
print(t.fillna(t.mean()))
print(t)
print("*"*60)

