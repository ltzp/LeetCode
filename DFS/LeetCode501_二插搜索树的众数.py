#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 0025 21:49
# @Author  : Letao
# @Site    : 
# @File    : LeetCode501_二插搜索树的众数.py
# @Software: PyCharm
# @desc    :
"""
求众数的思路，额外空间O(1)
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = [] #记录结果
        self.most = 0 #众数出现的次数
        self.cur_num = None #当前统计的次数
        self.cnt = 0 #当前结点出现次数
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        if node.val == self.cur_num:
            self.cnt += 1
        else:
            self.cnt = 1
            self.cur_num = node.val

        if self.cnt > self.most:
            self.most = self.cnt
            self.ans = [node.val]
        elif self.cnt == self.most:
            self.ans.append(node.val)
        self.dfs(node.right)


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    a.right = b
    b.right = c
    result = solve.findMode(a)
    print(result)
