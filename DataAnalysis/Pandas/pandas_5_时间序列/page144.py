# 时间序列
# start->开始时间
# end->结束时间
# periods->生成几个
# freq->时间间隔
# 导入
import pandas as pd

# 创建时间序列
# 每隔一天
print("每隔一天")
date1 = pd.date_range(start="20171230",end="20180131",freq="D")
print(date1)
print("*"*60)

# 每隔十天
print("每隔十天")
date2 = pd.date_range(start="20171230",end="20180131",freq="10D")
print(date2)
print("*"*60)

# 每隔一天生成十个
print("每隔一天生成十个")
date3 = pd.date_range(start="20171230",periods=10,freq="D")
print(date3)
print("*"*60)

# 每隔一个月生成十个
print("每隔一个月生成十个")
date4 = pd.date_range(start="20171230",periods=10,freq="M")
print(date4)
print("*"*60)

# 每隔一个小时生成十个
print("每隔一个小时生成十个")
date5 = pd.date_range(start="20171230",periods=10,freq="H")
print(date5)
print("*"*60)

# 每个月的第一天
print("每隔一个小时生成十个")
date6 = pd.date_range(start="20171230",periods=10,freq="MS")
print(date6)
print("*"*60)