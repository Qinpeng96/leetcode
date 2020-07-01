"""
面试题 08.12. 八皇后
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，
也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。
注意：本题相对原题做了扩展

示例:

 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
#逐个判断当前值是否合法，速度较慢
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
      out = []
      board = [["."]*n for _ in range(n)]

      def is_vaild(board,row,col, n):
        for i in range(1,min(row,col)+1):#判断左对角线
          if board[row-i][col-i] == 'Q':
            return False

        for i in  range(1,min(row+1, n-col)):#判断右对角线
          if board[row-i][col+i] == 'Q':
            return False

        for j in range(row):#判断之前列
          if board[j][col] == 'Q':
            return False

        return True

      def backtrack(board, row: int):
        if row == n:
          res = []
          for j in board:#对每一个合法的棋盘每行进行合并
            res.append(''.join(j))
          out.append(res)
          return 
        
        for col in range(n):
          if not is_vaild(board,row,col,n):
            continue
          board[row][col] = 'Q'#合法就赋值为Q，下一步进行回溯
          backtrack(board, row+1)
          board[row][col] = '.'#删除上一步的赋值Q
        
      backtrack(board, 0)
      return out

#本方法是构建了三个列表用于存放放过Q的坐标值，分别为列，左对角线，右对角线，回溯过程中增加行数
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
      out = []
      board = [["."]*n for _ in range(n)]
      def backtrack(board, row: int,left_diagonal,right_diagonal,column):
        if row == n:
          res = []
          for j in board:
            res.append(''.join(j))
          out.append(res)
          return 
        
        for col in range(n):
          if col in column or (row - col) in left_diagonal or (row + col) in right_diagonal:
            continue
          board[row][col] = 'Q'
          backtrack(board, row+1,left_diagonal + [row-col],right_diagonal + [row+col],column  + [col])
          board[row][col] = '.'
        
      backtrack(board, 0,[],[],[])
      return out
#此方法和上一种差不多，但是回溯过程中只有三个列表，行数时根据列column中的数值进行确定当前行数值的
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
      out = []
      board = [["."]*n for _ in range(n)]
      def backtrack(left_diagonal,right_diagonal,column):
        row = len(column)
        if row == n:
          res = []
          for j in board:
            res.append(''.join(j))
          out.append(res)
          return 
        
        for col in range(n):
          if col in column or (row - col) in left_diagonal or (row + col) in right_diagonal:
            continue
          board[row][col] = 'Q'
          backtrack(left_diagonal + [row-col],right_diagonal + [row+col],column  + [col])
          board[row][col] = '.'
        
      backtrack([],[],[])
      return out
if __name__ == "__main__":
  s = Solution()
  print(s.solveNQueens(8))
