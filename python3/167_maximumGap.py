#!/usr/bin/env python
#@Time    :2019/8/1 15:05 PM
#@Author  :yelf
#@Filename:167_maximumGap.py
#@Package :leetcode
#用到了sort（），建议用桶排序，时间复杂度最小
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max = 0
        if len(nums)<2:
            return 0
        for i in range(1,len(nums)):
            if max < nums[i]-nums[i-1]:
                max = nums[i]-nums[i-1]
        return max
        
#桶排序：不会
