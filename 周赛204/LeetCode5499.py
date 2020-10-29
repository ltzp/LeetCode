#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 0030 10:30
# @Author  : Letao
# @Site    : 
# @File    : LeetCode5499.py
# @Software: PyCharm
# @desc    :

#arr = [1,2,1,2,1,1,1,3], m = 2, k = 2

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        if not arr:
            return False
        if k <= 1:
            return True
        n = len(arr)
        tmep = []
        for i in range(n-m+1):
            start = i
            while len(tmep) < m:
                tmep.append(arr[start])
                start += 1
            else:
                count = 0
                compare_start = i
                while tmep == arr[compare_start:compare_start+m]:
                    count += 1
                    compare_start = compare_start+m
                    if count == k:
                        return True
            tmep.clear()
        return False





if __name__ == "__main__":
    solve = Solution()
    arr = input().split()
    arr = [int(i) for i in arr]
    m = int(input())
    k = int(input())
    result = solve.containsPattern(arr, m, k)
    print(result)