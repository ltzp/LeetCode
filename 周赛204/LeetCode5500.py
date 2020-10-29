#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 0030 11:40
# @Author  : Letao
# @Site    : 
# @File    : LeetCode5000.py
# @Software: PyCharm
# @desc    :
"""
设 f[i] 是以 nums[i] 结尾，乘积为正的最长子数组的长度。

设 g[i] 是以 nums[i] 结尾，乘积为负的最长子数组的长度。
"""
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        f = [0] * length
        g = [0] * length
        if nums[0]>0:
            f[0] = 1
        elif nums[0] < 0:
            g[0] = 1
        res = f[0]
        for i in range(1, length):
            if nums[i] > 0:
                f[i] = f[i-1] + 1
                if g[i-1] > 0:
                    g[i] = g[i-1] + 1
            elif nums[i] < 0:
                if g[i-1] > 0:
                    f[i] = g[i-1] + 1
                g[i] = f[i-1] + 1
            res = max(res, f[i])
        return res




if __name__ == "__main__":
    solve = Solution()
    nums = [-1]
    result = solve.getMaxLen(nums)
    print(result)