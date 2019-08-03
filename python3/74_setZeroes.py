#!/usr/bin/env pyhton
#@Time    :2019/8/2 PM 17:17
#@Author  :yelf
#@Filename:74_setZeroes.py
#@package :leetcode
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
示例 1:
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

class Solution:
    def setZeroes(self, matrix):
        row, column = set(),set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                    matrix[i][j] = 0
        return matrix
s =Solution()
print(s.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))
