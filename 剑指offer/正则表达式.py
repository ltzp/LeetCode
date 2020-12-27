#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/26
# @Author  : yuetao
# @Site    : 
# @File    : 正则表达式.py
# @Desc    :

"""
动态规划
思路来源：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/jian-zhi-offer-19-zheng-ze-biao-da-shi-pi-pei-dong/
dp[i][j] 表示s的前i个字符是否被p的前j个字符匹配
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    elif dp[i][j - 1]:
                        dp[i][j] = True
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True
                    elif dp[i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True
                    elif dp[i - 1][j - 1] and p[j - 1] == '.':
                        dp[i][j] = True
        return dp[-1][-1]


if __name__ == '__main__':
    solve = Solution()
    s = "aab"
    p = "c*a*b"
    result = solve.isMatch(s, p)
    print(result)