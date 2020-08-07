"""
[560. 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/)
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

***

使用前缀差，然后两次遍历，就可以计算出个数。但是会超时
"""
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        pre = [0]*(n+1)
        
        for i in range(1,n+1):
            pre[i] = nums[i-1] + pre[i-1]
        
        for i in range(1,n+1):
            for j in range(i,n+1):
               if pre[j] - pre[i-1] == k:
                    res += 1
        return res
```
"""
这里使用字典哈希记录相同前缀的个数。
例如每次前缀和为pre, 如果pre不在dic内，就把pre加入字典，赋值为1。否则就在原始的字典值上面加一。

**我们只考虑有多少个K值，或者说两个前缀和之间的差值等于K有所少个，与索引无关。并且两个前缀和之间的价值是连续的。所以我们每次计算当前的前缀和pre后，就可以在字典内查找pre - k是否在字典内，在的话有几个就加入几个到res输出**

注意：我们在查找pre-k是否在字典的时候，如果刚好 pre == k这个时候我们应该加入一个res输出值。所以初始化的字典内应该有dic[0] = 1
"""
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre = 0
        dic = {0:1}#初始化当前的前缀和等于K值的情况
        for num in nums:
            pre += num
            if pre - k in dic:#注意这里有一种两者相等的情况也要记录，即初始化dic[0] = 1
                res += dic[pre-k]
            if pre in dic:
                dic[pre] += 1
            else:
                dic[pre] = 1
        return res

```
