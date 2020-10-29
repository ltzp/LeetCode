#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024 21:05
# @Author  : Letao
# @Site    : 
# @File    : LeetCode190.py
# @Software: PyCharm
# @desc    : 颠倒二进制位
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        power = 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res


if __name__ == "__main__":
    solve = Solution()
    n = int(input())
    result = solve.reverseBits(n)
    print(result)

