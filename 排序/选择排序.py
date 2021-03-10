#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/10
# @Author  : yuetao
# @Site    : 
# @File    : 选择排序.py
# @Desc    :

"""
每一趟找出最小的元素，并且进行交换，放在前面的位置
"""


class Solution(object):
    def selectSort(self, nums):
        length = len(nums)
        for i in range(length):
            min_index = i
            for j in range(i + 1, length):
                if nums[j] < nums[min_index]:
                    min_index = j
            temp = nums[min_index]
            nums[min_index] = nums[i]
            nums[i] = temp
        return nums


if __name__ == '__main__':
    solve = Solution()
    nums = [6, 5, 4, 7, 8, 3, 2]
    result = solve.selectSort(nums)
    print(result)
