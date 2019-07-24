#!/usr/bin/env python
#@Time    :2019/7/24 19:14 PM
#@Author  :yelf
#@Filename:78_subsets.py
#@package :leetcode
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            for temp in result[:]:
                x = temp[:]
                x.append(num)
                result.append(x)
        return result
s = Solution()
print(s.subsets([1, 2, 3]))
