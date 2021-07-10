# 导入
import numpy as np
import pandas as pd
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)

# 读取csv数据
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(5))

# 按国家进行分组
grouped = df.groupby(by="Country")
# print(grouped)

# DataFrameGroupBy->将DataFramfe分为str和DataFrame两部分
# 可以进行遍历
# for i,j in grouped:
#     print(i,type(i))
#     print("-"*60)
#     print(j,type(j))
#     print("*"*60)

# 调用聚合方法
country_counts = grouped.count()       # 以不同国家为分类标准
# print(country_counts)
country_count = grouped["Brand"].count()   # 将数据缩减为一列
# print(country_count)

# 在美国和中国的店的数量
# print("在美国和中国的店的数量")
# print(country_count["US"])
# print(country_count["CN"])

# 在中国每个省份的店的数量
# china_data = df[df["Country"] == "CN"]
# china_gropued = china_data.groupby(by="State/Province")
# print(china_gropued["Brand"].count())

# 对多个字段进行分组-->双重索引
# grouped1 = df.groupby(by=["Country","State/Province"])['Country'].count()
# print(grouped1)
# print(type(grouped1))
grouped2 = df["Country"].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped2)
print(type(grouped2))

# 将上面的series变成DataFrame的创建方法-->多列成为DataFrame
# grouped3 = df[["Country"]].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped3)
# print(type(grouped3))
