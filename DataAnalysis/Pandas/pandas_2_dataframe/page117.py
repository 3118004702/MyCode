# pandas之布尔索引
# 导入
import pandas as pd

# pandas读取CSV文件
df = pd.read_csv("./dogNames2.csv")
# print(df)

# 对df进行排序
df1 = df.sort_values(by="Count_AnimalName",ascending=False)
# print(df1)

# 选取狗的名字使用次数超过80小于100的
print("选取狗的名字使用次数超过80小于100的")
df2 = df[(df["Count_AnimalName"]>80)&(df["Count_AnimalName"]<100)]
print(df2)