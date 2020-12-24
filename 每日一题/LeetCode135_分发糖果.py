#!/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

# @Author : yuetao
# @File : LeetCode135_分发糖果.py
# @Time : 2020/12/24
# @Desc:

"""
每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
dp[i] 和 dp[i-1] 、dp[i + 1] 有关
从左到右：如果dp[i]>dp[i-1] ，递增状态，dp[i] = dp[i-1] + 1
从右到左：dp[i] > dp[i+1], max(dp[i], dp[i+1] + 1)
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        dp = [1] * length
        # 从左到右递增的情况
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1
        # 从右到左
        for i in range(length-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i+1] + 1)
        return sum(dp)


if __name__ == '__main__':
    solve = Solution()
    ratings = [1,0,2]
    result = solve.candy(ratings)
    print(result)
