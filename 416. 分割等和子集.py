"""
[416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
***
这是典型的01背包问题的变形。因为这里是一个满足一个固定的背包值。
设定dp[i][j]表示背包内的个数i, 背包当前的容量是j，是否恰好满足。
其动态转移方程分析如下：
- 当前背包值是大于待加入的物体的体积的，所以可以选择加入或者不加入,从两个值中选择为True的那一个
- $$dp[i][j] = dp[i-1][j] \ \  or \ \ dp[i-1][j-nums[i]] $$
- 当nums[i] == j的时候，刚好放下该物品，赋值 $dp[i][j] = True$
- 当nums[i] ＞ｊ的时候，此时放不下，只能选择不放，承接上一个状态的，$dp[i][j] = dp[i-1][j]$
下面是威威大佬的图：
题解链接：
[https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/](https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200813183743162.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

"""
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        allsum = sum(nums)
        if allsum & 1: return False
        n = len(nums)
        if n <= 1:return False
        target = allsum // 2
        #动态规划，取到i的时候背包的价值和为j; 
        #dp[i][j] = dp[i-1][j]不取第i个
        #dp[i][j+s[i]] = dp[i-1][j]取第i个

        dp = [[False]*(target) for _ in range(n)]
        #初始化dp数组,将第一个元数放入容量为nums[0]的背包，j背包容量为j+1
        dp[0][nums[0]-1] = True

        for i in range(1,n):#从第二个物品开始放
            for j in range(target):
                if nums[i] < j+1:#第j个背包的容量是j+1
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]#当前状态可以取， 可以不取，选择为True的那一个
                elif j == nums[i]:
                    dp[i][j] =  True
                else:#如果待加入的值大于背包容量，只能不装入
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]


```
