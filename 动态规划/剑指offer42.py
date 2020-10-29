#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 0011 21:38
# @Author  : Letao
# @Site    : 
# @File    : 剑指offer42.py
# @Software: PyCharm
# @desc    : 连续子数组最大和
class Solution(object):
    res = float("-inf")

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] += dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
            if dp[i] > self.res:
                self.res = dp[i]
        return self.res

if __name__ == "__main__":
    solve = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solve.maxSubArray(nums)
    print(result)

