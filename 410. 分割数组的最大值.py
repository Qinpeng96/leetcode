"""
[410. 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/)
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
***
这道题的题目也没搞很明白，n长度的数组，分为m个组，计算每个组的和，找到当前分法的每个组的和的最大值。在多种分割方法中，选取一种最大值最小的分法，返回分的组数m。
***
实属不会，哎，索性还是偷官方的题解吧。

在下笔之前需要考虑下这些问题，

 1. 假如有m个分割数组，我们应该分割在哪一个位置。
 2. 后面的分割位置与前面的分割位置息息相关，并且要保证分出m个数组。
 3. 在计算一种分割方案的时候，我们怎么才能保证，这个方案的最大子段和是所有m分割方案里面最小的。

题解一使用的是动态规划：
dp[i][j] 表示将数组的前 i 个数分割为 j 段所能得到的最大连续子数组和的最小值。动态规划的参数含义设定也是一门艺术，偷不会。接下来就是动态转移方程：
由于动态规划是一个数一个数来考虑进行分割的，所以当前 i 个数中[0...k...i]是有多少个分成了 j - 1段。然后最后一段是由[k...i]组成的,所以需要枚举k.。之后就是确定最大子段和的最小值问题，我们现在对 dp[i][j]相当于是分成了两端。

之前的一段 [0, k]，其中 k < i, 之后的一段就是[k, i], 在确定前 i 个数能够取到的最小值的时候，dp[k][j-i]表示前 j -1段能够取得最小值。 之后得[k, i]是最后一段，所以最后一段得值就是 sum[k, i]，然后我们对两者进行比较，就能得出 dp[i][j]取得最小值应该是哪个。

$$ dp[i][j] = min\{ max (dp[k][j-1], sum[k,i] ) \};   k∈[0,i-1]$$ 
对于状态 dp[i][j]，由于我们不能分出空的子数组，因此合法的状态必须有 i ≥ j。对于不合法（i<j）的状态，由于我们的目标是求出最小值，因此可以将这些状态全部初始化为一个很大的数。在上述的状态转移方程中，一旦我们尝试从不合法的状态 dp[k][j-1]进行转移，那么 max(⋯) 将会是一个很大的数，就不会对最外层的min{⋯} 产生任何影响。

此外，我们还需要将 dp[0][0] 的值初始化为 0，在上述的状态转移方程中，当 j=1 时，唯一的可能性就是前 i 个数被分成了一段。如果枚举的 k=0，那么就代表着这种情况；如果 k =0，对应的状态 dp[k][0]是一个不合法的状态，无法进行转移。因此我们需要令 dp[0][0] = 0。



作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/split-array-largest-sum/solution/fen-ge-shu-zu-de-zui-da-zhi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。接下来就是具体的代码。
***
"""
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        nums = [0] + nums
        n = len(nums)
        sums = [0]

        for num in nums[1:]:#计算连续的子段和
            sums.append(sums[-1]+num)

        dp = [[float('inf')]*(m+1) for _ in range(n)]#构建一个dp列表
        dp[0][0] = 0
        
        #dp动态转移方程， j的取值范围取分段次数和i的个数中的最小值,因为有可能i的个数小于分段数
        for i in range(1, n):
            for j in range(1, min(i+1, m+1)):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sums[i] - sums[k]))
        return dp[-1][-1]

```
二分查找：
本题中，我们注意到：当我们选定一个值 x，我们可以线性地验证是否存在一种分割方案，满足其最大分割子数组和不超过 x。策略如下：

贪心地模拟分割的过程，从前到后遍历数组，用 sum 表示当前分割子数组的和，cnt 表示已经分割出的子数组的数量（包括当前子数组），那么每当 sum 加上当前值超过了 x，我们就把当前取的值作为新的一段分割子数组的开头，并将 cnt 加 1。遍历结束后验证是否 cnt 不超过 m。

这样我们可以用二分查找来解决。**二分的上界为数组 nums 中所有元素的和，下界为数组 nums 中所有元素的最大值**，通过二分查找，我们可以得到最小的最大分割子数组和，这样就可以得到最终的答案：

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m


        left = max(nums)#下界
        right = sum(nums)#上界
        while left < right:#二分法，在上界和下界之间找一个值
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/split-array-largest-sum/solution/fen-ge-shu-zu-de-zui-da-zhi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
