#!/usr/bin/env python
#@Time    :2019/7/24 11.47 AM
#@Author  :yelf
#@Filename:380_RandomizedSet.py
#@package :leetcode
# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
import random
#from random import choice
class RandomizedSet(object):
    def __init__(self):
        self.set1 = set()
    def insert(self, val):
        if val in self.set1:
            return False
        self.set1.add(val)
        return True
    def remove(self, val):
        if val not in self.set1:
            return False
        self.set1.remove(val)
        return True
    def getRandom(self):
        if not self.set1:
            return None
        return random.choice(list(self.set1))
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_1,param_2,param_3,sep="  ")
