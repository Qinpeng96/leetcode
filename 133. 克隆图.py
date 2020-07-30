"""
[133. 克隆图](https://leetcode-cn.com/problems/clone-graph/)
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回
***
使用DFS的方法，并且建立一个查找表，防止重复访问。

DFS还是有点麻烦，自己写的时候没写出来。
首先是建立一个clone 节点，其领域neighbor为空，接着就要更具原始节点的领域进行克隆。
这里就是DFS的关键：
#
            for item in node.neighbors:		#对于头节点的每一个相邻节点，加入到克隆的头的邻居中
                clone.neighbors.append(dfs(item))	#邻居中加入的是每一个邻接点的克隆，在使用一次DFS
    
每次在克隆点的接的邻域是 原始节点邻域点的DFS。这里有点绕，接下来仔细分析一下：

 1. 假如只有一个节点 ，邻域为空，那么函数最后返回clone, 成立。
 2. 假如头节点有邻域，我们在clone后接邻域的时候，要把这些邻域都接上，再对接上的这些邻域复制头节点和邻域。
 3. 所以这里接邻域的时候是接的邻域的DFS,层层下移，对每个邻接点又进行克隆，复制邻接。

主要的思想：再写的时候我们需要注意把 dfs()看作已经复制克隆好了的邻域，这样想的话会方便易懂许多。
""""


```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def dfs(node):
            if not node:
                return 
            if node  in visited:
                return visited[node]
            clone = Node(node.val, [])#建立一个头clone
            visited[node] = clone #将克隆的头加入已经访问过的表，防止重复访问。
            for item in node.neighbors:#对于头节点的每一个相邻节点，加入到克隆的头的邻居中
                clone.neighbors.append(dfs(item))#邻居中加入的是每一个邻接点的克隆，在使用一次DFS
            return clone#返回的是克隆的头节点
        return dfs(node)   
```
还有一种BFS的写法：

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        lookup = {}

        def bfs(node):
            if not node: return
            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.appendleft(node)
            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone

        return bfs(node)

作者：powcai
链接：https://leetcode-cn.com/problems/clone-graph/solution/dfs-he-bfs-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
