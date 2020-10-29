#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 0029 21:05
# @Author  : Letao
# @Site    : 
# @File    : 旋转数组中的最小数字.py
# @Software: PyCharm
# @desc    :
"""
最小数字不是在第一位就去在其中的某一位
"""


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        length = len(numbers)
        min = numbers[0]
        for i in range(1,length):
            if numbers[i] >= min:
                continue
            else:
                min = numbers[i]
                break
        return min

if __name__ == "__main__":

    """
    [3,4,5,1,2]
    [1,3,5]
    """
    solve = Solution()
    numbers = [1,3,5]
    result = solve.minArray(numbers)
    print(result)