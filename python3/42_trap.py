42_trap.py
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）.
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

#不会写，别人的代码
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        max_height = max(height)
        max_height_index = height.index(max_height)
        area = 0
        tmp = height[0]
        for height1 in height[:max_height_index]:
            if height1 > tmp:
                tmp = height1
            else:
                area += (tmp - height1)
        tmp = height[-1]
        for height1 in height[:max_height_index:-1]:
            if height1 > tmp:
                tmp = height1
            else:
                area += (tmp - height1)
        return area
