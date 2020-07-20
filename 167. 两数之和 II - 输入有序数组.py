"""
[167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

***

暴力搜索的方法，能过是能够过，就是效率太低了。

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n < 2 or numbers[0] > target: return []
   

        for i in range(n-1):
            temp = target - numbers[i]
            for j in range(i+1, n):
                if temp == numbers[j]:
                    return [i+1, j+1]
                elif temp < numbers[j]:
                    break     
        return []

***
接下来考虑双指针的方法：就只需要遍历一次即可
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n < 2 or numbers[0] > target: return []
        left, right = 0, n-1
        while left < right:
            temp = numbers[left]+ numbers[right]
            if temp == target:
                return [left+1, right+1]
            elif temp > target:
                right -= 1
            else:
                left += 1
        return [] 
