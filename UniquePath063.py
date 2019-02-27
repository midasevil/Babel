class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j==0:
                    obstacleGrid[i][j] = 1
                elif i ==0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j ==0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        print(obstacleGrid)
        return obstacleGrid[i][j]


s = Solution()
t = s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])

            

print(t)                    

