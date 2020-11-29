#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 23:42
# @Author  : Letao
# @Site    : 
# @File    : LeetCode42_接雨水.py
# @Software: PyCharm
# @desc    :
"""
维护一个单调递减的栈， 比栈顶大就需要弹出。
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 3:
            return 0
        stack = []
        res = 0
        for i in range(length):
            while stack and height[i] > height[stack[-1]]: # 如果当前值 > 栈顶元素， 则弹出
                value = stack.pop()
                if stack:
                    res += (min(height[i], height[stack[-1]]) - height[value])*(i - stack[-1] - 1)
            stack.append(i)
        return res





if __name__ == "__main__":
    solve = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solve.trap(height)
    print(result)