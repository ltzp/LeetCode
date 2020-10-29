#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 0002 22:26
# @Author  : Letao
# @Site    : 
# @File    : 面试题08.10.py
# @Software: PyCharm
# @desc    :颜色填充
# https://leetcode-cn.com/problems/color-fill-lcci/

class Solution(object):
    x = [0, 0, -1, 1]
    y = [-1, 1, 0, 0]
    X, Y = 0, 0

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m, self.Y = len(image), len(image) #行
        n, self.X = len(image[0]), len(image[0]) # 列
        used_flag = [[False for y in range(n)] for x in range(m)]
        value = image[sr][sc]
        self.dfs(image, sr, sc, used_flag, newColor, value)
        return image

    def dfs(self, image, sr, sc, flag, newColor, value):
        #sr 横坐标 ->列， sc 纵坐标->行
        if flag[sr][sc]:
            return
        flag[sr][sc] = True
        image[sr][sc] = newColor
        for k in range(0, 4):
            new_sr = sr + self.y[k]
            new_sc = sc + self.x[k]
            if new_sc >= 0 and new_sc < self.X and new_sr >= 0 and new_sr < self.Y and value == image[new_sr][new_sc]:
                self.dfs(image, new_sr, new_sc, flag, newColor, value)


if __name__ == "__main__":
    solve = Solution()
    image = [[0,0,0],[0,1,0]]
    sr = 0
    sc = 0
    newColor = 2
    result = solve.floodFill(image, sr, sc, newColor)
    print(result)
