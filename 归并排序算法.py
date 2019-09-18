# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List
##################################################

def MergeSort(a: List[int])->List:
    if len(a) <= 1: return a
    mid = len(a) // 2
    left_nums = MergeSort(a[:mid])
    right_nums = MergeSort(a[mid:])
    return Merge(left_nums, right_nums)

def Merge(a: List[int], b: List[int])->List:
    len_a = len(a)
    len_b = len(b)
    c = [0]*(len_a + len_b)
    i,j,k = 0,0,0
    while (i < len_a and j < len_b ):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        elif a[i] > b[j]:
            c[k] = b[j]
            j += 1
            k += 1
        else :
            c[k] = a[i]
            c[k+1] = b[j]
            k = k + 2
            i += 1
            j += 1

    while (i < len_a):
        c[k] = a[i]
        i += 1
        k += 1

    while (j < len_b):
        c[k] = b[j]
        j += 1
        k += 1   
    return c 


if __name__ == "__main__":
    a = [4,7,8,3,5,9]
    print(MergeSort(a))
