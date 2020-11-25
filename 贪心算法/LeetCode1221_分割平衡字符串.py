#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-25 23:19
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1221_分割平衡字符串.py
# @Software: PyCharm
# @desc    :
"""
统计L，R的数量，如果相等就res + 1
"""


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        index = 0
        count_L, count_R = 0, 0
        while index < len(s):
            if s[index] == 'L':
                count_L += 1
            else:
                count_R += 1
            if count_L == count_R:
                res += 1
                count_L = count_R = 0
            index += 1
        return res


if __name__ == "__main__":
    solve = Solution()
    s = "RLLLLRRRLR"
    result = solve.balancedStringSplit(s)
    print(result)