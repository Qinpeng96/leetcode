# -*- coding: utf-8 -*-
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        arr = sorted(nums)
        num = len(arr)
        min_err = 9999
        res = 999
        for i in range(num-2):
            left = i + 1
            right = num - 1
            while left < right :
                err = arr[i]+arr[left]+arr[right] - target
                if err == 0: return target
                if err > 0 :
                    right -= 1
                else:
                    left += 1
                if abs(min_err) > abs(err):
                    min_err = err
            if abs(min_err) < abs(res):
                res = min_err
        return target + res
            


if __name__ == "__main__":
    a = Solution()
    print(a.threeSumClosest([0,2,1,-3],1))
    print(a.threeSumClosest([1,2,-1,-4],1))
    print(a.threeSumClosest([1,2,5,10,11],12))
