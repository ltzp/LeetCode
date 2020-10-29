#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 0011 22:04
# @Author  : Letao
# @Site    : 
# @File    : 剑指offer54.py
# @Software: PyCharm
# @desc    : 二叉搜索树的第K大结点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):

    res = []

    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root)
        return self.res[len(self.res) -k]

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)

if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(2)
    a.left = b
    a.right = c
    b.right = d
    k = 1
    result = solve.kthLargest(a, k)
    print(result)