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

# 获取分类
temp_list = df["title"].str.split(": ").tolist()
# print(temp_list[:20])
cate_list = list(set([i[0] for i in temp_list]))
# print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)
# print(type(zeros_df))
# print(zeros_df.iloc[:20])

# 赋值
for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1

# print(zeros_df.iloc[:20])

# 求和
sum_ret = zeros_df.sum(axis=0)
print(sum_ret)