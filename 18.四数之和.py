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
        n = len(nums)
        #首先排除数组小于4的情况
        if n < 4: return []
        nums.sort() #对数组进行排序
        res = temp = []

        for i in range(n-2):
            for j in range(i+1,n-1):  #j从i+1开始
                left,right = j+1,n-1  #left从j+1开始
                while left < right:
                    if nums[left] + nums[right] > target - nums[i] -nums[j]:
                        right -= 1    #四个数之和大于目标，则右指针左移，减小和值
                    elif nums[left] + nums[right] < target - nums[i] -nums[j]:
                          left += 1  #四个数之和小于目标，则左指针右移，增大和值
                    else:            #找到了目标数组，添加去重操作
                        temp = [nums[i],nums[j],nums[left],nums[right]]
                        if temp not in res:
                            res.append(temp)
                        left += 1
                        right -= 1
        return res
        
if __name__ == "__main__":
    #初始化链表与数据
    data = [1, 0, -1, 0, -2, 2]
    a = Solution()
    t = a.fourSum(data,0)
    print(t)



