# DataFrame是二维的
import pandas as pd
import numpy as np

# 创建DataFrame
print("创建DataFrame数组")
t = np.arange(12).reshape(3,4)
t1 = pd.DataFrame(t)
print(t)
print(t1)
print("*"*60)

# 创建自己索引的DataFrame--index->横向索引--columns->纵向索引
t2 = pd.DataFrame(t,index=list("abc"),columns=list("WXYZ"))
print(t)
print(t2)
print("*"*60)

# 创建DataFrame->通过字典
print("创建DataFrame->通过字典")
d1 = {"name":["xiaoming","xiaohgang"],"age":[20,32],"tel":[10086,10010]}
t3 = pd.DataFrame(d1)
print(t3)
print("*"*60)

# 创建DataFrame->通过字典-->含有nan
print("创建DataFrame->通过字典")
d2 = [{"name":"xiaoming","age":32,"tel":10010},{"name":"xiaogang","tel":10000},{"name":"xiaoming","age":22}]
t4 = pd.DataFrame(d2)
print(t4)
print("*"*60)

# 获得DataFrame行索引
print("获得DataFrame行索引")
print(t4.index)
print("*"*60)

# 获得DataFrame列索引
print("获得DataFrame列索引")
print(t4.columns)
print("*"*60)

# 获得DataFrame对象值
print("获得DataFrame对象值")
print(t4.values)
print("*"*60)

# 获取DataFrame形状
print("获取DataFrame形状")
print(t4.shape)
print("*"*60)

# 获取DataFrame数据的数据类型
print("获取DataFrame数据的数据类型")
print(t4.dtypes)
print("*"*60)

# 查看DataFrame是几维的
print("查看DataFrame是几维的")
print(t4.ndim)
print("*"*60)
