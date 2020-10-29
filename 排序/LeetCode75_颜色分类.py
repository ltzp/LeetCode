#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 0010 20:11
# @Author  : Letao
# @Site    : 
# @File    : LeetCode75_颜色分类.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_max = max(nums)
        num_min = min(nums)
        count = [0 for i in range(num_min, num_max + 1)]
        for i in nums:
            count[i - num_min] += 1

        j = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[j] = i + num_min
                j += 1
                count[i] -= 1
        return nums


if __name__ == "__main__":
    solve = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    result = solve.sortColors(nums)
    print(result)
