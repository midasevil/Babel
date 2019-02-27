class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        dp = [[0]*n for i in range(m)]
        dp[0] = [1]*n
        for z in range(m):
            dp[z][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[i][j]


s = Solution()
print(s.uniquePaths(7, 3))
