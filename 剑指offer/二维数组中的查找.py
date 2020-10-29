#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 20:28
# @Author  : Letao
# @Site    : 
# @File    : 二维数组中的查找.py
# @Software: PyCharm
# @desc    :
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        cloumn = len(matrix[0])
        for i in range(row):
            for j in range(cloumn):
                if matrix[i][j] == target:
                    return True
        return False



if __name__ == "__main__":
    solve = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = int(input())
    result = solve.findNumberIn2DArray(matrix, target)
    print(result)
