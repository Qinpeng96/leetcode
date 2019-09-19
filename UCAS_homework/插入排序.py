# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List

    
##################################################
# def ModInsertSort(a:int, left:int, right:int):
#     temp = a[left]
#     mid = (right - left) // 2
#     if a a[mid] >= 

##使用二分法，把元素要插入的下角标找出来
def BinSearch(arr, key):
    left =  0
    right = len(arr) - 1

    while (left <= right):
        temp = (right + left) // 2
        if arr[temp] <= key and key < arr[temp+1]: #如果有元素相同，则下表滞后
            return temp+1
        elif arr[temp] > key:#二分分到左区间，右边界-1
            right = temp - 1
        elif arr[temp] < key:#二分分到右区间，左边界+1
            left = temp + 1
        # print(left)
    return left


#二分法查找相应元素下角标
def Binfind(arr, key):
    left =  0
    right = len(arr) - 1

    while (left <= right):
        temp = (right + left) // 2
        if arr[temp] == key:
            return temp+1
        elif arr[temp] > key:
            right = temp - 1
        elif arr[temp] < key:
            left = temp + 1
    return left

def ModInsertSort(arr):
    #取出列表长度
    num = len(arr)
    for i in range(1, num):
        left = 0
        right = i-1
        temp = arr[i]
        #left一旦大于right，跳出循环
        while left <= right:
            #取lift与right的中间位置（取整）
            mid = (left + right)//2
            
            #利用二分查找的特性，对中间位置的值与待插入数字比较
            #mid右边
            if arr[mid] < temp:
                left = mid+1
            #mid左边
            else:
                right = mid-1
		#查找出temp应插入的位置后，将left后面的数字均向后移动一位
        j = i-1
        while j >= left:
            arr[j+1] = arr[j]
            j -= 1
        #此时left位置上放置待插入的数字
        arr[left] = temp
    print(arr)


if __name__ == "__main__":
    # a = [3,5,4]
    a = [6,7,8,3,4,5,9]
    print(a,'\n')
    t = BinSearch(a,4)
    t1 = Binfind(a,4)
    ModInsertSort(a)



