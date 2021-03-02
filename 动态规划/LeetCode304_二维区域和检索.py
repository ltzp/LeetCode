#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/02
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode304_二维区域和检索.py
# @Desc    :

"""
动态规划，二维数组的前缀和
"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        if row <= 0:
            return
        col = len(matrix[0])
        self.dp =[[0 for j in range(col+1)] for i in range(row+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i+1][j+1] = self.dp[i][j+1] + self.dp[i+1][j] + matrix[i][j] - self.dp[i][j]



    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
        return result


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)
    param1 = numMatrix.sumRegion(1, 1, 2, 2)
    print(param1)
