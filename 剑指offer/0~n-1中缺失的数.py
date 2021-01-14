#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/12
# @Author  : yuetao
# @Site    : 
# @File    : 0~n-1中缺失的数.py
# @Desc    :
"""
等差数列求和公式-数组总和

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        n_sum = (n * (n + 1))/2
        print(n_sum)
        true_sum = sum(nums)
        return n_sum - true_sum


if __name__ == '__main__':
    nums = [1,2]
    solve = Solution()
    result = solve.missingNumber(nums)
    print(result)