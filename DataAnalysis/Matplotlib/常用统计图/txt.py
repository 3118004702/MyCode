# 条形图
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 输入数据
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊" ]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]
y = range(len(a))

# 图片大小
plt.figure(figsize=(20,15),dpi=80)

# 显示中文
font = font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf",size=14)

# 绘制图形
plt.barh(b,y,height=0.3)

# 显示标签
plt.title("条形图",fontproperties=font)
plt.xlabel("票房数",fontproperties=font)
plt.ylabel("电影名称",fontproperties=font)

# 绘制图例
plt.legend(prop=font,loc="best")

# 纵坐标刻度
plt.yticks(y,a,fontproperties=font)

# 显示图形
plt.show()

# 保存图形
plt.savefig("./txt.png")