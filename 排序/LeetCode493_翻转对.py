#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-28 22:38
# @Author  : Letao
# @Site    : 
# @File    : LeetCode493_翻转对.py
# @Software: PyCharm
# @desc    :
"""
归并排序
"""
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        mid = length >> 1
        res = 0
        res += self.reversePairs(nums[:mid])
        res += self.reversePairs(nums[mid:])
        nums[:] = sorted(nums[:mid]) + sorted(nums[mid:])
        left, right = 0, mid
        while left < mid and right < length:
            while left < mid and nums[left] <= nums[right] << 1:
                left += 1
            res += mid - left
            right += 1
        return res




if __name__ == "__main__":
    solve = Solution()
    nums = [-5, -5]
    result = solve.reversePairs(nums)
    print(result)