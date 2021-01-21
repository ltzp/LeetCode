#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/19
# @Author  : yuetao
# @Site    : 
# @File    : 和为s的两个数.py
# @Desc    :
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record_map = {}
        for num in nums:
            if num not in record_map:
                record_map[num] = 1
        for key in record_map.keys():
            if target - key in record_map:
                return [key, target-key]
        return []


if __name__ == '__main__':
    solve = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solve.twoSum(nums, target)
    print(result)
