#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/06
# @Author  : yuetao
# @Site    : 
# @File    : 二叉搜索树的后序遍历序列.py
# @Desc    :

"""
分治算法
"""


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def dfs(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            mid = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and dfs(i, mid - 1) and dfs(mid, j-1)
        return dfs(0, len(postorder) - 1)


if __name__ == '__main__':
    solve = Solution()
    postorder = [4, 8, 6, 12, 16, 14, 10]
    result = solve.verifyPostorder(postorder)
    print(result)
