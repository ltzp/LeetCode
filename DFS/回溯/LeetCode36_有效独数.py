#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 0015 23:10
# @Author  : Letao
# @Site    : 
# @File    : LeetCode36_有效独数.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.rows = [[False for j in range(10)]for i in range(9)]
        self.cols = [[False for j in range(10)] for i in range(9)]
        self.boxs = [[False for j in range(10)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                cur_char = board[i][j]
                if cur_char != '.':
                    n = ord(cur_char) - ord('0')
                    bx = int(j / 3)  # 列
                    by = int(i / 3)  # 行
                    if self.rows[i][n] or self.cols[j][n] or self.boxs[by * 3 + bx][n]:
                        return False
                    else:
                        self.rows[i][n] = True
                        self.cols[j][n] = True
                        self.boxs[by * 3 + bx][n] = True
        return True



if __name__ == "__main__":
    solve = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    result = solve.isValidSudoku(board)
    print(result)
