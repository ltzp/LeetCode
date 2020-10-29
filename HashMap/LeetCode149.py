class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return 2
        index_k_hashmap = dict()
        for i in range(n):
            every_k_hash = dict()
            for j in range(n):
                if i == j:
                    continue
                if points[j][0] - points[i][0] == 0:
                    k = "a"
                else:
                    k = (points[j][1] - points[i][1])/(points[j][0] - points[i][0])
                if k not in every_k_hash:
                    every_k_hash[k] = 1
                else:
                    every_k_hash[k] += 1
            index_k_hashmap[i] = every_k_hash
        max = 1
        for index, k_dict in index_k_hashmap.items():
            for value in k_dict.values():
                if value >= max:
                    max = value
        res = max+1
        return res


if __name__ == "__main__":
    solve = Solution()
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    result = solve.maxPoints(points)
    print(result)
