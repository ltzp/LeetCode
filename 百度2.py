#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 0003 19:59
# @Author  : Letao
# @Site    : 
# @File    : 百度2.py
# @Software: PyCharm
# @desc    :
import collections
class Solution:

    def deal(self,cows_map, cows, features, all_left_right):
        res = []
        for left_rigth in all_left_right:
            left = left_rigth[0]
            right = left_rigth[1]
            for i in range(left, right+1):
                if i not in cows_map:
                    cows_map[i] = 1
                else:
                    cows_map[i] += 1
        for key, value in cows_map.items():
            if value == features:
                res.append(key)
        print(len(res))
        my_res = sorted(res)
        print(" ".join(str(i) for i in my_res))


if __name__ == "__main__":
    T = int(input())
    solve = Solution()
    for i in range(T):
        infos = input().split()
        cows = int(infos[0])
        features = int(infos[1])
        #print(T, ",", cows,"," ,features)
        cows_map = {}
        all_left_right = []
        for j in range(features):
            feature = int(input())
            #print(feature)
            # left_right_infos = []
            for k in range(feature):
                input_infos = input().split()
                left = int(input_infos[0])
                right = int(input_infos[1])
                left_right = [left,right]
                all_left_right.append(left_right)
                #print(all_left_right)
        solve.deal(cows_map, cows, features, all_left_right)