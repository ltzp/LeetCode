#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 0010 21:51
# @Author  : Letao
# @Site    : 
# @File    : 面试题16.19大小面积.py
# @Software: PyCharm
# @desc    :水域的大小

class Solution(object):
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, 1, 1, -1, -1]
    s = 0
    def pondSizes(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not land:
            return res
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    self.s = 0
                    self.dfs(land, i, j)
                    res.append(self.s)
        return sorted(res)

    def dfs(self, land, x , y ):
        if land[x][y] != 0:
            return
        land[x][y] = 1
        self.s += 1
        for i in range(8):
            for j in range(8):
                new_x = x + self.dx[i]
                new_y = y + self.dy[j]
                if new_x < 0 or new_x >= len(land) or new_y < 0 or new_y >= len(land[0]) or land[new_x][new_y] != 0:
                    continue
                self.dfs(land, new_x, new_y)



if __name__ == "__main__":
    solve = Solution()
    lands = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]
    result = solve.pondSizes(lands)
    print(result)
