#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 0015 17:38
# @Author  : Letao
# @Site    : 
# @File    : 剪绳子I.py
# @Software: PyCharm
# @desc    :

"""
dp[i] = dp[i-3] * 3
"""


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        dp = [float("-inf")] * (n+1)
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 6
        if n == 6:
            return 9
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        dp[6] = 9
        for i in range(7, n+1):
            dp[i] = 3 * dp[i-3]
        return dp[n]

if __name__ == "__main__":
    solve = Solution()
    n = int(input())
    result = solve.cuttingRope(n)
    print(result)