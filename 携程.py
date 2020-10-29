#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 0008 19:30
# @Author  : Letao
# @Site    : 
# @File    : 携程.py
# @Software: PyCharm
# @desc    :

class Solution(object):

    def deal(self, opt_strs):
        self.res = []
        self.length = len(opt_strs)
        self.dfs(opt_strs, 0, "")
        return self.res


    def dfs(self,opt_strs, cur_index, path):
        if len(path) == self.length:
            self.res.append(path)
            return
        choice_str = opt_strs[cur_index]
        for i in range(0, len(choice_str)):
            path += choice_str[i]
            self.dfs(opt_strs, cur_index+1, path)
            path = path[:-1]


if __name__ == "__main__":
    solve = Solution()
    opt_strs = [i for i in input().split()]
    result = solve.deal(opt_strs)
    print(result)