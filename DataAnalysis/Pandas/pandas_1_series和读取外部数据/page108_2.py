# 导入
from pymongo import MongoClient
import pandas as pd

# 读取数据库文件
client = MongoClient()
collection = client["douban"]["tv1"]
data = list(collection.find())

print(data)

t1 = data[0]
t1 = pd.Series(t1)
print(t1)
