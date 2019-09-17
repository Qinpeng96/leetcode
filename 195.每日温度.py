# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List
##################################################
"""常规方法 超出时间限制
"""
class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        a = [0]*len(T)
        for i in range(len(T)):
            for j in range(i+1,len(T)): 
                if T[j] > T[i]:
                    a[i] = j - i
                    break
                else:
                    a[i] = 0
        return a
##################################################  
        
"""
使用栈进行操作
入栈条件：当前元素比栈顶元素小
出栈条件：遇到比自己大的温度，出栈时索引距离即天数差
使用枚举：可以同时使用下角标和元数值
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:        
        stack = []
        a = [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:a[stack.pop()] = i - stack[-1]
            stack.append(i)
        return a   
        
        
def main():
    s = Solution()
    h = s.dailyTemperatures([73,74,75,71,69,72,76,73])
    print(h)
    
main()