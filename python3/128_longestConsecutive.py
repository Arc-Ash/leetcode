#!/usr/bin/env python
#@Time    :2019/26/7/29 11:10 AM
#@Author  :yelf
#@Filename:128_longestConsecutive.py
#@package :leetcode
#On2渣方法
class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        res = 0
        for i in range(len(nums)):
            l,r = i,i+1
            while i<len(nums)-1:
                if nums[i] == nums[i + 1]:
                    l += 1
                    i += 1
                    r += 1
                elif nums[i] + 1 == nums[i+1]:
                    i += 1
                    r += 1
                else:
                    break
            res = max(res,r - l)
        return res
        
#本有优化的双指针：
class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        l,r,res = 0,1,0
        if len(nums) < 2:
            return len(nums)
        while r < len(nums):
            if nums[r] == nums[r-1]:
                    l += 1
            elif nums[r] - 1 != nums[r-1]:
                res = max(res, r-l)
                l = r
            r += 1
        res = max(res,r-l)
        return res
