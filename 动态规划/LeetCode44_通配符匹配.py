#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/27
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode44_通配符匹配.py
# @Desc    :

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        #第一个字符开始是不是"*"
        for i in range(1, n):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]




if __name__ == '__main__':
    solve = Solution()
    s = "adceb"
    p = "*a*b"
    result = solve.isMatch(s, p)
    print(result)
