#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 0028 20:19
# @Author  : Letao
# @Site    : 
# @File    : LeetCode117_填充每个节点的下一个右侧节点指针II.py
# @Software: PyCharm
# @desc    :


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return
        if node.left and node.right:
            node.left.next = node.right
        if node.left and not node.right:
            temp = node.next
            while temp:
                if temp.left:
                    node.left.next = temp.left
                    break
                elif temp.right:
                    node.left.next = temp.right
                    break
                temp = temp.next
        if node.right:
            temp = node.next
            while temp:
                if temp.left:
                    node.right.next = temp.left
                    break
                elif temp.right:
                    node.right.next = temp.right
                    break
                temp = temp.next
        self.dfs(node.right) #先构建好右子树
        self.dfs(node.left)


if __name__ == "__main__":
    solve = Solution()
    root = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(7)
    root.left = b
    root.right = c
    b.left = d
    b.right = e
    c.right = f
    result = solve.connect(root)
    print(result)