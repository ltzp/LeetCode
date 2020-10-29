#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 0009 20:46
# @Author  : Letao
# @Site    : 
# @File    : 扑克牌中的顺子.py
# @Software: PyCharm
# @desc    :

class Solution(object):


    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        record_zero = 0
        record_nums = list()
        for i in range(len(nums)):
            if nums[i] == 0:
                record_zero += 1
            else:
                record_nums.append(nums[i])
        print(record_nums)
        start = record_nums[0]
        for i in range(1, len(record_nums)):
            if record_nums[i] - start == 1:
                start = record_nums[i]
                continue
            if record_nums[i] - start > 3:
                return False
            if record_nums[i] - start == 3 and record_zero == 2:
                record_zero = 0
                start = record_nums[i]
                continue
            if record_nums[i] - start == 2 and record_zero > 0:
                record_zero -= 1
                start = record_nums[i]
                continue
            else:
                return False
        return True



if __name__ == "__main__":
    solve = Solution()
    nums = [ int(i) for i in input().split()]
    result = solve.isStraight(nums)
    print(result)