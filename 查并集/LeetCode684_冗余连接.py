#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode684_冗余连接.py
# @Desc    :
"""
判断是否含有圆，如果有圆则返回圆==时候的边
"""
class Solution(object):

    class UnionFind:

        def __init__(self, n):
            self.parent = list(range(n+1))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def merge(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)


    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        length = len(edges)
        uf = Solution.UnionFind(length)
        for i in range(length):
            if uf.find(edges[i][0]) != uf.find(edges[i][1]):
                uf.merge(edges[i][0], edges[i][1])
            else:
                return edges[i]
        return -1

if __name__ == '__main__':
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    solve = Solution()
    result = solve.findRedundantConnection(edges)
    print(result)
