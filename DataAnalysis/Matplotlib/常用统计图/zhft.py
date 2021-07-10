# 直方图
# 导入
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 输入数据
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊" ]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]
x = range(len(a))

# 图片大小
plt.figure(figsize=(20,8),dpi=80)

# 显示中文
font = font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf",size=14)

# 绘制直方图
plt.bar(x,b,width=0.3)

# 标签
plt.xlabel("电影名字",fontproperties=font)
plt.ylabel("电影票房",fontproperties=font)
plt.title("直方图",fontproperties=font)

# 刻度详细信息
plt.xticks(x,a,fontproperties=font,rotation=270)

# 显示图片
plt.show()

# 保存图片
plt.savefig("./movie.png")