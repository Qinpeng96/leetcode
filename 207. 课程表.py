"""
[207. 课程表](https://leetcode-cn.com/problems/course-schedule/)
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？


示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
***

#### 判断有向无环图，使用入度法，BFS
算法流程：

- 统计课程安排图中每个节点的入度，生成 入度表 indegrees。
- 借助一个队列 queue，将所有入度为 0 的节点入队。
- 当 queue 非空时，依次将队首节点出队，在课程安排图中删除此节点 pre：并不是真正从邻接表中删除此节点 pre，而是将此节点对应所有邻接节点 cur 的入度 −1，即 indegrees[cur] -= 1。
- 当入度 -1后邻接节点 cur 的入度为 0，说明 cur 所有的前驱节点已经被 “删除”，此时将 cur 入队。在每次 pre 出队时，执行 numCourses--；
- 若整个课程安排图是有向无环图（即可以安排），则所有节点一定都入队并出队过，即完成拓扑排序。换个角度说，若课程安排图中存在环，一定有节点的入度始终不为 0。
- 因此，拓扑排序出队次数等于课程个数，返回 numCourses == 0 判断课程是否可以成功安排。


作者：jyd
链接：https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegrees = [0 for _ in range(numCourses)]#记录每一个节点的入du
        adjacency = [[] for _ in range(numCourses)]#记录每一个节点的相连节点
        queue = collections.deque()

        #获得每一个课程节点的入度以及相连的节点
        for cur, pre in prerequisites:
            indegrees[cur] += 1#计算每一个当前课程的度，每一个前节点就多一个度
            adjacency[pre].append(cur)#创建一个表，pre -> cur
        
        for i in range(len(indegrees)):#对于所有度为0的课程，我们将其在度列中的索引加入队列
            if not indegrees[i]:
                queue.append(i)
        #BFS每次从队列左边弹出度为0的值， 然后使其相邻点得度减一，直到队列为空
        while queue:
            pre = queue.popleft()
            numCourses -= 1#每次减少一个度为0的节点，剩余的课程就少一门
            for cur in adjacency[pre]:#对于每一个0度节点所连接的节点，其度减一
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)#度减一之后如果的节点度为0，那么加入队列
        return not numCourses
```
"""
除此之外作者还提出了**DFS判断是否存在有向无环图**。
- 借助一个标志列表 flags，用于判断每个节点 i （课程）的状态：
	未被 DFS 访问：i == 0；
	已被其他节点启动的 DFS 访问：i == -1；
	已被当前节点启动的 DFS 访问：i == 1。
	
- numCourses 个节点依次执行 DFS，判断每个节点起步 DFS 是否存在环，若存在环直接返回 False。
- DFS 流程：
	 - 终止条件：当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，无需再重复搜索，直接返回 True。
	- 当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 2 次访问，即 课程安排图有环 ，直接返回 False。
	- 将当前访问节点 i 对应 flag[i] 置 1，即标记其被本轮 DFS 访问过；
	- 递归访问当前节点 i 的所有邻接节点 j，当发现环直接返回 False；
	- 当前节点所有邻接节点已被遍历，并没有发现环，则将当前节点 flag 置为 −1 并返回 True。
若整个图 DFS 结束并未发现环，返回 True

作者：jyd
链接：https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
***
"""
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1:return True#如果之前其他起始节点已经访问过
            elif flags[i] == 1:return False#如果本次节点已经访问过
            flags[i] = 1 # 如果该节点从未被访问过，本次访问，设置 1
            for j in adjacency[i]:#对节点i的相连节点进行DFS
                if not dfs(j, adjacency, flags):return False
            #如果与之所有相连的节点都没有发现环，那么本节点设置为 -1,为之后的节点表示，这个节点已经被访问过，没有环出现
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:#创建一个图表，每一个节点之后包含所连的节点
            adjacency[pre].append(cur)
        
        for i in range(numCourses):#对每一个节点进行DFS判断
            if not dfs(i, adjacency, flags): return False
        return True
```
