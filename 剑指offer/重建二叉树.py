#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 20:58
# @Author  : Letao
# @Site    : 
# @File    : 重建二叉树.py
# @Software: PyCharm
# @desc    :
"""
LeetCode106  - 构造二叉树相似
"""


import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        record_index = {}
        for index, value in enumerate(inorder):
            record_index[value] = index
        self.record = record_index
        self.pre = collections.deque()
        for i in preorder:
            self.pre.append(i)
        self.midorder = inorder
        return self.dfs(0, len(preorder)-1)

    def dfs(self, left, right):
        if left > right:
            return
        cur = self.pre.popleft()
        node = TreeNode(cur)
        index = self.record.get(cur)
        node.left = self.dfs(left, index-1)
        node.right = self.dfs(index+1, right)
        return node


if __name__ == "__main__":
    solve = Solution()
    property = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = solve.buildTree(property, inorder)
    print(result)
