"""
[136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
***
使用哈希字典的方法，第一次出现就加入，第二次出现就删除字典键值。
"""
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for c in nums:
            if c not in dic:#没出现过，创建键值对应
                dic[c] = c
            else:#第二次进入，删除键值
                del dic[c]
        for c in dic:
            return c

```
"""
下面是一种空间复杂度为O(1)的方法。
异或解法：异或运算满足交换律，a ^ b ^ a = a ^ a ^ b = b,因此ans相当于nums[0] ^ nums[1] ^ nums[2] ^ nums[3] ^ nums[4]..... 
然后再根据交换律把相等的合并到一块儿进行异或（结果为0），然后再与只出现过一次的元素进行异或，这样最后的结果就是，只出现过一次的元素（0^任意值=任意值）
异或的性质
两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是
如果同一位的数字相同则为 0，不同则为 1

异或的规律

- 任何数和本身异或则为0

- 任何数和 0 异或是本身

- 异或运算满足交换律，即：a ^ b ^ a = a ^ a ^ b = b
"""
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for c in nums:
            num = num ^ c
        return num
```
