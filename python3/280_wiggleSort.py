#@Time    :2019/7/30 10:21 AM
#@Author  :yelf
#@Filename:280_wiggleSort.py
#@package :leetcode
给定未排序的数组nums，将其重新排序，使得nums [0] <= nums [1]> = nums [2] <= nums [3] ....
例如，给定nums = [3,5,2,1,6,4]，一个可能的答案是[1,6,2,5,3,4]。
class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        for i in range(1,len(nums)-1,2):
            nums[i],nums[i+1] = nums[i+1],nums[i]
        return nums
s = Solution()
print(s.wiggleSort([]))
