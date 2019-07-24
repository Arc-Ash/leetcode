#!/usr/bin/env python
#@Time    :2019/7/24 11.25 AM
#@Author  :yelf
#@Filename:56_merge.py
#@package :leetcode
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Solution(object):
    def merge(self, intervals):
        result = []
        intervals.sort()
        for interval in intervals:
            if not result or result[-1][-1] < interval[0]:
                result.append(interval)
            else:
                result[-1][-1] = max(result[-1][-1],interval[-1])
        return result
