# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List
##################################################

def QuickSort(a: List[int], left:int, right:int)->List:
    if left >= right : return 
    j = right
    i = left
    key =  a[i]
    while i < j:
        #当从后面找到比key小的数，则交换
        while i < j and key <= a[j]:
            j -= 1
        
        #当从前面找到比key大的数，则交换
        while i < j and key >= a[i]:
            i += 1
        #交换两者数值
        temp = a[j]
        a[j] = a[i] 
        a[i] = temp
        print("a =%s , i = %d,j = %d"%(a,i,j))
    #经过i++,j--,直到i==j进行交换
    #将起始要确定位置的值放在他应该在的位置

    a[left] = a[i]
    a[i] = key 
    print("a =%s , i = %d,j = %d"%(a,i,j))
    QuickSort(a, left, i-1)
 
    QuickSort(a, i+1, right)
    return a 

if __name__ == "__main__":
    # a = [3,5,4]
    a = [6,7,8,3,4,5,9]
    print(a,'\n')
    print(QuickSort(a,0,6))
