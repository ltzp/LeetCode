class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    #进行判断上下左右为1的个数
                    nums = 0
                    if j - 1 >= 0 and grid[i][j-1] == 1:
                        nums += 1
                    if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                        nums += 1
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        nums += 1
                    if i + 1 < len(grid) and grid[i+1][j] == 1:
                        nums += 1
                    print(i, j, nums)
                    res += 4 - nums
        return res


if __name__ == "__main__":
    solve = Solution()
    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]
    result = solve.islandPerimeter(grid)
    print(result)
