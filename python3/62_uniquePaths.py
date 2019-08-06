#!/usr/bin/env python
#@Time    :2019/8/6 13:58 PM
#@Author  :yelf
#@Filename:62_uniquePaths.py
#@package :leetcode

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
例如，上图是一个7 x 3 的网格。有多少可能的路径？
说明：m 和 n 的值均不超过 100。

#三个阶乘
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #走m-1+n-1步
        r1,r2,r3 = 1,1,1
        for i in range(1,m+n-1):
            r1 *= i
        for i in range(1,m):
            r2 *= i
        for i in range(1,n):
            r3 *= i
        return r1//(r2*r3)
        
#精简
class Solution:
    def uniquePaths(self, m, n):
        f = lambda x:f(x-1)*x if x>=2 else 1
        return f(m+n-2)//(f(m-1)*f(n-1))
s =Solution()
print(s.uniquePaths(3,2))
