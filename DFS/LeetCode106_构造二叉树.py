#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 0025 18:44
# @Author  : Letao
# @Site    : 
# @File    : LeetCode106_构造二叉树.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inNode = inorder
        self.postNode = postorder
        self.node_map = {}
        for key, value in enumerate(inorder):
            self.node_map[value] = key
        print(self.node_map)
        return self.dfs(0, len(inorder)-1)


    def dfs(self, left_index, right_index):
        if left_index > right_index:
            return None
        cur_val = self.postNode.pop()
        root = TreeNode(cur_val)
        index = self.node_map.get(cur_val)
        root.right = self.dfs(index+1, right_index)
        root.left = self.dfs(left_index, index-1)
        return root



if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    solve = Solution()
    result = solve.buildTree(inorder, postorder)
    print(result)