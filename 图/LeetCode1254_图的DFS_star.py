#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 0007 22:14
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1254_图的DFS.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    res += int(self.dfs(grid,i,j))
        return res

    def dfs(self, grid, x, y):
        ans = True
        grid[x][y] = 1
        if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1:
            ans = False
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == 0:
                ans = self.dfs(grid, new_x, new_y) and ans
        return ans


if __name__ == "__main__":
    solve = Solution()
    grid = [[1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    result = solve.closedIsland(grid)
    print(result)
