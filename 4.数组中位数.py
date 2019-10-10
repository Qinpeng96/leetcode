"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0

"""
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int])->float:
        nums1 = nums1 + nums2
        nums1.sort()
        i = (len(nums1)-1) // 2
        j = len(nums1) // 2 
        value = (nums1[i] + nums1[j]) / 2
        return value
