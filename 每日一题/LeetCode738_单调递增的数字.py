#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-15 23:08
# @Author  : Letao
# @Site    : 
# @File    : LeetCode738_单调递增的数字.py
# @Software: PyCharm
# @desc    :
"""
单调栈，遇小变9，前一位-1
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N < 10:
            return N-1
        stack = []
        while N:
            temp = N % 10
            N = int(N/10)
            if not stack or stack[len(stack)-1] >= temp:
                stack.append(temp)
            else:
                stack.pop()
                stack.append(9)
                stack.append(temp-1)
        res = 0
        flag = False
        while stack:
            if stack[len(stack) - 1] == 9:
                flag = True
            if flag:
                res = res * 10 + 9
            else:
                res = res*10 + stack[len(stack)-1]
            stack.pop()
        return res


if __name__ == "__main__":
    solve = Solution()
    N = 332
    result = solve.monotoneIncreasingDigits(N)
    print(result)