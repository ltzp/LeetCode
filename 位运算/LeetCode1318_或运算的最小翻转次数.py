#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/15
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1318_或运算的最小翻转次数.py
# @Desc    :

import sys


def solve_problem(a, b, c):
    count = 0
    while a > 0 and b > 0 and c > 0:
        a_left = a & 1
        b_left = b & 1
        c_left = c & 1
        a = a >> 1
        b = b >> 1
        c = c >> 1
        if a_left == b_left and a_left == 1 and c_left == 0:
            count += 2
            continue
        if a_left | b_left != c_left:
            count += 1
            continue
    while b > 0 and c > 0:
        b_left = b & 1
        c_left = c & 1
        b = b >> 1
        c = c >> 1
        if b_left != c_left:
            count += 1
    while a > 0 and c > 0:
        a_left = a & 1
        c_left = c & 1
        a = a >> 1
        c = c >> 1
        if a_left != c_left:
            count += 1
    while a > 0 and b > 0 and c == 0:
        a_left = a & 1
        b_left = b & 1
        a = a >> 1
        b = b >> 1
        if a_left == b_left and a_left == 1:
            count += 2
            continue
        if a_left | b_left != 0:
            count += 1
            continue
    while b > 0:
        b_left = b & 1
        b = b >> 1
        if b_left == 1:
            count += 1
    while a > 0:
        a_left = a & 1
        a = a >> 1
        if a_left == 1:
            count += 1
    while c > 0:
        c_left = c & 1
        c = c >> 1
        if c_left == 1:
            count += 1
    return count


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        result = solve_problem(values[0], values[1], values[2])
        ans.append(result)
    print(ans)

