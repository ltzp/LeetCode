#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/29
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1631_最小体力消耗路径.py
# @Desc    :

class Solution(object):

    class UnionFind:
        def __init__(self):
            self.parent = list(range(10001))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]
        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row = len(heights)
        column = len(heights[0])
        uf = self.UnionFind()
        edges = []
        for i in range(row):
            for j in range(column):
                pos = i * column + j
                if i < row - 1:
                    edges.append([abs(heights[i+1][j] - heights[i][j]), pos, pos + column])
                if j < column -1:
                    edges.append([abs(heights[i][j+1] - heights[i][j]), pos, pos + 1])
        edges.sort()
        for edge in edges:
            uf.union(edge[1], edge[2])
            if uf.find(0) == uf.find(row * column - 1):
                return edge[0]
        return 0


if __name__ == '__main__':
    solve = Solution()
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    result = solve.minimumEffortPath(heights)
    print(result)
