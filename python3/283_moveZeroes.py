#@Time    :2019/7/29 20:20 PM
#@Author  :yelf
#@Filename:283_moveZeroes.py
#@package :leetcode
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
class Solution1:
    def moveZeroes(self,nums):
        flag = nums.count(0)
        for i in range(flag):
            nums.remove(0)
        nums.extend([0]*flag)
        return nums
class Solution2:
    def moveZeroes(self,nums):
        tmp,j = [0]*len(nums),0
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp[j] = nums[i]
                j += 1
        return tmp
s = Solution2()
print(s.moveZeroes([0,1,0,3,12]))
        
        
