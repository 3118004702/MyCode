# 导入
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)

# 读取数据
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(5))
# print(df["Genre"])

# 统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()  # [[],[],[]]
# print(temp_list)
genre_list = list(set([i for j in temp_list for i in j]))
print(genre_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zeros_df)

# 给每个电影出现分类的位置赋值为1
for i in range(df.shape[0]):
        zeros_df.loc[i,temp_list[i]] = 1
# print(zeros_df)

# 统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis=0)
# print(genre_count)

# 排序
genre_count = genre_count.sort_values()
# print(genre_count)

# 画图
plt.figure(figsize=(20,8),dpi=80)
_x = genre_count.index
_y = genre_count.values
plt.bar(range(len(_x)),_y,width=0.3,color="orange")
plt.xticks(range(len(_x)),_x)
# plt.show()