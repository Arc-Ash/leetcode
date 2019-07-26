325_MaxSubArrayLen.py



给定数组nums和目标值k，找到总和为k的子数组的最大长度。 如果没有，则返回0。
注意：整个nums数组的总和保证适合32位有符号整数范围。
例1：
给定nums = [1，-1,5，-2,3]，k = 3，
返回4.（因为子阵列[1，-1,5，-2]总和为3并且是最长的）
例2：
给定nums = [ -  -2，-1,2,1]，k = 1，
返回2.（因为子数组[-1,2]总和为1并且是最长的）
跟进：你能在O（n）时间做吗？

#本人解法，感觉有问题。。。。
#O（n2）
class Solution(object):
    def MaxSubArrayLen(self, nums, k):
        res = []
        if len(nums)<2:
            return k
        for i in range(len(nums)-1):
            if nums[i] == k:
                res.append(1)
                continue
            l, r= i+1, i+1
            flag = l - i + 1
            sum = nums[i]
            if nums[i] + nums[l] > k:
                continue
            elif sum + nums[l] == k:
                res.append(flag)
            while sum + nums[l] < k:
                sum += nums[l]
                l += 1
                flag+=1
                if l == len(nums):
                    break
                if sum + nums[l] == k:
                    res.append(flag)
                    break
        return max(res)
s = Solution()
print(s.MaxSubArrayLen([3],3))
