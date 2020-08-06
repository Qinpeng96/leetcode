"""
[137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii/)
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99
***
使用位运算，每一统计0-31位上面的个数，如果一个位上的个数不为3，那么说明这个位上的数是单个存在的，把这些单个存在的数并在一起就可以得到单独的那个数。

注意我们得到的数可能是负数，负数就是对应的正数+2**32。同理，如果这里不是出现三次，出现K次，我们就只需要改一下判断条件就好了。
"""
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            mask = 1 << i
            for c in nums:
                if mask & c != 0:
                    cnt += 1
            if cnt % 3 != 0:
                res |= mask
        return res - 2**32 if res > 2**31 -1 else res

```
