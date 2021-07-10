# 导入
import numpy as np

# 创建numpy数组
print("创建numpy数组")
t = np.arange(24).reshape(4,6).astype(float)
t[t<10] = 3
t[3,3] = np.nan
print(t)
print("*"*60)

# 深拷贝 --> 若直接用t1=t，则改变t1影响t
t1 = t.copy()
print(t1)
t1[:,0] = 0
print(t1)
# print(t)
print("*"*60)

# count_nonzero->计算非零个数方法
print("计算非零个数方法")
print(t1)
a = np.count_nonzero(t1)
print(a)
print("*"*60)

# 计算nan的个数->方法一-->利用np.nan != np.nan
print("计算nan的个数->方法一")
print(t)
b = np.count_nonzero(t != t)
print(b)
print("*"*60)

# 计算nan的个数->方法二
print("计算nan的个数->方法二")
print(t)
c = np.count_nonzero(np.isnan(t))
print(c)
print("*"*60)

# 和函数-->含有nan的一行或一列不能算
print(t)
t2 = np.sum(t,axis=0)   #0为列,1为行，None或不写为全部
print(t2)
print("*"*60)

# 均值
print("均值")
print(t)
t3 = np.mean(t,axis=0)
print(t3)
print("*"*60)

# 中值
print("中值")
print(t)
t4 = np.median(t,axis=0)
print(t4)
print("*"*60)

# 极值->最大值-最小值
print("极值")
print(t)
t5 = np.ptp(t,axis=0)
print(t5)
print("*"*60)

# 标准差
print("标准差")
print(t)
t6 = np.std(t,axis=0)
print(t6)
print("*"*60)
