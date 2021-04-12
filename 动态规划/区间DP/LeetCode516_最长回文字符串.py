#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/11
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode516_最长回文字符串.py
# @Desc    :

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][length-1]


if __name__ == '__main__':
    solve = Solution()
    s = "bbbab"
    result = solve.longestPalindromeSubseq(s)
    print(result)
