#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#200. 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

 

# 示例 1:

# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
# 示例 2:

# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append([i, j])
                    while queue:
                        row, col = queue.popleft()
                        if 0<=row<m and 0<=col<n and grid[row][col] == '1':
                            grid[row][col] = "*"#搜索过的岛屿
                            queue.append([row+1, col])
                            queue.append([row-1, col])
                            queue.append([row, col+1])
                            queue.append([row, col-1])
                    cnt += 1
        return cnt
# @lc code=end

