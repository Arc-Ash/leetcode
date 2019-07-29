#!/usr/bin/env python
#@Time    :2019/7/29 PM 16:00
#@Author  :yelf
#@Filename:189_rotate.py
#@package :leetode
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
#用切片
class Solution1:
    def rotate(self, nums, k):
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
#用pop和insert
class Solution2:
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0,nums.pop())
#用   
if __name__=="__main__":
    s=Solution()
    s.rotate()
