"""
33. 搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

[0,1,2,4,5,6,7]

"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = len(nums)
        if count == 0: return -1#列表为空，返回-1
        left, right = 0, count-1
        while left <= right: #循环跳出条件
            mid = (left + right) // 2 #计算中值
            if nums[mid] == target: #中间值刚好等于目标值，则输出
                return mid
            if nums[left] <= nums[mid]:#原始列表为升序列表
                if nums[left]<= target < nums[mid]:#如果目标再列表右边
                    right = mid - 1
                else:#如果目标在列表左边
                    left = mid + 1
            else:#列表的顺序为移位后的顺序
                if  nums[mid] < target <= nums[right]:#判断目标是否在列表右边
                    left = mid + 1
                else:#目标是否在列表左边
                    right -= 1
        return -1

    
if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2],4))

