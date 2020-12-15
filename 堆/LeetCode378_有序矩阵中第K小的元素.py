#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-01 20:46
# @Author  : Letao
# @Site    : 
# @File    : LeetCode378_有序矩阵中第K小的元素.py
# @Software: PyCharm
# @desc    :

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        pq = [(matrix[i][0], i, 0)for i in range(n)]
        print(pq)
        heapq.heapify(pq)
        for i in range(k-1):
            num,x,y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        return heapq.heappop(pq)[0]

if __name__ == "__main__":
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 8
    solve = Solution()
    result = solve.kthSmallest(matrix, k)
    print(result)