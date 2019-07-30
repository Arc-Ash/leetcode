#@Time    :2019/7/30 15:01 PM
#@Author  :yelf
#@Filename:287_findDuplicate.py
#@package :leetcode
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
示例 1:
输入: [1,3,4,2,2]
输出: 2
示例 2:
输入: [3,1,3,4,2]
输出: 3
说明：
不能更改原数组（假设数组是只读的）。只能使用额外的 O(1) 的空间。时间复杂度小于 O(n2) 。数组中只有一个重复的数字，但它可能不止重复出现一次。

#sort后，相邻元素相等即可判断
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = sorted(nums)
        for i in range(1,len(m)):
            if m[i] == m[i-1]:
                return m[i]
#用集合，
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
#开辟新的list： seen，这个会超时。。。
class Solution:
    def findDuplicate(self, nums):
        seen = []
        for num in nums:
            if num in seen:
                return num
            seen.append(num)
