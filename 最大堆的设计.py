
"""
堆是一个二叉树，其中每个父节点的值都小于或等于其所有子节点的值。整个堆的最小元素总是位于二叉树的根节点。
python的heapq模块提供了对堆的支持。
堆数据结构最重要的特征是heap[0]永远是最小的元素

1. 大顶堆：
所有的父节点的值都比孩子节点大，叶子节点值最小。root 根节点是第一个节点值最大

2. 小顶堆：
和大顶堆相反，所有父节点值，都小于子节点值，root 根节点是 第一个节点值最小

根据完全二叉树的性质，若将堆中的数据至顶向下，从左向右的存在一个一维数组里面，
则父节点的位置索引总是该节点位置索引减1再除2取整的结果。  p = (c-1) // 2
下面是系统自带的堆应用
import heapq

lst = [1,2,3,5,1,5,8,9,6]

'''
一秒变成堆
'''
heapq.heapify(lst)
[1, 1, 3, 5, 2, 5, 8, 9, 6]

'''
最小的（顶端）再见
'''
heapq.heappop(lst)
[1, 2, 3, 5, 6, 5, 8, 9]

'''
最小的滚蛋，新人进入
'''
heapq.heapreplace(lst,99)
[2, 5, 3, 9, 6, 5, 8, 99]

'''
新人比最小的大，新人进入；若否，则不管
'''
heapq.heappushpop(lst,1)
[2, 5, 3, 9, 6, 5, 8, 99]

heapq.heappushpop(lst,66)
[3, 5, 5, 9, 6, 66, 8, 99]

'''
最大的n个是谁；
最小的n个是谁；
'''
print(heapq.nlargest(3,lst))
[99, 66, 9]
print(heapq.nsmallest(3,lst))
[3, 5, 5]

'''
合并
'''
lst1 = [100,101]
lst2 = [3, 5, 5, 9, 6, 66, 8, 99]
lst = list(heapq.merge(lst1,lst2))-
[3, 5, 5, 9, 6, 66, 8, 99, 100, 101]
"""
from typing import List
"""
父节点与子节点的索引位置关系，p父节点，c子节点
p = (c-1)//2
c1 = 2*p+1
c2 = 2*p+2
本程序维护的是一个最大堆
"""

#对某一个父节点进行下沉，用于删除堆顶元数  arr数组；p节点；arr_len：数组长度
def downAdjust(arr, p, arr_len):
    temp = arr[p]#找到要下沉的父节点的值
    c = 2*p + 1 #计算出其左子节点的索引
    
    #最大堆降序排序
    while c <= arr_len:#当索引的位置在数组内的时候
        if (c+1) <= arr_len and arr[c] > arr[c+1]:#当前儿子比另一个儿子大
            c += 1#找到父节点的两个儿子中的较小的那一个
        if temp <= arr[c]:#如果父节点小于等于小儿子，不对，弹出，不能下沉
            break
        arr[p] = arr[c]#父节点值变成小儿子的值
        p = c#父节点的索引变成小儿子的索引
        c = 2*p+1
    arr[p] = temp
    return arr
    """最小堆升序排序
    while c <= arr_len:#当索引的位置在数组内的时候
        if (c+1) <= arr_len and arr[c] < arr[c+1]:#当前儿子比另一个儿子大
            c += 1#找到父节点的两个儿子中的较大的那一个
        if temp >= arr[c]:#如果父节点大于等于大儿子，不对，弹出，不能下沉
            break
        arr[p] = arr[c]#父节点值变成大儿子的值
        p = c#父节点的索引变成大儿子的索引
        c = 2*p+1
    arr[p] = temp
    return arr
    """


#对某一个节点'上浮' 在插入的时候,把新节点插入到完全二叉树的最后一个位置
def upAdjust(arr, length):
    c = length - 1#子节点
    p = (c-1) // 2#父节点
    temp = arr[c]#临时保存子节点
    
    while c > 0 and temp > arr[p]:#子节点存在且比父节点大
        arr[c] = arr[p]
        arr[p] = temp
        c = p
        p = (c-1)//2
    #弹出的时候，子节点小于等于其父节点的值的时候，填充上浮的值到正确的位置
    arr[c] = temp
    return arr

#构建一个最大二叉堆
def buildHeap(arr):
    n = len(arr) - 1#算出数组的长度
    p = (n-1) // 2#计算出倒数的父节点

    while p >= 0:
        arr = downAdjust(arr, p, n)
        p -= 1
    return arr

#堆排序
def heapSort(arr):
    buildHeap(arr)
    n = len(arr) - 1
    #建立一个最大堆排序，使用下沉
    for i in range(n, 0, -1):
        arr[i], arr[0] = arr[0],arr[i]
        arr = downAdjust(arr, 0, i-1)

    return arr

# s = [1,9,7,6,12,88,0,3,518,9,87,1]
s = [6,3,5,2,4,7,1]
print(heapSort(s))
# s.append(900)
# print(upAdjust(s,len(s)))
# print(heapSort(s))