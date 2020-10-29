#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 0014 22:01
# @Author  : Letao
# @Site    : 
# @File    : LeetCode3.py
# @Software: PyCharm
# @desc    : 最长无重复子串
import collections


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        windows = {}
        left, right = 0, 0
        res = 0
        length = len(s)
        while right < length:
            curr = s[right]
            right += 1
            if curr not in windows:
                windows[curr] = 1
            else:
                windows[curr] += 1
            while windows[curr] > 1:
                move_char = s[left]
                left += 1
                windows[move_char] -= 1
            res = max(res, right - left)
        return res


if __name__ == "__main__":
    solve = Solution()
    s = "bbbbb"
    result = solve.lengthOfLongestSubstring(s)
    print(result)
