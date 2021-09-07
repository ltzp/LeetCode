#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/09/01
# @Author  : yuetao
# @Site    : 
# @File    : 堆排序.py
# @Desc    :
import math

class Solution(object):
    def heap_sort(self, nums):
        length = len(nums)
        self.bulid_max_heap(nums, length)
        for i in range(length-1, 0, -1):
            #将最小的与最大的交换，取出最大的一个值
            self.swap(nums, 0, i)
            #将剩下的生成大根堆
            self.heap_adjust(nums, 0, i)
        return nums

    def bulid_max_heap(self, nums, length):
        #构造大根堆
        for i in range(math.floor(length/2), -1, -1):
            self.heap_adjust(nums, i, length)

    def heap_adjust(self, nums, i, size):
        left_child = 2 * i + 1
        right_child = 2 * (i + 1)
        # 默认当前的值最大
        max_value = i
        if left_child < size and nums[left_child] > nums[max_value]:
            max_value = left_child
        if right_child < size and nums[right_child] > nums[max_value]:
            max_value = right_child
        if max_value != i:
            self.swap(nums, i, max_value)
            self.heap_adjust(nums, max_value, size)

    def swap(self, nums, i, j):
        # 进行交换
        nums[i], nums[j] = nums[j], nums[i]



if __name__ == '__main__':
    solve = Solution()
    nums = [1, 5, 9, 7, 8, 3, 11, 15, 13]
    res = solve.heap_sort(nums)
    print(res)
