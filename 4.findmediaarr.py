from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int])->float:
        nums1 = nums1 + nums2
        nums1.sort()
        i = (len(nums1)-1) // 2
        j = len(nums1) // 2 
        value = (nums1[i] + nums1[j]) / 2
        return value
