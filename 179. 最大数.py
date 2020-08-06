"""
[179. 最大数](https://leetcode-cn.com/problems/largest-number/)
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
***
先转换成字符串的形式，使用冒泡排序，两两相邻进行比较，能够得到最大值的放在最后。
"""

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:return ""
        if len(nums) == 1:return str(nums[0])

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if (nums[j]+nums[j+1])>(nums[j+1]+nums[j]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]

        return ''.join(nums[::-1]) if not nums == ['0']*len(nums) else "0"
```
