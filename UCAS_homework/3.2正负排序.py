# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List 
##################################################
def P_N_Sort(a:List[int])->List:
    i = 0
    j = len(a) - 1
    while (i < j):
        while(i < j and a[i] < 0):
            i += 1
        while(i < j and a[j] > 0):
            j -= 1
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    return a        
if __name__ == "__main__":
    a = [-2,-3,3,-4,2,2]
    print(P_N_Sort(a))


