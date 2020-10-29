#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 0016 21:17
# @Author  : Letao
# @Site    : 
# @File    : LeetCode977_有序数组的平方.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A
        length = len(A)
        end = max(abs(A[0]), abs(A[length-1]))
        count = [0 for i in range(end + 1)]
        for i in range(length):
            if A[i] < 0:
                count[-A[i]] += 1
            else:
                count[A[i]] += 1
        res = []
        for j in range(end + 1):
            while count[j] >= 1:
                res.append(j*j)
                count[j] -= 1
        return res


if __name__ == "__main__":
    solve = Solution()
    A = [-2,0]
    result = solve.sortedSquares(A)
    print(result)