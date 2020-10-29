#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 0010 20:56
# @Author  : Letao
# @Site    : 
# @File    : 数组中重复的数字.py
# @Software: PyCharm
# @desc    :
"""
1.HashMap
2.数组性质，交换排序

"""


class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = set()
        for i in nums:
            if i in count:
                return i
            else:
                count.add(i)
    """
    2 3 1 0 2 5 3
    
    0 1 2 3 2 5 2
    
    """
    def findRepeatNumber2(self, nums):
        length = len(nums)
        for i in range(length):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
        return -1

if __name__ == "__main__":
    solve = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    result = solve.findRepeatNumber2(nums)
    print(result)