# 将每一列中的nan替换为该列其他非nan值的均值
# 导入
import numpy as np

# 替换方法
def fill_ndarray(t):
    for i in range(t.shape[1]):
        # 取得每一列
        t_col = t[:,i]
        # print(t_col)

        # 计算每一列中nan的个数
        nan_num = np.count_nonzero(np.isnan(t_col))
        # print(nan_num)

        # 判断列中是否有nan
        if nan_num > 0:
            # 取出列中非nan的值
            t_not_nan = t_col[t_col==t_col]
            # print(t_not_nan)

            # 计算列中非nan值的均值
            t_not_nan_mean = np.mean(t_not_nan)
            # print(t_not_nan_mean)

            # 将每一列的nan替换为非nan值的均值
            t_col[t_col != t_col] = t_not_nan_mean
            # print(t_col)
            # print(t)
    # 返回ndarray数组
    return t

# 主方法
if __name__ == '__main__':
    t = np.arange(24).reshape(4, 6).astype(float)
    t[1, 2:] = np.nan
    print(t)
    t1 = fill_ndarray(t)
    print(t1)