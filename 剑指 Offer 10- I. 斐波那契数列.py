"""
[剑指 Offer 10- I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
 

提示：

0 <= n <= 100
***


这是我加了字典记录的方法，减少递归。
"""
```python
class Solution:
    def fib(self, n: int) -> int:
        dic = {}

        def solve(n):
            if n == 0: return 0
            if n == 1: return 1

            if n-1 in dic:
                f1 = dic[n-1]
            else:
                f1 = solve(n-1)
                dic[n-1] =f1

            if n-2 in dic:
                f2 = dic[n-2]
            else:
                f2 = solve(n-2)
                dic[n-2] = f2

            return f1 + f2

        return solve(n) % 1000000007
```

这是大佬的方法：
```python
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

作者：jyd
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/mian-shi-ti-10-i-fei-bo-na-qi-shu-lie-dong-tai-gui/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
