# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties

# 输入数据
x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

# 图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图形
plt.plot(x, y)

# 显示中文
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

# 绘制坐标轴
xlabel = ["{}岁".format(i) for i in x]
plt.xticks(x, xlabel,fontproperties=font)

# 绘制网格
plt.grid(alpha=0.4)

# 显示图形
plt.show()

# 保存图形
plt.savefig("./t3.png")
