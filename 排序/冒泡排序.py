#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/10
# @Author  : yuetao
# @Site    : 
# @File    : 冒泡排序.py
# @Desc    :
"""
每一趟选择一个最大值
"""

class Solution(object):

    def BubbleSort(self, nums):
        length = len(nums)
        for i in range(length-1):
            #遍历的次数
            for j in range(length - i - 1):
                #进行比较循环，最大的移动到后面
                if nums[j] > nums[j + 1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return nums


if __name__ == '__main__':
    solve = Solution()
    nums = [421, 240, 115, 532, 305, 430, 124]
    result = solve.BubbleSort(nums)
    print(result)
