#@!/usr/bin/env pyhton
#@Time    :2019/7/26 9:32 AM
#@Aythor  :yelf
#@Filename:163_findMissingRanges.py
#@package :leetcode

给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。
示例：
输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]
#用双指针
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        res = []
        if not nums:
            return res
        l, r =lower, lower
        for i in range(len(nums)):
            if nums[i] == r:
                l, r = nums[i] + 1, nums[i] + 1
            elif nums[i] > r:
                r = max(r, nums[i] - 1)
                if l != r:
                    res.append('{}->{}'.format(str(l),str(r)))
                else:
                    res.append(str(nums[l]))
                l, r = nums[i] + 1, nums[i] + 1
        if l < upper:
            res.append('{}->{}'.format(str(l),str(upper)))
        else:
            res.append(str(l))
        return res
s = Solution()
print(s.findMissingRanges([1,3,50,75],0,99))

