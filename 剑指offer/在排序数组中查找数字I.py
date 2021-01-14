#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/12
# @Author  : yuetao
# @Site    : 
# @File    : 在排序数组中查找数字I.py
# @Desc    :
"""
二分法：找最左边或者最右边
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = self.search_left(nums, target)
        right = self.search_right(nums, target)
        if left == -1 or right == -1:
            return 0
        else:
            return right - left + 1


    def search_right(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int( (start + end) / 2)
            if target == nums[mid]:
                if mid == len(nums) - 1 or target < nums[mid + 1]:
                    return mid
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search_left(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if target == nums[mid]:
                if mid == 0 or target > nums[mid - 1]:
                    return mid
                end = mid - 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1





if __name__ == '__main__':
    solve = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    result = solve.search(nums, target)
    print(result)
