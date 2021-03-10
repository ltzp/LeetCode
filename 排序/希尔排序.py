#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/10
# @Author  : yuetao
# @Site    : 
# @File    : 希尔排序.py
# @Desc    :
"""

"""

class Solution(object):
    def sort_gap(self, nums):
        length = len(nums)
        gap = int(length/2)
        while gap > 0:
            for i in range(gap, length): #从后往前进行交换和查找
                while i >= gap and nums[i - gap] > nums[i]:
                    nums[i-gap], nums[i] = nums[i], nums[i-gap]
                    i -= gap #不能掉
            gap = int(gap/2)
        return nums


if __name__ == '__main__':
    solve = Solution()
    nums = [6, 5, 4, 7, 8, 3, 2]
    result = solve.sort_gap(nums)
    print(result)
