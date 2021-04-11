#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode152_乘积最大子数组.py
# @Desc    :
"""
但是我们在实例中可以发现，有负数的出现，这样的话一个正数乘以负数，即最大值乘以负数就变成了最小值。
因此最大值和最小值是可以相互转化的。在计算的时候，当前状态的值还有可能与之前的状态的值有关，存在后效性。可以通过消除后效性减少分类讨论的难度
"""

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
