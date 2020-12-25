#!/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

# @Author : yuetao
# @File : LeetCode1135_最小生成树.py
# @Time : 2020/12/25
# @Desc:
"""
会员题目：
输入：N = 3, conections = [[1,2,5],[1,3,6],[2,3,1]]
输出：6
解释：
N:点的个数，conections:[1,2,5]->[start, end, cost] 花费最小
选出任意 2 条边都可以连接所有城市，我们从中选取成本最小的 2 条。

最小生成树原理

prime:先定点，再找周围距离最短的点，并且找的这个点不在生成的联通分量内

Kruskal: 选短边

"""

class Solution:

    def minimumCost(self, N, conections):
        # 当边数小于 节点数-1 时，无法连接到每一个点
        if len(conections) < N - 1:
            return -1
        # 按照cost进行排序
        conections.sort(key=lambda node:node[2])
        self.parent = [i for i in range(N)]
        res, e, k = 0,0,0
        while e < N - 1:
            start, end, cost = conections[k]
            k += 1
            x, y = self.find(start-1), self.find(end-1)
            if x != y:
                e += 1
                res += cost
                self.parent[x] = y
        return res

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]




if __name__ == '__main__':
    solve = Solution()
    N = 3
    conections = [[1,2,5],[1,3,6],[2,3,1]]
    result = solve.minimumCost(N, conections)
    print(result)
