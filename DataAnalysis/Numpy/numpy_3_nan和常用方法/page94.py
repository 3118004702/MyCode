# coding = utf-8
import numpy as np

# 文件路径
us_data = ""
uk_data = ""

# 加载国家数据
us_datas = np.loadtxt(us_data,delimiter=",",dtype=int)
uk_datas = np.loadtxt(uk_data,delimiter=",",dtype=int)

# 分别构造全为0，1的数据->shape[0]表示有多少行
zeros_data = np.zeros((us_datas.shape[0],1)).astype(int)
ones_data = np.ones((uk_datas.shape[0],1)).astype(int)

# 分别添加一列全为0,1的数据
us_datas = np.hstack((us_datas,zeros_data))
uk_datas = np.hstack((uk_datas,ones_data))

# 拼接两组数据
final_data = np.vstack((us_datas,uk_datas))