class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies) == 0:
            return 0
        kind_map = dict()
        for candie in candies:
            if candie not in kind_map:
                kind_map[candie] = 1
            else:
                kind_map[candie] += 1
        return min(len(candies)/2, len(kind_map))

if __name__=="__main__":
    solve = Solution()
    candies = [1,1,2,3]
    result = solve.distributeCandies(candies)
    print(result)