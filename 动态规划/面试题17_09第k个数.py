#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-01 23:12
# @Author  : Letao
# @Site    : 
# @File    : 面试题17_09第k个数.py
# @Software: PyCharm
# @desc    :


class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        dp = [None] * k
        dp[0] = 1
        a, b, c = 0, 0, 0
        for i in range(1, k):
            dp[i] = min(dp[a] * 3, dp[b] * 5, dp[c] * 7)
            if dp[i] == dp[a] * 3:
                a += 1
            if dp[i] == dp[b] * 5:
                b += 1
            if dp[i] == dp[c] * 7:
                c += 1
        return dp[k - 1]


if __name__ == "__main__":
    solve = Solution()
    k = 5
    result = solve.getKthMagicNumber(k)
    print(result)
