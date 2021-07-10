# 使用matplotlib呈现出每个中国每个城市的店铺数量
# 导入
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 读取csv文件
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_4_数据的合并和分组聚合\starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

# 查看概览
# print(df.info())
# print(df.head(3))

# 选取中国
cn_data = df[df["Country"] == "CN"]
# print(cn_data)

# 按城市进行分组并简化为一列数据
cn_data_group = cn_data.groupby(by = "City")
# print(cn_data_group.count())
cn_data_simple = cn_data_group["Brand"].count()[:25]
# print(cn_data_simple)

# 画图
# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# x轴和y轴数据
_x = cn_data_simple.index
_y = cn_data_simple.values
xlabel = plt.xticks(range(len(_x)),_x,rotation=60)

# 画图
plt.bar(range(len(_x)),_y,width=0.3,color="orange")
# 显示
plt.show()