#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode697_数组的度.py
# @Desc    :

"""
输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = dict()
        for i in range(len(nums)):
            if nums[i] not in record:
                record[nums[i]] = [1, i, i]
            else:
                record[nums[i]][0] = record[nums[i]][0] + 1
                record[nums[i]][2] = i
        max_count = min_length = 0
        for length, start, end in record.values():
            if length > max_count:
                max_count = length
                min_length = end - start + 1
            elif length == max_count:
                cur_length = end - start + 1
                min_length = min(cur_length, min_length)
        return min_length



if __name__ == '__main__':
    solve = Solution()
    nums = [1, 2, 2, 3, 1]
    result = solve.findShortestSubArray(nums)
    print(result)
