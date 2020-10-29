#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 0011 19:11
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1457_uptodown.py
# @Software: PyCharm
# @desc    :
# https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    all_path = []

    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = []
        self.dfs(root, path)

        return self.all_path


    def dfs(self, node, path):
        if not node:
            return
        path += str(node.val)
        if not node.left and not node.right:
            self.all_path.append(path)
        self.dfs(node.left, path)
        self.dfs(node.right, path)


if __name__ == "__main__":
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(1)
    d = TreeNode(3)
    e = TreeNode(1)
    f = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    solve = Solution()
    result = solve.pseudoPalindromicPaths(a)
    print(result)