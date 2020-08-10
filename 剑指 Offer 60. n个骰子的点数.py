"""
[剑指 Offer 60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 

限制：

1 <= n <= 11
***
我的思路是这样：
比如只有1234，三个面
一个骰子概率[1/4, 1/4, 1/4, 1/4，即每一个数的频次为[1, 1, 1, 1]
两个骰子的频次为[1,2,3,4,3,2,1 ],计算的方法如下：
#
		[1, 1, 1, 1]
	+      [1, 1, 1, 1]
	+         [1, 1, 1, 1]
	+            [1, 1, 1, 1]
	=   [1, 2, 3, 4, 3, 2, 1]
长度为多少就移位加多少次。得到[1,2,3,4,3,2,1 ]之后，再对它移位相加四次就是三个骰子的频次值。

以此类推，一个骰子六个面也是一样的计算方法，只不过初始的时候是[1,1,1,1,1,1],移位累计是6次。
"""
```python
class Solution:
    def twoSum(self, n: int) -> List[float]:
        # length = n*5 + 1
        zero = [0] * 5
        num = [1] * 6
        out = [1] * 6

        def count(out, num, length):#计算两个数的循环移位相加
            for _ in range(5):
                num.insert(0,num.pop())
                for i in range(length):
                    out[i] += num[i]
            return out

        for i in range(1, n):#对骰子的个数进行循环
            num.extend(zero)
            out.extend(zero)
            num = count(out, num, (i+1)*5+1)[:]
            # print(num)

        allsum = sum(out)
        for i in range(n*5+1):#计算概率
            out[i] = out[i] / allsum
        return out

```
"""
还有一种大佬们的动态规划求解方法;
n个骰子，一共有6**n种情况
#
	n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
	n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)

可以看作是从前(n-1)个骰子投完之后的状态转移过来。
其中F（N,S）表示投第N个骰子时，点数和为S的次数
"""
```python
class Solution:
    def twoSum(self, n: int) -> List[float]:

        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1

        for i in range(2,n+1):#骰子的个数，也就是dp矩阵的行数
            for j in range(i,i*6+1):#计算每一行的数据。两个骰子就是2-13， 三个骰子:3-18,左闭右开
                for k in range(1,7):#这里是对上一层的状态进行累加，如果上一层的列序号比当前的小，那么前6个值累加就是本层的值
                    if j >= k+1:
                        dp[i][j] +=dp[i-1][j-k]
        res = []
        for i in range(n,n*6+1):#计算特定层的概率
            res.append(dp[n][i]*1.0/6**n)
        return res

#####动态规划

作者：up2m
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/rong-yi-li-jie-de-pythondong-tai-gui-hua-fang-fa-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
