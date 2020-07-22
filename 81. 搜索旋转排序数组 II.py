"""
[81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
***
这道题是承接[33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)和
[剑指 Offer 11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)这两道题的方法组合而成的。

 1. 首先是搜索旋转排序数组这道题，提供了一个在区分左右占优区间之后，再一次区分target目标值是在左区间还是右区间的思路。
 2. 剑指这道题，提供了一个去除重复数字对搜索的影响。那就是对中，右两个数进行判断，区别是左占优，还是右占优。但是在中等于右的时候，这个条件就不成立，
 因为此时可能除了中右相等，可能左中右都相等。待寻找的值可能在左边，也可能在右边，例如下面这个例子，所以我们只有逐个缩小区间进行进一步分析。
 #
	 [0,0,0,0,1,0]
	 [0,1,0,0,0,0]
这个时候中右，甚至左中右都相等，我们无法直接知道目标值是在左区间还是右区间，所以只有逐个缩小区间范围。那为什么是右区间减一了？ 
首先，中右的值是相等的，我们去掉最右边的值，在取中值的时候，也相当于中值左移，并且去掉右边的值，对元素索引没有影响，如果去掉左边的，或者中间的值，对元素的索引会产生变化。
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]: return True
            if nums[mid] < nums[right]:#右占优
                if nums[mid] < target  <= nums[right]:#目标值在右边
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:#左边占优
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:#中右相等，此时缩小区间
                right -= 1
        return False            