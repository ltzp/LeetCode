#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 0002 19:23
# @Author  : Letao
# @Site    : 
# @File    : LeetCode416.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        all_sum = sum(nums)
        if all_sum & 1:
            return False
        half_sum = int(all_sum/2)
        dp = [[False for j in range(half_sum+1)] for i in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, half_sum + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[len(nums)][half_sum]


if __name__ == "__main__":
    solve = Solution()
    nums = [int(i) for i in input().split()]
    result = solve.canPartition(nums)
    print(result)