#!/usr/bin/env python
#@Time    :2019/8/1 13:56 PM
#@Author  :yelf
#@Filename:387_firstUniqChar.py
#@Package :leetcode
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
案例:
s = "leetcode"
返回 0.
s = "loveleetcode",
返回 2.

#本人渣方法:count效率低
class Solution:
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
        
#效率高：find和rfind返回下标
 class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.find(s[i]) == s.rfind(s[i]):
                return i
        return -1
