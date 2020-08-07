"""
[剑指 Offer 03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
***
#### 开始整剑指offer 
这道题目，想到的是用字典来做。第二次加入的时候，就弹出返回当前数字。
"""
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] > 1:
                return num
```
"""
但是注意这道题，说的是长度为n,数值也在0~n-1。如果我们对其使用排序，那么索引和数值在没有重复元素的情况下将会一一对应。

遍历数组 nums，设索引初始值为 i = 0

- 若 nums[i] = i ： 说明此数字已在对应索引位置，无需交换，因此跳过；
- 若 nums[nums[i]] = nums[i] ： 代表索引 nums[i] 处和索引 i 处的元素值都为 nums[i] ，即找到一组重复值，返回此值 nums[i]；
- 否则： 交换索引为 i 和 nums[i]的元素值，将此数字交换至对应索引位置。
- 若遍历完毕尚未返回，则返回 -1 。
- 
**注意：**
Python 中， a, b = c, d 操作的原理是先暂存元组 (c, d) ，然后 “按左右顺序” 赋值给 a 和 b 。
因此，若写为 $$nums[i],  nums[nums[i]] = nums[nums[i]], nums[i]$$则 nums[i] 会先被赋值，之后 nums[nums[i]] 指向的元素则会出错。
"""
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:#本位就是本数，跳过
                continue
            elif nums[i] == nums[nums[i]]: #要置换的数和当前的数相同，直接返回
                return nums[i]
            else:#否则置换，注意交换的顺序，开始我就是交换的顺序不对一直出不来结果
                nums[nums[i]], nums[i] =  nums[i] , nums[nums[i]]
            

```

