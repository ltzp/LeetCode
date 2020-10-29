#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 0007 20:33
# @Author  : Letao
# @Site    : 
# @File    : LeetCode200_图的DFS.py
# @Software: PyCharm
# @desc    :图的深度遍历

class Solution(object):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, x, y):
        grid[x][y] = '0'
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or grid[new_x][new_y] == '0':
                continue
            self.dfs(grid, new_x, new_y)



if __name__ == "__main__":
    solve = Solution()
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    result = solve.numIslands(grid)
    print(result)
