"""
递归找出所有

"""

import queue
from collections import defaultdict,deque


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """

        """
        以 0 点为根，构造多叉树，层次遍历
        """
        points = defaultdict(list)
        flag = [False]*n
        result = [1]*n
        q = deque()
        q.append(0)
        while q:
            val = q.popleft()
            flag[val] = True
            for edge in edges:
                if edge[0] == val and not flag[edge[1]]:
                    points[val].append(edge[1])
                    q.append(edge[1])
                elif edge[1] == val and not flag[edge[0]]:
                    points[val].append(edge[0])
                    q.append(edge[0])
                else:
                    continue
        print(points)
        tree_set = defaultdict(set)

        # for i in range(0, n):
        #     tree_set[i]
        #     points[i]
        for point in points:
            index = point
            self.get_all_point(index, point, points, tree_set, labels)
        print(tree_set)
        for tree in tree_set:
            result[tree] = result[tree] + len(tree_set[tree])
        return result

    def get_all_point(self, index, point, points, tree_set, labels):
        if point not in points:
            return None
        else:
            for val in points[point]:
                if labels[val] == labels[index]:
                    tree_set[index].add(val)
                self.get_all_point(index, val, points, tree_set, labels)


if __name__ == "__main__":
    solve = Solution()
    n = 4
    edges = [[0,1],[1,2],[0,3]]
    labels = "bbbb"
    result = solve.countSubTrees(n, edges, labels)
    print(result)
