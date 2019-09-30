# -*- coding: utf-8 -*-
"""
@author: 79877
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
]

"""
from typing import List 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''
        本解法的思路是沿着数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p2]互换
        三色旗问题，最初可将其看为四类：red，white，blue和unclassified
           |——0——|--1---|--unclassified--|--2---|
                 |      |                |
                red   white             blue
           当white与blue未重合时：
               如果nums[w]为0，则交换放到red区间，red和white都加1。
               如果nums[w]为1，则white指针加1。
               如果nums[w]为2，则交换放到 blue 区间，blue减1。
        '''
        r, w, b = 0, 0, len(nums) - 1
        
        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1







class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        res2 = 0
        sum = 0
        for i in range(n):
            sum = sum + nums[i]
            if nums[i] == 2:
                res2 += 1
        res1 = sum - res2
        res0 = n - res2 - res1
        for i in range(res0):
            nums[i] = 0
        for i in range(res1):
            nums[res0+i] = 1
        for i in range(res2):
            nums[res0+res1+i] = 2

        """
        Do not return anything, modify nums in-place instead.
        """
        
if __name__ == "__main__":
    #初始化链表与数据
    data = [2,0,2,1,1,0]
    a = Solution()
    print(a.sortColors(data))



