#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-03 12:25
# @Author  : Letao
# @Site    : 
# @File    : LeetCode941_有效的山脉数组.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        if length <= 2:
            return False
        start = 0
        max_array = A[0]
        for index, value in enumerate(A):
            if index == start:
                continue
            if A[index] == A[index-1]:
                return False
            if A[index] >= max_array:
                max_array = A[index]
                start = index
        if start == 0 or start == length-1:
            return False
        for i in range(length):
            if i + 1 <= start and A[i] >= A[i+1]:
                return False
            if i >= start and i + 1 <length and A[i] <= A[i+1]:
                return False
        return True


if __name__ == "__main__":
    solve = Solution()
    A = [1,7,9,5,4,1,2]
    result = solve.validMountainArray(A)
    print(result)