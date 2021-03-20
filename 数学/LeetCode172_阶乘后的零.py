#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/20
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode172_阶乘后的零.py
# @Desc    :

"""
/表示除法
//表示整数除法
以5为因子进行除法
"""
import sys
class Solution(object):
    def my_trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 1
        for i in range(2, n + 1):
            total *= i
        result = 0
        while total % 10 == 0:
            result += 1
            total //= 10
        return result

    def trailingZeroes(self, n):
        result = 0
        for i in range(5, n + 1,5):
            curr = i
            while curr % 5 == 0:
                result += 1
                curr //=5
        return result

if __name__ == '__main__':
    solve = Solution()
    n = int(sys.stdin.readline().strip())
    result = solve.trailingZeroes(n)
    print(result)
