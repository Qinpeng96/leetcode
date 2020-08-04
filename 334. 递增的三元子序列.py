"""
[334. 递增的三元子序列](https://leetcode-cn.com/problems/increasing-triplet-subsequence/)
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false
***
这道题题目的意思是，数组列表内从左到右，有三个递增的数字即可，不要求连续。但是时间复杂度O(n)。
我也是看了下评论说使用first记录最小值，second记录倒数次大值。然后找一个比second大的数就可以了。

算法流程如下：
- 首先是找到两个递增的数字(不要求连续)，第一个赋值给first,第二个赋值给second。注意，在找两个递增的数的时候，可能遇到全是递减的数的情况，那么就会出界，所以判断越界的条件应该放在首位。如果找完了还是没有找到这样的数据，那么直接返回False.
- 有了first 和second，我们就需要根据下一个待加入的值来更新first，或者second,或者直接输出True。定义c为待加入的数
- 情况一：c < first 说明我们的第一个最小值需要更新，万一后面有以这个最小值c开头的三个递增数。所以first = c ,但是这里的second保持不变。因为我们这里要找三个递增数，缩小了左边界后，我们的右边界应该还是保持不变，这样才能和之后的数进行比较。
- 情况二： first < c < second 这个时候我们的右边界需要缩小，后面大于second的数肯定大于c。左边界应该保持不变。
- 情况三：c > second 说明刚好已经有三个数递增的了，可以直接输出。
- 情况四：当 c  == scond 或者 c == first的时候，我们什么也不做，相当于跳过这次。
最后如果弹出循环之后，说明数组内没有这样的递增数列，返回false。
"""
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        if n < 3: return False
        i, j = 0, 1
        
        while j < n and nums[i] >= nums[j]:#注意这里是大于等于都不可以
            nums[i] = nums[j]
            j += 1

        if j < n:
            first, second = nums[i], nums[j]
        else:
            return False

    
        for c in nums[j+1:]:
            if c < first:
                first = c
            elif first < c < second:
                second = c
            elif second < c:
                return True
        return False
                
```
"""
看了官方的解答，自己真菜。
主要是首先就是不用首先找到两个递数，它是直接在for循环中，从列表开始就开始找的。
- 第一步就是把f,s都变成nums[0]
- 这里的顺序也有讲究，首先是对f_min进行的比较，在对second。
- 例如第二个数nums[1] < nums[0],在判断的时候，首先就会赋值给first。second就不考虑了，只有当first < nums[i] < second的时候，才会更新second。

- 不得不说非常的巧妙啊！
"""
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f_min = float('inf')
        s_min = float('inf')
        for i in range(len(nums)):
            if nums[i] <= f_min:
                f_min = nums[i]
            elif nums[i] <= s_min:
                s_min = nums[i]
            else:
                return True
        return False
```
