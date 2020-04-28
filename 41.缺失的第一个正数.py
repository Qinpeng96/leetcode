# -*- coding: utf-8 -*-
"""
@author: 79877
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
"""
from typing import List 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n= len(nums)
        i,k = 0,0
        # while( i < n ):       #循环弹出非正值
        #     if ( nums[i] < 0 ):
        #         nums.pop(i)
        #         n -= 1
        #     else:
        #         i += 1
        if n == 1 and nums[0]==1:return 2
        #循环弹出非正值
        for i in range(n):
            if nums[k] <= 0:
                nums.pop(k)
                n -= 1
            else: k += 1 
        print(nums)
        if len(nums) == 1 and nums[0]==1:return 2
        
        #生成一个连续数组进行对比
        arr = [x+1 for x in range(k)]
        print(arr)
        #从连续数组开始查找，没有就弹出返回
        for j in range(len(arr)):
            if arr[j] in nums:
                j += 1
                if j==len(arr):return arr[-1]+1
            else: return arr[j]
        return 1
        

if __name__ == "__main__":
    #初始化链表与数据
    data = [1,-1]
    a = Solution()
    t = a.firstMissingPositive(data)
    print(t)



