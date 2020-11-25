#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-24 22:11
# @Author  : Letao
# @Site    : 
# @File    : LeetCode944_删列造序.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        length = len(A[0])
        length_A = len(A)
        res = 0
        for i in range(length):
            cur_char = ord(A[0][i])
            for j in range(1, length_A):
                if ord(A[j][i]) > cur_char:
                    cur_char = ord(A[j][i])
                else:
                    res += 1
                    break
        return res


if __name__ == "__main__":
    solve = Solution()
    A = ["zyx", "wvu", "tsr"]
    result = solve.minDeletionSize(A)
    print(result)