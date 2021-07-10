# 多次条形图
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 输入数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

bar_width = 0.2
x_14 = range(len(b_14))
x_15 = [i + bar_width for i in x_14]
x_16 = [i + 2 * bar_width for i in x_14]

# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 中文
font = font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf",size=14)

# 绘制图形
plt.bar(x_14,b_14,label="9月14日",width=bar_width)
plt.bar(x_15,b_15,label="9月15日",width=bar_width)
plt.bar(x_16,b_16,label="9月16日",width=bar_width)

# 标签
plt.title("多次条形图",fontproperties=font)
plt.xlabel("电影名称",fontproperties=font)
plt.ylabel("票房",fontproperties=font)

# 图例
plt.legend(prop=font,loc="best")

# 坐标轴刻度
plt.xticks(x_15,a,fontproperties=font)

# 显示图形
plt.show()

# 保存图片
plt.savefig("./duocitiaoxingtu.png")