#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/26
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode85_最大的矩型.py
# @Desc    :

"""
单调栈思想，同84题解法相似
参考解法：https://leetcode-cn.com/problems/maximal-rectangle/solution/dan-diao-zhan-fa-ba-wen-ti-zhuan-hua-che-uscz/

"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix) #行
        n = len(matrix[0]) #列
        heights = [0] * (n + 2)
        res = 0
        for i in range(m):
            stack = []
            for j in range(n + 2):
                if 1 <= j <= n:
                    if matrix[i][j-1] == "1":
                        heights[j] += 1
                    else:
                        heights[j] = 0
                #例如84题求出每一列的高度
                while stack and heights[stack[-1]] > heights[j]:
                    # 当前的hight < 栈内最后一个下标对应的值，开始出站，计算大小
                    cur = stack.pop()
                    res = max(res, (j - stack[-1] - 1) * heights[cur])
                stack.append(j)
        return res


if __name__ == '__main__':
    solve = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    result = solve.maximalRectangle(matrix)
    print(result)
