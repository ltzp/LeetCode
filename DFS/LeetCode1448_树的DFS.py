#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 0008 23:00
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1448_树的DFS.py
# @Software: PyCharm
# @desc    :TOP Down DFS

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    res = 0
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, -float('inf'))
        return self.res

    def dfs(self, node, max_num):
        if not node:
            return
        if node.val >= max_num:
            self.res += 1
        max_num = max(max_num, node.val)
        self.dfs(node.left, max_num)
        self.dfs(node.right, max_num)


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(3)
    e = TreeNode(1)
    f = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f
    result = solve.goodNodes(a)
    print(result)
