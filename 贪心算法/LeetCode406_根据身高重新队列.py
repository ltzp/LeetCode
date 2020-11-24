#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-16 22:19
# @Author  : Letao
# @Site    : 
# @File    : LeetCode406_根据身高重新队列.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        if len(people) == 0:
            return result


if __name__ == "__main__":
    solve = Solution()
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    result = solve.reconstructQueue(people)
    print(result)