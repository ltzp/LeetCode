#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode978_最长湍流子数组.py
# @Desc    :

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        if length < 2:
            return length
        increase = [1] * length
        decrease = [1] * length
        res = 0
        for i in range(1, length):
            if arr[i] > arr[i-1]:
                increase[i] = decrease[i-1] + 1
                decrease[i] = 1
            elif arr[i] < arr[i-1]:
                decrease[i] = increase[i-1] + 1
                increase[i] = 1
            else:
                increase[i] = 1
                decrease[i] = 1
            res = max(res, max(increase[i], decrease[i]))
        return res




if __name__ == '__main__':
    solve = Solution()
    arr = [9,4,2,10,7,8,8,1,9]
    result = solve.maxTurbulenceSize(arr)
    print(result)
