"""
[338. 比特位计数](https://leetcode-cn.com/problems/counting-bits/)
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
***
我们可以发现一下规律：
#
	0：0
	1：1
	----
	2：1    发现 dp[2] = dp[0]+1   base = 2
	3：2    发现 dp[3] = dp[1]+1   base = 2
	-------
	4：1    发现 dp[4] = dp[0]+1   base = 4
	5：2    发现 dp[5] = dp[1]+1   base = 4
	6：2    发现 dp[6] = dp[2]+1   base = 4
	7：3    发现 dp[7] = dp[3]+1   base = 4
	-------------------
	8：1    发现 dp[8] = dp[0]+1   base = 8
	9：2    发现 dp[9] = dp[1]+1   base = 8

根据上述的规律不难找出动态转移方程

"""
```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:return [0] 
        if num == 1:return [0,1]
        dp =[0]*(num+1)
        dp[1] = 1
        base = 2
        for i in range(2, num+1):
            if i // base == 2:#如果刚好是base的两倍
                base *= 2#base倍增
            dp[i] = dp[i-base]+1
        return dp
                       
```
