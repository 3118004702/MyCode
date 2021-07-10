# 导入
import random

import numpy as np

# 创建数组
print("创建数组")
t1 = np.array([1,2,3])
print(t1)
print(type(t1))    # t1的类型未numpy.array
print('*'*30)

t2 = np.array(range(10))
print(t2)
print(type(t2))
print('*'*30)

t3 = np.arange(4,10,2)
print(t3)
print(type(t3))
print(t3.dtype)   # t3中的数据的数据类型
print('*'*30)

# numpy中的数据类型
print("numpy中的数据类型")
t4 = np.array(range(1,4),dtype=float)
print(t4)
print('*'*30)

# numpy中的bool类型
print("numpy中的bool类型")
t5 = np.array([1,1,0,1,0,0],dtype=bool)
print(t5)
print(t5.dtype)
print('*'*30)

# 调整数据类型
print("调整数据类型")
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)
print('*'*30)

# numpy中的小数
print("numpy中的小数")
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)
t8 = np.round(t7,2)     # 取小数
print(t8)
