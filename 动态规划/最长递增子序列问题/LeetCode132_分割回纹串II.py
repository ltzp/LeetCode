#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode132_分割回纹串II.py
# @Desc    :
"""
和最长递增子序列一样
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [length for i in range(length)]
        for i in range(length):
            if self.isPalindrome(s[0:i+1]):
                dp[i] = 0
                continue
            for j in range(0, i):
                if self.isPalindrome(s[j+1:i+1]):
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[length-1]

    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False


if __name__ == '__main__':
    solve = Solution()
    s = input()
    result = solve.minCut(s)
    print(result)
