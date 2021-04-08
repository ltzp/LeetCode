#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/29
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1319_连通网络的次数.py
# @Desc    :

class Solution(object):
    class UnionFind:
        def __init__(self, length):
            self.parent = list(range(length))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1
        uf = self.UnionFind(n)
        res = 0
        for connect in connections:
            if uf.find(connect[0]) != uf.find(connect[1]):
                uf.union(connect[0], connect[1])
                res += 1
        return (n-1) - res


if __name__ == '__main__':
    solve = Solution()
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    result = solve.makeConnected(n, connections)
    print(result)
