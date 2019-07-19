class solution(object):
    def twosum(nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
print(solution.twosum([3,2,4],6))
#速度最快：
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        keys = {}
        for i, v in enumerate(nums):
            if target-v in keys:
                return [keys[target-v],i]
            else:
                keys[v] = i

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
