#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 23:44
# @Author  : Letao
# @Site    : 
# @File    : LeetCode901_股票价格跨度.py
# @Software: PyCharm
# @desc    :
"""
单调递减的栈
"""
class StockSpanner(object):

    def __init__(self):
        self.stack = []


    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res



