#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 0010 16:46
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1544.py
# @Software: PyCharm
# @desc    :"abBAcC"


class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        res = []
        res_str = ""
        res.append(ord(s[0]))
        for i in range(1, len(s)):
            if not res:
                res.append(ord(s[i]))
                continue
            end_char = res.pop()
            cur_char = ord(s[i])
            if abs(end_char - cur_char) == 32:
                continue
            res.append(end_char)
            res.append(cur_char)
        #print(res)
        if not res or len(res) == 0:
            return res_str
        for i in res:
            res_str += chr(i)
        return res_str

if __name__ == "__main__":
    solve = Solution()
    s = "leEeetcode"
    result = solve.makeGood(s)
    print(result)