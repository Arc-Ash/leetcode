#!/usr/bin/env python
#@Time    :2019/7/22 17:32 PM
#@Author  :yelf
#@Filename:259_threeSumSmaller.py
#@package :leetcode
# 给定有n个整数的nums数组，找到索引三元组i，j，k的数量，其中0 <= i <j <k <n满足条件nums [i] + nums [j] + nums [k ] <目标。
# 例如，给定nums = [-2,0,1,3]和target = 2。
# 返回2.因为有两个三元组[-2,0,1],[-2,0,3]，其总和小于2.
class Solution(object):
    def threeSumSmaller(self,nums,target):
        nums.sort()
        print(nums)
        lenth = len(nums)
        count = 0
        for i in range(lenth-2):
            j = i + 1
            k = lenth-1
            while j < k:
                result = nums[i] + nums[j] + nums[k]
                if result <= target:
                    k -= 1
                    count += 1
                else:
                    j += 1
        return count
s = Solution()
print(s.threeSumSmaller([-2,0,1,3],2))
        
