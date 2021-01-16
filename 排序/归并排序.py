#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/15
# @Author  : yuetao
# @Site    : 
# @File    : 归并排序.py
# @Desc    :
class Solution:

    def deal(self, nums):
        self.length = len(nums)
        self.temp = [None] * self.length
        self.sort(nums, 0, self.length - 1)
        return nums

    def sort(self, nums, left, right):
        if left >= right:
            return
        mid = int((left+right)/2)
        self.sort(nums, left, mid)
        self.sort(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        i = left #左边数组
        j = mid + 1 #右边第一个元素
        t = 0 #缓存数组起始点
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                self.temp[t] = nums[i]
                i += 1
            else:
                self.temp[t] = nums[j]
                j += 1
            t += 1
        while i <= mid:
            self.temp[t] = nums[i]
            i += 1
            t += 1
        while j <= right:
            self.temp[t] = nums[j]
            j += 1
            t += 1
        t = 0
        #将temp中的元素全部拷贝到原数组中
        while left <= right:
            nums[left] = self.temp[t]
            left += 1
            t += 1




if __name__ == '__main__':
    nums = [9,8,7,6,5,4,3,2,1]
    solve = Solution()
    result = solve.deal(nums)
    print(result)
