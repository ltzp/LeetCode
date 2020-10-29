#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 0007 21:18
# @Author  : Letao
# @Site    : 
# @File    : LeetCode332_图的DFS.py
# @Software: PyCharm
# @desc    :
import collections
class Solution(object):
    res = []

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        plane_hash = collections.defaultdict(list)
        for i in range(len(tickets)):
            plane_hash[tickets[i][0]].append(tickets[i][1])
        #print(plane_hash)
        for key, values in plane_hash.items():
            new_valus = sorted(values)
            plane_hash[key] = new_valus
        #print(plane_hash)
        self.dfs(plane_hash, 'JFK')
        return self.res

    def dfs(self, graph, plane):
        self.res.append(plane)
        arived = graph.get(plane)
        if not arived:
            return
        value = arived[0]
        graph[plane] = arived[1:]
        self.dfs(graph, value)



if __name__ == "__main__":
    solve = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    result = solve.findItinerary(tickets)
    print(result)
