#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 0025 23:28
# @Author  : Letao
# @Site    : 
# @File    : LeetCode617_合并二叉树.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(t1, t2)

    def dfs(self, node1, node2):
        if not node1 and not node2:
            return
        if not node1 and node2:
            return node2
        if node1 and not node2:
            return node1
        node = TreeNode(node1.val + node2.val)
        node.left = self.dfs(node1.left, node2.left)
        node.right = self.dfs(node1.right, node2.right)
        return node

if __name__ == "__main__":
    solve = Solution()
    t1 = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(2)
    d = TreeNode(5)
    t1.left = b
    t1.right = c
    b.left = d
    t2 = TreeNode(2)
    e = TreeNode(1)
    f = TreeNode(3)
    g = TreeNode(4)
    h = TreeNode(7)
    t2.left = e
    t2.right = f
    e.right = g
    f.right = h
    result = solve.mergeTrees(t1, t2)
    print(result)
