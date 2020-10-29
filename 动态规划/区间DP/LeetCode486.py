#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 0001 18:19
# @Author  : Letao
# @Site    : 
# @File    : LeetCode486.py
# @Software: PyCharm
# @desc    : dp区间问题，dp[i][j] 表示当数组剩下的部分为下标 ii 到下标 jj 时，当前玩家与另一个玩家的分数之差的最大值，注意当前玩家不一定是先手
#https://leetcode-cn.com/problems/predict-the-winner/solution/yu-ce-ying-jia-by-leetcode-solution/

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        dp = [[0]*length for i in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        print(dp)
        for i in range(length-2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][length-1] >= 0

if __name__ == "__main__":
    solve = Solution()
    nums = [1, 5, 2, 4, 6]
    result = solve.PredictTheWinner(nums)
    print(result)