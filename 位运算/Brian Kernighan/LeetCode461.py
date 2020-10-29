#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024 20:24
# @Author  : Letao
# @Site    : 
# @File    : LeetCode461.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        res = 0
        while xor:
            if xor & 1:
               res += 1
            xor = xor >> 1
        return res


if __name__ == "__main__":
    solve = Solution()
    x = int(input())
    y = int(input())
    result = solve.hammingDistance(x, y)
    print(result)