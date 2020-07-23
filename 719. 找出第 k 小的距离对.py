"""
[719. 找出第 k 小的距离对](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/)
给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

示例 1:

输入：
nums = [1,3,1]
k = 1
输出：0 
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
提示:

2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
*****
还是不太理解具体的思路操作。
一个数组，两两元数之间就有一个差值，我们需要计算出所有的差值，然后在里面找到第k小的差值。上面说的差值都是差值的绝对值，是一个正整数。
代码有点难理解，以后回过头在分析，使用的方法和上一篇[287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)是类似的，
通过统计小于等于mid的值的个数，然后可以知道本次比mid小的距离数量有多少个。我们的目的就是找到第k小的距离，每个计算的cnt就是比当前mid距离差值小的个数。

==如果cnt大于等于k,说明我们的预设差值mid过大了。比mid小的个数太多了，需要较小mid的值。于是right = mid。==

==如果cnt<k，说明我们设置的mid距离差值太小了，需要增大我们的距离差值mid,于是left = mid + 1。==

"""


```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]#计算出距离差值k的左右范围
        while left < right:
            mid = (left + right) // 2
            cnt, start = 0, 0
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:#找出距离差值小于距离设定中值的个数
                    #[s, i]的距离大于mid, s增加。当[s, i]距离小于mid,说明[s+1,i],[s+2, i]...
                    #之间所有距离都会小于mid,他们总的个数为 i-start 个
                    start += 1    
                cnt += i - start#统计小于mid的个数有多少个
            if cnt < k:#cnt个数偏小，mid需要右移
                left = mid + 1
            else:
                right = mid
        return left
```
