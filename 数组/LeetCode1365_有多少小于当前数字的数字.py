#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 0026 17:22
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1365_有多少小于当前数字的数字.py
# @Software: PyCharm
# @desc    :


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return
        length = len(nums)
        res = []
        for i in range(length):
            cur_num = nums[i]
            count = 0
            for j in range(length):
                if cur_num == nums[j]:
                    continue
                if nums[j] < cur_num:
                    count += 1
            res.append(count)
        return res


if __name__ == "__main__":
    nums = [8,1,2,2,3]
    solve = Solution()
    result = solve.smallerNumbersThanCurrent(nums)
    print(result)