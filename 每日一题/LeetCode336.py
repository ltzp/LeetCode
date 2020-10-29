#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 0006 18:42
# @Author  : Letao
# @Site    : 
# @File    : LeetCode336.py
# @Software: PyCharm
# @desc    : 超时
# https://leetcode-cn.com/problems/palindrome-pairs/
import math

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                else:
                    str = words[i] + words[j]
                    if self.judge(str):
                        res.append([i, j])
        return res
    def judge(self,str):
        length = len(str)
        if length == 1:
            return True
        mid = math.floor(length/2)
        if length % 2 == 1:
            str = str[:mid] + str[mid+1:]
        length = len(str)
        flag = True
        start = 0
        end = length - 1
        while start < length/2 and end >= length/2 :
            if str[start] == str[end]:
                start += 1
                end -= 1
            else:
                flag = False
                break
        return flag


if __name__ == "__main__":
    solve = Solution()
    words = ["a",""]
    result = solve.palindromePairs(words)
    print(result)
#[[0,3],[3,0],[2,3],[3,2]]