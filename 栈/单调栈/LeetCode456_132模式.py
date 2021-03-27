#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/24
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode456_132模式.py
# @Desc    :

"""
单调栈：左边取最小值，右边取比当前值小的最大值
栈内是单调递减，如果当前值比栈顶大，则出栈的值就是右测比当前值小的最大值
"""

import sys
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length <= 2:
            return False
        left_min = [float("inf")] * length
        for i in range(1, length):
            left_min[i] = min(left_min[i-1], nums[i-1])
        stack = []
        for i in range(length-1, -1, -1):
            nums_k = float("-inf")
            while stack and stack[-1] < nums[i]:
                nums_k = stack.pop()
            if left_min[i] < nums_k:
                return True
            stack.append(nums[i])
        return False


    def my_find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length <= 2:
            return False
        left_min = nums[0]
        for i in range(1, length - 1):
            if nums[i] < left_min:
                left_min = nums[i]
            else:
                for j in range(i, length):
                    if nums[i] > nums[j] > left_min:
                        return True
        return False



if __name__ == '__main__':
    solve = Solution()
    nums = list(map(int, sys.stdin.readline().strip().split()))
    result = solve.find132pattern(nums)
    print(result)
