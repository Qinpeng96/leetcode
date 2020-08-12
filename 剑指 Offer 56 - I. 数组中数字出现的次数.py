"""
[剑指 Offer 56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000
 ***
 这道题我知道是用异或解答，但是我们对整个数组进行一遍异或之后，我们得到的值是其中不重复的两个值的异或。
 这可把把我难住了。没办法只有看题解：

假设我们数组内的单个值为 1 和 5，那么这两者的异或值等于
#
	1:001
	5:101
	^:010 	两者异或的结果就是010，为了区分这两个数，我们对其进行观察，发现两个从低到高为相异的位的异或为1
所以我们可以找一个两者相异的位， 找出来之后再分别对其数组进行求异或，因为他们的这一位值是不相等的，所以可以把数组区分成两堆。
"""
```python
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0
        a, b = 0, 0
        for num in nums:#先求出来两个数的异或值
            res = res ^ num

        mask = 1#设定一个mask,找出两个不相同的一个位
        while res & mask == 0:
            mask <<= 1

        res1 = mask
        for num in nums:
            if mask & num:#将数组区分为两个部分，分别求异或，得到的值就是答案
                a ^= num
            else:
                b ^= num

        return [a, b]

```
