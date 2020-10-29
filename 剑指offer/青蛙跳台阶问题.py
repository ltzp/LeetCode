#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 0029 20:55
# @Author  : Letao
# @Site    : 
# @File    : 青蛙跳台阶问题.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        ways = [1]*(n+1)
        ways[1] = 1
        ways[2] = 2
        if n <= 2:
            return ways[n]
        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n] % 1000000007

if __name__ == "__main__":
    solve = Solution()
    n = int(input())
    result = solve.numWays(n)
    print(result)