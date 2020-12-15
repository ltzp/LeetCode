#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-30 20:34
# @Author  : Letao
# @Site    : 
# @File    : LeetCode451_根据字符出现频率排序.py
# @Software: PyCharm
# @desc    :

import heapq
import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s_map = collections.defaultdict(int)
        for i in s:
            s_map[i] += 1
        heap = []
        for key, value in s_map.items():
            heapq.heappush(heap, (-value, key))
        result = []
        while heap:
            fre, char = heapq.heappop(heap)
            for _ in range(-fre):
                result.append(char)
        return ''.join(result)



if __name__ == "__main__":
    solve = Solution()
    s = "tree"
    result = solve.frequencySort(s)
    print(result)