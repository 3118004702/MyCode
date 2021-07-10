# 复合索引，通过复合索引取值
# 导入
import numpy as np
import pandas as pd

# 创建数组
df = pd.DataFrame(np.arange(12,24).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
# print(df)

# 将多列设置为索引-->drop为False时保留原数据
print("将多列设置为索引")
df1 = df.set_index(["X","Y"])
print(df)
print(df1)
print(df1.index)
print("*"*60)

# Series类型的复合索引-->df1[["W"]]为DataFrame类型
print("Series类型的复合索引")
s1 = df1["W"]
print(df)
print(s1)
print(type(s1))
print("*"*60)

# Series根据复合索引取值
print("Series根据复合索引取值")
print(s1)
print(s1[13][14])
print(s1[13,14])
print("-"*40)
print(s1[13])
print("*"*60)

# Series通过复合索引修改值
print("Series通过复合索引修改值")
print(s1)
s1[13][14] = 55
print(s1)
print("*"*60)

# swaplevel（）交换索引先后次序
print("swaplevel（）交换索引先后次序")
s2 = s1.swaplevel()
print(s1)
print(s2)
print("*"*60)

# DataFrame的复合索引
print("DataFrame的复合索引")
print(df1)
print("*"*60)

# DataFrame通过复合索引取值-->Series类型
print("DataFrame通过复合索引取值")
print(df1.loc[13].loc[14])
print(type(df1.loc[13].loc[14]))
print("*"*60)

# DataFrame通过复合索引取值-->DataFrame类型
print("DataFrame通过复合索引取值")
print(df1.loc[13])
print(type(df1.loc[13]))
print("*"*60)

# swaplevel（）交换索引先后次序
print("swaplevel（）交换索引先后次序")
df2 = df1.swaplevel()
print(df1)
print(df2)
print("*"*60)
