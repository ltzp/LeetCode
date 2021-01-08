#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode990_等式方程的可满足性.py
# @Desc    : 查并集，一般公司不会考察
"""
https://zhuanlan.zhihu.com/p/93647900
https://leetcode-cn.com/problems/satisfiability-of-equality-equations/solution/shi-yong-bing-cha-ji-chu-li-bu-xiang-jiao-ji-he-we/
"""

class Solution(object):

    class UnionFind:

        def __init__(self):
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def merge(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)


    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf = Solution.UnionFind()
        for equation in equations:
            if equation[1] == "=":
                index1 = ord(equation[0]) - ord("a")
                index2 = ord(equation[3]) - ord("a")
                uf.merge(index1, index2)
        for equation in equations:
            if equation[1] == "!":
                index1 = ord(equation[0]) - ord("a")
                index2 = ord(equation[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True



if __name__ == '__main__':
    solve = Solution()
    equations = ["a==b","b!=c","c==a"]
    result = solve.equationsPossible(equations)
    print(result)
