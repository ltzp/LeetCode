#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/06
# @Author  : yuetao
# @Site    : 
# @File    : 二叉搜索树与双向链表.py
# @Desc    :


# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            record_node.append(root)
            dfs(root.right)

        record_node = list()
        dfs(root)
        length = len(record_node)
        for i in range(length):
            record_node[i].left = record_node[(i+length-1)% length]
            record_node[i].right = record_node[(i + 1)% length]
        return record_node[0]

if __name__ == '__main__':
    solve = Solution()
    root = Node(4)
    a = Node(2)
    b = Node(5)
    c = Node(1)
    d = Node(3)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    result = solve.treeToDoublyList(root)
