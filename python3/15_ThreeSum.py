#!/usr/bib/env python
#@Time 2019/7/22 10:06 AM
#@Author    :yelf
#@Filename  :15_ThreeSum.py
#@package   :leetcode
#给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#时间过长：
class Solution(object):
    def threeSum(self, nums):
        result = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    sort = sorted([nums[i], nums[j], -nums[i] - nums[j]])
                    if sort not in result:
                        result.append(sort)
                else:
                    pass
        return result
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

#优解
#一重i判重，二重左方j，三重右方k
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        lenth = len(nums)
        for i in range(lenth-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = lenth - 1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif res < 0:
                    j += 1
                else:
                    k -= 1
        return result
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
