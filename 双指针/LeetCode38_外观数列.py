#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 0016 20:44
# @Author  : Letao
# @Site    : 
# @File    : LeetCode38_外观数列.py
# @Software: PyCharm
# @desc    :
"""
双指针:start 和 end 记录每个字符连续的位置
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        count = 1
        while count < n:
            length = len(s)
            record_index = []
            cur_char = s[0]
            start, end = 0, 0
            for i in range(length):
                if i == length-1:
                    if s[i] == cur_char:
                        end += 1
                        record_index.append({cur_char: [start, end]})
                    else:
                        record_index.append({cur_char: [start, end]})
                        record_index.append({s[i]: [length-1, length]})
                else:
                    if s[i] == cur_char:
                        end += 1
                    else:
                        record_index.append({cur_char: [start, end]})
                        cur_char = s[i]
                        start = i
                        end = i+1
            next_s = ""
            for i in record_index:
                for key, value in i.items():
                    nums = value[1] - value[0]
                    record_str = key
                    next_s += str(nums) + record_str
            s = next_s
            count += 1
        return s



if __name__ == "__main__":
    solve = Solution()
    n = 5
    result = solve.countAndSay(n)
    print(result)
