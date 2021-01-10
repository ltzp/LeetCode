#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/10
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode228_区间汇总.py
# @Desc    :
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        length = len(nums)
        i = 0
        res = []
        while i < length:
            record = str(nums[i])
            j = i + 1
            while j < length:
                if nums[j] - nums[i] == j - i:
                    j += 1
                else:
                    break
            if j - i == 1:
                res.append(record)
            else:
                record += "->" + str(nums[j-1])
                res.append(record)
            i = j
        return res


if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    solve = Solution()
    result = solve.summaryRanges(nums)
    print(result)
