#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/10
# @Author  : yuetao
# @Site    : 
# @File    : 把数字翻译成字符串.py
# @Desc    :
"""
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
类似ip地址的题目，选一位或者选连续两位
"""


class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        self.s_num = str(num)
        self.length = len(self.s_num)
        self.res = 0
        self.dfs(0,"")
        return self.res


    def dfs(self,cur_index, cur_str):
        if cur_index >= self.length:
            print(cur_str)
            self.res += 1
            return
        cur_str += chr(int(self.s_num[cur_index]) + ord("a"))
        self.dfs(cur_index+1, cur_str)
        cur_str = cur_str[:-1]
        if cur_index + 1 <= self.length -1 and 10 <= int(self.s_num[cur_index] + self.s_num[cur_index+1])<=25:
            cur_str += chr(int(self.s_num[cur_index] + self.s_num[cur_index+1]) + ord("a"))
            self.dfs(cur_index + 2, cur_str)




if __name__ == '__main__':
    solve = Solution()
    num = 506
    result = solve.translateNum(num)
    print(result)
