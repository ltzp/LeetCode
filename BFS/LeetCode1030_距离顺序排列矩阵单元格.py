#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-17 22:25
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1030_距离顺序排列矩阵单元格.py
# @Software: PyCharm
# @desc    :
import collections
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        if R == 0 or C == 0:
            return [[]]
        arr = [[0 for j in range(C)]for i in range(R)]
        res = []
        my_deque = collections.deque()
        arr[r0][c0] = 1
        my_deque.append([r0, c0])
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]
        while my_deque:
            cur_x, cur_y = my_deque.popleft()
            if [cur_x, cur_y] not in res:
                res.append([cur_x, cur_y])
            for i in range(4):
                dx = cur_x + x[i]
                dy = cur_y + y[i]
                if dx < 0 or dx >= R or dy < 0 or dy >= C or arr[dx][dy] == 1 or [dx, dy] in res:
                    continue
                arr[dx][dy] = 1
                res.append([dx, dy])
                my_deque.append([dx, dy])
        return res




if __name__ == "__main__":
    solve = Solution()
    R = 2
    C = 3
    r0 = 1
    c0 = 2
    result = solve.allCellsDistOrder(R, C, r0, c0)
    print(result)