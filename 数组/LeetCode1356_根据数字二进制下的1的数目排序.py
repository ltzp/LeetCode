#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-06 11:03
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1356_根据数字二进制下的1的数目排序.py
# @Software: PyCharm
# @desc    :


"""
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
"""

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        length = len(arr)
        if length == 0:
            return arr
        record_map = {}
        for i in range(length):
            one_number = self.get_count_one(arr[i])
            if one_number not in record_map:
                record_map[one_number] = [arr[i]]
            else:
                now_record = record_map.get(one_number)
                now_record.append(arr[i])
                record_map[one_number] = sorted(now_record)
        record_map = sorted(record_map.items())
        for key, value in record_map:
            res.extend(value)
        return res


    def get_count_one(self, num):
        cnt = 0
        while num:
            cnt += num & 1
            num >>= 1
        return cnt

if __name__ == "__main__":
    solve = Solution()
    arr = [0,1,2,3,4,5,6,7,8]
    # arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    result = solve.sortByBits(arr)
    print(result)