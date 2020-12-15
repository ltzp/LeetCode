#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-28 23:50
# @Author  : Letao
# @Site    : 
# @File    : LeetCode621_任务调度_填桶法.py
# @Software: PyCharm
# @desc    :
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        record = [0] * 26
        for i in tasks:
            record[ord(i) - ord('A')] += 1
        count_max = 0
        for i in record:
            count_max = max(i, count_max)
        equal_count_max = 0
        for r in record:
            if r == count_max:
                equal_count_max += 1
        return max((n + 1) * (count_max - 1) + equal_count_max, len(tasks))


if __name__ == "__main__":
    solve = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    result = solve.leastInterval(tasks, n)
    print(result)
