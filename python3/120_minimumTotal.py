#！/usr/bin/env python
#@Time    :2019/8/9 AM
#@Author  :yelf
#@Filename:120_minimumTotal.py
#@package :leetcode
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

class Solution:
    def minimumTotal(self, triangle):
        lenth = len(triangle)
        pre = triangle[0]
        for i in range(1,lenth):
            now = triangle[i][:]
            for j in range(len(now)):
                if j == 0:
                    now[j] += pre[j]
                elif j == len(now)-1:
                    now[j] += pre[j-1]
                else:
                    now[j] = min(pre[j],pre[j-1]) + now[j]
            pre = now[:]
        return min(now)
s = Solution()
print(s.minimumTotal([[1],[2,3],[4,5,6]]))
#print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[-1],[-2,-3],[-4,-5,-6]]))
