# 统计出911数据中不同月份不同类型的电话的次数的变化情况
# 导入
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', None)   #显示完整的列
pd.set_option('display.max_rows', None)  #显示完整的行

# 读取外部数据
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_5_时间序列\911.csv"
df = pd.read_csv(file_path)
# print(df.head(5))
# df1 = df.copy()
# print(df1.info())
# print(df1.head(5))

# 提取分类的列并分割成列表
df_title_list = df["title"].str.split(": ").tolist()
jh_list = [set(i[0] for i in df_title_list)]
print(jh_list)
# print(df1_title_list[:20])
# print(type(df1_title_list))

# 将列表变为DataFrame数组
df_title_dataframe = pd.DataFrame(df_title_list)
# print(type(df_title_dataframe))
# print(df_title_dataframe.head(5))

# 将df1_title_dataframe的0列赋值给原数据的title列
df.loc[:,"title"] = df_title_dataframe.iloc[:,0]
# print(df.head(20))

# 选择
# for i in [0,1,2]:
#     print(t_list[i])
# 选取危险为EMS的
df_E = df[df.loc[:,"title"] == "EMS"].copy()
# print(df_E.info())
# print(df_E.head(5))

# 将时间那一列设为padans的时间序列
df_E.loc[:,"timeStamp"] = pd.to_datetime(df_E.loc[:,"timeStamp"])

# 将时间序列设为索引
df_E.set_index("timeStamp",inplace=True)
# print(df_E.info)
# print(df_E.head(5))

# 统计出某一类中不同月份的电话的次数的变化情况
count_by_month = df_E.resample("M").count()["lat"]
print(count_by_month)
print("*"*60)