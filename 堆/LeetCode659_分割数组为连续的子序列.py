#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode659_分割数组为连续的子序列.py
# @Desc    :
"""
[1,2,5,5,6,6,7,8,8,9]
"""
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = {}
        for i in range(len(nums)):
            if nums[i] not in record:
                record[nums[i]] = [i]
            else:
                record[nums[i]].append(i)
        res = []
        index = -1
        length = len(record)
        for key, value in record.items():
            index += 1
            if len(res) < 3:
                res.append(key)
                record.get(key).pop()
                if len(res) == 3 and record.get(key) and index != length-1:
                    res = []
                    res.append(key)
                    record.get(key).pop()
                continue
            else:
                res = []
                res.append(key)
                record.get(key).pop()
        if len(res) < 3:
            return False
        return True


if __name__ == '__main__':
    solve = Solution()
    nums = [2,5,5,5,6,7,8,8,8,9]
    result = solve.isPossible(nums)
    print(result)