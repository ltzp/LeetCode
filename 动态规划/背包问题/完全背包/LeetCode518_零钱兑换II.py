#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/07
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode518_零钱兑换II.py
# @Desc    :
"""
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
如果求组合数就是外层for循环遍历物品，内层for遍历背包

"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j - coin]
        return dp[amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    solve = Solution()
    result = solve.change(amount, coins)
    print(result)
