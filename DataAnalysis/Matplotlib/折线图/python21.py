# 导入
from matplotlib import pyplot as plt
import random
# from matplotlib import font_manager

# 数据
x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制图形
plt.plot(x,y)

# 显示中文
# my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHer.ttc")

# 绘制横坐标
_xtick_lables = ["10点{}分".format(i) for i in range(60)]
_xtick_lables += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::5],_xtick_lables[::5],rotation=45,fontproperties="SimHei")

# 添加描述信息
plt.xlabel("时间",fontproperties="SimHei")
plt.ylabel("温度",fontproperties="SimHei")
plt.title("10点到12点",fontproperties="SimHei")

# 保存图片
plt.savefig("./t2.png")

# 展示图片
plt.show()