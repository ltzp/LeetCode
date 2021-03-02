#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/29
# @Author  : yuetao
# @Site    : 
# @File    : 二叉树的最近公共祖先.py
# @Desc    :

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
        self.res = TreeNode(None)
        self.dfs(root, p, q)
        return self.res

    def dfs(self, node, p, q):
        if not node:
            return
        left_flag = self.dfs(node.left, p, q)
        right_flag = self.dfs(node.right, p, q)
        if (left_flag and right_flag) or ((node.val == p.val or node.val == q.val) and (left_flag or right_flag)):
            self.res = node
        return left_flag or right_flag or (node.val == p.val or node.val == q.val)


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(6)
    e = TreeNode(2)
    f = TreeNode(0)
    g = TreeNode(8)
    h = TreeNode(7)
    i = TreeNode(4)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i
    solve = Solution()
    result = solve.lowestCommonAncestor(a, b, i)
    print(result.val)