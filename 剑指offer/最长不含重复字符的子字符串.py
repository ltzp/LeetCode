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
        length = len(s)
        if length <= 1:
            return length
        windows = {}
        res = 0
        left, right = 0,0
        while right < length:
            cur = s[right]
            right += 1
            if cur not in windows:
                windows[cur] = 1
            else:
                windows[cur] += 1
            while windows[cur] > 1:
                move_char = s[left]
                left += 1
                windows[move_char] -= 1
            res = max(res, right - left)
        return res



if __name__ == '__main__':
    solve = Solution()
    s = "abcabcbb"
    result = solve.lengthOfLongestSubstring(s)
    print(result)
