#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 10:20
# @Author  : Letao
# @Site    : 
# @File    : LeetCode79_单词搜索.py
# @Software: PyCharm
# @desc    :


class Solution:
    def exist(self, boar, word: str) -> bool:
        if (not board or not board[0]):
            return False
        m = len(board)
        n = len(board[0])
        l = len(word)
        visited = [[False] * n for _ in range(m)]

        def track_back(i, j, k):
            if (k == l - 1):
                return board[i][j] == word[k]
            if (board[i][j] == word[k]):
                visited[i][j] = True
                for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    new_i, new_j = i + x, j + y
                    if (0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j] and track_back(new_i, new_j, k + 1)):
                        return True
                visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if (track_back(i, j, 0)):
                    return True
        return False


if __name__ == "__main__":
    solve = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    result = solve.exist(board, word)
    print(result)