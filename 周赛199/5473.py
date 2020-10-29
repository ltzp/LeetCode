


class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        size = len(target)
        dp = [0]*size
        if target[0]=='1':
            dp[0] = 1
        for i in range(1, size):
            if target[i] == '0' and target[i] == target[i-1]:
                dp[i] = dp[i-1]
            if target[i] == '0' and target[i] != target[i-1]:
                dp[i] = dp[i - 1] + 1
            if target[i] == '1' and target[i] == target[i-1]:
                dp[i] = dp[i - 1]
            if target[i] == '1' and target[i] != target[i-1]:
                dp[i] = dp[i - 1] + 1
        return dp[size-1]


if __name__ == "__main__":
    solve = Solution()
    target = "001011101"
    result = solve.minFlips(target)
    print(result)