#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-08 21:15
# @Author  : Letao
# @Site    : 
# @File    : LeetCode122_买卖股票的最佳时机II.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        length = len(prices)
        if length <= 1:
            return res
        for i in range(1, length):
            if prices[i-1] < prices[i]:
                res += prices[i] - prices[i-1]
        return res



if __name__ == "__main__":
    solve = Solution()
    prices = [7,1,5,3,6,4]
    result = solve.maxProfit(prices)
    print(result)