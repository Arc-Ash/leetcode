90_subsetsWithDup.py

class Solution:
    def subsetsWithDup(self, nums):
        result = [[]]
        nums.sort()
        for num in nums:
            for temp in result[:]:
                    x = temp[:]
                    x.append(num)
                    if x not in result:
                        result.append(x)
        return result
s = Solution()
print(s.subsetsWithDup([4,4,4,1,4]))
