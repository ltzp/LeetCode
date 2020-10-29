#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 0029 20:44
# @Author  : Letao
# @Site    : 
# @File    : 斐波拉契数列.py
# @Software: PyCharm
# @desc    :
"""
可以DP
可以递归
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        F = [0] * (n+1)
        if n == 0:
            return F[n]
        F[1] = 1
        for i in range(2, n+1):
            F[i] = F[i-1] + F[i-2]
        return F[n]%1000000007

if __name__ == "__main__":
    solve = Solution()
    n = 3
    result = solve.fib(n)
    print(result)