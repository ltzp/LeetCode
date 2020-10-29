#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 0006 21:20
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1378.py
# @Software: PyCharm
# @desc    :
from collections import defaultdict
class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        weight_hash = defaultdict(int)
        for i in range(lo, hi + 1):
            key = i
            count = 0
            while i != 1:
                if i % 2 == 0:
                    i = i/2
                else:
                    i = 3 * i + 1
                count += 1
            weight_hash[key] = count
        sort_weight = sorted(weight_hash.items(), key=lambda d: (d[1], d[0]))
        print(sort_weight)
        return sort_weight[k-1][0]


if __name__ == "__main__":
    lo = 144
    hi = 163
    k = 5
    solve = Solution()
    result = solve.getKth(lo, hi, k)
    print(result)