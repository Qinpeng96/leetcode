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
        i = (len(nums1)-1) // 2 #由于中位数有的是要计算左右两数的平均值
        j = len(nums1) // 2 #所以当列表的个数为偶数的时候，需要进行平均值计算
        value = (nums1[i] + nums1[j]) / 2
        return value

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    solution = Solution()
    output = solution.findMedianSortedArrays(nums1, nums2)
    print(output)
