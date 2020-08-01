"""
[645. 错误的集合](https://leetcode-cn.com/problems/set-mismatch/)
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]
注意:

给定数组的长度范围是 [2, 10000]。
给定的数组是无序的
***
这里使用的是东哥的一种比较对照方法。给定数组长度为n,那么其对照的索引长度也为n。如果给定的数组中有重复、缺少值，
那么就会出现两个数对应同一个索引的情况和有一个索引没有对应的情况。
***
- 首先取索引。从0 ~ n-1取，每一个索引有一个对应的元素值对应着索引中的一个索引，这个索引对应的元素值变为负数。
当有重复的nums的时候，重复元数值的索引对应元数会被翻转两次变为一个正数，这个时候说明出现了重复值，重复值就是本次索引对应的值。
 - 接着再循环一遍，发现谁是正数就说明这个数的对应的索引没有被安排到，逆向思维，对应这个索引的元素就是缺失的元素。
 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200801175137871.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
"""
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        n = len(nums)
        for i in range(n):
            index = abs(nums[i])-1#计算出实际真实对应坐标
            if nums[index] > 0:#如果该坐标的数大于0，反转
                nums[index] = -nums[index]
            else:#如果该坐标的数小于0，那么说明已经反转过一次，找到被复制的数
                dup = abs(nums[i])
        mis = -1
        for i in range(n):#找到时去的数
            if nums[i] > 0:
                mis = i+1
        return [dup, mis]
```
