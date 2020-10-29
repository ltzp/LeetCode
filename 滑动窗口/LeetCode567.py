#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 0014 22:31
# @Author  : Letao
# @Site    : 
# @File    : LeetCode567.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        windows, s1_map = {}, {}
        for i in s1:
            if i not in s1_map:
                s1_map[i] = 1
            else:
                s1_map[i] += 1
        s1_length = len(s1)
        s2_length = len(s2)
        left, right = 0, 0
        valid = 0
        while right < s2_length:
            curr_char = s2[right]
            right += 1
            if curr_char in s1_map:
                if curr_char not in windows:
                    windows[curr_char] = 1
                else:
                    windows[curr_char] += 1
                if windows[curr_char] == s1_map[curr_char]:
                    valid += 1
            while right - left >= s1_length:
                if valid == len(s1_map):
                    return True
                move_char = s2[left]
                left += 1
                if move_char in s1_map:
                    if windows[move_char] == s1_map[move_char]:
                        valid -= 1
                    windows[move_char] -= 1
        return False


if __name__ == "__main__":
    solve = Solution()
    s1 = "ab"
    s2 = "eidboaoo"
    result = solve.checkInclusion(s1, s2)
    print(result)
