#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 0005 22:32
# @Author  : Letao
# @Site    : 
# @File    : LeetCode37_解读数.py
# @Software: PyCharm
# @desc    :

"""
self.rows：row记录这一行的值是否被用过
self.cols：col记录这一列的值是否被用过
self.boxs：boxs记录这小矩形是否被用过
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.rows = [[False for j in range(10)] for i in range(9)]
        self.cols = [[False for j in range(10)] for i in range(9)]
        self.boxs = [[False for j in range(10)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                cur_char = board[i][j]
                if cur_char != '.':
                    n = ord(cur_char) - ord('0')
                    bx = int(j / 3)  # 列
                    by = int(i / 3)  # 行
                    self.rows[i][n] = True
                    self.cols[j][n] = True
                    self.boxs[by * 3 + bx][n] = True
        # print(self.rows)
        # print(self.cols)
        # print(self.boxs)
        return self.dfs(board, 0, 0)

    def dfs(self, board, x, y):
        if y == 9:
            return True
        nx = (x + 1) % 9
        ny = y
        if nx == 0:
            ny = y + 1
        if board[y][x] != '.':
            return self.dfs(board, nx, ny)
        for i in range(1, 10):
            bx = int(x / 3)
            by = int(y / 3)
            box_key = by * 3 + bx
            if not self.rows[y][i] and not self.cols[x][i] and not self.boxs[box_key][i]:
                self.rows[y][i] = True
                self.cols[x][i] = True
                self.boxs[box_key][i] = True
                board[y][x] = chr(i + ord('0'))
                if self.dfs(board, nx, ny):
                    return True
                board[y][x] = '.'
                self.rows[y][i] = False
                self.cols[x][i] = False
                self.boxs[box_key][i] = False
        return False


if __name__ == "__main__":
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    solve = Solution()
    result = solve.solveSudoku(board)
    print(result)
