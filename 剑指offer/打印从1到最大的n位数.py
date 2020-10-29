#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 0030 21:26
# @Author  : Letao
# @Site    : 
# @File    : 打印从1到最大的n位数.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n == 0:
            return res
        cur_num = 1
        while cur_num < 10 ** n:
            res.append(cur_num)
            cur_num +=1
        return res


if __name__ == "__main__":
    solve = Solution()
    n = int(input())
    result = solve.printNumbers(n)
    print(result)