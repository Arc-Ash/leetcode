#!/usr/bin/env python
#@Time    :2019/7/24 11.47 AM
#@Author  :yelf
#@Filename:219_containsNearbyDuplicate.py
#@package :leetcode
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        lenth = len(nums)
        if lenth <= 1:
            return False
        keys = {}
        for i in range(lenth):
            if nums[i] in keys:
                if i-keys[nums[i]] <= k:
                    return True
            keys[nums[i]] = i
        return False
        
#优化：
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        keys = {}
        for i,j in range(lenth):
            if nums[i] in keys:
                if i-keys[nums[i]] <= k:
                    return True
            keys[nums[i]] = i
        return False
