#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time    :2019/7/20 14.51 PM
#@Author  :yelf
#@Filename:26_removeDuplicates.py
#@package :leetcode

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

#nums = [1,1,2]
#a = nums
#print(list(set(a)))

class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(list(set(nums)))
        return len(nums)
a = Solution()
print(a.removeDuplicates(nums))
