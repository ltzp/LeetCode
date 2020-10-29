#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 0001 19:25
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1000_example.py
# @Software: PyCharm
# @desc    :

"""
1,3,5,2 ->4,5,2->9,2->11 代价：4+9+11 =24
1,3,5,2 ->4,5,2->4,7->11 代价：4+7+11= 22


"""

class Solution(object):
    def mergeStones(self, stones):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        length = len(stones)
        s = [0] * (length+1)
        for i in range(1, length+1):
            s[i] = s[i-1] + stones[i-1]
        # 2. 初始化dp数组
        dp = [[0 for i in range(length + 1)] for j in range(length + 1)]
        for small_length in range(2, length+1):
            l = 1
            while (l + small_length - 1 <= length):  # (l + length -1)表示的是长度为length时右边界的索引
                r = l + small_length - 1
                dp[l][r] = float("inf")
                for k in range(l, r):  # 将length内的石子从k, k+1中间进行合并; k+1的最大值正好是r，不会越界
                    dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + s[r] - s[l - 1])
                l += 1
        return dp[1][length]

if __name__ == "__main__":
    stones = [1,3,5,2]
    solve = Solution()
    result = solve.mergeStones(stones)
    print(result)