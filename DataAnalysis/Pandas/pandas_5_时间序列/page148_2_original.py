# 现在我们有2015到2017年25万条911的紧急电话的数据，请统计出出这些数据中不同类型的紧急情况的次数，如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？
# 导入
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)

# 读取csv文件
file_path = "C:\MyCode\DataAnalysis\Pandas\pandas_5_时间序列\911.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(5))


# 将时间变为pandas的时间序列
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

# 不同危险进行分类，并转化为一列
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
# print(len(care_list))
# print(care_list)
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))
# print(df.info())
# print(df.head(20))

# 将时间序列设置为索引
df.set_index("timeStamp",inplace=True)

# 画图
plt.figure(figsize=(20, 8), dpi=80)


# 分组
for group_name,group_data in df.groupby(by='cate'):
    count_by_month = group_data.resample("M").count()["title"]

    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)),_y,label=group_name)

plt.xticks(range(len(_x)),_x,rotation=45)
plt.legend(loc="best")
plt.show()