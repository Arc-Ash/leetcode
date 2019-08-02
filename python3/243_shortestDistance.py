#!/usr/bin/env python
#@Time    :2019/8/2 9:52 AM
#@Author  :yelf
#@Filename:243_shortestDistance.py
#@package :leetcode

给定一个单词列表和两个单词word1和word2，返回列表中这两个单词之间的最短距离。
For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

class Solution:
    def shortestDistance(self,words,word1,word2):
        min_distance = len(words) - 1
        p1,p2 = -1,-1
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
                if p2 != -1 and p1-p2 < min_distance:
                    min_distance = p1-p2
            elif words[i] == word2:
                p2 = i
                if p1 != -1 and p1-p2 < min_distance:
                    min_distance = p2-p1
        return min_distance
s = Solution()
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))
