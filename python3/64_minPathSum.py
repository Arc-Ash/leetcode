#!usr/bin/env python
#@Time    :2019/8/6 17:43 PM
#@Author  :yelf
#@Filename:64_minPathSum.py
#@package :leetcode
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

#算是动态规划吧，代码简单，原地
class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i != 0 and j != 0:
                    grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1]
s = Solution()
print(s.minPathSum([[0,1],[1,0]]))
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
