#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/27
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode205_同构字符串.py
# @Desc    :
"""
输入: s = "egg", t = "add"
输出: true
record_map 记录映射的值
used_char 字符是否被映射
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length_s = len(s)
        length_t = len(t)
        if length_s != length_t:
            return False
        record_map = {}
        used_char = []
        for i in range(length_s):
            if s[i] not in record_map:
                record_map[s[i]] = t[i]
                if t[i] in used_char:
                    return False
                used_char.append(t[i])
            else:
                if record_map.get(s[i]) != t[i]:
                    return False
        return True


if __name__ == '__main__':
    solve = Solution()
    s = "ab"
    t = "aa"
    result = solve.isIsomorphic(s, t)
    print(result)
