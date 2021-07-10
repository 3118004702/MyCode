# 导入
import numpy as np

# 数据路径
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# numpy导入
t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int")
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)

# 打印
# print(t1)
# print("*"*100)
# print(t2)
#
# 取一行
# print(t1[2])
#
# 取连续的多行
# print(t1[2:])
#
# 取不连续的多行
# print(t1[2,8,10])
#
# 取一列
# print(t1[:,0])
#
# 取连续的多列
# print(t1[:,2:])
#
# 取不连续的多列
# print(t1[:,[0,2]])
#
# 取一个值
# print(t1[2,3])
#
# 取多行多列
# print(t1[2:5,1:4])
#
# 取多个值
# print(t1[[0,2,2],[0,1,3]])