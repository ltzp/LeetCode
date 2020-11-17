#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-12 23:23
# @Author  : Letao
# @Site    : 
# @File    : LeetCode922_按奇偶排序数组.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        if length < 2:
            return A
        for i in range(length):
            if i % 2 == 0:
                if A[i] % 2 == 0:
                    continue
                else:
                    for j in range(i + 1, length):
                        if A[j] % 2 == 0:
                            A[i], A[j] = A[j], A[i]
                            break
            if i % 2 == 1:
                if A[i] % 2 == 1:
                    continue
                else:
                    for j in range(i + 1, length):
                        if A[j] % 2 == 1:
                            A[i], A[j] = A[j], A[i]
                            break
        return A


if __name__ == "__main__":
    solve = Solution()
    A = [4, 2, 5, 7]
    result = solve.sortArrayByParityII(A)
    print(result)
