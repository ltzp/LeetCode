
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        n = len(wall)
        if n == 0:
            return 0
        if n == 1 and len(wall[0]) == 1:
            return 1
        if n == 1 and len(wall[0]) > 1:
            return 0
        all_length = 0
        for i in wall[0]:
            all_length += i
        not_through_map = {}
        for i in range(0, n):
            valus = []
            index = 0
            for j in range(0, len(wall[i])):
                index = index + wall[i][j]
                if index != all_length:
                    valus.append(index)
            not_through_map[i] = valus
        through_map = {}
        for key, values in not_through_map.items():
            for value in values:
                if value not in through_map:
                    through_map[value] = 1
                else:
                    through_map[value] += 1
        max = 0
        for nums in through_map.values():
            if nums > max:
                max = nums
        return n-max


if __name__ == "__main__":
    solve = Solution()
    wall = [[1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]]
    result = solve.leastBricks(wall)
    print(result)