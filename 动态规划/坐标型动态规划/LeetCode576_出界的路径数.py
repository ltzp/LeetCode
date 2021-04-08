#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/07
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode576_出界的路径数.py
# @Desc    :
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        Dir = [[0,-1], [-1, 0], [0, 1], [1, 0]]
        dp = [[[0] * (N+1) for _ in range(n)] * m for _ in range(m)]
        for k in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    for d in Dir:
                        dx = x + d[0]
                        dy = y + d[1]
                        if dx < 0 or dx >=m or dy < 0 or dy >= n:
                            dp[x][y][k] += 1
                        else:
                            dp[x][y][k] += dp[dx][dy][k-1]
        return dp[i][j][N] % (10 ** 9 + 7)


if __name__ == '__main__':
    solve = Solution()

