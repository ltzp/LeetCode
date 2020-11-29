#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 23:42
# @Author  : Letao
# @Site    : 
# @File    : LeetCode496_下一个更大元素I.py
# @Software: PyCharm
# @desc    :
"""
单调递减栈
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        length = len(nums2)
        dic = dict()
        stack = []
        for i in range(length):
            while stack and stack[-1] < nums2[i]:
                temp = stack.pop()
                dic[temp] = nums2[i]
            stack.append(nums2[i])
        return [dic.get(i, -1) for i in nums1]


if __name__ == "__main__":
    solve = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = solve.nextGreaterElement(nums1,nums2)
    print(result)