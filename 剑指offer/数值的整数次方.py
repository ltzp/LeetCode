#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25
# @Author  : yuetao
# @Site    : 
# @File    : 数值的整数次方.py
# @Desc    :

"""

2^4 -> 2^2 * 2^2

"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        N = n
        if n < 0:
            x = float(1/x)
            N = -N
        res = float(1)
        while N > 0:
            if N & 1:
                res = res * x
            x = x * x
            N = N >> 1
        return res



if __name__ == '__main__':
    solve = Solution()
    x = int(input())
    n = int(input())
    result = solve.myPow(x, n)
    print(result)
