#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/16
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode59_旋转矩阵II.py
# @Desc    :
import sys
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0 for i in range(n)] for j in range(n)]
        operate = 0
        count = 0
        total = n * n
        mid = int(n/2)
        start_row, start_column, end_row, end_column = 0, 0, n - 1, n - 1
        while True:
            if operate % 4 == 0:
                #从左到右
                if count == total:
                    nums[mid][mid] = total
                    break
                for i in range(start_column, end_column + 1):
                    count += 1
                    nums[start_column][i] = count
                start_row += 1
                operate += 1
            if operate % 4 == 1:
                #从上到下
                if count == total:
                    break
                for i in range(start_row, end_row + 1):
                    count += 1
                    nums[i][end_column] = count

                end_column -= 1
                operate += 1
            if operate % 4 == 2:
                #从右到左
                if count == total:
                    break
                for i in range(end_column, start_column - 1, -1):
                    count += 1
                    nums[end_row][i] = count

                end_row -= 1
                operate += 1
            if operate % 4 == 3:
                #从下到上
                if count == total:
                    break
                for i in range(end_row, start_row - 1, -1):
                    count += 1
                    nums[i][start_column] = count
                start_column += 1
                operate += 1

        return nums


if __name__ == '__main__':
    solve = Solution()
    n = int(sys.stdin.readline().strip())
    result = solve.generateMatrix(n)
    print(result)
