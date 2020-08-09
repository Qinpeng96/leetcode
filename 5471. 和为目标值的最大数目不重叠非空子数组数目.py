"""
[5471. 和为目标值的最大数目不重叠非空子数组数目](https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)
给你一个数组 nums 和一个整数 target 。

请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。

 
示例 1：

输入：nums = [1,1,1,1,1], target = 2
输出：2
解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
示例 2：

输入：nums = [-1,3,5,1,4,2,-9], target = 6
输出：2
解释：总共有 3 个子数组和为 6 。
([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。
示例 3：

输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
输出：3
示例 4：

输入：nums = [0,0,0], target = 0
输出：3
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
***

开始的思路：利用前缀和，利用双指针，右指针右移，左指针从头遍历。找到目标值。左指针移动到右指针位置，右指针右移一位。结果超时了，惭愧啊。
"""
```python
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        n = len(nums)
        out = 0
        num = [0]*(n+1)
        for i in range(1,n+1):#计算前缀
                num[i] += num[i-1] + nums[i-1]
        
        i, j = 0, 1
        Flag = 0
        pre = 0
        while j <= n:#遍历查找，每查到一次，就整体后移
            if Flag:
                i = pre
            else:
                i = 0
                
            while i < j:
                if num[j]-num[i] == target:
                    out += 1
                    pre = j
                    Flag = 1
                    break
                else:
                    i += 1
            j += 1
        return out
```
"""
大佬们也是使用的前缀和，只不过这里并没有要求我们返回具体的下标，只叫我们返回符合条件的个数。所以我们用不着每次都遍历一次。
直接把前缀和加入到一个集合内，后面的  **(前缀和 - 目标值)** 如果在集合内,那么输出加一。

注意：这个时候我们需要做三件事：
- 清楚集合内部的元数，因为我们这里不能包含之前的元数。并且把0加入到集合
- 清楚前缀和的值，我们从新开始计算
- 集合加0是为了当某一个刚好就等于目标值，一相减，值等于0，但是0元素不是之前的前缀和，我们所以需要加入一个0在集合，表示[0：i]一段都是满足条件的，不需要两个前缀和之间相减。
"""
```python
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        out = 0
        res = set()
        res.add(0)
        presum = 0
        for num in nums:
            presum += num
            if (presum - target) in res:#查找差值是否在前缀和的集合内
                out += 1
                res.clear() #得到之后就要清楚前缀和的集合
                res.add(0)
                presum = 0 #得到之后就要清楚前缀和
            else:
                res.add(presum)
        return out

```
