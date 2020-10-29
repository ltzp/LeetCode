#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 0029 18:32
# @Author  : Letao
# @Site    : 
# @File    : LeetCode6_Z字形变换.py
# @Software: PyCharm
# @desc    :
"""
找间隔规律
每行进行循环
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        length = len(s)
        res = ""
        space = 2 * numRows - 2
        for i in range(0, numRows):
            j = 0
            while j+i < length:
                if j + i >= length:
                    break
                res += s[j+i]
                if i != 0 and i != numRows-1 and j + space - i < length:
                    res += s[j + space - i]
                j += space
        return res


if __name__ == "__main__":
    solve = Solution()
    s = "LEETCODEISHIRING"
    numRows = 4
    result = solve.convert(s, numRows)
    print(result)
