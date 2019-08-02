#!/usr/bin/env python
#@Time    :2019/8/2 10:43 AP
#@Author  :yelf
#@Filename:11_maxArea.py
#@package :leetcode
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
#双指针法，从左右侧开始遍历
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_res = -1
        l,r = 0,len(height)-1
        while l != r:
            max_res = max(max_res,min(height[l], height[r])*(r - l))
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return max_res
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
