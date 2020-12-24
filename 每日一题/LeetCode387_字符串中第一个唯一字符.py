#!/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

# @Author : yuetao
# @File : LeetCode387_字符串中第一个唯一字符.py
# @Time : 2020/12/23
# @Desc:  easy

class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for i in range(len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = [i]
            else:
                hash_map.get(s[i]).append(i)
        res_index = float("inf")
        for key,value in hash_map.items():
            if len(value) >= 2:
                continue
            else:
                res_index = min(res_index, value[0])
        if res_index == float("inf"):
            return -1
        else:
            return res_index


if __name__ == '__main__':
    solve = Solution()
    s = "loveleetcode"
    result = solve.firstUniqChar(s)
    print(result)
