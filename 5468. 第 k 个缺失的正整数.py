"""
[5468. 第 k 个缺失的正整数](https://leetcode-cn.com/problems/kth-missing-positive-number/)
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。

示例 1：

输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
 

提示：
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
***
首先计算给出的数组中缺失的数字的个数，如果已经在这个数组中找到第K个了。那么就直接输出。
否则就继续递增，检验数字是否在arr 内部，如果不在，则计数器加一，直到找到第k个。
"""

```python3
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n):#建立一个arr长度的数组，看下在这个长度内落了几个
            if i+1 not in arr:
                cnt += 1
                if cnt == k:
                    return i+1
        
        m = k-cnt+1#如果在arr长度内的数字丢失的个数少于K个，那么从arr的长度n继续寻找，直到找到为止
        # print(m)
        i = 1
        while cnt < k:
            if n+i not in arr:
                cnt += 1
            i += 1
        return i+n-1
```