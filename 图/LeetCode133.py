#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 0012 23:22
# @Author  : Letao
# @Site    : 
# @File    : LeetCode133.py
# @Software: PyCharm
# @desc    :

class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        return self.dfs(node)


    def dfs(self, node):
        if not node:
            return
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            for i in node.neighbors:
                clone_node.neighbors.append(self.dfs(i))
        return clone_node