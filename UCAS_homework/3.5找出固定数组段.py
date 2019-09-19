# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List 
##################################################
def BinSearch(arr, u, v):
    left =  0
    right = len(arr) - 1
    key = (u + v) // 2
    while (left <= right):
        temp = (right + left) // 2
        if arr[temp] == key: #如果有元素相同，则下表滞后
            return temp
        elif arr[temp] > key:#二分分到左区间，右边界-1
            right = temp - 1
        elif arr[temp] < key:#二分分到右区间，左边界+1
            left = temp + 1
        # print(left)
    return left

def showU2V(a,u,v):
    i = BinSearch(a, u, v)
    j = BinSearch(a, u, v)
    while (a[j] < v):
        j += 1
    while (a[i] > u):
        i -= 1
    return a[i+1:j]

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9]
    b = showU2V(a,2,6)
    print (b)


