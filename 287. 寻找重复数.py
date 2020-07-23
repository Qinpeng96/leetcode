"""
[287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
***
思路：

这道题要求我们查找的数是一个整数，并且给出了这个整数的范围（在 1 和 n 之间，包括 1 和 n），并且给出了一些限制，于是可以使用二分查找法定位在一个区间里的整数；

二分法的思路是先猜一个数（有效范围 [left, right]里的中间数 mid），然后统计原始数组中小于等于这个中间数的元素的个数 cnt，如果 cnt 严格大于 mid，
（注意我加了着重号的部分「小于等于」、「严格大于」）。根据抽屉原理，重复元素就在区间 [left, mid] 里；

与绝大多数二分法问题的不同点是：正着思考是容易的，即：思考哪边区间存在重复数是容易的，因为有抽屉原理做保证。我们通过一个具体的例子来分析应该如何编写代码；

以 [2, 4, 5, 2, 3, 1, 6, 7] 为例，一共 8 个数，n + 1 = 8，n = 7，根据题目意思，每个数都在 1 和 7 之间。

例如：区间 [1, 7]的中位数是 4，遍历整个数组，统计小于等于 4 的整数的个数，如果不存在重复元素，最多为 4 个。等于 4的时候区间 [1, 4] 内也可能有重复元素。
但是，如果整个数组里小于等于 4 的整数的个数严格大于 4 的时候，就可以说明重复的数存在于区间 [1, 4]

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:#每次找一个中位数
            mid = (left + right) // 2
            cnt = 0#计算得到比中位数小于等于的值的个数
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt > mid:#如果比mid小于等于的值的个数大于mid,那么重复的数肯定在mid左边
                right = mid
            else:#否则，重复的数在mid右边
                left = mid + 1
        return left#最后弹出left,就是为重复值
```
