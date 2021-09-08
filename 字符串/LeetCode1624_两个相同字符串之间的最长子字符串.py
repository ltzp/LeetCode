#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/09/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1624_两个相同字符串之间的最长子字符串.py
# @Desc    :

import sys

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -1
        if not s:
            return res
        record_index = dict()
        length = len(s)
        for i in range(length):
            if s[i] not in record_index:
                record_index[s[i]] = [i]
            else:
                record_index[s[i]].append(i)
        res = 0
        for key,value in record_index.items():
            if len(value) >= 2:
                res = max(res, value[-1] - value[0])
        return res - 1


if __name__ == '__main__':
    solve = Solution()
    s = sys.stdin.readline().strip()
    res = solve.maxLengthBetweenEqualCharacters(s)
    print(res)
