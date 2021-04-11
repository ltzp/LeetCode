#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode91_解码方法.py
# @Desc    :
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        length = len(s)
        dp = [0] * length
        dp[0] = 1
        for i in range(1, length):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    if i == 1:
                        dp[i] = 1
                    else:
                        dp[i] = dp[i-2]
            else:
                value = int(s[i-1]) * 10 + int(s[i])
                if 11 <= value <= 26:
                    if i == 1:
                        dp[i] = dp[0] + 1
                    else:
                        dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[length-1]


if __name__ == '__main__':
    solve = Solution()
    s = "2101"
    result = solve.numDecodings(s)
    print(result)
