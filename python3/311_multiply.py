#!/usr/bin/env pyhton
#@Time    :2019/8/3 AM 10:32
#@Author  :yelf
#@Filename:311_multiply.py
#@package :leetcode

Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.
Example:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

class Solution(object):
    def multiply(self,listA,listB):
    
s = Solution()
print(s.multiply([
  [ 1, 0, 0],
  [-1, 0, 3]
],[
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]))

#On3渣方法，三层for
class Solution(object):
    def multiply(self, listA, listB):
        rowA = len(listA)
        #columnA = rowB
        columnA = len(listA[0])
        rowB = len(listB)
        columnB = len(listB[0])
        listC = [[0]*columnB for i in range(rowA)]
        for i in range(rowA):
            for j in range(columnB):
                sum = 0
                for k in range(columnA):
                    sum += listA[i][k]*listB[k][j]
                listC[i][j] = sum
        return listC
s = Solution()
print(s.multiply([
    [1, 0, 0],
    [-1, 0, 3]
], [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]))
        
