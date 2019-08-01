#!/usr/bin/env python
#@Time    :2019/8/1 15:45 PM
#@Author  :yelf
#@Filename:347_topKFrequent.py
#@Package :leetcode
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

#本人用字典的渣方法
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = list(set(nums))
        dic = dict.fromkeys(keys)
        for i in range(len(keys)):
            dic.update({keys[i]:nums.count(keys[i])})
        res = []
        for j in range(k):
            res.append(max(dic,key=dic.get))
            dic.pop(res[-1])
        return res
        
#Python 中提供一个字典结构用作哈希表和在 collections 库中的 Counter 方法去构建我们需要的哈希表。
#在 Python 中可以使用 heapq 库中的 nlargest 方法，可以在相同时间内完成，但只需要一行代码解决。
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
