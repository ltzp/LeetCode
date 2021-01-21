#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/19
# @Author  : yuetao
# @Site    : 
# @File    : 左旋转字符串.py
# @Desc    :
"""
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
"""


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]


if __name__ == '__main__':
    solve = Solution()
    s = "abcdefg"
    k = 2
    result = solve.reverseLeftWords(s, k)
    print(result)
