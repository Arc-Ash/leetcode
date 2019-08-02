#!/usr/bin/env pyhton
#@Time    :2019/8/2 PM 17:17
#@Author  :yelf
#@Filename:84_largestRectangleArea.py
#@package :leetcode
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

class Solution(object):
    def largestRectangleArea(self, heights):
        res = 0
        for i in range(len(heights)):
            min_height = len(heights)*max(heights)
            for j in range(i,len(heights)):
                min_height = min(min_height,heights[j])
                res = max(res,min_height*(j-i+1))
        return res
s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
