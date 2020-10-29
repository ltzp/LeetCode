#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 0026 15:07
# @Author  : Letao
# @Site    : 
# @File    : LeetCode538_把二叉树转为累加树.py
# @Software: PyCharm
# @desc    :
"""
二叉树的反先序遍历
右->中->左
RML
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.right)
        self.sum += node.val
        node.val = self.sum
        self.dfs(node.left)

if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(4)
    b = TreeNode(1)
    c = TreeNode(6)
    d = TreeNode(0)
    e = TreeNode(2)
    f = TreeNode(5)
    g = TreeNode(7)
    h = TreeNode(8)
    i = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.right = i
    g.right = h
    result = solve.convertBST(a)
    print(result)