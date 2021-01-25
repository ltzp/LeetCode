#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/25
# @Author  : yuetao
# @Site    : 
# @File    : 不用加减乘除做加法.py
# @Desc    :
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a = a & x
        b = b & x
        while b != 0:
            c = (a & b) << 1 & x
            a = a ^ b
            b = c
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    solve = Solution()
    a = int(input())
    b = int(input())
    result = solve.add(a, b)
    print(result)
