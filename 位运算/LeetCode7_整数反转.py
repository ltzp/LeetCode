#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024 23:44
# @Author  : Letao
# @Site    : 
# @File    : LeetCode7_整数反转.py
# @Software: PyCharm
# @desc    :

class Solution(object):


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > (2 ** 31) - 1 or x < (-2) ** 31:
            return 0
        flag = True
        if x < 0:
            flag = False
        x = abs(x)
        my_str = str(x)
        resver = my_str[::-1]
        if not flag:
            if -int(resver) < (-2) ** 31:
                return 0
            return -int(resver)
        if int(resver) > (2 ** 31) - 1:
            return 0
        return int(resver)

if __name__ == "__main__":
    solve = Solution()
    x = int(input())
    result = solve.reverse(x)
    print(result)
