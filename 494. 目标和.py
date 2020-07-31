"""
[343. 整数拆分](https://leetcode-cn.com/problems/integer-break/)
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
***
我的思路就是先找下规律：
#
	5:		2x3=6
	6:		3x3=9
	7:		3x4=12
	8:		2x3x3=18
	9:		3x3x3=27
	10:		3x3x4=36
	
大致的规律就是，需要把一个平均分为堆数和堆里面的个数最相近的那种情况。
这就需要使用除法，每次除以一个数，得到商和余数。例如 
#
	8 // 2 = 4
	8 // 3 = 2 ~2
	8 // 4 = 2 
分析之后，我发现，只需要除数在2到 n // 2这个范围内就可以了。

得到商和余数之后，我们的目的是凑出最大的值。所以余数需要加载在商上面，根据平均性的原则，我们每一个商加一，平均分配，因为余数是肯定小于商的个数的， 除数就是商的个数。
例如 
8 // 3 = 2~2 ： 表示商为2,有3个，余数为2。此时需要将余数尽可能平均加在商上面，最终的商就是2；3；3；如果是余数为0的情况，就直接相乘就可以了。

"""
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        out = 0
        temp = 1
        for i in range(2, n//2+2):
            res = n % i
            num = n // inengg
            if res == 0:#余数为0，直接相乘
                out = max(out, num**i)
            else:#余数不为0，要把余数平分在商上面
                temp = num**(i-res)#有i-res个商不会得到余数的分配,先相乘
                for _ in range(res):#能够得到余数的商，进行相乘
                    temp *= (num+1)
            out = max(out, temp)
        return out
```
经过上面的分析，最终得到一个简化的版本：

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        out = 0
        for i in range(2, n//2+2):
            res = n % i
            num = n // i
            out = max(out, num**(i-res) * (num+1)**res)
        return out
```
方法二：动态规划的方法
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200730093307193.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
***

