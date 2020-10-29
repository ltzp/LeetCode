#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 0008 20:22
# @Author  : Letao
# @Site    : 
# @File    : 面试题17.12.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    start = pointer = TreeNode(-1)
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return self.start.right


    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        node.left = None
        self.pointer.right = node
        self.pointer = node
        self.dfs(node.right)

if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(3)
    result = solve.convertBiNode(a)