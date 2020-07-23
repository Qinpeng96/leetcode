[658. 找到 K 个最接近的元素](https://leetcode-cn.com/problems/find-k-closest-elements/)
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

示例 1:

输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]
 

示例 2:

输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]
 

说明:

k 的值为正数，且总是小于给定排序数组的长度。
数组不为空，且长度不超过 104
数组里的每个元素与 x 的绝对值不超过 104
***
在这里感谢威威大佬的[题解](https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/)。
主要有两种方法做这道题：
方法一：
由于最后要保留 K 个元数，我们就需要删除 n - k个元数，并且，这些被删除的元数都在两端，所以可以使用左右两边相互碰撞的方法。从最左端和最右端开始碰撞对比，
谁的差值小，谁就保留，另一个数则删除。

经过 n - k次重复之后就找到了左边界，输出 arr[left, left+k]。

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 排除法（双指针）
        size = len(arr)
        left = 0
        right = size - 1

        # 我们要排除掉 size - k 这么多元素
        remove_nums = size - k
        while remove_nums:
            # 调试语句
            # print(left, right, k)
            # 注意：这里等于号的含义，题目中说，差值相等的时候取小的
            # 因此相等的时候，尽量缩小右边界
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
            remove_nums -= 1
        return arr[left:left + k]

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
方法二：
二分查找最优区间的左边界（因为列表需要的长度已知，所以只找到左边界即可）

上一种方法的结论：
“排除法”的结论：（这个结论对于这道问题来说非常重要，可以说是解题的关键）

如果 x 的值就在长度为 size 区间内（不一定相等），要得到 size - 1 个符合题意的最接近的元素，此时看左右边界：

1、如果左边界与 x 的差值的绝对值较小，删除右边界；
2、如果右边界与 x 的差值的绝对值较小，删除左边界；
3、如果左、右边界与 x 的差值的绝对值相等，删除右边界。

讨论“最优区间的左边界”的取值范围：

首先我们讨论左区间的取值范围，使用具体的例子，就很很清楚地找到规律：

1、假设一共有 5 个数，[0, 1, 2, 3, 4]，找 3 个数，左边界最多到 2；

2、假设一共有 8 个数，[0, 1, 2, 3, 4, 5, 6, 7]，找 5 个数，左边界最多到 3。

因此，“最优区间的左边界”的索引的搜索区间为 [0, size - k]，注意，这个区间的左右都是闭区间，都能取到。

定位左区间的索引，有一点技巧性，但并不难理解。由排除法的结论，我们先从 [0, size - k] 这个区间的任意一个位置
（用二分法就是当前候选区间的中位数）开始，定位一个长度为 (k + 1) 的区间，根据这个区间是否包含 x 开展讨论。

1、如果区间包含 x，我们尝试删除 1 个元素，好让区间发生移动，便于定位“最优区间的左边界”的索引；
2、如果区间不包含 x，就更简单了，我们尝试把区间进行移动，以试图包含 x，但也有可能区间移动不了（极端情况下）。


说明一下，这里代码的意思就是首先确定一个整个区间，再来移动整个区间的起始位置，我也不是很理解，以后再看这种解法。
```python
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left = 0
        right = size - k

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            # 尝试从长度为 k + 1 的连续子区间删除一个元素
            # 从而定位左区间端点的边界值
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
