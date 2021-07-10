# 现在我们有北上广、深圳、和沈阳5个城市空气质量数据，请绘制出5个城市的PM2.5随时间的变化情况
# 导入
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', None)   #显示完整的列
pd.set_option('display.max_rows', None)  #显示完整的行

# 读取csv文件
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_6_案例\PM2.5\BeijingPM20100101_20151231.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(5))

# 将表示时间的几个字段组合成一个pandas的时间序列
period = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
# print(period)
# print(type(period))

# 在原数据后再增加一列
df["datetime"] = period
# print(df.info())
# print(df.head(5))

# 把datetime设置为索引
df.set_index("datetime",inplace=True)

# 进行降采样
df = df.resample("7D").mean()
# print(df.info())
# print(df.head(5))

# 处理缺失数据->删除缺失数据
# print(df["PM_US Post"])
data = df["PM_US Post"].dropna()
data_china = df["PM_Dongsi"].dropna()

# 画图
# 横坐标和纵坐标数据
x = data.index
x_china = data_china.index
y = data.values
y_china = data_china.values

# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 折线图
plt.plot(range(len(x)),y,label="us")
plt.plot(range(len(x_china)),y_china,label="china")

# 绘制图例
plt.legend(loc="best")

# 横坐标刻度
print(df.shape)    # 用于确定步长
plt.xticks(range(0,len(x),10),list(x)[::10],rotation=45)

# 显示图片
plt.show()




