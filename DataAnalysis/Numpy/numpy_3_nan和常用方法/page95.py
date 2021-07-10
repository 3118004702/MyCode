# 导入
import numpy as np

# 生成全为0的numpy数组
print("生成全为0的numpy数组")
t1 = np.zeros((3,4))
print(t1)
print("*"*60)

# 生成全为1的numpy数组
print("生成全为1的numpy数组")
t2 = np.ones((4,5))
print(t2)
print("*"*60)

# 生成单位数组
print("生成单位数组")
t3 = np.eye(6)
print(t3)
print("*"*60)

# 返回最大值的位置
print("返回最大值的位置")
print(t3)
t4 = np.argmax(t3,axis=0)
print(t4)
print("*"*60)

# 返回最小值的位置
print("返回最小值的位置")
t3[t3==1] = -1
t5 = np.argmin(t3,axis=1)
print(t3)
print(t5)
print("*"*60)