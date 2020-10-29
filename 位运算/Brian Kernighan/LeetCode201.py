#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024 19:53
# @Author  : Letao
# @Site    : 
# @File    : LeetCode201.py
# @Software: PyCharm
# @desc    :位移相关的算法叫做「Brian Kernighan 算法」，它用于清除二进制串中最右边的 11

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while n > m:
            n = n & (n-1)
        return n

if __name__ == "__main__":
    solve = Solution()
    m = int(input())
    n = int(input())
    result = solve.rangeBitwiseAnd(m, n)
    print(result)