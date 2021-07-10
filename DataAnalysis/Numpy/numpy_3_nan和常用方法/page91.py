# 数组的拼接
import numpy as np

# 生成numpy数组
print("生成numpy数组")

t1 = np.arange(12).reshape(2,6)
t2 = np.arange(12,24).reshape(2,6)

print(t1)
print(t2)

print('*'*60)

# 竖直拼接->vertically
print("竖直拼接")

t3 = np.vstack((t1,t2))

print(t3)

print('*'*60)

# 水平拼接->horizontally
print("水平拼接")

t4 = np.hstack((t1,t2))

print(t4)

print('*'*60)

# 数组的行列交换
t5 = np.arange(12,24).reshape(3,4)

# 行交换
print(t5)

t5[[1,2],:] = t5[[2,1],:]

print(t5)

print("*"*60)

# 列交换
print(t5)

t5[:,[0,2]] = t5[:,[2,0]]

print(t5)

print('*'*60)