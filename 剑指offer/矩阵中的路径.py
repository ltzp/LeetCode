#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 0030 21:34
# @Author  : Letao
# @Site    : 
# @File    : 矩阵中的路径.py
# @Software: PyCharm
# @desc    :
# TODO
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """




if __name__ == "__main__":
    solve = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    result = solve.exist(board, word)
    print(result)
