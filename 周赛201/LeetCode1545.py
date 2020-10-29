#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 0010 17:32
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1545.py
# @Software: PyCharm
# @desc    :reverse(x) 返回反转 x 后得到的字符串，而 invert(x) 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）
"""
S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
S2 =  S1 + 1  + 反转后的S1
"""
class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        i = 1
        S = [0]
        while i < n:
            S = S + [1] + self.my_reversed(S)
            i += 1
        return (str(S[k - 1]))

    def my_reversed(self, S):
        for i in range(len(S)):
            if S[i] == 0:
                S[i] = 1
            else:
                S[i] = 0
        return (S[::-1])

if __name__ == "__main__":
    solve = Solution()
    n = 4
    k = 11
    result = solve.findKthBit(n, k)
    print(result)