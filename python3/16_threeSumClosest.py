!/usr/bib/env python
#@Time 2019/7/22 16.12 PM
#@Author    :yelf
#@Filename  :16_threeSumClosest.py
#@package   :leetcode
#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
#假定每组输入只存在唯一答案。例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#仿照例题15，使用三数之和减去target平方判断大小
class Solution(object):
    def threeSumClosest(self, nums,target):
        nums.sort()
        lenth = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(lenth - 2):
            j = i + 1
            k = lenth - 1
            while j<k:
                ad = nums[i] + nums[j] + nums[k]
                if ad == target:
                    return target
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while j<k and nums[k] == nums[k-1]:
                        k -= 1
                elif ad<target:
                    j += 1
                else:
                    k -= 1
                if (result-target)**2 > (ad-target)**2:
                    result = ad
        return result
s = Solution()
print(s.threeSumClosest([-1,2,1,-4],1))
