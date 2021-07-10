# 导入
import numpy as np

# 创建numpy数组
print("创建numpy数组")
t = np.arange(24)
t1 = t.reshape(4,6)
print(t)
print('*'*30)
print(t1)
print('*'*50)

# numpy中的布尔索引，显示t1中的值与比较的值的大小
print("numpy中的布尔索引，显示t1中的值与比较的值的大小")
t2 = t1 < 10
print(t2)
print('*'*50)

# t1中小于10的值赋为3
print("t1中小于10的值赋为3")
print(t1)
t1[t1<10] = 3
print(t1)
print('*'*50)

# 选出t1中大于20的值
print("选出t1中大于20的值")
print(t1)
t3 = t1[t1>20]
print(t3)
print('*'*50)

# numpy中的三元运算符
print("numpy中的三元运算符")
t4 = np.where(t1<=3,100,300)
print(t1)
print(t4)
print('*'*50)

# numpy中的裁剪
print("numpy中的裁剪")
print(t1)
t1 = t1.astype(float)
t1[3,3:] = np.nan
print(t1)
t5 = t1.clip(10,18)
print(t5)
