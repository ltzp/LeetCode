#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 0029 17:58
# @Author  : Letao
# @Site    : 
# @File    : LeetCode404_左叶子之和.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return
        if node.left and not node.left.left and not node.left.right:
            self.res += node.left.val
        self.dfs(node.left)
        self.dfs(node.right)


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    result = solve.sumOfLeftLeaves(a)
    print(result)