#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 23:43
# @Author  : Letao
# @Site    : 
# @File    : LeetCode739_每日温度.py
# @Software: PyCharm
# @desc    :
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        length = len(T)
        res = [0] * length
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                temp = stack.pop()
                res[temp] = i - temp
            stack.append(i)
        return res



if __name__ == "__main__":
    solve = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = solve.dailyTemperatures(temperatures)
    print(result)