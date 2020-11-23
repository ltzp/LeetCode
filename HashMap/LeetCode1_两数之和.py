#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-21 19:30
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1_两数之和.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_record = {}
        for i in range(len(nums)):
            if nums[i] in hash_record:
                hash_record[nums[i]].append(i)
            else:
                hash_record[nums[i]] = [i]
        # print(hash_record)
        res = []

        for key, value in hash_record.items():
            if target-key in hash_record:
                value = sorted(value)
                cur_value = value[0]
                res.append(cur_value)
                hash_record.get(key).remove(cur_value)
                res.append(hash_record.get(target-key)[0])
                break
        return sorted(res)


if __name__ == "__main__":
    solve = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solve.twoSum(nums, target)
    print(result)