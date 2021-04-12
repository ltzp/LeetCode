#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/11
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode5_最长回文子串.py
# @Desc    :
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s
        length = len(s)
        max_length = 1
        begin = 0
        dp = [[False] * length for i in range(0, length)]
        for i in range(0, length):
            dp[i][i] = True
        for j in range(1, length):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > max_length:
                    max_length = j-i+1
                    begin = i
        return s[begin: begin+max_length]


if __name__ == '__main__':
    solve = Solution()
    s = "a"
    result = solve.longestPalindrome(s)
    print(result)
