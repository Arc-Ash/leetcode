#!/usr/bin/env python
#@Time    :2019/7/25 14:29 PM
#@Author  :yelf
#@Filename:295_MedianFinder.py
#@package :leetcode
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

#半成品代码：
class MedianFinder(object):
    def __init__(self):
        self.tmp = []
    def addNum(self, num):
        self.tmp = num
        #self.tmp.append(num)
    def findMedian(self):
        if len(self.tmp)%2 != 0:
            return self.tmp[(len(self.tmp)-1)//2]
        else:
            return 0.5*( self.tmp[len(self.tmp)//2] + self.tmp[len(self.tmp)//2-1] )
s = MedianFinder()
s.addNum([2,1])
print(s.findMedian())
