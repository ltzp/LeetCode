

class Solution:

    res = []
    flag = False

    def deal(self, num):
        sqr_map = {}
        for i in range(1, 11):
            sqr_map[i] = i**2
        root = 0
        for key, value in sqr_map.items():
            if value < num:
                continue
            else:
                root = key - 1
                break
        for i in range(root, 0, -1):
            self.flag = False
            self.dfs(num, sqr_map, i, [], 0)
        return self.res

    def dfs(self, num, sqr_map, node, path, squares_sum):
        if self.flag:
            return
        squares_sum += sqr_map.get(node)
        if num < squares_sum:
            return
        elif num == squares_sum:
            path.append(node)
            self.res.append(path)
            self.flag = True
            return
        else:
            path.append(node)
            for i in range(node, 0, -1):
                if squares_sum + sqr_map.get(i) > num:
                    continue
                self.dfs(num, sqr_map, i, path, squares_sum)


if __name__ == "__main__":
    solve = Solution()
    #num = int(input())
    num = 63
    result = solve.deal(num)
    print(result)
