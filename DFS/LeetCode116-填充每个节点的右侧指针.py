#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 0014 19:16
# @Author  : Letao
# @Site    : 
# @File    : LeetCode116-填充每个节点的右侧指针.py
# @Software: PyCharm
# @desc    :

"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return
        left = node.left
        right = node.right
        while left:
            left.next = right
            left = left.right
            right = right.left
        self.dfs(node.left)
        self.dfs(node.right)

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    g = Node(6)
    h = Node(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = g
    c.right = h
    solve = Solution()
    result = solve.connect(a)
