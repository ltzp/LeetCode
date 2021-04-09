#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode152_乘积最大子数组.py
# @Desc    :
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [[float("-inf")] * 2 for _ in range(length)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        for i in range(1, length):
            if nums[i] >= 0:
                dp[i][0] = min(nums[i], nums[i] * dp[i-1][0])
                dp[i][1] = max(nums[i], nums[i] * dp[i-1][1])
            else:
                dp[i][0] = min(nums[i], dp[i-1][1] * nums[i])
                dp[i][1] = max(dp[i-1][0] * nums[i], nums[i])
        res = dp[0][1]
        for i in range(length):
            res = max(res,dp[i][1])
        return res


if __name__ == '__main__':
    solve = Solution()
    nums = [-2,3,-4]
    result = solve.maxProduct(nums)
    print(result)
