#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1289_下降路径最小和II.py
# @Desc    :
class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        if not arr:
            return 0
        row = len(arr)
        column = len(arr[0])
        dp = [[float("inf") for _ in range(column)] for _ in range(row)]
        for i in range(column):
            dp[0][i] = arr[0][i]
        for i in range(1, row):
            for j in range(column):
                pre_row_min = min(dp[i-1][:j] + dp[i-1][j+1:])
                dp[i][j] = pre_row_min + arr[i][j]
        return min(dp[row-1])


if __name__ == '__main__':
    solve = Solution()
    matrix = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
    result = solve.minFallingPathSum(matrix)
    print(result)
