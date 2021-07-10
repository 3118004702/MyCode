# 现在我们有2015到2017年25万条911的紧急电话的数据，请统计出出这些数据中不同类型的紧急情况的次数
# 导入
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)   #显示完整的列
pd.set_option('display.max_rows', None)  #显示完整的行

# 读取csv文件
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_5_时间序列\911.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(8))

# 获取不同分类的列
df_title = df["title"]
# print(df_title[:20])

# 将其划分开
dif_title = df_title.str.split(": ").tolist()
# print(dif_title[:20])

# 将划分开的内容变成DataFrame数组
df_dif_title = pd.DataFrame(dif_title)
# print(type(df_dif_title))
# print(df_dif_title.info())
# print(df_dif_title.head(8))

# 对DataFrame数组分类
d = df_dif_title.groupby(by=0)
print(d.count())