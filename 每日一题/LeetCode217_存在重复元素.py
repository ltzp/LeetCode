#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-15 23:33
# @Author  : Letao
# @Site    : 
# @File    : LeetCode217_存在重复元素.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                return True
        return False



if __name__ == "__main__":
    solve = Solution()
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = solve.containsDuplicate(nums)
    print(result)
