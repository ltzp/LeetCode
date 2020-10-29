class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res = ""
        self.k = k
        nums = []
        for i in range(1, n+1):
            nums.append(str(i))
        self.dfs(nums, "",  n)
        return self.res

    def dfs(self, n , num,  size):
        if len(num) == size:
            self.k -= 1
            if self.k == 0:
                self.res = num
                return
            return
        for i in range(len(n)):
            self.dfs(n[:i]+n[i+1:], num + str(n[i]), size)


if __name__ == "__main__":
    solve = Solution()
    n = int(input())
    k = int(input())
    result = solve.getPermutation(n, k)
    print(result)