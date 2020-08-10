"""
[994. 腐烂的橘子](https://leetcode-cn.com/problems/rotting-oranges/)
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例 1：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200810002807537.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)



输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 

提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2
***

思路就是BFS,但是限制条件需要特别注意一下：
- 初始的时候，全部都是新鲜的，返回   -1
- 初始的时候，全部都是坏， 或者没有新鲜的，也没有坏的，返回 0
- 最后BFS之后还有新鲜的，返回-1
- 否则，返回计算的过程数，注意要减一，因为最后一轮坏的需要在BFS弹出一遍。
"""
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        Fresh = 0

        for i in range(m):#将腐烂的加入队列，并且看是否还有1
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    Fresh = 1#存在新鲜的

        #全是新鲜的 -1， 没有新鲜的也没有坏的0， 只有坏的 0
        if not Fresh: return 0
        elif Fresh and not queue: return -1
        cnt = 0
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x,y in [(i,j+1), (i,j-1), (i-1,j), (i+1,j)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        # print(x,y,cnt)
                        grid[x][y] = 2
                        queue.append((x,y))
        
        #最后看下是否还有新鲜的
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:return -1


        return cnt-1

```
