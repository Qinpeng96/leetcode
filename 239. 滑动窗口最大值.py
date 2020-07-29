"""
[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：

你能在线性时间复杂度内解决此题吗？

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
***
我们可以使用**双向队列**，该数据结构可以从两端以常数时间压入/弹出元素。

存储双向队列的索引比存储元素更方便，因为两者都能在数组解析中使用。

 1. 首先填充双向队列中的，填充k-1个前面的数字，之后每加入一个数字，就进行递减栈的判断。
 2. 为什么使用的是递减栈，因为我们需要找的是一个最大的数，如果待加入的数比原来的栈的某一个数大，那么就需要删除这些没用的小的数，保留待加入的较大的数。
 3. 每当待加入的数大于递减栈的尾部数，就弹出尾部的数，直到栈为空，或者栈中的数大于待加入的数，这个时候再将待加入的数，加入到栈中。
 4. 每一个栈是一个递减栈，待加入的数加入到栈中之后，最左边的数就是一个最大的数(作为输出)。
 5. 还有一个问题，每次我们左边的数是这一段大的，但是怎么能够保证这个左边的最大值，在之后的段中会随着窗口的移动，这个较大值会消失。
    由于我们知道窗口的大小k,那么待加入的索引减去最左边的值的索引如果大于k,那么说明这个最大值不应该出现在这一段窗口之后，所以要pop删除。

注意：双向队列里面存储的是数组的索引，而不是数字。因为我们需要在维护递减栈的最大值是不是属于当前的滑动窗口的时候，需要进行索引坐标的判断


"""
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums): return []
        queue = collections.deque()#存储的是索引
        out = []
        for i, num in enumerate(nums):
            if i < k-1:#初始化把栈填充到k-1个，填充的时候维护一个递减栈，但是不用判断最大值的归属
                while queue and nums[queue[-1]] < num:
                        queue.pop()
                queue.append(i)
            else:#对之后的每一个值进行判断
                if queue and i - queue[0] >= k:#对栈中的左边最大值索引进行判断，看是否属于当前的滑动窗口
                    queue.popleft()#如果不属于当前的滑动窗口，就删除栈左边的最大值
                while queue and nums[queue[-1]] < num:#如果栈不为空，且栈中的最后一个元数索引的数值小于待加入的数值
                    queue.pop()#进行弹出压栈
                queue.append(i)
                out.append(nums[queue[0]])#每次的输出是，栈最左边的值
        return out
```
