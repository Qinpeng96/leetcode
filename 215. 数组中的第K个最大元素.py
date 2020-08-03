"""
[215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度
***
   模块heapq中一些重要的函数
   #
                           函 数                         描 述
                  heappush(heap, x)                   将x压入堆中
                    heappop(heap)                 从堆中弹出最小的元素
                    heapify(heap)                    让列表具备堆特征
              heapreplace(heap, x)               弹出最小的元素，并将x压入堆中
                  nlargest(n, iter)              返回iter中n个最大的元素
                 nsmallest(n, iter)      	     返回iter中n个最小的元素
使用自带的堆来做，控制在k个范围内
"""
"""
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k: 
                heapq.heappop(heap)
        return heapq.heappop(heap) # [5,6]  从堆中弹出最小的元素
```
"""
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        def downAdjust(arr, p, arr_len):#实现一个最大堆排序，先实现一个最小堆
            temp = arr[p]
            c = 2*p + 1

            while c <= arr_len:
                if (c+1) <= arr_len and arr[c] > arr[c+1]:
                    c += 1#找一个小儿子
                if temp <= arr[c]:#不能实现
                    break
                arr[p] = arr[c]
                p = c 
                c = 2*p+1
            arr[p] = temp
            return arr

        #建立一个小堆
        def buildHeap(arr, n):
            p = (n-1) // 2#计算其父节点索引

            while p >= 0:
                arr = downAdjust(arr, p, n)
                p -= 1
            return arr

        def maxHeap(nums, k):#建立一个最大堆排序
            n = len(nums) - 1
            nums = buildHeap(nums,n)

            #建立一个最大堆排序
            for i in range(n, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                nums = downAdjust(nums, 0, i-1)
            return nums[:k]

        
        heapq = maxHeap(nums, k)
        return heapq[-1]
#*********************************************************#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 替换nums[i]后维护最小堆：自顶向下调整新元素位置，直至该值满足(parent value < son value)
        def shift(i,k):
            flag=0
            while (i*2+1)<k and flag==0 :
                t=i
                if nums[i]>nums[2*i+1]:            
                    t=2*i+1
                if (i*2+2)<k and nums[t]>nums[2*i+2]  :            
                    t=2*i+2
                if t==i:
                    flag=1
                else :
                    nums[i],nums[t]=nums[t],nums[i]
                    i=t  
        
        #O(k):建立大小为K的最小堆， k/2-1是最后一个非叶节点，因为shift是向下调整，所以倒序从最下面出发，不然(4 32 1)->(2 34 1)->(2 14 3)->(2 14 3) 结果不对
        for i in range(k/2,-1,-1):
            shift(i,k)

        #O((N-k)logK)，剩余元素依次比较替换
        for i in range(k,len(nums)):
            if nums[0]<nums[i]:
                nums[0]=nums[i]
                shift(0,k)
        return nums[0]
        #sum=O(Nlogk-k(logK-1))
    

if __name__ == "__main__":
    s = Solution()
    nums =[1,2,3,5,6,4,7,8]
    print(s.findKthLargest(nums, 2))
        
