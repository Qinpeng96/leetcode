"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      m = len(grid)
      n = len(grid[0])

      for i in range(1,n):#将第一行的值逐次相加
        grid[0][i] += grid[0][i-1] 
      for i in range(1,m):#将第一列的数逐次相加
        grid[i][0] += grid[i-1][0]

      for i in range(1, m):#对内部的格子进行判断，每个格子的值为达到该格子的值
        for j in range(1, n):
            grid[i][j] += min(grid[i][j-1],grid[i-1][j])#从上一个路径中选一个最近的
      return grid[m-1][n-1]
      
if __name__ == "__main__":
  s = Solution()
  print(s.minPathSum(
[[1,2],[1,1]
]))


    
