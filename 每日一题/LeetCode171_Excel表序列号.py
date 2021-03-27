#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/25
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode171_Excel表序列号.py
# @Desc    :
import sys

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        length = len(columnTitle)
        left_index = length - 1
        count = 1
        while left_index >= 0:
            cur_char = columnTitle[left_index]
            result += (ord(cur_char) - ord('A') + 1) * 26**(count-1)
            count += 1
            left_index -= 1
        return result


if __name__ == '__main__':
    solve = Solution()
    columnTitle = sys.stdin.readline().strip()
    result = solve.titleToNumber(columnTitle)
    print(result)