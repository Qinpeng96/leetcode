"""
[剑指 Offer 61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .
***
- 首先对数组排序，统计0 的个数和看是否有重复的非0元数出现。
- 接着就对数据大小进行分析，当非0的最大值减去最小值小于等于4的时候，数据就是有效连续的。

"""
```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        change = 0
        dic = {}

        #找出0的个数和有无重复的其他数字，有就返回False
        for c in nums:
            if c == 0:
                change += 1
            else:
                if c not in dic:#字典判断重复，有重复就返回False
                    dic[c] = c
                else:
                    return False
        if nums[-1] - nums[change]  <= 4:#数组中差值小于等于4的时候有效
            return True
        else:
            return False

```
大佬的更加简洁的写法：

```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

作者：jyd
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
