#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-10 17:52
# @Author  : Letao
# @Site    : 
# @File    : LeetCode31_下一个排列组合.py
# @Software: PyCharm
# @desc    :
"""
解题思路：
4，5，3，1 ->5，1，3，4
1.从右到左找出非递增的下标i ,(例如以上例子就是0：以为1->3->5是增加的)
2.从右到左找出比i大的第一个数的下标j, (例如以上例子就是1)
3.i,j 进行交换
4,从i 开始一直到length进行交换

"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = length - 1
            while j >= i and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = length - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    solve = Solution()
    nums = [1,2,3]
    solve.nextPermutation(nums)
    print(nums)
