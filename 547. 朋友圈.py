"""
[547. 朋友圈](https://leetcode-cn.com/problems/friend-circles/)
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2 
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:

输入: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
注意：

N 在[1,200]的范围内。
对于所有学生，有M[i][i] = 1。
如果有M[i][j] = 1，则有M[j][i] = 1。
***

首先是DFS的方法：
- 每次以i作为关系的开始段，如果i没被使用过，就将其加入used。DFS查找与其有关系的点。
- DFS函数输入关系的起始点，对这个关系的起始点的所有没被使用过的接受点，且两者是有关系的。这样就就关系点加入used,表示已经是一个圈子里面的。
- DFS内的循环就是找到以这个点作为起始点的所有关系接受点，再以这些接受点作为起始点，找有关系的点，加入used.
- 直到以 i 开头的关系点找不到了，就换 i+1,继续找。
"""
```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        used = set()
        num = 0

        def dfs(i):#每次寻找与起始点i有关系且没被使用过的点
            for j in range(n):
                if M[i][j] == 1 and j not in used:
                    used.add(j)
                    dfs(j)

        for i in range(n):#每次以i作为其实的关系，如果i不在，则数量加一
            if i not in used:
                num += 1
                used.add(i)
                dfs(i)
        return num
```
"""
但是这道题主要是想考一个知识点：**并查集**。具体的实现可以看[这篇文章](https://www.cnblogs.com/yscl/p/10185293.html).
并查集主要有三个函数：
- 查找函数：查找该点的最上层的父节点是谁
- 连接函数：将两个节点联通起来，这样以来，两个区域内的点都会被联通。
- 判断是否联通：两个节点分别找到自己的根节点，看是否相等
下面是东哥画的一张图[东哥的文章](https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/unionfind-suan-fa-xiang-jie)，帮助理解.
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200805232816162.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
并查集有几个细节的地方：
- 找祖先的函数find，由于我们保存方式类似树一样,所以祖先的时候需要递归，直到找到祖先
- 在联通两个节点的时候，我们需要首先找两个节点的祖先是否相同，如果相同，直接返回。如果不同：
- 当左节点的祖先的长度小，就把右祖先加到左祖先来。并且修该右祖先指向左祖先。
- 最后由于连通了两个群，所以集合的个数减一。
"""
```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        f = {}
        s = {}
        count = len(M)

        def find(x):
            f.setdefault(x, x)
            # 路径压缩
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            nonlocal count
            x_father, y_father = find(x), find(y)
            if x_father == y_father: return
            # 将小树的根节点连接到大叔的根节点
            if s.setdefault(x_father, 1) < s.setdefault(y_father, 1):
                f[x_father] = y_father
                s[y_father] += s[x_father]
            else:
                f[y_father] = x_father
                s[x_father] += s[y_father]
            count -= 1

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return count

作者：powcai
链接：https://leetcode-cn.com/problems/friend-circles/solution/dfs-bing-cha-ji-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        return self.findCircleNum(M)
    
    def init_tree(self, total_node):
        """
        初始化所有节点树
        """
        self.tree_num = total_node  #连通集的个数
        self.tree_node = [1]*total_node #根节点所在树的节点总数，被合并的停止更新,初始为1
        self.parent = [i for i in range(total_node)]#初始化的时候每一个的父节点就是自己

    def find(self, node):
        """
        查找根节点
        """
        while self.parent[node] != node:#未达到根节点的时候
            self.parent[node] == self.parent[self.parent[node]]#树的压缩，最高为3
            node = self.parent[node]
        return node
    
    def union(self, p, q):
        #首先找到两者的祖先
        p = self.find(p)
        q = self.find(q)
        if p == q:#两个点的祖先相同
            return 
        #如果祖先不同，则可以连接，但是小树去连接大树的根
        if self.tree_node[p] > self.tree_node[q]:#p是大树，q是小树
            self.parent[q] = p#小树连到大树
            self.tree_node[p] += self.tree_node[q]#大树被连接后，更新其节点个数
        else:
            self.parent[p] = q#这里pq节点数相同，或者q为大树
            self.tree_node[q] += self.tree_node[p]
        self.tree_num -= 1#合并一次过后就减少一个圈子
    
    def findCircleNum(self, M):#寻找连通集的个数
        n = len(M)
        self.init_tree(n)
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.union(i,j)
        return self.tree_num


```
