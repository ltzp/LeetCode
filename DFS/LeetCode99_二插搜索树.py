#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 0008 19:42
# @Author  : Letao
# @Site    : 
# @File    : LeetCode99_二插搜索树.py
# @Software: PyCharm
# @desc    : 二叉搜索树中序遍历既是排好序的数组，如果排序不满足，则不是二叉搜索树


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    node = []
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        x = None
        y = None
        pre = self.node[0]
        for i in range(1, len(self.node)):
            if pre.val > self.node[i].val:
                y = self.node[i]
                if not x:
                    x = pre
        if x and y:
            x.val, y .val = y.val, x.val

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.node.append(node)
        self.dfs(node.right)


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(2)
    a.left = b
    a.right = c
    c.left = d