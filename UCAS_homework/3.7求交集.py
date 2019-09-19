# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List 
##################################################
def QuickSort(a, left, right):
    if left >= right : return 
    j = right
    i = left
    key =  a[i]
    while i < j:
        #当从后面找到比key小的数，则交换
        while i < j and key <= a[j]:
            j -= 1
        
        #当从后面找到比key大的数，则交换
        while i < j and key >= a[i]:
            i += 1
        #交换两者数值
        temp = a[j]
        a[j] = a[i] 
        a[i] = temp
    #经过i++,j--,直到i==j进行交换
    #将起始要确定位置的值放在他应该在的位置

    a[left] = a[i]
    a[i] = key 
    QuickSort(a, left, i-1)
    QuickSort(a, i+1, right)
    return a 

def Num1AndNum2(a, b):
    #首先进行快速排序
    a1 = QuickSort(a,0,len(a)-1)
    b1 = QuickSort(b,0,len(b)-1)
    i,j = 0,0
    c = []
    #利用i，j 两个游标对数据进行比较相等就赋值给C
    while i < len(a1) and j < len(b1):
        if(a1[i] == b1[j]):
            c.append(a1[i])
            i += 1
            j += 1
        elif a1[i] > b1[j]:
            j += 1
        else: i += 1
    return c

if __name__ == "__main__":
    a = [9,3,4,1,5]
    b = [2,8,5,1,6,8]

    res = Num1AndNum2(a,b)
    print (res)


