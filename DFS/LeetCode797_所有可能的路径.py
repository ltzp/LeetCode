#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/09/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode797_所有可能的路径.py
# @Desc    :
import copy
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(graph)
        record = dict()
        end = length - 1
        for i in range(length):
            record[i] = graph[i]
        self.res = []
        self.dfs(0, end, [], record)
        return self.res

    def dfs(self, key, end, path, record):
        if key == end:
            path.append(key)
            copy_path = path[:]
            self.res.append(copy_path)
            return
        path.append(key)
        connect = record.get(key)
        for j in range(len(connect)):
            self.dfs(connect[j], end, path, record)
            path.pop()





if __name__ == '__main__':
    graph = [[1],[]]
    solve = Solution()
    res = solve.allPathsSourceTarget(graph)
    print(res)
