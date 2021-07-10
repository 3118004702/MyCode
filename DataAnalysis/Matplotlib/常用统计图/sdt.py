# 绘制散点图
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 输入数据
x_3 = range(1,32)
x_10 = range(51,82)
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

# 图形大小
plt.figure(figsize=(20,8),dpi=80)

# 显示中文
font = font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf",size=14)

# 绘制图形
plt.scatter(x_3,y_3,label="3月")
plt.scatter(x_10,y_10,label="5月")

# 标签
plt.xlabel("时间",fontproperties=font)
plt.ylabel("温度",fontproperties=font)
plt.title("散点图",fontproperties=font)

# x轴细化
_x = list(x_3) + list(x_10)
_xticks_label = ["3月{}日".format(i) for i in x_3]
_xticks_label += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3],_xticks_label[::3],fontproperties=font,rotation=45)


# 绘制图例
plt.legend(prop=font,loc="best")

# 展示图形
plt.show()

# 保存图片
plt.savefig("./t1.png")

