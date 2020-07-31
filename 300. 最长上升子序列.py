"""
[300. 最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到
***
由于这里不是一个连续的递增，所以开始我打算使用栈来做，就不对。借鉴了大佬的思路。
动态规划方法：dp[i] 表示第i个数字（包含）截至的最长递增串的长度。由于每个数字都需要和前面的所有数字进行比较，所以是由两个for循环组成。

这里主要是dp动态转移方程：
nums[i]是需要和前面比它小的数字的dp值加一来确定的，但是前面的数字中，比nums[i]小的数字可能有多个，我们就需要找一个dp值最大的加一。所以形成了下面的递推公式：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200731142717108.png#pic_center)
"""
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)#从前面的dp钟选一个最大的
        return max(dp)
```
