#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 0014 22:00
# @Author  : Letao
# @Site    : 
# @File    : LeetCode438.py
# @Software: PyCharm
# @desc    : 找到字符串中所有字母异位词
# 解题思路 : 维护一个固定大小的窗口，左边入窗，则右边出窗
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        length = len(p)
        s_length = len(s)
        if s_length < length:
            return
        s_arr, p_arr = [0] * 26, [0] * 26
        for i in p:
            p_arr[ord(i)-97] += 1
        for i in range(0, length):
            s_arr[ord(s[i])-97] += 1
        res = []
        l, r = 0, length-1
        while r <= s_length - 1 and r - l == length-1:
            if s_arr == p_arr:
                res.append(l)
            if r == s_length - 1:
                break
            r += 1
            s_arr[ord(s[r])-97] += 1
            s_arr[ord(s[l])-97] -= 1
            l += 1
        return res




if __name__ == "__main__":
    solve = Solution()
    s = "abab"
    p = "ab"
    result = solve.findAnagrams(s, p)
    print(result)