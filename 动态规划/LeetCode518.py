#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 0010 19:55
# @Author  : Letao
# @Site    : 
# @File    : LeetCode518.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        #定义dp[i] 存放每个面额的存放的记录
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] = dp[i] + dp[i - coin]
        return dp[-1]

if __name__ == "__main__":
    solve = Solution()
    amount = 5
    coins = [1, 2, 5]
    result = solve.change(amount, coins)
    print(result)