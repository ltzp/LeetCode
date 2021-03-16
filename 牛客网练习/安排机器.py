#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/16
# @Author  : yuetao
# @Site    : 
# @File    : 安排机器.py
# @Desc    :
import sys

class Solution(object):

    def get_result(self, N, M, machines, tasks):
        result = 0
        count = 0
        machines.sort(key=lambda x:(x[0], x[1]), reverse=True)
        tasks.sort(key=lambda x:(x[0], x[1]), reverse=True)
        dp = [0] * 105
        j = 0
        for i in range(M):
            while j < N and machines[j][0] >= tasks[i][0]:
                dp[machines[j][1]] += 1
                j += 1
            for k in range(tasks[i][1], 105):
                if dp[k]:
                    count += 1
                    dp[k] -= 1
                    result += 200 * tasks[i][0] + 3 * tasks[i][1]
                    break
        return count, result


if __name__ == '__main__':
    solve = Solution()
    nums = list(map(int,sys.stdin.readline().strip().split()))
    N,M = nums[0],nums[1]
    machines = []
    tasks = []
    for i in range(N):
        machine = list(map(int,sys.stdin.readline().strip().split()))
        machines.append(machine)
    for i in range(M):
        task = list(map(int,sys.stdin.readline().strip().split()))
        tasks.append(task)
    count, result = solve.get_result(N, M, machines, tasks)
    print(count, result)