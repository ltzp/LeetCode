#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-04 18:44
# @Author  : Letao
# @Site    : 
# @File    : LeetCode57_插入区间_2.py
# @Software: PyCharm
# @desc    :


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        if not placed:
            ans.append([left, right])
        return ans


if __name__ == "__main__":
    solve = Solution()
    intervals = [[1,2], [3,5], [6,7], [8,10], [12, 16]]

    # intervals = [[1,5]]
    newInterval = [4, 8]
    result = solve.insert(intervals, newInterval)
    print(result)