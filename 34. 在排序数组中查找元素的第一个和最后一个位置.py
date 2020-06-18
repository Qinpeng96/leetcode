"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
思路：
首先是二分查找，找到一个目标值，再对目标值左右分别开始搜索相同的目标值。但是实际上这样的结果虽然是通过了，但是好像效果不是很好。
"""
from typing import List
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count = len(nums)
        left, right = 0, count-1
        if count == 0: return [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = right = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < count - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            elif nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                return [-1, -1]
"""

"""
首先这里和二分法寻找数字有一些区别：
第一个，本次的搜索区域是左闭右开的，之前是左闭右闭。
第二个，while里面是 ＜ 不是 ≤
第三个，就是每次判断条件之后的左右指针更新

其中情况分为三种，等于，大于，小于。

大于：当mid 大于目标值时，right 就要改变， 由于右开，所以变成 right = mid 。
小于：当mid小于目标值时，这个时候就是移动左边界，由于左闭，所以 left = mid + 1
等于：当mid与目标值等于的时候，因为要求左边界的值，所以需要收敛有边界，则right =mid,因为这里的是左闭右开的，所以
[ left ····mid····right )，当中间等于时，只需判断[left, mid) ,即right=mid,右开即可。

最后这里说一下判断数组越界的问题，如果是找左边界，会有数组左右两种越界，其中左越界就是找到列表最左端了还是没有匹配，
这里的判断就是 nums[left] != target，第一个值都不满足，说明target 比最小数还要大。 另一种情况就是右越界，left == count，
就是已经超出列表的索引了。找右边界也是类似的，越界的条件有所不同，其中左越界是 left==0 ，右越界是nums[left-1] != target

"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count = len(nums)
        left, right = 0, count
        start, end = 0, 0

        if count == 0: return [-1, -1]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
        #判断越界的情况
        if left == count or nums[left] != target:
            start = -1
        else:
            start = left

        left, right = mid, count
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid 
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1

        if left == 0 or nums[left-1] != target:
            end = -1
        else:
            end = left - 1

        return [start , end]
        
    
if __name__ == "__main__":
    s = Solution()
    # print(s.searchRange([2,2],1))
    print(s.searchRange([5,5,5,5,7,7,8,8,10,10,10],5))

