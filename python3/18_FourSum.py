#!/usr/bin/env python
#@Time    :2019/7/23 9:49 PM
#@Author  :yelf
#@Filename:18_FourSum.py
#@package :leetcode

# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：答案中不可以包含重复的四元组。
# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        lenth = len(nums)
        if lenth<4:
            return []
        for a in range(lenth-3):
            if a>0 and nums[a] == nums[a-1]:
                continue
            for i in range(a+1,lenth-2):
                if i>a+1 and nums[i] == nums[i-1]:
                    continue
                j = i + 1
                k = lenth - 1
                while j < k:
                    res = nums[i] + nums[j] + nums[k] + nums[a]
                    if res == target:
                        result.append([nums[a],nums[i],nums[j],nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif res < target:
                        j += 1
                    else:
                        k -= 1
        return result
s = Solution()
print(s.fourSum([-1,-5,-5,-3,2,5,0,4],-7))
