#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/18
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode721_账户合并.py
# @Desc    :
import collections
class Solution(object):

    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))

        def find_parent(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find_parent(self.parent[index])
            return self.parent[index]

        def merge(self, index1, index2):
            self.parent[self.find_parent(index1)] = self.find_parent(index2)

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_index = dict()
        email_name = dict()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_index:
                    email_index[email] = len(email_index)
                    email_name[email] = name
        # print(email_index)
        # print(email_name)
        uf = Solution.UnionFind(len(email_index))
        for account in accounts:
            first_email_index = email_index[account[1]]
            for email in account[2:]:
                uf.merge(first_email_index, email_index[email])
        indexToEmail = collections.defaultdict(list)
        for email,index in email_index.items():
            index = uf.find_parent(index)
            indexToEmail[index].append(email)
        res = []
        for emails in indexToEmail.values():
            res.append([email_name[emails[0]]] + sorted(emails))
        return res


if __name__ == '__main__':
    solve = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    result = solve.accountsMerge(accounts)
    print(result)
