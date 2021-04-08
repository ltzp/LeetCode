#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/07
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode322_换零钱.py
# @Desc    :
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i >= coin and dp[i-coin] != float("inf"): #边界情况
                    dp[i] = min(dp[i-coin]+1, dp[i])
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


if __name__ == '__main__':
    solve = Solution()
    coins = [1, 2, 5]
    amount = 11
    result = solve.coinChange(coins, amount)
    print(result)
