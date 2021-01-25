#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/25
# @Author  : yuetao
# @Site    : 
# @File    : 求1+2+n.py
# @Desc    :

class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        return int(((n + 1) * n)/2)

    def sumNumsTwo(self, n):
        if n == 1:
            return 1
        return n + self.sumNums(n - 1)

if __name__ == '__main__':
    solve = Solution()
    n = int(input())
    result = solve.sumNumsTwo(n)
    print(result)
