# 希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
# 导入
import numpy as np
from matplotlib import pyplot as plt

# 读取外部数据
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

# 选取评论数小于500000的数据
t_uk =  t_uk[t_uk[:,-1] < 500000]

# 输入数据
t_uk_comment = t_uk[:,-1]
t_uk_like = t_uk[:,1]

# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制图形
plt.scatter(t_uk_comment,t_uk_like)

# 显示图形
plt.show()