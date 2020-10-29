#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024 20:56
# @Author  : Letao
# @Site    : 
# @File    : LeetCode191.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += 1
            n = n & (n-1)
        return res



if __name__ == "__main__":
    solve = Solution()
    n = int(input())
    result = solve.hammingWeight(n)
    print(result)