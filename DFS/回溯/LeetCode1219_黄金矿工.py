#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/18
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1219_黄金矿工.py
# @Desc    :
class Solution(object):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        self.row = len(grid)
        self.column = len(grid[0])
        self.res = 0
        for i in range(self.row):
            for j in range(self.column):
                used = [[False for _ in range(self.column)] for c in range(self.row)]
                if grid[i][j] == 0:
                    continue
                else:
                    self.dfs(i, j, grid, used, 0)
        return self.res

    def dfs(self, i, j, grid, used, sum):
        if grid[i][j] == 0:
            return
        if 0 > i or i >= self.row or 0 > j or j >= self.column and used[i][j]:
            return
        sum += grid[i][j]
        used[i][j] = True
        self.res = max(sum, self.res)
        for index in range(4):
            new_x = i + self.dx[index]
            new_y = j + self.dy[index]
            if 0 <= new_x < self.row and 0 <= new_y < self.column and not used[new_x][new_y]:
                self.dfs(new_x, new_y, grid, used, sum)
        sum -= grid[i][j]
        used[i][j] = False


if __name__ == '__main__':
    solve = Solution()
    grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    result = solve.getMaximumGold(grid)
    print(result)
