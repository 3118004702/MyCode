# series是一维的
# 导入
import pandas as pd

# 创建series数组->默认索引
print("创建series数组->默认索引")
t1 = pd.Series([1,2,3,12,3,4])
print(t1)
print(type(t1))
print("*"*60)

# 创建series数组->自建索引
print("创建series数组->自建索引")
t2 = pd.Series([1,23,2,2,3],index=list("abcde"))
print(t2)
print(t2.astype(float))
print("*"*60)

# 创建series数组->通过字典创建
print("创建series数组->通过字典创建")
temp_dict = {"name":"xiaohong","age":30,"tel":10086}
t3 = pd.Series(temp_dict)
print(t3)
print("*"*60)

# series数组索引
print("series数组索引")
print(t3)
print(t3["age"])
print(t3[1])
print(t3["tel"])
print(t3[2])
print(t3[:3])
print("*"*60)

# series数组取索引
print("series数组取索引")
a = t3.index
print(a)
for i in a:
    print(i)
print(type(t3.index))
print(list(t3.index))
print("*"*60)

# series数组取值
print("# series数组取值")
b = t3.values
print(b)
print(type(t3.values))

print("*"*60)
