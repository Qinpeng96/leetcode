"""
130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，
或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:return []
        m, n = len(board), len(board[0])
        queue = collections.deque()
        
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O': queue.append([i, j])
        
        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == 'O': queue.append([i ,j])
        
        while queue:#对每一个边缘位置的四周进行判断，是否为“O”,然后将其周围的四个点加入队列
            row, col  = queue.popleft()
            if 0<=row<m and 0<=col<n and board[row][col] == 'O':
                board[row][col] = '*'
                queue.append([row+1, col])
                queue.append([row-1, col])
                queue.append([row, col+1])
                queue.append([row, col-1])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'





