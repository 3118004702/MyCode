# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 输入数据
x = range(11,31)
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 显示中文
font = font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=14)

# 绘制图形
plt.plot(x,y1,label="自己",linestyle='--')
plt.plot(x,y2,label="同桌",linestyle=':')

# 添加图例
plt.legend(prop = font,loc = "best")

# 绘制横坐标
_xticks_label =["{}岁".format(i) for i in x]
plt.xticks(x,_xticks_label,fontproperties=font)

# 显示图形
plt.show()

# 保存图片
plt.savefig("./t4.png")