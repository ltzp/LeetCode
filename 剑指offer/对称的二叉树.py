#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31
# @Author  : yuetao
# @Site    : 
# @File    : 对称的二叉树.py
# @Desc    :

"""
输入：root = [1,2,2,3,4,4,3]
输出：true
中序遍历对称之后就可以:[1,2,2,2,null,2]->错误

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     self.mid_order = []
    #     self.dfs(root)
    #     start, end = 0, len(self.mid_order)-1
    #     while start < end:
    #         if self.mid_order[start] == self.mid_order[end]:
    #             start += 1
    #             end -= 1
    #         else:
    #             return False
    #     return True
    #
    # def dfs(self, node):
    #     if not node:
    #         return
    #     self.dfs(node.left)
    #     self.mid_order.append(node.val)
    #     self.dfs(node.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left , right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.dfs(left.left, right.right) and self.dfs(left.right,right.left)


if __name__ == '__main__':
    solve = Solution()
    root = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)
    root.left = b
    root.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    result = solve.isSymmetric(root)
    print(result)
