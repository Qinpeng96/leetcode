# -*- coding: utf-8 -*-
"""
@author: 79877
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d 
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""
from typing import List 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        count = len(nums)
        if count < 4: return []
        nums = sorted(nums)
        for i in range(count-3):
            for j in range(i+1,count-2):
                left, right = j+1, count-1
                while left < right:
                    temp = nums[i]+nums[j]+nums[left]+nums[right]
                    if temp < target:
                        left += 1
                    elif temp > target:
                        right -= 1
                    else:
                        if [nums[i],nums[j],nums[left],nums[right]] not in res:
                            res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
     
if __name__ == "__main__":
    #初始化链表与数据
    data = [1, 0, -1, 0, -2, 2]
    a = Solution()
    t = a.fourSum(data,0)
    print(t)



