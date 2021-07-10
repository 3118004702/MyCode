# 导入
from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

# 设置图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制折线图
plt.plot(x,y)

# 绘制x轴的刻度
_xtick_lables = [i/2 for i in range(4,49)]
plt.xticks(_xtick_lables)

# 保存
# plt.savefig("./t1.png")

# 显示
plt.show()