"""
[221. 最大正方形](https://leetcode-cn.com/problems/maximal-square/)
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
***
DP方程：
$$ dp[i][j] = dp[i-1][j-1]+2*sqrt(dp[i-1][j-1])+1, 左；上；对角三者相等，且不为0$$
$$  minlen = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) ; $$
$$ dp[i][j] = minlen +2*sqrt(minlen )+1, 左；上；对角三者不相等，且不为0$$

这道题目使用动态规划来做。只有当左，上，对角，当前值都不为0的时候才更新当前的面积值。
- 第一种更新方式：三个数值都一样，当前值等于 n + 2*sqrt(n)+ 1
- 左，上，对角，三个值不一样，说明不能取到一个大的正方形，有残缺。只能按照最小的值来计算，也是上述的公式。
-注意：当行列都为1的时候，直接返回当前行列的最大值即可。 
"""
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n) for _ in range(m)]

        maxarea = 0
        for i in range(m):#矩阵赋值，str -> int
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                maxarea = max(maxarea, dp[i][j])
                
        if n == 1 or m == 1: return maxarea#只有一行或者一列的特殊情况

        #从左到右，从上到下，动态规划
        for i in range(1,m):
            for j in range(1, n):
                if dp[i-1][j-1] and dp[i-1][j] and dp[i][j-1] and dp[i][j]:#如果四个位置都不为0
                    if dp[i-1][j-1] == dp[i-1][j] == dp[i][j-1]:#如果左，上，对角；三个元数相同，计算当前的面积
                        dp[i][j] = dp[i-1][j-1] + 2*sqrt(dp[i-1][j-1]) + 1
                    else:#如果三个格子的数值不完全一样，取最小的计算面积
                        minlen = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                        dp[i][j] = minlen + 2*sqrt(minlen) + 1
                    maxarea = max(maxarea, dp[i][j])#取当前矩阵的最大面积
        # print(dp)
        return int(maxarea)

```
大佬是通过计算正方形边长来计算的：

```python
class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        res = 0  # 记录结果
        # 定义dp数组，每个元素代表当前位置可以达到的最大的正方形的边长
        # 长宽都多补了一行是为了更方便处理边界上的点也防止越界发生
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        # 从 dp 的 [1,1] 位置开始遍历
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # 下面需要将坐标映射回 matrix 中，注意 dp 数组和 matrix 元素对应关系
                if matrix[i - 1][j - 1] == '1':# 只有 1 才有可能构成正方形
                    if dp[i - 1][j - 1] and dp[i - 1][j] and dp[i][j - 1]:
                        # 如果当前点的左、上、左上都为 1， 才有机会构成更大的正方形
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    else:
                        # 否则说明当前点的左、上、左上不全为1，也就是有0
                        # 那么当前节点构成的最大正方形就是自身构成的边长为 1 的正方形
                        dp[i][j] = 1
                    res = max(res, dp[i][j])
        return pow(res, 2)

作者：LotusPanda
链接：https://leetcode-cn.com/problems/maximal-square/solution/xiong-mao-shua-ti-python3-dong-tai-gui-hua-dpshu-z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
