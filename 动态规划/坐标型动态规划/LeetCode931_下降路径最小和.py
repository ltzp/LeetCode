#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode931_下降路径最小和.py
# @Desc    :
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        column = len(matrix[0])
        dp = [[float("inf") for _ in range(column)] for _ in range(row)]
        for i in range(column):
            dp[0][i] = matrix[0][i]
        for i in range(1, row):
            for j in range(column):
                if i-1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + matrix[i][j])
                if i-1 >= 0 and 0 <= j < column:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + matrix[i][j])
                if i - 1 >= 0 and j + 1 < column:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + matrix[i][j])
        return min(dp[row-1])


if __name__ == '__main__':
    solve = Solution()
    matrix = [[-48]]
    result = solve.minFallingPathSum(matrix)
    print(result)
