#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode547_省份数量.py
# @Desc    :

class Solution(object):

    class UnionFind:

        def __init__(self, n):
            self.parent = list(range(n))

        # 找到自己的父节点
        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]


        # 合并两棵树的节点
        def merge(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        length = len(isConnected)
        uf = Solution.UnionFind(length)
        for i in range(length):
            for j in range(i + 1, length):
                if isConnected[i][j] == 1:
                    uf.merge(i, j)
        res = 0
        for i in range(length):
            if uf.parent[i] == i:
                res += 1
        return res


if __name__ == '__main__':
    solve = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    result = solve.findCircleNum(isConnected)
    print(result)
