#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time    :2019/7/20 16:57 PM
#@Author  :yelf
#@File    :167_Two_sum2.py
#@package :leetcode
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# 说明:
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return 0
        key = {}
        for i,j in enumerate(nums):
            if target-j in key:
                return [key[target-j]+1,i+1]
            else:
                key[j] = i
s = Solution()
print(s.twoSum([5,234,294,4,4],9))
