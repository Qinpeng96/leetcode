"""
[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
***
说明：从列表1的之后开始，对比列表1的最后一个和列表2的最后一个值，谁的值大，就与列表的倒数位置进行交换，一直循环，直到m = 0，或者  n = 0，两种情况。
其中m = 0的时候，说明列表1的值已经被使用完了，把列表2的剩余值赋值到列表1的前面。
n = 0的时候，说明列表2已经使用完了，我们就可以直接结束，因为列表1中的数字在原始位置还是不变。
"""


```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if m == 0:#列表1前面的数被使用完了，将列表2的赋值过来
                nums1[:n] = nums2[:n]
                return

            if nums1[m-1] < nums2[n-1]:#第二个列表的对应大
                nums1[m+n-1], nums2[n-1] = nums2[n-1], nums1[m+n-1]
                n -= 1
            else:#第一个列表的值大m
                nums1[m-1], nums1[m+n-1] = nums1[m+n-1], nums1[m-1] 
                m -= 1
```
