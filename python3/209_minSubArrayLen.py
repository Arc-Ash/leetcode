#!usr/bin/env python
#@Time    :2019/7/26 14:16 PM
#@Author  :yelf
#@Filename:209_minSubArrayLen.py
#@package :leetcode
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
示例: 
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

#本人O（n2）算法
class Solution(object):
    def minSubArrayLen(self, s, nums):
        res = len(nums)
        if s>sum(nums):
            return 0
        for i in range(len(nums)-1):
            if nums[i] >= s:
                return 1
            j = i+1
            sums = nums[i]
            if sums + nums[j] >= s:
                res = min(res,j-i+1)
            while j < (len(nums)-1) and sums + nums[j] < s:
                sums += nums[j]
                j += 1
                if sums + nums[j] >= s:
                    res = min(res, j-i+1)
                    break
        return res


#双指针
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if s > sums(nums):
            return 0
        l, r, res, sums = 0, 0, len(nums), 0
        while r<len(nums):
            while sums<s and r<len(nums):
                sums += nums[r]
                r += 1
            while sums>=s and l>=0:
                res.min(res,r-1)
                sums -= nums[l]
                l += 1
        return res
        
