#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 0006 19:32
# @Author  : Letao
# @Site    : 
# @File    : 小红书.py
# @Software: PyCharm
# @desc    :
"""
10
2 3 4
5 3 2 6
"""
class Solution:

    def deal(self,X, L ,T, N, N_NUMS):
        dp = [float("inf")] * (X+1)
        if L > max(N_NUMS):
            return 0
        if L in N_NUMS:
            dp[L] = 1
        if T in N_NUMS:
            dp[T] = 1
        for i in range(T+1, X+1):
            if i in N_NUMS:
                dp[i] = min(dp[i-L], dp[i-T]) + 1
            else:
                dp[i] = min(dp[i - L], dp[i - T])
        return dp[X]


if __name__ == "__main__":
    solve = Solution()
    X = int(input())
    infos = input().split()
    L = int(infos[0])
    T = int(infos[1])
    N = int(infos[2])
    N_NUMS = [ int(i) for i in input().split()]
    result = solve.deal(X, L, T, N, N_NUMS)
    print(result)