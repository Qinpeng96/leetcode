"""
[128. 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/)
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
***
我的想法是利用字典，每次加入的时候看左右两边的数是否存在，存在的话就更新其本身以及周围的长度值。
注意：有重复的数字的时候直接跳过。
但是注意这里的复杂度可能最坏为O(n^2)。不满足题意。
"""
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        out = 0
        def count(left, right, num):#更新左右的长度值
            while left in dic:
                dic[left] = num
                left -= 1
            while right in dic:
                dic[right] = num
                right += 1

        for c in nums:
            if c not in dic:#字典内不存在，加入，长度为1
                dic[c] = 1
            else:#有重复的数字，跳过
                continue                
            #对左，右，左右都存在的情况进行判断，最后更新连续的数列的长度
            if c+1 in dic and c-1 not in dic:
                dic[c] += dic[c+1]
            elif c-1 in dic and c+1 not in dic:
                dic[c] += dic[c-1]
            elif c-1 in dic and c+1 in dic:
                dic[c] += dic[c-1] + dic[c+1]
            out = max(out, dic[c])
            count(c-1, c+1, dic[c])
            
        return out
```
"""
下面看一下官方的题解
算法思想
- 对每个元素进行判断，是不是序列的开始。即nums[i]-1是否在哈希表中（O（1）的时间）。
- 如果nums[i]-1在set中，说明不是序列的开始，则跳过。
- 如果nums[i]-1不在，说明nums[i]是序列的开始。判断nums[i]+1是否在哈希集合中，直到没有出现在集合中，判断此时的长度cur_len。和最长序列长度进行比较，max_len = max(curr_len,max_len)。
"""
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)#去重
        out = 0#总的最长序列长度
        for c in nums:
            res = 0#本次序列长度
            if c-1 in dic:#如果前一个值在集合中，说明本次不是开头
                continue
            while c in dic:#本次是一个序列的开头，计算这个开头的序列长度
                res += 1
                c += 1
            out = max(out, res)
        return out
```
