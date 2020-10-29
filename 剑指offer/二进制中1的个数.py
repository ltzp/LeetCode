#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 0030 20:42
# @Author  : Letao
# @Site    : 
# @File    : 二进制中1的个数.py
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
            if n & 1:
                res += 1
            n = n >> 1
        return res
