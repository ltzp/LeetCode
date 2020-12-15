#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 22:09
# @Author  : Letao
# @Site    :
# @File    : LeetCode316_去除重复字母.py
# @Software: PyCharm
# @desc    :
"""
单调栈 + 贪心
"""
#TODO
#https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        seen = set()
        last_occurrence = {c: i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)


if __name__ == "__main__":
    solve = Solution()
    s = "cbacdcbcz"
    result = solve.removeDuplicateLetters(s)
    print(result)