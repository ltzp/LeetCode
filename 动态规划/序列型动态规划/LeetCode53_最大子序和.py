#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode53_最大子序和.py
# @Desc    :
"""
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

在状态的计算过程中我们可以发现，后面状态的计算只与当前状态的值有关，而与此阶段之前的值无关，所以具有无后效性。
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [float("-inf") for _ in range(length)]
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, length):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(dp[i], res)
        return res


if __name__ == '__main__':
    solve = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solve.maxSubArray(nums)
    print(result)
