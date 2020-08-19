"""
[546. 移除盒子](https://leetcode-cn.com/problems/remove-boxes/)
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
当你将所有盒子都去掉之后，求你能获得的最大积分和。

 

示例：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----> [1, 3, 3, 3, 1] (1*1=1 分) 
----> [1, 1] (3*3=9 分) 
----> [] (2*2=4 分)
 

提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
***

我们可以换一种思路，用 f(l, r, k) 表示移除区间 [l, r] 加上该区间右边等于 a_r的 k个元素组成的这个序列的最大积分。例如序列 \{ 6, 3, 6, 5, 6, 7, 6, 6, 8, 6 \}，l = 1（下标从 1 开始），r = 5，那么 f(l, r, 3) 对应的元素就是 $\{ {\color{red}[6, 3, 6, 5, 6]}, 7, {\color{red}6}, {\color{red}6}, 8, {\color{red}6} \}$ 中标记为红色的部分。f(l, r, k) 的定义是移除这个红色的序列获得的最大积分。请注意此时我们约定 7 和 8 已经先被移除，所以在这个状态下我们可以认为最后四个 6 是连续的，也就是说实际上序列是这样的：$\{ [6, 3, 6, 5, 6], 6, 6, 6 \}$，此时我们可以有这样一些策略来移除盒子：

$\{\color{orange}{[6,3,6,5,} \color{red}{6],6,6,6}\}$，删除后面的四个 6，再删除前面的这个区间，这样获得的分数为 $f(1, 4, 0) + 4^2$
$\{ {\color{orange}[6, 3}, {\color{red}6]}, [5], {\color{red} 6, 6, 6, 6} \}$，删除一个 5，然后后面的 5 个 6 一起删除，再删除前面的橘黄色区间，这样获得的分数是 $f(1, 2, 5) + f(4, 4, 0)$
$\{ {\color{orange}[ }{\color{red}6]},[3, 6, 5], {\color{red} 6, 6, 6, 6} \}$ 删除 3、6、5 之后再删除 5 个 6，这样获得的分数是 $f(1, 1, 5) + f(2, 4, 0)$
***
动态转移方程：

这个就是我们转移的时候使用的策略，我们可以推导出这样的动态规划转移方程：

$$\color{black} f(l, r, k) = \max 
\begin{cases}
f(l, r - 1, 0) + (k + 1)^2 \\
\max_{i = l}^{r - 1} \{ [f(l, i, k + 1) + f(i + 1, r - 1, 0)] \times { \color{red} \epsilon 
(a_i == a_r)} \} \}
\end{cases}
$$
当ai == ar的时候取1，否则取0
"""
***
下面是代码：

```python
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0]*n for i_ in range(n)]for _ in range(n)]
        result = self.dfs(boxes, dp, 0, n-1, 0)
        return result

    def dfs(self, boxes, dp, l, r, k):
        if l>r:return 0
        if dp[l][r][k] !=0:return dp[l][r][k]#相当于是备忘录，有值就直接返回
        while r>l and boxes[r-1]==boxes[r]:#如果有和末尾r相同的元素，计数器加一，右边界左移
            r -= 1
            k += 1
        dp[l][r][k] = self.dfs(boxes, dp, l, r-1, 0)+(k+1)**2#先计算下当前的状态
        for i in range(l, r):#在循环遍历内部的状态，把当前的状态和内部状态去一个最大值，自顶向下求解
            if boxes[i]==boxes[r]:
                dp[l][r][k] = max(dp[l][r][k], self.dfs(boxes, dp, l, i, k+1)+self.dfs(boxes, dp, i+1, r-1, 0))
        return dp[l][r][k]            
```
