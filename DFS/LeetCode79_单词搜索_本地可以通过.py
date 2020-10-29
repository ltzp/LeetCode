#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 10:20
# @Author  : Letao
# @Site    : 
# @File    : LeetCode79_单词搜索.py
# @Software: PyCharm
# @desc    :


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.grids = board
        self.row = len(board)
        self.cloumn = len(board[0])
        self.target = word
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        for i in range(self.row):
            for j in range(self.cloumn):
                if self.grids[i][j] == self.target[0]:
                    used = [[False for j in range(self.cloumn)] for i in range(self.row)]
                    if self.dfs(0, used, i, j):
                        return True
        return False

    def dfs(self, cur_index, used, row, cloumn):
        if used[row][cloumn]:
            return False
        if self.grids[row][cloumn] != self.target[cur_index]:
            return False
        if cur_index == len(self.target) - 1:
            return True
        used[row][cloumn] = True
        for i in range(4):
            new_row = row + self.dx[i]
            new_cloumn = cloumn + self.dy[i]
            if new_row >= 0 and new_row < self.row and new_cloumn >= 0 and new_cloumn < self.cloumn :
                if not used[new_row][new_cloumn]:
                    if self.dfs(cur_index + 1, used, new_row, new_cloumn):
                        return True
        used[row][cloumn] = False
        return False


if __name__ == "__main__":
    solve = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    result = solve.exist(board, word)
    print(result)
# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         self.grids = board
#         self.row = len(board)
#         self.cloumn = len(board[0])
#         self.target = word
#         self.dx = [-1, 1 , 0 , 0]
#         self.dy = [0, 0 , -1, 1]
#         for i in range(self.row):
#             for j in range(self.cloumn):
#                 if self.grids[i][j] == self.target[0]:
#                     used = [[False for j in range(self.cloumn)] for i in range(self.row)]
#                     if self.dfs(0, "", used, i, j):
#                         return True
#         return False
#
#     def dfs(self, cur_index, path, used, row, cloumn):
#         if used[row][cloumn]:
#             return True
#         if self.grids[row][cloumn] != self.target[cur_index]:
#             return False
#         if self.grids[row][cloumn] == self.target[cur_index]:
#             used[row][cloumn] = True
#             path += self.grids[row][cloumn]
#             if len(path) == len(self.target):
#                 return True
#             for i in range(4):
#                 new_row = row + self.dx[i]
#                 new_cloumn = cloumn + self.dy[i]
#                 if new_row >=0 and new_row < self.row and new_cloumn >=0 and new_cloumn < self.cloumn and not used[new_row][new_cloumn] and self.grids[new_row][new_cloumn] == self.target[cur_index+1]:
#                     if self.dfs(cur_index+1, path, used, new_row, new_cloumn):
#                         return True
#             return False