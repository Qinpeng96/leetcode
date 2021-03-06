"""
[779. 第K个语法符号](https://leetcode-cn.com/problems/k-th-symbol-in-grammar/)
在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。

给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）


例子:

输入: N = 1, K = 1
输出: 0

输入: N = 2, K = 1
输出: 0

输入: N = 2, K = 2
输出: 1

输入: N = 4, K = 5
输出: 1

解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001

注意：

N 的范围 [1, 30].
K 的范围 [1, 2^(N-1)].
***
根据下面的关系式不难发现：
#
	第一行: 0
	第二行: 0 1
	第三行: 0 1 10
	第四行: 0 1 10 1001
每一行的前半部分数和上一行一样，后半部分数与上一行相反。并且行数与每行的个数有如下关系式：
#
	K = 2**(N - 1)
对于每一次的N，K
- K值小于等于上一行的个数，即 K <= 2**(N-2)，那么K的值与上一行中的第K个值是相同的。
- 如果 K 值大于上一行的个数，即 K＞2**(N - 2)，K值位于与上一行K-2**(N-2)的对应位置相反。
- 根据这个递推公式，将本行数据一分为二。我们可以计算出 如果在本行的左边就和上一行的对应位置相等；如果在右边，就和上一行的对应位置相反。
- 其中递归的初始弹出条件  K== 1：return 0； K==2, return 1;
"""

```python
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        #K == 2**(N-1)
        def solve(N, K):
            if K == 1: return 0
            if K == 2: return 1
            if K  > 2**(N-2):#K在上一行右边
                K = K - 2**(N-2)
                N -= 1
                return 0**solve(N, K)
            else:#K在上一行左边
                N -= 1
                return solve(N, K)
        return solve(N, K)
```
