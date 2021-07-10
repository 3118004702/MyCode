# -*- coding:utf-8 -*-
'''
将target与每行第一个数比较,从最后一行开始
target小则行rows减1
targetda则列clos加1

'''

class Solution:
    def Find(self, target, array):
        # 确定行列数
        rows = len(array) - 1
        cols = len(array[0]) - 1
        # 初始化i，j
        i = rows
        j = 0
        # 查找
        while i >= 0 and j <= cols:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:       #隐藏条件：target = array[i][j]
                return True
        # 查找失败
        return False