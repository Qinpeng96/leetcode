"""
[329. 矩阵中的最长递增路径](https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/)
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
***
"""

纯暴力不加记录表，超时！
```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.maxlen = 0
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        def backtrack(i, j, cnt, pre):
            self.maxlen = max(self.maxlen, cnt)
            if 0 <= i < m and 0 <= j < n and matrix[i][j] > pre :
                backtrack(i+1, j, cnt+1, matrix[i][j])
                backtrack(i-1, j, cnt+1, matrix[i][j]) 
                backtrack(i, j+1, cnt+1, matrix[i][j]) 
                backtrack(i, j-1, cnt+1, matrix[i][j])
            else:
                return 
        for i in range(m):
            for j in range(n):
                backtrack(i+1, j, 1, matrix[i][j])
                backtrack(i-1, j, 1, matrix[i][j])
                backtrack(i, j+1, 1, matrix[i][j])
                backtrack(i, j-1, 1, matrix[i][j]) 
                
        return self.maxlen
```
接下来加上一个记录表格。加记录表意味着我们在dfs函数需要返回当前前数字之后能够达到的最远长度。
而当前数字能够达到的最远长度又与和他相邻的的四个点的最远长度+1有关。这样就可以得到一个递归公式。
```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        out = 1
        memo = {}
        #每次都找比当前值小的数进行递归计数
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            max_len = 0
            for di, dj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= di < m and 0 <= dj < n and matrix[di][dj] < matrix[i][j]:
                    max_len = max(max_len, dfs(di,dj))#从四个方案中找一个最长的
            memo[(i,j)] = max_len + 1#本次的值，比之前的值多一个
            return memo[(i,j)] #返回当前的最大长度

        for i in range(m):
            for j in range(n):
                out = max(out, dfs(i,j))
        return out

        


```
