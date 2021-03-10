#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/10
# @Author  : yuetao
# @Site    : 
# @File    : 插入排序.py
# @Desc    :
"""
左边有序，每次将一个元素和左边有序的进行比较，如果小的话，则进行移动。查找插入的位置需要从左到右
"""

class Solution(object):

    def insertionSort(self, nums):
        # 自己写的，从左到右扫描
        length = len(nums)
        right = 0  #有序数组的最右边
        for i in range(1, length):
            if nums[i] >= nums[right]:
                right += 1
            else:
                j = 0
                while j <= right:
                    if nums[j] > nums[i]:
                        break
                    j += 1
                temp = nums[i]
                for k in range(i, j, -1):
                    nums[k] = nums[k-1]
                nums[j] = temp
                right += 1
        return nums


    def insertionSortTwo(self, nums):
        # 从右到左扫描，比目标值大的自动后移动
        for i in range(1, len(nums)):
            value = nums[i] #目标值
            j = i - 1
            while j >= 0:
                if nums[j] > value:
                    nums[j + 1] = nums[j]
                    j -= 1
                else:
                    break
            nums[j+1] = value
        return nums


if __name__ == '__main__':
    solve = Solution()
    nums = [421, 240, 115, 532, 305, 430, 124]
    result = solve.insertionSortTwo(nums)
    print(result)
