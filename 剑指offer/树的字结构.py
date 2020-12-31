#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31
# @Author  : yuetao
# @Site    : 
# @File    : 树的字结构.py
# @Desc    :
"""

输入：A = [3,4,5,1,2], B = [4,1]
输出：true

三种情况：
1.A,B在一开始就相等
2.B在A的左侧
3.B在A的右侧
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not A or not B:
            return False
        return self.dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


    def dfs(self, node1, node2):
        if not node2:
            return True
        if not node1 or node1.val != node2.val:
            return False
        return self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)





if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    f = TreeNode(4)
    g = TreeNode(1)
    f.left = g
    solve = Solution()
    result = solve.isSubStructure(a, f)
    print(result)

