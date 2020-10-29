#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 0014 22:32
# @Author  : Letao
# @Site    : 
# @File    : LeetCode76.py
# @Software: PyCharm
# @desc    :https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/hua-dong-chuang-kou-tong-yong-si-xiang-jie-jue-zi-/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        windows = {}
        t_map = {}
        for i in t:
            if i not in t_map:
                t_map[i] = 1
            else:
                t_map[i] += 1
        print(t_map)
        left, right = 0, 0
        valid = 0
        start, end = 0, float("inf")
        s_length = len(s)
        while right < s_length:
            curr = s[right]
            right += 1
            if curr in t_map:
                if curr not in windows:
                    windows[curr] = 1
                else:
                    windows[curr] += 1
                if windows[curr] == t_map[curr]:
                    valid += 1
            while valid == len(t_map):
                if right - left < end:
                    start = left
                    end = right - left
                move_char = s[left]
                left += 1
                if move_char in t_map:
                    if windows[move_char] == t_map[move_char]:
                        valid -= 1
                    windows[move_char] -= 1
        if end == float("inf"):
            return ""
        return s[start:start + end]


if __name__ == "__main__":
    solve = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    # a = {"A":1, "B":1}
    # b = {"B":1, "A":1}
    # if a == b:
    #     print("1")
    # else:
    #     print("2")
    result = solve.minWindow(s, t)
    print(result)
