#!/usr/bin/env python
#@Time    :2019/7/25 10:19 AM
#@Author  :yelf
#@Filename:152_maxProduct.py
#@package :leetcode
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#解法一：记录当前最大最小，下一个数为负数时，最小值跳最大
class Solution:
    def maxProduct(self, nums):
        result, imax, imin = nums[0], 1, 1
        for i in nums:
            if i < 0:
                imax, imin = imin, imax
            imax = max(i,i*imax)
            imin = min(i,i*imin)
            result = max(result, imax)
        return result
        
#解法二：正向，反向找出相乘list中较大值
class Solution:
    def maxProduct(self, nums):
        #B = nums[::-1]
        B = list(reversed(nums))
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            print(1,nums[i])
            B[i] *= B[i - 1] or 1
            print(2,B[i])
        print(nums,"\n",B)
        return max(max(nums), max(B))
s = Solution()
print(s.maxProduct([2,-5,-2,-4,3]))
