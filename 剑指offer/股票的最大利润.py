#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/25
# @Author  : yuetao
# @Site    : 
# @File    : 股票的最大利润.py
# @Desc    :

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        length = len(prices)
        dp = [0] * length
        dp[0] = 0
        re_value = dp[0]
        min_value = prices[0]
        for i in range(1, length):
            if prices[i] < min_value:
                min_value = prices[i]
            dp[i] = max(dp[i-1], prices[i] - min_value)
            if re_value < dp[i]:
                re_value = dp[i]
        return re_value


if __name__ == '__main__':
    solve = Solution()
    prices = [7,2,5,3,6,4,1,8]
    result = solve.maxProfit(prices)
    print(result)
