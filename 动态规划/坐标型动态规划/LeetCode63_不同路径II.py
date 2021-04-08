#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/07
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode63_不同路径II.py
# @Desc    :
"""
坐标型看移动的位置，根据移动的方向来判断状态
dp[i][j] = dp[i-1][j] , dp[i][j-1]
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        row = len(obstacleGrid)
        cloumn = len(obstacleGrid[0])
        dp = [[0 for _ in range(cloumn)] for i in range(row)]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for i in range(1, cloumn):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        for j in range(1, row):
            if obstacleGrid[j][0] == 1:
                dp[j][0] = 0
            else:
                dp[j][0] = dp[j-1][0]
        for i in range(1, row):
            for j in range(1, cloumn):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row-1][cloumn-1]



if __name__ == '__main__':
    obstacleGrid = [[0,1],[0,0]]
    solve = Solution()
    result = solve.uniquePathsWithObstacles(obstacleGrid)
    print(result)