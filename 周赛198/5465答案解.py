#!/usr/bin/python3

"""
直接DFS, 用一个外部字典记录每个字符出现的次数；
用一个外部数组ans记录每个节点子树(包含该节点)中包含的该节点字符总数；
在遍历到节点u的时候，假设节点u的字符是c，那么该节点的字符总数ans[u] = {DFS遍历完节点u之后的ans1[u]} - {DFS遍历前ans2[u]}
ans1[u]其实也就是从根节点途径节点u到u所有子树遍历完之后的所有字符c的数量，ans2[u]其实就是该节点到根节点之前的这一部分的字符c的数量；
相减之后，刚好结果就是位置u和之后子树中所有的字符c的数量

"""
from collections import defaultdict

class Solution:
    def countSubTrees(self, n, edges, labels):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u: int, pre: int):
            c = labels[u]
            ans[u] -= cnt[c]
            cnt[c] += 1
            for v in graph[u]:
                if v == pre:
                    continue
                dfs(v, u)
            ans[u] += cnt[c]
        ans = [0] * n
        cnt = defaultdict(int)
        dfs(0, -1)
        return ans


if __name__ == "__main__":
    solve = Solution()
    n = 4
    edges = [[0,1],[1,2],[0,3]]
    labels = "bbbb"
    result = solve.countSubTrees(n, edges, labels)
    print(result)