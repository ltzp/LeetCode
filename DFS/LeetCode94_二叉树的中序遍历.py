#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 0014 18:05
# @Author  : Letao
# @Site    : 
# @File    : LeetCode94_二叉树的中序遍历.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    solve = Solution()
    result = solve.inorderTraversal(a)
    print(result)