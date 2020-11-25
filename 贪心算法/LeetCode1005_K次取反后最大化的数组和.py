#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-25 20:41
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1005_K次取反后最大化的数组和.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        print(A)
        for i in range(len(A)):
            value = A[i]
            if value < 0 and K > 0:
                A[i] = abs(value)
                K -= 1
        if K <= 0:
            return sum(A)
        else:
            if K % 2 == 0:
                return sum(A)
            else:
                return sum(A) - 2 * min(A)


if __name__ == "__main__":
    solve = Solution()
    A = [2, -3, -1, 5, -4]
    K = 2
    result = solve.largestSumAfterKNegations(A, K)
    print(result)
