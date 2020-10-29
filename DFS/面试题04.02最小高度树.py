#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 0002 19:22
# @Author  : Letao
# @Site    : 
# @File    : 面试题04.02最小高度树.py
# @Software: PyCharm
# @desc    :构造最小高度的二叉树, 每次取中间的一个数为根节点

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__ == "__main__":
    solve = Solution()
    nums = [-10,-3,0,5,9]
    result = solve.sortedArrayToBST(nums)
