#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 0015 17:38
# @Author  : Letao
# @Site    : 
# @File    : 剪绳子I.py
# @Software: PyCharm
# @desc    :

#TODO


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        dp = [float("-inf")] * (n+1)
        dp[2] = 1
        dp[3] = 2
        for i in range(3, n+1):
            cur_status = []
            length = i
            while length > 1:



if __name__ == "__mian__":
    solve = Solution()
    n = int(input())
    result = solve.cuttingRope(n)
    print(result)