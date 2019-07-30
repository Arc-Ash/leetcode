#@Time    :2019/7/30 10:21 AM
#@Author  :yelf
#@Filename:215_findKthLargest.py
#@package :leetcode
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

#用python自建库sort：
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]
s = Solution()
print(s.findKthLargest([1, 3, 4],4))

#不用sort：
class Solution:
    def findKthLargest(self, nums, k):
        for i in range(k-1):
            nums.remove(max(nums))
        return max(nums)
        
#双for渣方法：On2
class Solution:
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums[len(nums)-k]
        
#
