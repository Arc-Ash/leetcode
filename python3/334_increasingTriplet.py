#@Time    :2019/7/30 15:31 PM
#@Author  :yelf
#@Filename:334_increasingTriplet.py
#@package :leetcode
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
数学表达式如下:
如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
示例 1:
输入: [1,2,3,4,5]
输出: true
示例 2:
输入: [5,4,3,2,1]
输出: false

#初步渣方法：
class Solution:
    def increasingTriplet(self, nums):
        if len(nums)<3:
            return False
        for i in range(len(nums)):
            l, r = i, i+1
            while r<len(nums):
                if nums[r] > nums[l]:
                    if max(nums[r:]) != nums[r]:
                        return True
                r += 1
        return False
s = Solution()
print(s.increasingTriplet([2,4,-2,-3]))

#改良复杂度：
