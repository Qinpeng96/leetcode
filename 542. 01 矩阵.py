"""
[542. 01 矩阵](https://leetcode-cn.com/problems/01-matrix/)
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
通过次数36,475提交次数81,411

***
第一种是BFS的方法，但是注意一点，为了访问查找的速度。我们的visited设置的是一个集合，集合的查找时间是O(1)。之前我设置的是列表，结果就超时了。
首先是把所有0的节点加入双向队列和集合，在每次从队列里面左pop一个坐标值,使其上下左右有意义的节点，且节点不在visited内时就在上一个节点的基础上加一。
"""
```python
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        
        row = len(matrix)
        col = len(matrix[0])
        zeroes_pos = [(i, j) for i in range(row) for j in range(col) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        queue = collections.deque(zeroes_pos)
        visited = set(zeroes_pos)

        
        while queue:
            x, y = queue.popleft()
            for xi, yj in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= xi < row and 0 <= yj < col and (xi, yj) not in visited: 
                    matrix[xi][yj] = matrix[x][y]+1
                    queue.append((xi, yj))
                    visited.add((xi, yj))
                                    
        return matrix
```
"""
接下来是一种动态规划的方法：
我开始也是这样从左上到右下， 再反过来从右下到左上。但是我没有注意一个问题，就是边界的问题。
例如从左上到右下的时候，只有左边和上方的节点是计算过的，所以该点的更新只能与这两个点有关。在这两个点中取一个最小。同理， 倒过来计算也是一样的。
"""
```python
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist
```
