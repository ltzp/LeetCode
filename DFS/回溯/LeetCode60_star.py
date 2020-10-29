class Solution(object):

    res = []
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.target = k
        used = [False] * (n+1)
        self.dfs(n, used,[])
        result = ""
        for i in self.res:
            result += str(i)
        return result

    def dfs(self, n, used, result):
        if self.res:
            return
        if len(result) == n:
            self.target -= 1
            if self.target == 0:
                self.res = self.res + result
        for i in range(1, n+1):
            if used[i]:
                continue
            used[i] = True
            result.append(i)
            self.dfs(n, used, result)
            used[i] = False
            result.pop()





if __name__ == "__main__":
    solve = Solution()
    n = 3
    k = 3
    result = solve.getPermutation(n,k)
    print(result)