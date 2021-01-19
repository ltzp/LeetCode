#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/12
# @Author  : yuetao
# @Site    : 
# @File    : 最长不含重复字符的子字符串.py
# @Desc    :
"""
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        length = len(s)
        if length <= 1:
            return length
        node = length
        while node > 0:
            i = 0
            while i + node <= length:
                str = s[i: i + node]
                hash_map = dict()
                for k in str:
                    if k not in hash_map:
                        hash_map[k] = 1
                    else:
                        break
                if len(hash_map) == node:
                    res = node
                    return res
                i += 1
            node -= 1
        return res


if __name__ == '__main__':
    pass
