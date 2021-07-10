# pandas重采样
# 统计出911数据中不同月份电话次数的变化情况
# 导入
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', None)   #显示完整的列
pd.set_option('display.max_rows', None)  #显示完整的行

# 读取外部数据
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_5_时间序列\911.csv"
df = pd.read_csv(file_path)

# 将时间那一列转化为pandas的时间序列
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
# print(df.head(5))

# 将时间那一列设置为索引
df.set_index("timeStamp",inplace=True)
# print(df.head(5))

# 统计出911数据中不同月份电话次数
count_by_month = df.resample("M").count()["lat"]
# print(count_by_month)
# print(type(count_by_month))

# 画图
plt.figure(figsize=(20,8),dpi=80)

# 输入横坐标和纵坐标数据
x = count_by_month.index
y = count_by_month.values

# 绘制横坐标并格式化数据-->去掉后面的具体时间
_x = [i.strftime("%Y-%m-%d") for i in x]
_x = plt.xticks(range(len(x)),_x,rotation = 45)

# 折线图
plt.plot(range(len(x)),y)

plt.show()