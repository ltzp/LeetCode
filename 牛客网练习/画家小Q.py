#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/16
# @Author  : yuetao
# @Site    : 
# @File    : 画家小Q.py
# @Desc    :
import sys


class Solution(object):

    def solve(self, row, cloumn, paints):
        self.m = row
        self.n = cloumn
        self.paints = paints
        result = 0
        for i in range(row):
            for j in range(cloumn):
                if self.paints[i][j] == "Y":
                    self.left_right(i, j)
                    result += 1
                elif self.paints[i][j] == "B":
                    self.right_left(i, j)
                    result += 1
                elif self.paints[i][j] == "G":
                    self.left_right(i, j)
                    self.paints[i][j] = "B"
                    self.right_left(i, j)
                    result += 2
        return result

    def left_right(self, i, j):
        if i >= 0 and i < self.m and j >= 0 and j < self.n and (self.paints[i][j] == "Y" or self.paints[i][j] == "G"):
            if self.paints[i][j] == "Y":
                self.paints[i][j] = "X"
            else:
                self.paints[i][j] = "B"
            self.left_right(i - 1, j - 1)
            self.left_right(i + 1, j + 1)

    def right_left(self, i, j):
        if i >= 0 and i < self.m and j >= 0 and j < self.n and (self.paints[i][j] == "B" or self.paints[i][j] == "G"):
            if self.paints[i][j] == "B":
                self.paints[i][j] = "X"
            else:
                self.paints[i][j] = "Y"
            self.right_left(i + 1, j - 1)
            self.right_left(i - 1, j + 1)


if __name__ == '__main__':
    nums = list(map(int, sys.stdin.readline().strip().split()))
    paint = []
    for i in range(nums[0]):
        line = sys.stdin.readline().strip()
        words = []
        for char in line:
            words.append(char)
        paint.append(words)
    solution = Solution()
    result = solution.solve(nums[0], nums[1], paint)
    print(result)
