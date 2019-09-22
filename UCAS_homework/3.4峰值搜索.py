# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List 
##################################################
def PeakkSort(a):
    n = len(a)
    i = n // 2
    while(1):          
        if(a[i-1]>a[i] and a[i]>a[i+1]): #降序，峰顶在i及i左边                  
            m=a[i-1]           
            i=i/2               
        if(a[i-1]<a[i] and a[i]>a[i+1]): #找到峰顶                 
            m=a[i]            
            break              
        if(a[i-1]<a[i] and a[i]<a[i+1]): #升序，峰顶在i及i右边                 
            m=a[i+1]            
            i=(n-i)/2+i        
    return m


if __name__ == "__main__":
    b = [1,2,3,4,6,5,4,2]
    res = PeakkSort(b)
    print (res)


