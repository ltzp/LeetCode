#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 23:45
# @Author  : Letao
# @Site    : 
# @File    : LeetCode239_滑动窗口最大值.py
# @Software: PyCharm
# @desc    :
"""
双端队列
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res, stack = list(), list()
        if not nums:
            return res
        for i, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                stack.pop()
            stack.append(i)
            if i - stack[0] >= k:
                stack.pop(0)
            if i >= k - 1:
                res.append(nums[stack[0]])
        return res


if __name__ == "__main__":
    solve = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = solve.maxSlidingWindow(nums, k)
    print(result)