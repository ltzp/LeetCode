#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-29 14:21
# @Author  : Letao
# @Site    : 
# @File    : LeetCode976_三角形最大周长.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return 0
        A = sorted(A)
        for i in range(length-1, 1, -1):
            if A[i-2] + A[i-1] > A[i]:
                return A[i-2] + A[i-1] + A[i]

        return 0


if __name__ == "__main__":
    solve = Solution()
    A = [3,6,2,3]
    result = solve.largestPerimeter(A)
    print(result)