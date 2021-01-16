#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/12
# @Author  : yuetao
# @Site    : 
# @File    : 数组中的逆序对.py
# @Desc    :


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0
        self.dfs(nums, 0, len(nums) - 1, [])
        return self.res

    #进行排序
    def dfs(self, nums, left, right, temp):
        if left >= right:
            return
        mid = left + right >> 1
        self.dfs(nums, left, mid, temp)
        self.dfs(nums, mid + 1, right, temp)
        self.merge(nums, left, mid, right, temp)


    #合并数组
    def merge(self, nums, left, mid, right, temp):
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                #前面一个数组i到mid的距离是后面一个数组j的逆序对
                self.res += mid - i + 1
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        for i in range(len(temp)):
            nums[left + i] = temp[i]
        temp.clear()



if __name__ == '__main__':
    solve = Solution()
    nums = [4,5,6,7]
    result = solve.reversePairs(nums)
    print(result)
