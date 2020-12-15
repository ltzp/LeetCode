#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-01 22:53
# @Author  : Letao
# @Site    : 
# @File    : 面试题17_14最小的K个数.py
# @Software: PyCharm
# @desc    :
import heapq
class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        heapq.heapify(arr) #
        # res = []
        # while k:
        #     res.append(heapq.heappop(arr))
        #     k -= 1
        return heapq.nsmallest(k, arr)

if __name__ == "__main__":
    solve = Solution()
    arr = [1,3,5,7,2,4,6,8]
    k = 4
    result = solve.smallestK(arr, k)
    print(result)