#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 0025 19:43
# @Author  : Letao
# @Site    : 
# @File    : LeetCode845_数组中的最长山脉.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return 0
        res = 0
        for i in range(1, length-1):

            left_index = i
            right_index = i
            if A[left_index] < A[left_index - 1] or A[right_index] < A[right_index + 1]:
                continue

            left_count = 0
            while left_index >= 1 and A[left_index] > A[left_index - 1]:
                left_index -= 1
            else:
                left_count = i - left_index
            right_count = 0
            while right_index < length -1 and A[right_index] > A[right_index + 1]:
                right_index += 1
            else:
                right_count = right_index - i
            if left_count > 0 and right_count > 0:
                res = max(right_count + left_count + 1, res)
        return res


if __name__ == "__main__":
    solve = Solution()
    A = [0,1,2,3,4,5,4,3,2,1,0]
    result = solve.longestMountain(A)
    print(result)