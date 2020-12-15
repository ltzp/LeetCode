#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-29 00:08
# @Author  : Letao
# @Site    : 
# @File    : LeetCode767_重构字符串.py
# @Software: PyCharm
# @desc    :
"""
S = "aab" -> S = "aba"

"""

import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        hash_map = collections.defaultdict(int)
        for s in S:
            hash_map[s] += 1
        max_deep = max(hash_map.values())
        if max_deep > (len(S) + 1)/2:
            return ""
        hash_lists = sorted(hash_map.items(), key=lambda value:value[1], reverse=True)
        res = ['a'] * len(S)
        index = 0
        for key, value in hash_lists:
            while index < len(S) and value > 0:
                res[index] = key
                index += 2
                if index >= len(S):
                    index = 1
                value -= 1
        return "".join(res)


if __name__ == "__main__":
    solve = Solution()
    S = "aaab"
    result = solve.reorganizeString(S)
    print(result)
