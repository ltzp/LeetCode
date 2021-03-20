#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/20
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode189_旋转数组.py
# @Desc    :

class Solution(object):
    def over_rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k >= length:
            k = k % length
        step = 0
        while step < k:
            lats_num = nums[length-1]
            end_index = length - 1
            while end_index > 0:
                nums[end_index] = nums[end_index - 1]
                end_index = end_index - 1
            nums[0] = lats_num
            step += 1
        return nums

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        return nums

if __name__ == '__main__':
    solve = Solution()
    nums = [-1,-100,3,99]
    k = 2
    result = solve.rotate(nums, k)
    print(result)
