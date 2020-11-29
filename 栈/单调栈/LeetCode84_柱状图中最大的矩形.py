#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 23:46
# @Author  : Letao
# @Site    : 
# @File    : LeetCode84_柱状图中最大的矩形.py
# @Software: PyCharm
# @desc    :
"""
单调递增栈，当小于的时候，就开始出栈计算面积。
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        res = i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                k = stack.pop()
                if stack:
                    res = max(res, heights[k] * (i - stack[-1] - 1))
                else:
                    res = max(res, heights[k] * i)
        while stack:
            k = stack.pop()
            if stack:
                res = max(res, heights[k] * (i - stack[-1] - 1))
            else:
                res = max(res, heights[k] * i)
        return res




if __name__ == "__main__":
    solve = Solution()
    heights = [2,1,5,6,2,3]
    result = solve.largestRectangleArea(heights)
    print(result)