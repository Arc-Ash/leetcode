#!/usr/bin/env pyhton
#@Time    :2019/8/5 AM 11:13
#@Author  :yelf
#@Filename:36_isValidSudoku.py
#@package :leetcode
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
class Solution:
    def isValidSudoku(self, board):
        lenth = len(board)
        for i in range(lenth):
            for j in range(lenth):
                #横竖不重
                if board[i][j] == ".":
                    continue
                for k in range(lenth-1,j,-1):
                    if board[i][j] == board[i][k]:
                        return False
                for k in range(lenth-1,i,-1):
                    if board[i][j] == board[k][j]:
                        return False
                #小格子不重
                for k in range(i+1,lenth):
                    if k%3 == 0:
                       break
                    for h in range(j//3*3,j//3*3+3):
                        if board[i][j] == board[k][h]:
                            return False
        return True
s = Solution()
print(s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

#稍微好一点，lenth换9
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                for k in range(8,j,-1):
                    if board[i][j] == board[i][k]:
                        return False
                for k in range(8,i,-1):
                    if board[i][j] == board[k][j]:
                        return False
                for k in range(i+1,9):
                    if k%3 == 0:
                       break
                    for h in range(j//3*3,j//3*3+3):
                        if board[i][j] == board[k][h]:
                            return False
        return True
