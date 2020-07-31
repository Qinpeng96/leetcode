"""
[面试题 08.03. 魔术索引](https://leetcode-cn.com/problems/magic-index-lcci/)
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，
若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

示例1:

 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0
示例2:

 输入：nums = [1, 1, 1]
 输出：1
提示:

nums长度在[1, 1000000]之间

***
这道题 提示使用二分有点迷。

 1. 从头开始遍历，注意这里是有序的数组，所以假如nums[ 0 ] = 3
 2. 这个时候 nums[ 1 ]的值肯定是大于3的，但是索引为1，就不满足，这样可以直接跳过
 3. 具体能够跳到哪了？nums[ 0 ]   = 3, 那么我们至少应该从索引为3开始找起
 4. 因为有可能nums[0,1,2,3] = 3,所以是从索引为3开始找起
"""
```python
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        if nums[0]==0:return 0
        p, n = 0, len(nums)
        while p < n:
            if nums[p] > p: p = nums[p]#第一个值大于索引值，索引值移动到[第一个值处]
            elif nums[p] == p: return p
            else: p += 1
        return -1

```
