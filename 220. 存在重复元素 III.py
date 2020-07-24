"""
[220. 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii/)
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

 示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
***
我们将数据分到 M 个桶 中。
每个数字nums[i] 都被我们分配到一个桶中
分配的依据就是 nums[i] // (t + 1)
这样相邻桶内的数字最多相差2 * t + 1
不相邻的桶一定不满足相差小于等于t
同一个桶内的数字最多相差t
因此如果命中同一个桶内，那么直接返回True
如果命中相邻桶，我们再判断一下是否满足 相差 <= t
否则返回False
***
例如一堆数值，我们以10的大小作为分桶的容量，那么这些数值将会落在：
[0,10],  [11,20],  [21,30], [......]每一个桶内，每一个桶内的数值只差是肯定小于桶的容量的，所以我们设置桶的容量为(t + 1)。那么我们一个桶内的任意两个值的差值总是小于等于t的。

**注意**差值小于等于t的两个数可以在相邻的桶内，例如25 与 32，一个在二桶，一个在三桶。但是两者的数值差是小于 t = 9的。因此，我们还需要判断相邻桶内的值是否满足条件。这里的条件还有一个数值的索引值只差小于等于k.

两者的索引值之差小于等于k是一个需要维护的条件，因为当索引值之差大于k的时候，就算两者的数值之差小于等于t，也是不满足条件的。因此在末尾，如果当前的索引值大于等于k, 说明需要弹出最前面的一个索引值，需要有一个弹出hash表中最小的索引。留出一个空位等着下一个数进来进行判断。
"""
```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0: return False
        bucket = {}
        bucket_size = t+1
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size #将不同的段的分到不同的桶

            if bucket_num in bucket:#如果本次分到之前桶，之前存在一样的桶
                return True 
            
            bucket[bucket_num] = nums[i]#本次分到的桶没有被分过

            #在本次桶没有分到重复的情况下，和上一个桶里面的值对比，看是否符合条件
            if (bucket_num-1) in bucket and abs(bucket[bucket_num] - bucket[bucket_num-1]) <= t:
                return True
            #在本次桶没有分到重复的情况下，和下一个桶里面的值对比，看是否符合条件
            if (bucket_num+1) in bucket and abs(bucket[bucket_num] - bucket[bucket_num+1]) <= t:
                return True
            #如果当前的索引值大于k,那么比如第一个加进来的值的索引为0，之后的值和0的索引值只差肯定大于等于k
            #w为了少存储，可以删除前面索引很小的值（不可能满足条件）
            if i >= k:
                bucket.pop(nums[i-k] // bucket_size)
        return False



```
