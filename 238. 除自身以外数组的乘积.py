"""
[238. 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self/)
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。


示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间
***
由于不能使用除法，那么为什么我们不计算一遍左乘，再计算一遍右乘，再把两者的乘积相乘就等于当前的结果了。
例如：[2,3,4,5,6]
#
		左乘					右乘
	[1, 2, 1, 1, 1] 	[1, 1, 1, 6, 1]
	[1, 2, 6, 1, 1] 	[1, 1, 30, 6, 1]
	[1, 2, 6, 24, 1] 	[1, 120, 30, 6, 1]
	[1, 2, 6, 24, 120] 	[360, 120, 30, 6, 1]

最后两者的对应位置相乘即可。
"""
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*(n)
        right = [1]*(n)
        

        for i in range(n-1):
            left[i+1] = left[i]*nums[i]
            right[n-i-2] = right[n-i-1]*nums[n-i-1]

        return [left[i]*right[i] for i in range(n)]
```
