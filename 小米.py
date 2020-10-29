#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 0008 18:29
# @Author  : Letao
# @Site    : 
# @File    : 小米.py
# @Software: PyCharm
# @desc    :


class Solution(object):

    def deal(self, password):
        length = len(password)
        if length < 8 or length > 120:
            return 1
        digit, upper, lower, other = 0, 0, 0, 0
        for i in password:
            if i.isdigit():
                digit = 1
            elif i.isupper():
                upper = 1
            elif i.islower():
                lower = 1
            else:
                other = 1
        if digit and upper and lower and other:
            return 0
        else:
            return 2


if __name__ == "__main__":
    s = input()
    passwords = [ i for i in s.split()]
    solve = Solution()
    for i in passwords:
        print(solve.deal(i))