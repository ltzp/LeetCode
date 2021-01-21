#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/19
# @Author  : yuetao
# @Site    : 
# @File    : 翻转单词顺序.py
# @Desc    :
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        strs = s.split(" ")
        res = ""
        while strs:
            cur_str = strs[-1]
            if cur_str == '':
                strs.pop()
                continue
            else:
                res += strs.pop() + " "
        return res[:-1]


if __name__ == '__main__':
    s = "  hello world!  "
    solve = Solution()
    result = solve.reverseWords(s)
    print(result)
