# 使用matplotlib呈现出店铺总数排名前10的国家
# 导入
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 读取csv文件
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_4_数据的合并和分组聚合\starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

# 查看概览
print(df.info())
print(df.head(3))

# 按国家进行分组
country_data = df.groupby(by=df["Country"])
# print(country_data.count())

# 对分组后的数据进行排序
country_data_sort = country_data["Brand"].count().sort_values(ascending=False)
# print(country_data_sort)

# 对排序后的数据进行选择-->店铺总数排名前10
df1 = country_data_sort.head(10)
# print(country_data_sort.head(10))

# 画图
# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 横坐标与纵坐标数据
_x = df1.index
# print(type(_x))
_y = df1.values

_xlabel = plt.xticks(range(len(_x)),_x)
# 画图
plt.bar(range(len(_x)),_y)
# 显示
plt.show()