# 现在我们有全球排名靠前的10000本书的数据，那么请统计一下下面几个问题：
# 不同年份书的数量
# 不同年份书的平均评分情况
# 导入
import pandas as pd
from matplotlib import pyplot as plt

# 读取csv文件
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_4_数据的合并和分组聚合\\books.csv"
df = pd.read_csv(file_path)

# 概览
# print(df.info())
# print(df.head(2))

# 选取非空的数据
data1 = df[pd.notnull(df["original_publication_year"])]
# print(data1)

# 按年份分组并且简化为一列数据-->不同年份数数量
# grouped = data1.groupby(by="original_publication_year")["title"].count()
# print(grouped)

# 按年份分组并且简化为一列数据-->不同年份书的平均评分
grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
print(grouped)

# 画图
_x = grouped.index
_y = grouped.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
plt.show()
