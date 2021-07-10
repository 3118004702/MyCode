# 导入
import numpy as np
import pandas as pd

# 创建DataFrame数组
df = pd.DataFrame(np.arange(12,24).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
# print(df)

# 查看索引
print("查看索引")
print(df)
print(df.index)
print("*"*60)

# 修改索引
print("修改索引")
df.index = ["aa","bb","cc"]
print(df)
print(df.index)
print("*"*60)

# 根据索引重新构建数据-->未曾出现的索引，其行的值都为nan
print("根据索引重新构建数据-->未曾出现的索引，其行的值都为nan")
df1 = df.reindex(["aa","pp"])
print(df)
print(df1)
print("*"*60)

# 将某列设置为索引-->不保留原有数据
print("将某列设置为索引-->不保留原有数据")
df2 = df.set_index("Y")
print(df)
print(df2)
print("*"*60)

# 将某列设置为索引-->保留原有数据
print("将某列设置为索引-->保留原有数据")
df3 = df.set_index("Y",drop=False)
print(df)
print(df3)
print("*"*60)

# unique（）某列去重后的结果
print("unique（）某列去重后的结果")
df.index = ["ll","ll","mm"]
print(df)
print(df.index.unique())
print(len(df.index))
print(list(df.index))
print("*"*60)

# index索引有长度

# index索引对象可以转换成列表类型