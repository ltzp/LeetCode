#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 0011 20:44
# @Author  : Letao
# @Site    : 
# @File    : 机器人运动范围.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1
        self.used = [[False for j in range(0, n)] for i in range(0, m)]
        self.res = 0
        self.all_m = m
        self.all_n = n
        self.target = k
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
        self.dfs(0, 0)
        return self.res

    def dfs(self, row, col):
        if self.used[row][col] or self.get_sum(row, col) > self.target:
            return
        self.used[row][col] = True
        self.res += 1
        for i in range(4):
            new_x = row + self.dx[i]
            new_y = col + self.dy[i]
            if new_x < 0 or new_x >= self.all_m or new_y < 0 or new_y >= self.all_n:
                continue
            self.dfs(new_x, new_y)

    def get_sum(self, x, y):
        return int(x / 10) + x % 10 + int(y / 10) + y % 10


if __name__ == "__main__":
    solve = Solution()
    m = int(input())
    n = int(input())
    k = int(input())
    # m, n, k = 2, 3, 1
    result = solve.movingCount(m, n, k)
    print(result)
