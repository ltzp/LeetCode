#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024 18:23
# @Author  : Letao
# @Site    : 
# @File    : LeetCode459.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        if size <= 1:
            return False
        mid = int(size//2 + 1)
        for i in range(1, mid):
            if size % i == 0:
                if all(s[j] == s[j-i] for j in range(i, size)):
                    return True
        return False


if __name__ == "__main__":
    solve = Solution()
    s = input()
    result = solve.repeatedSubstringPattern(s)
    print(result)