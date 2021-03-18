#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/18
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode115_不同的子序列.py
# @Desc    :
import sys

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_length = len(s)
        t_length = len(t)
        dp = [[0 for j in range(s_length + 1)] for i in range(t_length + 1)]
        for i in range(s_length + 1):
            dp[0][i] = 1
        for i in range(1, t_length + 1):
            for j in range(1, s_length + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    solve = Solution()
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    result = solve.numDistinct(s, t)
    print(result)