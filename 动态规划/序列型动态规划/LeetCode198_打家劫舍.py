#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode198_打家劫舍.py
# @Desc    :

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        if not nums:
            return res
        length = len(nums)
        dp = [0 for j in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[length-1]

if __name__ == "__main__":
    nums = [1,2,3,1]
    solve = Solution()
    res = solve.rob(nums)
    print(res)
