#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-22 22:02
# @Author  : Letao
# @Site    : 
# @File    : LeetCode242_有效的字母异位词.py
# @Software: PyCharm
# @desc    :


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_length = len(s)
        t_length = len(t)
        if s_length != t_length:
            return False
        hash_s = {}
        for i in range(s_length):
            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] = hash_s.get(s[i]) + 1
        hash_t = {}
        for i in range(t_length):
            if t[i] not in hash_t:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] = hash_t.get(t[i]) + 1
        if hash_t != hash_s:
            return False
        else:
            return True

if __name__ == "__main__":
    solve = Solution()
    s = "rat"
    t = "car"
    result = solve.isAnagram(s, t)
    print(result)