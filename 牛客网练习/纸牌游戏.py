#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/16
# @Author  : yuetao
# @Site    : 
# @File    : 纸牌游戏.py
# @Desc    :
import sys

def solve(values):
    values = sorted(values)
    i = len(values) - 1
    result = 0
    while i >= 0:
        if i - 1 >= 0:
            result += values[i] - values[i - 1]
        else:
            result += values[i]
        i -= 2
    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    result = solve(values)
    print(result)

