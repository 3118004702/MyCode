import numpy as np
import pandas as pd

# 读取数据
file_path = "datasets_IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# 查看概览
print("查看概览")
print(df.info())
print(df.head(1))
print("*"*60)

# 获取平均分
print("获取平均分")
print(df["Rating"].mean())
print("*"*60)

# 导演的人数
print("导演的人数")
print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))
print("*"*60)

# 获取演员的人数
print("获取演员的人数")
temp_actors_list = df["Actors"].str.split(",").tolist()
actor_list = [i for j in temp_actors_list for i in j]
actors_num = len(set(actor_list))
print(actors_num)
print("*"*60)
