63_uniquePathsWithObstacles.py
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        row,column = len(obstacleGrid),len(obstacleGrid[0])
        dp = [1]+[0]*column
        for i in range(row):
            for j in range(column):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j-1]
        return dp[-2]
s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0],[0,0]
]))
