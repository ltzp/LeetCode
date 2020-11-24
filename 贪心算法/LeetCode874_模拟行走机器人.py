#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-24 20:01
# @Author  : Letao
# @Site    : 
# @File    : LeetCode874_模拟行走机器人.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        x = y = di = 0
        obstacles = set(map(tuple, obstacles))
        res = 0
        for command in commands:
            if command == -2: # left
                di = (di - 1) % 4
            elif command == -1: #rigth
                di = (di + 1) % 4
            else:
                for i in range(command):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        res = max(res, x * x + y * y)
        return res




if __name__ == "__main__":
    solve = Solution()
    commands = [4,-1,3]
    obstacles = [[2,4]]
    result = solve.robotSim(commands, obstacles)
    print(result)