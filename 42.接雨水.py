# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
# height:[0,1,0,2,1,0,1,3,2,1,2,1]
         [0,1,2,3,4,5,6,7,8,9,10,11]
"""
class Solution:
    def trap(self, height):
        if not height: return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            print(stack)
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) \
                * (i-stack[-1] - 1)
            stack.append(i)
        return res
    