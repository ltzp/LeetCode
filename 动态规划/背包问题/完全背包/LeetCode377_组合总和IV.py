#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/07
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode377_组合总和IV.py
# @Desc    :
"""
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

如果求排列数就是外层for遍历背包，内层for循环遍历物品。

target:背包的数量
nums:货物的价值

"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        print(dp)
        return dp[target]


if __name__ == '__main__':
    nums = [1,2,3]
    target = 4
    solve = Solution()
    result = solve.combinationSum4(nums, target)
    print(result)
