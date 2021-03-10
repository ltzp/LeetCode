#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/10
# @Author  : yuetao
# @Site    : 
# @File    : 快速排序.py
# @Desc    :
"""
以第一个数为标准，当left 和right 相交的时候，就是一趟排序完毕。
"""


class Solution(object):
    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        pivot = nums[left]
        low = left
        high = right
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[right] = pivot
        self.quick_sort(nums, low, right - 1)
        self.quick_sort(nums, right + 1, high)
        return nums


if __name__ == '__main__':
    solve = Solution()
    nums = [6, 5, 4, 7, 8, 3, 2, 9, 6]
    result = solve.quick_sort(nums, 0, len(nums) - 1)
    print(result)
