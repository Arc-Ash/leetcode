89_grayCode.py
格雷编码
class Solution:
    def fun(self,n):
        return [i^i>>1 for i in range(2**n)]
s=Solution()
print(s.fun(3))
