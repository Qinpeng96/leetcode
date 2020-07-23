"""
[69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
***
这里有舍去小数，所以选择使用左闭右开区间，最后结果减一，即为左边界。
"""
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return x
        left, right = 1, x
        while left < right :#左闭右开
            mid = (left + right) // 2
            m = mid * mid
            if m == x: return mid
            if m > x: right = mid
            else: left = mid + 1
        return left - 1     
```
