#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-09 14:44
# @Author  : Letao
# @Site    : 
# @File    : LeetCode973_最接近原点的K个数.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        res = []
        length = len(points)
        if length == 0 or K <= 0:
            return res
        record_map = {}
        for index, point in enumerate(points):
            key = point[0]**2 + point[1]**2
            if key not in record_map:
                record_map[key] = [index]
            else:
                record_map.get(key).append(index)
        record_map = sorted(record_map.items(), key=lambda x:x[0])
        index_sort = []
        for key, value in record_map:
            index_sort.extend(value)
        result_index = index_sort[:K]
        for i in result_index:
            res.append(points[i])
        return res



if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    solve = Solution()
    result = solve.kClosest(points, K)
    print(result)