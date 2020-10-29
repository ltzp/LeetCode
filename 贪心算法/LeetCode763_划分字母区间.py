#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 0022 17:59
# @Author  : Letao
# @Site    : 
# @File    : LeetCode763_划分字母区间.py
# @Software: PyCharm
# @desc    :
"""

"ababcbacadefegdehijhklij"  [9,7,8]

"caedbdedda"  [1,9]
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        if not S:
            return res
        last = [0] * 26  #记录每个字符最后的下标
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i
        start, end = 0, 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

if __name__ == "__main__":
    solve = Solution()
    S = "qiejxqfnqceocmy"
    result = solve.partitionLabels(S)
    print(result)