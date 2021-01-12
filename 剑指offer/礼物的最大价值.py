#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/10
# @Author  : yuetao
# @Site    : 
# @File    : 礼物的最大价值.py
# @Desc    :

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        cloumn = len(grid[0])
        dp =[[ 0 for j in range(cloumn)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, cloumn):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, row):
                dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, row):
            for j in range(1, cloumn):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    solve = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = solve.maxValue(grid)
    print(result)
