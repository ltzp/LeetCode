#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31
# @Author  : yuetao
# @Site    : 
# @File    : 顺时针打印矩阵.py
# @Desc    :

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        operate = 0 #记录操作次数
        row = len(matrix)
        column = len(matrix[0])
        res = []
        record = 0 #记录res中存放的已经添加的数字个数
        all = row * column
        start_row, start_column, end_row, end_column = 0, 0, row - 1, column - 1 #记录每次循环起始和终止的行和列
        while True:
            if operate % 4 == 0:
                if record == all:
                    break
                for i in range(start_column, end_column + 1):
                    res.append(matrix[start_row][i])
                    record += 1
                start_row += 1
                operate += 1
            if operate % 4 == 1:
                if record == all:
                    break
                for i in range(start_row, end_row + 1):
                    res.append(matrix[i][end_column])
                    record += 1
                end_column -= 1
                operate += 1
            if operate % 4 == 2:
                if record == all:
                    break
                for i in range(end_column, start_column - 1, -1):
                    res.append(matrix[end_row][i])
                    record += 1
                end_row -= 1
                operate += 1
            if operate % 4 == 3:
                if record == all:
                    break
                for i in range(end_row, start_row - 1, -1):
                    res.append(matrix[i][start_column])
                    record += 1
                start_column += 1
                operate += 1
        return res


if __name__ == '__main__':
    solve = Solution()
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

    result = solve.spiralOrder(matrix)
    print(result)
