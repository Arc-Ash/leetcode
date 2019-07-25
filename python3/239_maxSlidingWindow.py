#!/usr/bin/env phython
#@Time    :2019/7/25 11.52 AM
#@Author  :yelf
#@Filename:239_maxSlidingWindow.py
#@package :leetcode
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口最大值。
# 示例:
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
#用for，别用while（效率也不高）
class Solution:
    def maxSlidingWindow(self, nums, k):
        lenth = len(nums)
        res = []
        if lenth < k or nums == res:
            return []
        for i in range(lenth-k+1):
            res.append(max(nums[i:i+k]))
        return res
