"""
[162. 寻找峰值](https://leetcode-cn.com/problems/find-peak-element/)
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
***
寻找峰值，就是找一个数即大于左边，也大于右边。由于极值可能处于列表两端。所以开始就在元数的左右两端加一个负无穷，最后得到的峰值坐标减一就可以了。
"""

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float('inf')] + nums + [-float('inf')] #左右加负无穷
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:return mid - 1
            if nums[mid-1] < nums[mid] < nums[mid+1]:#递增数列，峰值在右
                left = mid + 1 
            else:#其他情况峰值在左
                right = mid
```
