# 英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图
# 导入
import numpy as np
from matplotlib import pyplot as plt

# 导入外部数据
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")
t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

# 获取评论的数据
t_us_comments = t_us[:,-1]
print(t_us_comments.max(),t_us_comments.min())

# 选取评论数小于5000的
t_us_comments = t_us_comments[t_us_comments<=5000]
# 组数
d = 250
bin_nums = int((t_us_comments.max()-t_us_comments.min())/d)

# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制图形
plt.hist(t_us_comments,bin_nums)

# 显示图形
plt.show()