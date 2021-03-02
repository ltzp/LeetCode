#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/25
# @Author  : yuetao
# @Site    : 
# @File    : n个骰子的点数.py
# @Desc    :
"""
第几个骰子出现第几的次数。例如：2个骰子出现3的次数，(2,1)(1,2) -> 2/36 -> 1/18

dp[i][j]：第i个骰子出现j的概率
"""


class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp =[[0 for j in range(6*n + 1)] for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1/6
        for i in range(2, n + 1):
            for j in range(i, 6*i + 1):
                for k in range(1,7):
                    if j - k < 1:
                        continue
                    dp[i][j] += dp[1][k]*dp[i-1][j-k]
        res = [0 for _ in range(5*n + 1)]
        index = n
        for j in range(len(res)):
            res[j] = dp[n][index]
            index += 1
        return res

if __name__ == '__main__':
    n = int(input())
    solve = Solution()
    result = solve.dicesProbability(n)
    print(result)