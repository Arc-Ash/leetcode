#!/usr/bin/env python
#@Time    :2019/26/7/26 16:09 PM
#@Author  :yelf
#@Filename:238_productExceptSelf.py
#@package :leetcode
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
说明:请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

#本人的渣方法：
class Solution:
    def productExceptSelf(self, nums):
        res = []
        sums = 1
        for i in range(len(nums)):
            sums *=nums[i]
        for i in range(len(nums)):
            res.append(int(sums/nums[i]))
        return res
        
 #不用除法：最优
 class Solution:
    def productExceptSelf(self, nums):
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], l = res[i] * l, l * nums[i]
            res[j], r = res[j] * r, r * nums[j]
        return res
s = Solution()
print(s.productExceptSelf([7,3,20,5]))
 
