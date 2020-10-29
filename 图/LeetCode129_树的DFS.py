#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 0008 17:27
# @Author  : Letao
# @Site    : 
# @File    : LeetCode129_树的DFS.py
# @Software: PyCharm
# @desc    :

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, num):
        num = num * 10 + node.val
        if not node.left and not node.right:
            self.res += num
            return
        if node.left:
            self.dfs(node.left, num)
        if node.right:
            self.dfs(node.right, num)

        return 0

if __name__=="__main__":
    solve = Solution()
    a = TreeNode(4)
    b = TreeNode(9)
    c = TreeNode(0)
    e = TreeNode(5)
    f = TreeNode(1)
    a.left = b
    a.right = c
    b.left = e
    b.right = f
    result = solve.sumNumbers(a)
    print(result)