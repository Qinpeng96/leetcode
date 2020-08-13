"""
[399. 除法求值](https://leetcode-cn.com/problems/evaluate-division/)
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。
***
- 首先是建立一个连接图和一个权重的字典
- 进行DFS, 同时还要建立一个集合，防止DFS陷入循环。
- 每次从当前点找到其对应的一系列连接点进行递归查找，当函数的返回值不为0的时候，说明已经找到了对应的点，计算出其权重。这个时候加入到权重字典，在break，跳出循环


"""


***
下面是powcai大佬的题解代码

```python3
# DFS
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        #建立连接关系图定义
        graph = defaultdict(set)  #这里使用集合，因为不会有重复的元数
        weights = defaultdict()     #权重的对应集合关系
        lookup = {}                 #查找表，防止DFS陷入循环

        #建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weights[(equ[0], equ[1])] = values[idx]
            weights[(equ[1], equ[0])] = 1.0/values[idx]
        #DFS
        def dfs(start, end, visited):
            #当图中有这个关系连接的时候，直接返回
            if (start, end) in weights:
                return weights[(start, end)]
            #当起点或者终点不在图内的时候，返回0
            if start not in graph or end not in graph:
                return 0
            #已经访问过的点不能继续访问，陷入循环
            if start in visited:
                return 0
            #两个点都在图内，且起始点（递归过后的每一个点）此时没被访问过
            visited.add(start)
            res = 0
            for tmp in graph[start]:
                res = dfs(tmp, end, visited) * weights[(start, tmp)]
                #如果某一条边的权重不为0，那么加入到权重列表，方便下次查找
                if res != 0:
                    weights[(start, end)] = res
                    break
            visited.remove(start)
            return res
        
        #开始计算
        res = []
        for que in queries:
            tmp = dfs(que[0], que[1], set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res
        
# BFS
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict, deque
        graph = defaultdict(set)
        weight = defaultdict()
        lookup = {}
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])
        res = []
        for start, end in queries:
            if (start, end) in weight:
                res.append(weight[(start, end)])
                continue
            if start not in graph or end not in graph:
                res.append(-1)
                continue
            if start == end:
                res.append(1.0)
                continue
            stack = deque()
            # 将从start点可以到达下一个节点压入栈内
            for tmp in graph[start]:
                stack.appendleft((tmp, weight[(start, tmp)]))
            # 记录访问节点
            visited = {start}
            # 为了跳出双循环
            flag = False
            while stack:
                c, w = stack.pop()
                if c == end:
                    flag = True
                    res.append(w)
                    break
                visited.add(c)
                for n in graph[c]:
                    if n not in visited:
                        weight[(start, n)] = w * weight[(c, n)]
                        stack.appendleft((n, w * weight[(c, n)]))
            if flag:
                continue
            res.append(-1.0)
        return res
```