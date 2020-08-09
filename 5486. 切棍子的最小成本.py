"""
[5486. 切棍子的最小成本](https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick/)
有一根长度为 n 个单位的木棍，棍上从 0 到 n 标记了若干位置。例如，长度为 6 的棍子可以标记如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809171125919.png#pic_center)


给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。

你可以按顺序完成切割，也可以根据需要更改切割的顺序。

每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。对棍子进行切割将会把一根木棍分成两根较小的木棍
（这两根木棍的长度和就是切割前木棍的长度）。请参阅第一个示例以获得更直观的解释。

返回切棍子的 最小总成本 。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809171145535.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

示例 1：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809171202638.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
输入：n = 7, cuts = [1,3,4,5]
输出：16
解释：按 [1, 3, 4, 5] 的顺序切割的情况如下所示：

第一次切割长度为 7 的棍子，成本为 7 。第二次切割长度为 6 的棍子（即第一次切割得到的第二根棍子），第三次切割为长度 4 的棍子，最后切割长度为 3 的棍子。总成本为 7 + 6 + 4 + 3 = 20 。
而将切割顺序重新排列为 [3, 5, 1, 4] 后，总成本 = 16（如示例图中 7 + 4 + 3 + 2 = 16）。
示例 2：

输入：n = 9, cuts = [5,6,1,4,2]
输出：22
解释：如果按给定的顺序切割，则总成本为 25 。总成本 <= 25 的切割顺序很多，例如，[4，6，5，2，1] 的总成本 = 22，是所有可能方案中成本最小的。
 

提示：

2 <= n <= 10^6
1 <= cuts.length <= min(n - 1, 100)
1 <= cuts[i] <= n - 1
cuts 数组中的所有整数都 互不相同
***
周赛的时候没做出来，日常惭愧。这道题和[戳气球](https://leetcode-cn.com/problems/burst-balloons/)那道题非常想，只是做题的时候没有想出来怎么写。

其实也是一样的思路，和戳气球一样，那个是计算乘法，这个是计算加法。
- 首先对左右两边进行补充，这样我们才能够计算裁剪后左右的值，为了方便我们就再左边加0，右边加n。原来的cuts= [1,3,4,5]；加了过后的数组变为 [0,1,3,4,5,7],首尾是用来计算中间部分的长度会用到。
- 接下来就是限制条件，之前的打气球没有啥限制条件。但是这道题有一个条件就是两个要裁剪的地方，中间如果没有要裁剪的地方，那么这样的两者之间的损耗是0.转换为程序语言就是 dp[i][i+1] = 0.
- 设置一个dp动态转移矩阵，dp[i][j]表示**裁剪点i**与**裁剪点 j**之间的损耗。
- 我们可以得到动态转移方程如下所示：

$$dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+cost(i,j))$$
- 这里的损失就是i, j之间的长度。
- 我们可以推出答案是在dp[0][-1]这个位置。我们的遍历顺序应该是怎么样得了？根据下图的解释，我们应该 i 从下到上，j 从左到右进行遍历![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809172741375.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
代码如下：
"""
```python
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n] 
        m = len(cuts)
        cuts.sort()
        # print(cuts)
        dp = [[float('inf')]*m for _ in range(m)] 

        #相邻切割点不能再分，损耗为0
        for i in range(m):
            for j in range(m):
                if j == i+1:
                    dp[i][j] =  0 

        for i in range(m-1, -1, -1):#i从下到上
            for j in range(i+1, m):# j 从左到右
                if j - i > 1: #只有当i - j 中有裁剪点才进入
                    for k in range(i+1,j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+cuts[j]-cuts[i])#动态转移方程
        # print(dp)
        return dp[0][-1]
```
