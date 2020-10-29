#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 0008 18:08
# @Author  : Letao
# @Site    : 
# @File    : 网易.py
# @Software: PyCharm
# @desc    :

import collections


class Solution(object):
    new_set = set()

    def findItinerary(self, grids):
        res = 0
        point_hash = collections.defaultdict(set)
        max_point = 0
        for i in range(len(grids)):
            if grids[i][0] >= max_point:
                max_point = grids[i][0]
            if grids[i][1] >= max_point:
                max_point = grids[i][1]
            point_hash[grids[i][0]].add(grids[i][1])
        print(max_point)
        print(point_hash)
        new_point_hash = collections.defaultdict(set)
        for key,value in point_hash.items():
            used = [False] * max_point
            self.new_set = set()
            self.dfs(point_hash, key, used)
            new_point_hash[key] = self.new_set
            # if key not in new_point_hash:
            #     new_point_hash[key] = self.new_set
        for key, values in new_point_hash.items():
            for m in values:
                if m in new_point_hash:
                    other_point = new_point_hash.get(m)
                    if key in other_point:
                        res += 1
        return res

    def dfs(self, point_hash, point, used):
        if used[point - 1]:
            return
        if point not in point_hash:
            return
        points = point_hash.get(point)
        used[point-1] = True
        self.new_set = self.new_set.union(points)
        for value in points:
            self.dfs(point_hash, value, used)
        return self.new_set

if __name__ == "__main__":
    solve = Solution()
    grids = [[1, 3], [2, 1], [3, 2], [3, 5], [4, 5], [5, 4], [5, 6]]
    result = solve.findItinerary(grids)
    print(result)
