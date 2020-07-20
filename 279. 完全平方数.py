"""
[279. 完全平方数](https://leetcode-cn.com/problems/perfect-squares/)
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
***
首先想到的是使用动态规划的方法，dp[ i ]就表示数字 i 所需要的最小组合个数。

 1. 初始化dp列表，在平方和索引的位置置为1，为了方便计算，就多设置了0索引，其实没用。
 2. 从左向右依次计算所需最小组合个数，这里对每一个数要开一下平方，因为要想使得值最小，就需要和之前得平方数位置之间建立关系式。就是 min( dp[ i ], dp[ i - j * j ] + dp[ j * j ] )。当前数的最小组合数等于之前的平方组合数和两者之间的差值构成。
 3. 最后就是一步一步迭代，计算得到最后的一位就是输出答案。
```python
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        sqrt_n = int(sqrt(n))#dp中平方和数的个数是根据输入n开方求出来的
        for i in range(1, sqrt_n+1):#初始化dp列表，平方和位置置为1，所需数字为1
            dp[i*i] = 1
            
        for i in range(2, n+1):#从左向右依次计算所需最小组合个数
            sqrt_i = int(sqrt(i))
            for j in range(1, sqrt_i+1):
                dp[i] = min(dp[i], dp[i-j*j] + dp[j*j])
        return dp[-1]                                
"""
还有一种BFS方法：
因为是广度优先遍历，顺序遍历每一行，所以当节点差出现0时，此时一定是最短的路径。
如绿色所示，若此时节点为0，表示根节点可以由路径上的平方数{1,1,9}构成，返回此时的路径长度3，后续不在执行。
如红色所示，若节点值在之前已经出现，则不需要再计算，一定不会是最短路径，最短路径还未出现。

借助队列实现广度优先遍历（层次遍历）

初始化队列queue=[n]，访问元组visited={}，初试化路径长度step=0

特判，若n==0，返回0。

循环条件，队列不为空：

step+=1，因为循环一次，意味着一层中的节点已经遍历完，所以路径长度需要加一。
定义当前层中的节点数l=len(queue)，遍历当前层的所有节点：
令tmptmp为队首元素。
遍历所有可能数ii的平方数，遍历区间[1,int( sqrt(tmp)+1))：
定义x=tmp-i^{2}
 
若x==0，返回当前的路径长度。
若x not in visited，表示当前节点未出现过：将该节点入队并在访问数组中加入。返回step
```python
"""
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        if n == 0: return 0
        queue = deque([n])
        step = 0
        visited = set()
        while(queue):
            step+=1
            l=len(queue)
            for _ in range(l):
                tmp=queue.pop()
                for i in range(1,int(tmp**0.5)+1):
                    x=tmp-i**2
                    if(x==0):#刚好满足，返回步数
                        return step
                    if(x not in visited):#如果之前已经计算过，现在不用加入列表，肯定不行
                        queue.appendleft(x)
                        visited.add(x)
        return step
"""
作者：wu_yan_zu
链接：https://leetcode-cn.com/problems/perfect-squares/solution/dong-tai-gui-hua-bfs-zhu-xing-jie-shi-python3-by-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
