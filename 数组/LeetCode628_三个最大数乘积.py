#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/20
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode628_三个最大数乘积.py
# @Desc    :
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])



if __name__ == '__main__':
    solve = Solution()
    nums = [-100,-98,-1,2,3,4]
    result = solve.maximumProduct(nums)
    print(result)
