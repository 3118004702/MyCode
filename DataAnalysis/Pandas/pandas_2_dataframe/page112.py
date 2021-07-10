import numpy as np
import pandas as pd

# 导入外部数据
df = pd.read_csv("./dogNames2.csv")
print(df)
print("*"*60)

# 显示头几行
print("显示头几行")
print(df.head(5))
print("*"*60)

# 显示尾几行
print("显示尾几行")
print(df)
print(df.tail(3))
print("*"*60)

# 显示概览
print("显示概览")
print(df.info())
print("*"*60)

# 快速综合统计结果
print("快速综合统计结果")
print(df.describe())
print("*"*60)

# DataFrame中排序的方法->默认升序
print("DataFrame中排序的方法")
df = df.sort_values(by="Count_AnimalName",ascending=False)
print(df)
print("*"*60)

# DataFrame取行或列
# 取前20行
print("取前20行")
print(df[:20])
print("*"*60)

# 取Row_Labels列
print("取Row_Labels列")
print(df["Row_Labels"])
print("*"*60)
# Row_Labels列的属性
print("Row_Labels列的属性")
print(type(df["Row_Labels"]))