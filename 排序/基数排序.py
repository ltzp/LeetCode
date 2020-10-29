#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 0010 21:37
# @Author  : Letao
# @Site    : 
# @File    : 桶排序.py
# @Software: PyCharm
# @desc    :
"""


"""
# TODO
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_max = max(nums)
        high = len(str(num_max))
        print(high)
        length = len(nums)
        count = [0 for i in range(10)]
        for i in range(0, high):
            division = 10 ** i
            for j in range(length):
                num = int(nums[j]/division % 10)
                count[num] += 1
            print(count)



if __name__ == "__main__":
    solve = Solution()
    nums = [421, 240, 115, 532, 305, 430, 124]
    result = solve.sortColors(nums)
    print(result)
