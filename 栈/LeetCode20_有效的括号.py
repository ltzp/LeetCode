#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 0014 18:36
# @Author  : Letao
# @Site    : 
# @File    : LeetCode20_有效的括号.py
# @Software: PyCharm
# @desc    :
import collections
class Solution(object):

    bracket_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = collections.deque()
        for i in range(len(s)):
            for value in self.bracket_map.values():
                if s[i] == value:
                    stack.append(s[i])
            if s[i] in self.bracket_map:
                if not stack:
                    return False
                elif self.bracket_map.get(s[i]) != stack[-1]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True



if __name__ == "__main__":
    solve = Solution()
    s = "{[]}"
    result = solve.isValid(s)
    print(result)