#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode238_除自身以外数组的乘积.py
# @Desc    :

"""
示例:

输入: [1,2,3,4]
输出: [24,12,8,6]

"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        dp_left = [1] * length
        dp_left[0] = 1
        for i in range(1, length):
            dp_left[i] = dp_left[i-1] * nums[i-1]
        dp_right = [1] * length
        dp_right[length-1] = 1
        for i in range(length-2, -1, -1):
            dp_right[i] = dp_right[i+1] * nums[i+1]
        res = []
        for i in range(length):
            res.append(dp_left[i] * dp_right[i])
        return res




if __name__ == '__main__':
    solve = Solution()
    nums = [1,2,3,4]
    result = solve.productExceptSelf(nums)
    print(result)
