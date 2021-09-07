#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/09/07
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode130_被围绕的区域.py
# @Desc    :
class Solution(object):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.row = len(board)
        self.cloumn = len(board[0])
        for i in range(self.row):
            self.dfs(i, 0, board)
            self.dfs(i, self.cloumn - 1, board)
        for i in range(self.cloumn - 1):
            self.dfs(0, i, board)
            self.dfs(self.row-1, i, board)
        for i in range(self.row):
            for j in range(self.cloumn):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, x, y, board):
        if x < 0 or x > self.row-1 or y < 0 or y > self.cloumn - 1 or board[x][y] != 'O':
            return
        board[x][y] = 'A'
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            self.dfs(new_x, new_y, board)



if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # board = [["X","X","X"],["X","O","X"],["X","X","X"]]
    # board = [["X","O","X"],["X","O","X"],["X","O","X"]]
    # board = [["O","X","X","O","X"],
    #          ["X","O","O","X","O"],
    #          ["X","O","X","O","X"],
    #          ["O","X","O","O","O"],
    #          ["X","X","O","X","O"]]
    solve = Solution()
    res = solve.solve(board)
    print(res)
