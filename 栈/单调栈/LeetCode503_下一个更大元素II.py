#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 23:43
# @Author  : Letao
# @Site    : 
# @File    : LeetCode503_下一个更大元素II.py
# @Software: PyCharm
# @desc    :
"""
对于循环数组的处理：通过余数，然后将数组的长度扩大到两倍

"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        length = len(nums)
        res = [-1] * length
        for i in range(length * 2):
            while stack and nums[stack[-1]] < nums[i%length]:
                res[stack.pop()] = nums[i%length]
            stack.append(i % length)
        return res



if __name__ == "__main__":
    nums = [1,2,1]
    solve = Solution()
    result = solve.nextGreaterElements(nums)
    print(result)