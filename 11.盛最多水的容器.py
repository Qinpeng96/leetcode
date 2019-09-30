# -*- coding: utf-8 -*-
"""
@author: 79877
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，
垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

"""
from typing import List 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        i, j = 0, n-1
        while (i<j):
            area = max(area, (j-i) * min(height[i], height[j]))
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return area
            

        
        
if __name__ == "__main__":
    #初始化链表与数据
    data = [1,8,6,2,5,4,8,3,7]
    a = Solution()
    print(a.maxArea(data))



