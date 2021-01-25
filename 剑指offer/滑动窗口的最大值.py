#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/24
# @Author  : yuetao
# @Site    : 
# @File    : 滑动窗口的最大值.py
# @Desc    :
import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        stack = []
        if not nums:
            return res
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                stack.pop()
            stack.append(index)
            if index - stack[0] >= k:
                stack.pop(0)
            if index >= k - 1:
                res.append(nums[stack[0]])
        return res


if __name__ == '__main__':
    solve = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = solve.maxSlidingWindow(nums, k)
    print(result)
