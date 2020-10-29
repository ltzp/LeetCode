#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027 19:34
# @Author  : Letao
# @Site    : 
# @File    : LeetCode144_二叉树的前序遍历.py
# @Software: PyCharm
# @desc    :

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        if not root:
            return self.res
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return
        self.res.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    result = solve.preorderTraversal(a)
    print(result)