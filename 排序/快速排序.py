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
        i = left
        j = right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        self.quick_sort(nums, left, i - 1)
        self.quick_sort(nums, i + 1, right)
        return nums


if __name__ == '__main__':
    solve = Solution()
    nums = [6, 5, 4, 7, 8, 3, 2, 9]
    result = solve.quick_sort(nums, 0, len(nums) - 1)
    print(result)
