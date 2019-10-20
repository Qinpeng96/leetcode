# -*- coding: utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长增子序列。
设长度为N的数组为{a0，a1, a2, ...an-1)，则假定以aj结尾的数组序列的最长递增子序列长度为L(j)，
则L(j)={ max(L(i))+1, i<j且a[i]<a[j] }。也就是说，我们需要遍历在j之前的所有位置i(从0到j-1)，
找出满足条件a[i]<a[j]的L(i)，求出max(L(i))+1即为L(j)的值。最后，我们遍历所有的L(j)（从0到N-1），
找出最大值即为最大递增子序列。时间复杂度为O(N^2)。
[2,8,4,-4,5,9,11]
[1, 2, 2, 1, 3, 4, 5]
5
"""
from typing import List
class Solution:
    def longestincreasestr(self, arr: List) -> list:
        num = len(arr)
        longest = [1]*num
        i = 0
        for j in range(1,num):
            while i < j:
                if (arr[j]>arr[i] and longest[j]<longest[i]+1): 
                    longest[j] = longest[i] + 1
                i += 1
            i = 0
        print(longest)
        return max(longest)


if __name__ == "__main__":
    a = Solution()
    print(a.longestincreasestr([2,8,4,-4,5,9,11]))
#    print(a.longestCommonPrefix(["",""]))
