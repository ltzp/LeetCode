#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/28
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode188_股票买卖.py
# @Desc    :
"""
dp[i][j]:表示j天,最多i次交易完成后，最大利润
"""



class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        length = len(prices)
        if k >= int(length/2):
            max_value = 0
            for i in range(1, length):
                if prices[i] > prices[i-1]:
                    max_value += prices[i] - prices[i-1]
            return max_value
        dp = [[0] * (length + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(1, length):
                val = 0
                for m in range(0, j+1):
                    val = max(val, prices[j] - prices[m] + dp[i-1][m])
                dp[i][j] = max(dp[i][j-1], val)
        return dp[k][length-1]

if __name__ == '__main__':
    solve = Solution()
    k = 2
    prices = [3,2,6,5,0,3]
    result = solve.maxProfit(k, prices)
    print(result)
