#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 0016 19:46
# @Author  : Letao
# @Site    : 
# @File    : LeetCode49_字母异位词分组.py
# @Software: PyCharm
# @desc    :

"""
以元组为key
"""

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return res.values()


if __name__ == "__main__":
    solve = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solve.groupAnagrams(strs)
    print(result)