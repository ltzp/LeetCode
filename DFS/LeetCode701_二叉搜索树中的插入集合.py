#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 0030 18:35
# @Author  : Letao
# @Site    : 
# @File    : LeetCode701_二叉搜索树中的插入集合.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        self.flag = False
        self.dfs(root, val)
        return root

    def dfs(self, node, val):
        if self.flag:
            return
        if not node:
            return
        if node.val < val:
            self.dfs(node.right, val)
            if self.flag:
                return
            node.right = TreeNode(val)
            self.flag = True
            return
        if node.val > val:
            self.dfs(node.left, val)
            if self.flag:
                return
            node.left = TreeNode(val)
            self.flag = True
            return




if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(7)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    val = 5
    result = solve.insertIntoBST(a, val)
    print(result)