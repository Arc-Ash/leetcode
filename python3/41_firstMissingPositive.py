#!/usr/bin/env python
#@Time    :2019/8/2 11:56 AM
#@Author  :yelf
#@Filename:41_firstMissingPositive.py
#@package :leetcode
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3
示例 2:
输入: [3,4,-1,1]
输出: 2

#初步双for思路
class Solution1:
    def firstMissingPositive(self, nums):
        nums.sort()
        if 1 not in nums:
            return 1
        for i in range(nums.index(1)+1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] != nums[i-1]+1:
                return nums[i-1]+1
        return nums[-1]+1
 
#细化，
class Solution:
    def firstMissingPositive(self, nums):
        #n = list(set(nums))
        i = 1
        while i in nums:
            i += 1
        return i
s = Solution()
print(s.firstMissingPositive([0,2,2,1,1]))
