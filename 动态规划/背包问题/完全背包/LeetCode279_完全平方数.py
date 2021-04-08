#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/07
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode279_完全平方数.py
# @Desc    :
import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i - j*j] + 1, dp[i])
                j += 1
        return dp[n]


if __name__ == '__main__':
    solve = Solution()
    n = int(sys.stdin.readline().strip())
    result = solve.numSquares(n)
    print(result)
