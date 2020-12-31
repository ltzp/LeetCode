#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31
# @Author  : yuetao
# @Site    : 
# @File    : 二叉树的镜像.py
# @Desc    :
"""
root = [4,2,7,1,3,6,9]

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.dfs(node.left)
        self.dfs(node.right)


if __name__ == '__main__':
    solve = Solution()
    root = TreeNode(4)
    a = TreeNode(2)
    b = TreeNode(7)
    c = TreeNode(1)
    d = TreeNode(3)
    e = TreeNode(6)
    f = TreeNode(9)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    solve.mirrorTree(root)