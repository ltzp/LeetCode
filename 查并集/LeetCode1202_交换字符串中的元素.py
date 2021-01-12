#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/11
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1202_交换字符串中的元素.py
# @Desc    :

import collections


class Solution(object):

    class UnionFind:

        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def merger(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)


    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        length = len(s)
        uf = Solution.UnionFind(length)
        for pair in pairs:
            uf.merger(pair[0], pair[1])
        # print(uf.parent)
        record_map = collections.defaultdict(list)
        for i, ch in enumerate(s):
            record_map[uf.find(i)].append(ch)
        # print(record_map)
        for record in record_map.values():
            record.sort(reverse=True)
        res = list()
        for i in range(length):
            x = uf.find(i)
            res.append(record_map[x][-1])
            record_map[x].pop()
        return "".join(res)



if __name__ == '__main__':
    solve = Solution()
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    result = solve.smallestStringWithSwaps(s, pairs)
    print(result)
