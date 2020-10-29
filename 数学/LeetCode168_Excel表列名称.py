#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 0030 19:19
# @Author  : Letao
# @Site    : 
# @File    : LeetCode168_Excel表列名称.py
# @Software: PyCharm
# @desc    :


# TODO
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            temp = (n-1) % 26
            res = chr(temp + 65) + res
            n -= temp
            n = n //26
        print(res)
        return res

if __name__ == "__main__":
    # 52 AZ
    solve = Solution()
    n = int(input())
    result = solve.convertToTitle(n)