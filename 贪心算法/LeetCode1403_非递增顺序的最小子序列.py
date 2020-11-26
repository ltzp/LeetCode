#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 21:39
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1403_非递增顺序的最小子序列.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        # print(nums)
        res = []
        pre_sum, sum_nums = 0, sum(nums)
        for i in nums:
            pre_sum += i
            res.append(i)
            if pre_sum > sum_nums - pre_sum:
                return res

if __name__ == "__main__":
    solve = Solution()
    nums = [4, 3, 10, 9, 8]
    result = solve.minSubsequence(nums)
    print(result)