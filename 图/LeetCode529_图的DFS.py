#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 0020 15:13
# @Author  : Letao
# @Site    : 
# @File    : LeetCode529_图的DFS.py
# @Software: PyCharm
# @desc    : 扫雷游戏

class Solution(object):
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, 1, 1, -1, -1]
    row = 0
    cloumn = 0

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.row = len(board)
        self.cloumn = len(board[0])
        x = click[0]
        y = click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            self.dfs(board, x, y)
        return board

    def dfs(self, board, x, y):
        count = 0
        for i in range(8):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if new_x >= 0 and new_x < self.row and new_y >= 0 and new_y < self.cloumn and board[new_x][new_y] == 'M':
                    count +=1
        if count > 0:
            board[x][y] = chr(count + ord('0'))
            return
        board[x][y] = 'B'
        for i in range(8):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if new_x < 0 or new_x >= self.row or new_y < 0 or new_y >= self.cloumn or board[new_x][new_y] != 'E':
                continue
            self.dfs(board, new_x, new_y)


if __name__ == "__main__":
    solve = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    result = solve.updateBoard(board, click)
    print(result)
