# -*- coding: utf-8 -*-
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
"""
自己写的，不是很好

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = left = right =  0
        if len(nums) == 1:
            return 1
        while (right < len(nums)):
            while (right< len(nums) and nums[left] == nums[right]):
                right += 1
            if (left != right and right< len(nums)):
                left += 1
                nums[left] = nums[right]
                count += 1
                right += 1
        return count+1
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

if __name__ == "__main__":
    a = Solution()
    print(a.removeDuplicates([2,2]))
    