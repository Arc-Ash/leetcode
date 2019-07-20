# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 你找到的子数组应是最短的，请输出它的长度。
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time      :20.19/7/20 10.00 PM
#@Author    :yelf
#@File      :584_findUnsortedSubarray.py
#@package   :Leetcode
class Solution:
    def findUnsortedSubarray(self, nums):
        #排序得到新list
        count = len(nums)
        a = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == a[i]:
                count -= 1
            else:
                break
        nums.reverse()
        a.reverse()
        #先减去前面相同的
        #翻转，再减去后面相同的count
        for i in range(len(nums)):
            if nums[i] == a[i]:
                count -= 1
            else:
                break
        return count
a = Solution()
print(a.findUnsortedSubarray([2,3,4,5,6,9,7,8,89,66,54]))

# 代码最少：利用pop
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         if nums==sorted(nums):
#             return 0
#         while nums[0]==min(nums):
#             nums.pop(0)
#         while nums[-1]==max(nums):
#             nums.pop()
#         return len(nums)
