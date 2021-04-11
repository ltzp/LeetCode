#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode300_最长递增子序列.py
# @Desc    :
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * length
        dp[0] = 1
        LIS = 1
        for i in range(1, length):
            dp[i] = 1
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                if LIS < dp[i]:
                    LIS = dp[i]
        return LIS


if __name__ == '__main__':
    solve = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = solve.lengthOfLIS(nums)
    print(result)
