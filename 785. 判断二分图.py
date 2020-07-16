"""
785. 判断二分图
给定一个无向图graph，当这个图为二分图时返回true。

如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。


示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释: 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释: 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:

graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。

"""
from typing import List
##深度优先搜索，每一次都染色一个之后斗鱼其相接的点进行染色判断
#先找到一个没被染色的节点u，把它染上一种颜色，之后遍历所有与它相连的节点v，如果节点v已被染色并且颜色和节点u一样，
#那么就不是二分图。如果这个节点v没有被染色，先把它染成与节点u不同颜色的颜色，
# 然后遍历所有与节点v相连的节点...如此递归下去。
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)#计算有多少个点
        UNCOLORED, RED, BLUE = 0, 1, 2#设置三种颜色
        record = [UNCOLORED] * (n)#为这些点建立一个列表，记录他们的颜色
        valid = True#初始化默认是可分的

        #用于检验当前染色是否符合要求
        def dfs(i, color):
            nonlocal valid
            record[i] = color#将当前点进行染色
            dif_color = BLUE if color == RED else RED#取一个相反的颜色
            for j in range(len(graph[i])):#对本次染色点的邻接点进行染色判断
                if record[graph[i][j]] == UNCOLORED:#紧邻点如果无色，进行染相反色，然后再次递归
                    dfs(graph[i][j],dif_color)
                    if valid == False:##这里很重要，递归之后对valid进行判断，如果为False,放弃递归，直接返回
                        return#所以每当递归的过程中出现了一个False之后，就会从这里，一步一步往上跳出程序
                elif record[graph[i][j]] == dif_color:#邻接点已经染了相反颜色，继续下一个邻接点判断
                    continue
                else:#如果邻接点染的相同颜色，valid 赋值 False,返回本次递归
                    valid = False
                    return 

        for i in range(n):#对n个点进行循环判断
            if record[i] == UNCOLORED:#如果没有被染色，那么将其然染色后进行判断
                dfs(i, RED)#深度优先判断，如果不可分，则会将valid赋值为False
                if valid == False:#只要返回一个False,那么程序结束
                    break
        return valid

###########  DFS简洁写法
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = [0] * len(graph)

        def dfs(pos, color):
            vis[pos] = color
            for i in graph[pos]:
                # 颜色相同 or （未访问 且 继续深搜为False）
                # 可直接返回False
                if vis[i] == color or not (vis[i] or dfs(i, -color)):
                    return False
            return True

        # 不一定为联通图，需遍历每一个节点
        for i in range(len(graph)):
            if not vis[i] and not dfs(i, 1):
                return False
        return True


# 作者：GiaoGiaoWo
# 链接：https://leetcode-cn.com/problems/is-graph-bipartite/solution/python3-dfs-ji-jian-dai-ma-shi-jian-88kong-jian-10/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
###########

#**********      本题还可以使用BFS来做      *************#
#BFS 的核心就是队列，首先进入for 循环，加一个节点进来，染色。寻找与其相接的点是否染色，如果染色一样，
#返回False。颜色不一样，继续看其他相邻点。遇到没有染色的节点，此时染不同色，同时加入列表中，因为染色后就要找它相邻节点
#
#1.for 循环， 看当前节点是否已经染色，如果染色就看下一节点，否则就默认染成红色（大多数的节点在while queue中就已经被染色）
#2.for循环，对当前已经才染色过，并且加入队列的点，列表循环，每次从列表弹出一个节点，看和其相邻的节点是否染色，
#      如果已经染色并且颜色相同，直接返回False;
#      如果染色，但是颜色不同，什么也不做，看其他相邻点
#      如果还未染色，这次染成不一样的颜色，加入队列，看是否可分
#3.循环结束都没有False,那么说明可分，返回True
#
#注意：这里没有用双向队列，因为可以不考虑顺序，每个节点的相邻节点都会被判断，不用考虑顺序

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        record = [0] * n
        UNCOLORED, RED, BLUE = 0, 1, -1#设置三种颜色

        for i in range(n):
            if record[i] != UNCOLORED:
                continue

            record[i] = RED#如果没有填色，则默认填红色
            queue = [i]#将染色后的序号加入列表
            while queue:
                node = queue.pop()#弹出当前已染色的节点索引
                for block in graph[node]:#和已染色的点相邻的快
                    if record[block] == UNCOLORED:#m没有染色，染成不同的颜色
                        record[block] = BLUE if record[node] == RED else RED
                        queue.append(block)
                    elif record[block] == record[node]:#如果颜色相同，返回False
                        return False
        return True
            

#******************************************************#
if __name__ == "__main__":
    s = Solution()
    graph = [[1,3], [0,2], [1,3], [0,2]]
    # graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    print(s.isBipartite(graph))
