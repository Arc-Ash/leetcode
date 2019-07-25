#!/usr/bin/env python
#@Time    :2019/7/25 16:29 PM
#@Author  :yelf
#@Filename:228_summaryRanges.py
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
示例 1:
输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:
输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
#用format输出
#用双指针来做
class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return res
        l = r = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                r += 1
            else:
                if l != r:
                    res.append('{}->{}'.format(nums[l],nums[r]))
                else:
                    res.append(str(nums[l]))
                l = r = i
        if l != r:
            res.append('{}->{}'.format(nums[l],nums[r]))
        else:
            res.append(str(nums[l]))
        return res
s = Solution()
print(s.summaryRanges([1,2]))
