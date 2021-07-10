from matplotlib import pyplot as plt
from matplotlib import font_manager
# 输入数据
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

x = interval + [150]

# 图片大小

plt.figure(figsize=(20,8),dpi=80)

# x轴刻度
_x = [i-0.5 for i in range(13)]
plt.xticks(_x,x)

# 显示网格
plt.grid()

# 绘制条形图
plt.bar(range(12),quantity,width=1)

# 显示图形
plt.show()