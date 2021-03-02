#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/29
# @Author  : yuetao
# @Site    : 
# @File    : 二叉搜素树的最近公共祖先.py
# @Desc    :
"""
搜索二叉树性质：左边小右边大。
如果当前节点在查找的两个节点中间，则返回当前节点
如果都小，则左边进行dfs
如果都大，则右边进行dfs
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.res = TreeNode(None)
        if p.val > q.val:
            self.dfs(root, q, p)
        else:
            self.dfs(root, p, q)
        return self.res

    def dfs(self, node, node1, node2):
        if node1.val <= node.val <= node2.val:
            self.res = node
            return
        if node.val < node1.val and node.val < node2.val:
            self.dfs(node.right, node1, node2)
        if node.val > node1.val and node.val > node2.val:
            self.dfs(node.left, node1, node2)


if __name__ == '__main__':
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(8)
    d = TreeNode(0)
    e = TreeNode(4)
    f = TreeNode(7)
    g = TreeNode(9)
    h = TreeNode(3)
    i = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i
    solve = Solution()
    result = solve.lowestCommonAncestor(a, g, i)
    print(result.val)
