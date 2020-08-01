"""
[264. 丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/)
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
***
这道题万万没想到=-=，三指针！
我们可以知道下一个丑数肯定是由之前一个丑数乘以2/3/5得到了最小的大于前一个丑数的值。
但是具体是乘以谁？这个就不知道了，所以这道题弄了一个三指针。
- 初始化的时候，三个指针都等于 0 ，即是从dp[0] 开始乘起来的
- 这三个指针每一个对应的乘数都不一样 i2-->2, i3-->3, i5-->5.
- 之后就是由哪一个丑数乘以2/3/5得到的本次丑数，那么那个数的指针坐标就要加一后移
- 例如 dp[0]开始i2, i3,i5都为0，分别乘以2，3，5之后，2最小。这个时候i2坐标后移，等于1， i3=i5=0
- 下一轮开始 dp[1]*2 ;  dp[0]*3;  dp[0]*5; 我们可以得到3是最小值，所以i3后移。
- 这里解释一下为什么本次是ix算出来的丑数，那么ix就需要后移：因为本次算出来的都是一个可以得到合法的最小丑数，如果不后移，那么下一次得到的丑数还有一个和上一次计算出来的丑数一摸一样大的值。


"""

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            min_val = min(dp[i2]*2, dp[i3]*3, dp[i5]*5)#计算最小正确丑数
            dp[i] = min_val

            if dp[i2]*2 == min_val:#丑数是由谁计算得到的，谁的索引就加一
                i2 += 1
            if dp[i3]*3 == min_val:
                i3 += 1
            if dp[i5]*5 == min_val:
                i5 += 1
        return dp[-1]


```
