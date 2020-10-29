#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 0030 11:40
# @Author  : Letao
# @Site    : 
# @File    : LeetCode5501.py
# @Software: PyCharm
# @desc    :
"""
https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island/
36.5
连通图：去掉一个点，其他连通块不连通
Tarjan 算法求割点
"""
class Solution(object):

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(self, i, j):
        self.st[i][j] = True
        for m in range(4):
            a = i + self.dx[m]
            b = j + self.dy[m]
            if a >=0 and a < self.n and b >=0 and b < self.m and not self.st[a][b] and self.grids[a][b] == 1:
                self.dfs(a, b)

    def check(self):
        cnt = 0
        self.st = [[False for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if not self.st[i][j] and self.grids[i][j] == 1:
                    cnt += 1
                    self.dfs(i, j)
        return cnt > 1

    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.n = len(grid)
        self.m = len(grid[0])
        self.grids = grid

        if self.check():
            return 0
        for i in range(self.n):
            for j in range(self.m):
                if self.grids[i][j]:
                    self.grids[i][j] = 0
                    if self.check():
                        return 1
                    self.grids[i][j] = 1
        return 2

if __name__ == "__main__":
    solve = Solution()
    grid =  [[0,0,0],[0,1,0],[0,0,0]]
    result = solve.minDays(grid)
    print(result)