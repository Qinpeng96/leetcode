"""
[209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
***
下面是滑动窗口法：每次加一个新数进来，如果和大于s,那么计算区间长度，每一取一个最小的区间长度。
如果和大于s，那么就需要缩小左边界，并且判断缩小之后 的总和是否满足大于等于s。
每次不满足总和大于等于s,我们就要右移right, 加入一个新的数进来。
"""
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        length = float('inf')
        left, right = 0, 0
        ans = 0
        while right < n:
            ans += nums[right]
            while ans >= s:
                if right + 1 - left < length:
                    length = min(right + 1 - left, length)
                ans -= nums[left]
                left += 1
            right += 1

        return length if length != float('inf')  else 0
```
"""
下面是powcai大佬的二分法：
num[i]的值是前i个数的总和， nums[j] - nums[i]就是（ j , i ]的总和，所以我们可以使用二分进行区间缩小。
区间的上界就是所有数的总和，下界就是s。
"""
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums : return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        #print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res 

作者：powcai
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/hua-dong-chuang-kou-on-er-fen-fa-onlogn-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
